
import matplotlib as mtp
import numpy as np
import pandas as pd
import antropy as ant
import seaborn as sns
from scipy import stats
import tensorflow as tf
from typing import Tuple
from mne.datasets import eegbci
import matplotlib.pyplot as plt
from mne.preprocessing import ICA
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans

from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

from scipy.signal import welch, periodogram
from scipy.stats import skew, kurtosis, iqr
from sklearn.metrics import silhouette_score

from sklearn.preprocessing import LabelEncoder
from matplotlib.animation import FuncAnimation
from mne.channels import make_standard_montage
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import mne, pywt, os, nolds, warnings, time, pickle, umap, joblib, json, base64




from datetime import datetime
from google.cloud import storage
import tensorflow as tf
from keras import layers
from dotenv import load_dotenv
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding as asym_padding
from cryptography.hazmat.primitives import hashes, serialization


load_dotenv()


# Initialize GCS client
storage_client = storage.Client()



def load_model_from_gcs(bucket_name, model_path, local_model_dir='/tmp/model'):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blobs = bucket.list_blobs(prefix=model_path)

    if not os.path.exists(local_model_dir):
        os.makedirs(local_model_dir)

    for blob in blobs:
        if blob.name.endswith('/'):
            continue  # Skip directories
        file_path = os.path.join(local_model_dir, os.path.relpath(blob.name, model_path))
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        blob.download_to_filename(file_path)

    # Check if the SavedModel file exists in the local directory
    if not os.path.exists(os.path.join(local_model_dir, 'saved_model.pb')) and not os.path.exists(os.path.join(local_model_dir, 'saved_model.pbtxt')):
        raise FileNotFoundError(f'SavedModel file does not exist in {local_model_dir}')

    return layers.TFSMLayer(local_model_dir, call_endpoint='serving_default')

# Generate a secure AES key
def generate_aes_key():
    return os.urandom(32)  # AES-256

# Encrypt data using AES
def encrypt_data(data, key):
    iv = os.urandom(16)  # Initialization vector
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data.encode()) + padder.finalize()
    ct = encryptor.update(padded_data) + encryptor.finalize()
    return base64.b64encode(iv + ct).decode('utf-8')

# Decrypt data using AES
def decrypt_data(encrypted_data, key):
    encrypted_data = base64.b64decode(encrypted_data)
    iv = encrypted_data[:16]
    ct = encrypted_data[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ct) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()
    return data.decode('utf-8')

# Encrypt AES key using RSA
def rsa_encrypt(data: bytes, public_key) -> bytes:
    return public_key.encrypt(data, asym_padding.OAEP(mgf=asym_padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

# Decrypt AES key using RSA
def rsa_decrypt(data: bytes, private_key) -> bytes:
    return private_key.decrypt(data, asym_padding.OAEP(mgf=asym_padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

# Save profile and encrypted AES key function
def save_profile_and_key(user_id, profile, aes_key, public_key, bucket_name):
    user_folder = f'{user_id}/'
    encrypted_profile = encrypt_data(json.dumps(profile.tolist()), aes_key)
    encrypted_aes_key = rsa_encrypt(aes_key, public_key)

    profile_blob = storage_client.bucket(bucket_name).blob(f'{user_folder}profile.json')
    profile_blob.upload_from_string(json.dumps({'profile': encrypted_profile, 'timestamp': str(datetime.now())}))

    key_blob = storage_client.bucket(bucket_name).blob(f'{user_folder}key.bin')
    key_blob.upload_from_string(encrypted_aes_key)

# Load profile and encrypted AES key function
def load_profile_and_key(user_id, private_key, bucket_name):
    user_folder = f'{user_id}/'

    profile_blob = storage_client.bucket(bucket_name).blob(f'{user_folder}profile.json')
    profile_data = json.loads(profile_blob.download_as_string())

    key_blob = storage_client.bucket(bucket_name).blob(f'{user_folder}key.bin')
    encrypted_aes_key = key_blob.download_as_string()
    aes_key = rsa_decrypt(encrypted_aes_key, private_key)

    decrypted_profile = json.loads(decrypt_data(profile_data['profile'], aes_key))
    return np.array(decrypted_profile), profile_data['timestamp'], aes_key



# Key functions for utility 


# Final Primary Preprocessing function
def preprocess_data(base_folder, selected_electrodes, segment_length=1000, overlap=500, num_users=None):

    # _____________________________________________ Process EEG data
    segmented_ica_data = prepare_ica_data_for_model(base_folder, segment_length, overlap, electrodes=selected_electrodes, num_electrodes=None, num_users=num_users)
    segmented_ica_df = convert_segmented_data_to_df(segmented_ica_data)
    normalized_ica_df, scaler = normalize_ica_features(segmented_ica_df)
    eeg_data = prepare_ica_data_for_dnn(normalized_ica_df)

    # ______________________________________________Process feature data
    feature_metrics = process_eeg_data(base_folder, segment_length, overlap, electrodes=selected_electrodes, num_electrodes=None, num_users=num_users)
    feature_weights = compute_feature_weights(feature_metrics)
    transformed_metrics = transform_feature_metrics(feature_metrics, feature_weights)
    organized_data = organize_feature_metrics(transformed_metrics)
    normalized_data, scaler = normalize_features(organized_data)
    feature_data = prepare_data_for_dnn(normalized_data)


    # Reshape eeg_data to include the number of components
    num_components = normalized_ica_df['component'].nunique()
    eeg_data = eeg_data.reshape((eeg_data.shape[0], eeg_data.shape[1]//num_components, num_components))

    return eeg_data, feature_data



# Define the ceda_predict function
def ceda_predict(model, mode, eeg_data=None, feature_metrics=None, prev_profile=None):
    if mode == 'profile':
        if eeg_data is not None:
            profile = model.predict({
                'eeg_input': eeg_data,
                'metrics_input': np.zeros((eeg_data.shape[0], model.input[1].shape[1]))
            })[0]
            return profile
        elif feature_metrics is not None:
            # Create dummy EEG data with the correct shape
            eeg_dummy_data = np.zeros((feature_metrics.shape[0], model.input[0].shape[1], 4))  # Adjusting the last dimension to 4
            profile = model.predict({
                'eeg_input': eeg_dummy_data,
                'metrics_input': feature_metrics
            })[0]
            return profile
        else:
            raise ValueError("Either eeg_data or feature_metrics must be provided")
    elif mode == 'eeg_age':
        if prev_profile is None:
            raise ValueError("prev_profile must be provided for eeg_age mode")
        if eeg_data is not None:
            _, eeg_age = model.predict({
                'eeg_input': eeg_data,
                'metrics_input': np.zeros((eeg_data.shape[0], model.input[1].shape[1])),
                'prev_profile_input': prev_profile
            })
            return eeg_age
        elif feature_metrics is not None:
            # Create dummy EEG data with the correct shape
            eeg_dummy_data = np.zeros((feature_metrics.shape[0], model.input[0].shape[1], 4))  # Adjusting the last dimension to 4
            _, eeg_age = model.predict({
                'eeg_input': eeg_dummy_data,
                'metrics_input': feature_metrics,
                'prev_profile_input': prev_profile
            })
            return eeg_age
        else:
            raise ValueError("Either eeg_data or feature_metrics must be provided")
    else:
        raise ValueError("Unknown mode. Use 'profile' or 'eeg_age'.")


# Wavelet entropy function
def wentropy(signal, mode='shannon', param=None):
    cA, cD = pywt.dwt(signal, 'haar')
    eps = 1e-10  # small constant to avoid log2(0)

    # Check for NaN or very small sum
    if np.isnan(cA).all() or np.isnan(cD).all():
        return 0

    if np.isnan(cA).any():
        if len(cA[~np.isnan(cA)]) > 0:
            cA = np.where(np.isnan(cA), np.interp(np.flatnonzero(np.isnan(cA)), np.flatnonzero(~np.isnan(cA)), cA[~np.isnan(cA)]), cA)
        else:
            cA_mean = np.nanmean(cA)
            cA = np.where(np.isnan(cA), cA_mean, cA)

    if np.isnan(cD).any():
        if len(cD[~np.isnan(cD)]) > 0:
            cD = np.where(np.isnan(cD), np.interp(np.flatnonzero(np.isnan(cD)), np.flatnonzero(~np.isnan(cD)), cD[~np.isnan(cD)]), cD)
        else:
            cD_mean = np.nanmean(cD)
            cD = np.where(np.isnan(cD), cD_mean, cD)

    # Calculate probabilities
    cA_sum, cD_sum = np.sum(cA), np.sum(cD) + eps
    if cA_sum == 0 or cD_sum == 0:
        return 0

    pA = cA / cA_sum
    pD = cD / cD_sum

    # Handle zeros and negative values
    pA = np.clip(pA, a_min=1e-10, a_max=1.0)
    pD = np.clip(pD, a_min=1e-10, a_max=1.0)

    # Normalize the probabilities
    pA = pA / (np.sum(pA) + eps)
    pD = pD / (np.sum(pD) + eps)

    # Calculate entropies
    if mode == 'shannon':
        entA = -np.sum(pA * np.log2(pA + eps))
        entD = -np.sum(pD * np.log2(pD + eps))

        # Clip infinite values
        entA = np.clip(entA, -1e10, 1e10)
        entD = np.clip(entD, -1e10, 1e10)

    elif mode == 'sure':
        entA = -np.sum(pA**param)
        entD = -np.sum(pD**param)
    elif mode == 'log energy':
        entA = np.log(np.sum(cA ** 2))
        entD = np.log(np.sum(cD ** 2))
    else:
        raise ValueError("Unknown entropy mode.")
    wentropy = entA + entD

    return wentropy


# ----------------------------- Feature extraction
def extract_features(ica_data, segment_length=1000, overlap=500):

    """
    Extracts comprehensive features from each EEG segment and aggregates them.

    Parameters:
    ica_data : ndarray
        The EEG data segmented into windows with shape (channels, data_points)
    segment_length : int
        Length of each segment
    overlap : int
        Overlap between segments

    Returns:
    aggregated_features : dict
        Aggregated features for each component
    """

    aggregated_features = {}

    warnings.filterwarnings("ignore", category=RuntimeWarning, message="signal has very low mean frequency, setting min_tsep = 250")
    start_time = time.time()

    num_segments = (len(ica_data[0]) - overlap) // (segment_length - overlap)
    idx = 0
    for component_idx, component in enumerate(ica_data):
        idx += 1  # Increment the index for each component
        print(f"      Processing component {idx}/{len(ica_data)}")



        comp_start_time = time.time()
        segmented_data = np.array_split(component, num_segments)
        segment_features_list = []

        for segment in segmented_data:
            # Basic statistical features
            features = {
                'max': np.max(segment),
                'mean': np.mean(segment),
                'median': np.median(segment),
                'var': np.var(segment),
                'std': np.std(segment),
                'min': np.min(segment),
                'range': np.ptp(segment),
                'rms': np.sqrt(np.mean(np.square(segment))),
                'energy': np.sum(np.square(segment)),
                'iqr': stats.iqr(segment),
                'mean_diff': np.mean(np.diff(segment)),
                'skew': stats.skew(segment),
                'kurtosis': stats.kurtosis(segment),
                'mad': np.median(np.abs(segment)),
                'ptp': np.ptp(segment),
                'euclidean_norm': np.linalg.norm(segment)
            }

            # Power Spectral Density (PSD) features
            freqs, psd = welch(segment, fs=1024, nperseg=len(segment))
            features.update({
                'mean_psd': np.mean(psd),
                'std_psd': np.std(psd)
            })

            # Entropy measures
            features.update({
                'wentropy_shannon': wentropy(segment, 'shannon'),
                'wentropy_sure': wentropy(segment, 'sure', param=1),
                'wentropy_log_energy': wentropy(segment, 'log energy'),
                'wentropy_abs_shannon': wentropy(np.abs(segment), 'shannon'),
                'wentropy_abs_sure': wentropy(np.abs(segment), 'sure', param=1),
                'wentropy_abs_log_energy': wentropy(np.abs(segment), 'log energy'),
                'stats_entropy': stats.entropy(segment + 1e-10, base=2),
                'stats_entropy_abs': stats.entropy(np.abs(segment) + 1e-10, base=2),
                'perm_entropy': ant.perm_entropy(segment, normalize=True),
                'spectral_entropy': ant.spectral_entropy(segment, sf=1024, method='welch', normalize=True),
                'svd_entropy': ant.svd_entropy(segment, normalize=True),
                'app_entropy': ant.app_entropy(segment),
                'sample_entropy': ant.sample_entropy(segment)
            })

            # Non-linear dynamics
            features.update({
                'higuchi_fd': ant.higuchi_fd(segment),
                'petrosian_fd': ant.petrosian_fd(segment),
                'katz_fd': ant.katz_fd(segment),
                'lyapunov': nolds.lyap_r(segment, emb_dim=10)  # Lyapunov exponent using nolds
            })

            # Wavelet transform features
            coeffs = pywt.wavedec(segment, 'db4', level=5)
            for i, coeff in enumerate(coeffs):
                features.update({
                    f'wavelet_coeff_{i}_mean': np.mean(coeff),
                    f'wavelet_coeff_{i}_std': np.std(coeff),
                    f'wavelet_coeff_{i}_energy': np.sum(np.square(coeff))
                })

            # Bandpower features
            def bandpower(freqs, psd, band):
                idx_band = np.logical_and(freqs >= band[0], freqs <= band[1])
                return np.sum(psd[idx_band])

            features.update({
                'alpha_power': bandpower(freqs, psd, (8, 12)),
                'beta_power': bandpower(freqs, psd, (13, 30)),
                'gamma_power': bandpower(freqs, psd, (30, 45)),
                'delta_power': bandpower(freqs, psd, (1, 4)),
                'theta_power': bandpower(freqs, psd, (4, 8))
            })

            # Temporal features
            features.update({
                'autocorr': np.correlate(segment, segment, mode='full')[len(segment)-1]
            })

            segment_features_list.append(features)

        # Aggregate features for each component
        df_segment_features = pd.DataFrame(segment_features_list)
        aggregated_features[component_idx] = df_segment_features.mean().to_dict()


    # Cross-correlation between components
    cross_corr_features = {}
    for i in range(len(ica_data)):
        for j in range(i + 1, len(ica_data)):
            cross_corr = np.correlate(ica_data[i], ica_data[j], mode='full')[len(ica_data[i]) - 1]
            cross_corr_features[f'cross_corr_{i}_{j}'] = cross_corr
    aggregated_features.update(cross_corr_features)

    end_time = time.time()
    print(f"    Feature extraction complete in {end_time - start_time:.2f} seconds.")

    return aggregated_features





# ----------------------------- Main processing function for eeg
def process_eeg_data(base_folder, segment_length=1000, overlap=500, electrodes=None, num_electrodes=None, num_users=None):
    # Load raw data
    raw_data_dict = load_raw_data(base_folder, electrodes, num_electrodes)
    print("Raw data loaded.")

    # Convert to metric structure
    metric_data_dict = convert_to_metric_structure(raw_data_dict)
    print("Data converted to metric structure.")

    # Apply ICA to the raw data metric
    ica_results = apply_ica(metric_data_dict)
    print("ICA applied to data.")

    feature_metrics = {}

    # Limit the number of users for testing
    users = list(ica_results.keys())
    if num_users is not None and num_users < len(users):
        users = users[:num_users]

    for user_idx, user_id in enumerate(users):
        user_ica = ica_results[user_id]
        user_feature_metrics = []

        print(f"Processing user {user_idx + 1}/{len(users)}: {user_id}")
        print(f"  Number of sessions: {len(user_ica['ica_data'])}")

        for session_idx, session_data in enumerate(user_ica['ica_data']):
            print(f"  Processing session {session_idx + 1}/{len(user_ica['ica_data'])}: {user_ica['sessions'][session_idx]}")
            print(f"    Number of ICA components: {len(session_data)}")

            # Extract and aggregate features for each session
            aggregated_features = extract_features(session_data, segment_length, overlap)
            user_feature_metrics.append({
                'session': user_ica['sessions'][session_idx],
                'features': aggregated_features
            })

        # Aggregate features across sessions
        aggregated_user_features = {}
        for component_idx in range(len(session_data)):
            component_features_list = [session['features'][component_idx] for session in user_feature_metrics]
            df_component_features = pd.DataFrame(component_features_list)
            aggregated_user_features[component_idx] = df_component_features.mean().to_dict()

        feature_metrics[user_id] = aggregated_user_features

    return feature_metrics




def prepare_ica_data_for_model(base_folder, segment_length=1000, overlap=500, electrodes=None, num_electrodes=None, num_users=None):
    # Load raw data
    raw_data_dict = load_raw_data(base_folder, electrodes, num_electrodes)
    print("Raw data loaded.")

    # Convert to metric structure
    metric_data_dict = convert_to_metric_structure(raw_data_dict)
    print("Data converted to metric structure.")

    # Apply ICA to the raw data metric
    ica_results = apply_ica(metric_data_dict)
    print("ICA applied to data.")

    segmented_ica_data = {}

    # Limit the number of users for testing
    users = list(ica_results.keys())
    if num_users is not None and num_users < len(users):
        users = users[:num_users]

    for user_idx, user_id in enumerate(users):
        user_ica = ica_results[user_id]
        user_segmented_data = []

        print(f"Processing user {user_idx + 1}/{len(users)}: {user_id}")
        print(f"  Number of sessions: {len(user_ica['ica_data'])}")

        for session_idx, session_data in enumerate(user_ica['ica_data']):
            print(f"  Processing session {session_idx + 1}/{len(user_ica['ica_data'])}: {user_ica['sessions'][session_idx]}")
            print(f"    Number of ICA components: {len(session_data)}")

            session_segmented_data = []

            for component_idx in range(session_data.shape[0]):  # Iterate over ICA components
                component_data = session_data[component_idx]
                print(f"    Component {component_idx + 1} data shape: {component_data.shape}")

                # Segment the component data
                segmented_data = segment_data(component_data, segment_length, overlap)
                print(f"    Component {component_idx + 1} data shape after segmentation: {segmented_data.shape}")

                for segment_idx, segment in enumerate(segmented_data):
                    print(f"    Processing segment {segment_idx + 1}/{len(segmented_data)} for component {component_idx + 1}")

                    session_segmented_data.append({
                        'user_id': user_id,
                        'session_id': user_ica['sessions'][session_idx],
                        'component': component_idx,
                        'segment': segment_idx,
                        'data': segment
                    })

            user_segmented_data.extend(session_segmented_data)
        segmented_ica_data[user_id] = user_segmented_data

    return segmented_ica_data


# Convert segmented ica data to DataFrame
def convert_segmented_data_to_df(segmented_ica_data):
    data_list = []
    for user_id, sessions in segmented_ica_data.items():
        for session in sessions:
            row = {
                'user_id': session['user_id'],
                'session_id': session['session_id'],
                'component': session['component'],
                'segment': session['segment']
            }
            row.update({f'data_point_{i}': value for i, value in enumerate(session['data'].flatten())})
            data_list.append(row)
    return pd.DataFrame(data_list)


# Normalize ICA features
def normalize_ica_features(data):
    feature_columns = [col for col in data.columns if col not in ['user_id', 'session_id', 'component', 'segment']]
    scaler = StandardScaler()
    data[feature_columns] = scaler.fit_transform(data[feature_columns])
    return data, scaler

# Prepare ICA data for DNN
def prepare_ica_data_for_dnn(normalized_data):
    
    """
    This function extracts the relevant numerical feature columns from the preprocessed DataFrame
    and converts it into a NumPy array format for input into a DNN.
    """
    feature_columns = [col for col in normalized_data.columns if col not in ['user_id', 'session_id', 'component', 'segment']]
    return normalized_data[feature_columns].values

def apply_ica(metric_data_dict, default_n_components=15):
    ica_results = {}
    for user_id, user_data in metric_data_dict.items():
        ica_data = []
        for data in user_data['metrics']:
            raw = mne.io.RawArray(data, mne.create_info(user_data['electrodes'], sfreq=256, ch_types='eeg'))
            eegbci.standardize(raw)

            montage = make_standard_montage('standard_1005')
            raw.set_montage(montage)
            raw.filter(14., 30., fir_design='firwin')

            # Determine the number of components dynamically
            n_components = min(default_n_components, len(raw.info['ch_names']))
            if n_components < 2:
                n_components = len(raw.info['ch_names'])

            # Fit ICA
            ica = ICA(n_components=n_components, random_state=97, max_iter=2000)
            ica.fit(raw)
            ica_raw = ica.apply(raw.copy())
            ica_data.append(ica_raw.get_data())

        ica_results[user_id] = {
            'sessions': user_data['sessions'],
            'ica_data': ica_data,
            'ica': ica
        }
    return ica_results

# ---------------------------------- Function to segment the data
def segment_data(raw_data, segment_length=1000, overlap=500):
    if not isinstance(raw_data, np.ndarray):
        raw_data = np.array(raw_data)  # Ensure raw_data is a NumPy array

    if raw_data.ndim == 1:  # If raw_data is 1D, make it 2D
        raw_data = raw_data[np.newaxis, :]

    n_channels = raw_data.shape[0]
    n_timepoints = raw_data.shape[1]
    segmented_data = []

    for start in range(0, n_timepoints - segment_length + 1, segment_length - overlap):
        end = start + segment_length
        if end <= n_timepoints:
            segment = raw_data[:, start:end]
            segmented_data.append(segment)
    segmented_data = np.array(segmented_data)

    # Debug: Print shape of segmented data
    # print("Shape of segmented_data:", segmented_data.shape)

    return segmented_data


def identify_available_channels(base_folder):
    """
    Identify available channels in the EDF files.

    Parameters:
    - base_folder (str): The base folder containing user data folders.

    Returns:
    - available_channels (set): A set of all available channels across all EDF files.
    """
    available_channels = set()

    # Iterate over each user's folder
    for user_folder in os.listdir(base_folder):
        user_folder_path = os.path.join(base_folder, user_folder)
        if os.path.isdir(user_folder_path):
            # Iterate over each EDF file (session) in the user's folder
            for edf_file in os.listdir(user_folder_path):
                if edf_file.endswith('.edf'):
                    edf_file_path = os.path.join(user_folder_path, edf_file)
                    raw = mne.io.read_raw_edf(edf_file_path, preload=True)
                    available_channels.update(raw.ch_names)

    return available_channels


def load_raw_data(base_folder, electrodes=None, num_electrodes=None):
    raw_data_dict = {}
    for user_folder in os.listdir(base_folder):
        user_path = os.path.join(base_folder, user_folder)
        if os.path.isdir(user_path):
            user_data = {'sessions': [], 'electrodes': [], 'metrics': []}
            for session_file in os.listdir(user_path):
                if session_file.endswith('.edf'):
                    edf_path = os.path.join(user_path, session_file)
                    raw = mne.io.read_raw_edf(edf_path, preload=True)
                    if electrodes:
                        raw.pick_channels(electrodes)
                    if num_electrodes and len(raw.info['ch_names']) > num_electrodes:
                        raw.pick_channels(raw.info['ch_names'][:num_electrodes])
                    data = raw.get_data()
                    user_data['sessions'].append(session_file)
                    user_data['electrodes'] = raw.info['ch_names']
                    if data.ndim == 1:
                        data = data.reshape(1, -1)
                    user_data['metrics'].append(data)
            raw_data_dict[user_folder] = user_data
    return raw_data_dict


#Convert to Metric Structure
def convert_to_metric_structure(raw_data_dict):
    """
    Convert raw data into a metric structure.

    Parameters:
    - raw_data_dict (dict): Dictionary containing raw data metrics for each user.

    Returns:
    - metric_dict (dict): Dictionary containing the metric structure for each user.
    """
    metric_dict = {}

    for user_id, user_data in raw_data_dict.items():
        sessions = user_data['sessions']
        electrodes = user_data['electrodes']
        data = user_data['metrics']
        metric_dict[user_id] = {
            'sessions': sessions,
            'electrodes': electrodes,
            'metrics': data
        }
    return metric_dict



def print_metric_structure(metric_dict):
    """
    Print the metric structure for each user.

    Parameters:
    - metric_dict (dict): Dictionary containing the metric structure for each user.
    """
    for user_id, user_data in metric_dict.items():
        print(f"User: {user_id}")
        print(f"Electrodes: {user_data['electrodes']}")
        for session_label, session_metric in zip(user_data['sessions'], user_data['metrics']):
            print(f"Session: {session_label}")
            for electrode, data in session_metric.items():
                print(f"Electrode: {electrode}, Data shape: {data.shape}")
                print(data)  # Print raw EEG data array


def plot_eeg(metric_dict, user_id, session_idx, electrode):
    """
    Plot EEG data for a specific user, session, and electrode.

    Parameters:
    - metric_dict (dict): Dictionary containing the metric structure for each user.
    - user_id (str): The user ID to plot.
    - session_idx (int): The session index to plot.
    - electrode (str): The electrode to plot.
    """
    user_data = metric_dict[user_id]
    session_data = user_data['metrics'][session_idx]
    electrode_data = session_data[electrode]

    plt.figure(figsize=(10, 4))
    plt.plot(electrode_data)
    plt.title(f"EEG Data - User: {user_id}, Session: {user_data['sessions'][session_idx]}, Electrode: {electrode}")
    plt.xlabel("Time Points")
    plt.ylabel("Amplitude")
    plt.show()



# Function to check if a value is a number
def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

# Function to compute feature weights using Euclidean Norm across components

def compute_feature_weights(feature_metrics):
    feature_weights = {}
    for user_id, user_data in feature_metrics.items():
        user_features = []
        for component_data in user_data.values():
            user_features.append(list(component_data.values()))

        feature_matrix = np.array(user_features)
        feature_weights[user_id] = np.linalg.norm(feature_matrix, axis=0)
    return feature_weights



# Function to transform the feature metrics using the computed weights
def transform_feature_metrics(feature_metrics, feature_weights):
    transformed_metrics = {}
    for user_id, user_data in feature_metrics.items():
        transformed_user_data = {}
        weights = feature_weights[user_id]
        for component, features in user_data.items():
            transformed_features = {k: v * w for (k, v), w in zip(features.items(), weights)}
            transformed_user_data[component] = transformed_features
        transformed_metrics[user_id] = transformed_user_data
    return transformed_metrics


# Function to organize the transformed feature metrics for model input
def organize_feature_metrics(transformed_metrics):
    organized_data = []

    for user_id, user_data in transformed_metrics.items():
        for component, transformed_features in user_data.items():
            row = [user_id, component]
            row.extend(transformed_features.values())
            organized_data.append(row)

    feature_columns = list(transformed_metrics[list(transformed_metrics.keys())[0]].values())[0].keys()
    columns = ['user_id', 'component'] + list(feature_columns)

    df = pd.DataFrame(organized_data, columns=columns)

    max_value = 1e10
    df = df.applymap(lambda x: max_value if is_number(x) and x == float('inf') else
                     (-max_value if is_number(x) and x == float('-inf') else x))

    df = df.applymap(lambda x: max_value if is_number(x) and x > max_value else
                     (-max_value if is_number(x) and x < -max_value else x))

    df = df.apply(lambda x: x.interpolate() if x.isnull().any() else x, axis=0)

    return df




# Function to normalize features
def normalize_features(organized_data):
    feature_columns = [col for col in organized_data.columns if col not in ['user_id', 'component']]
    scaler = StandardScaler()
    organized_data[feature_columns] = scaler.fit_transform(organized_data[feature_columns])
    return organized_data, scaler


# Function to prepare data for DNN
def prepare_data_for_dnn(organized_data):
    feature_columns = [col for col in organized_data.columns if col not in ['user_id', 'component']]
    return organized_data[feature_columns].values
