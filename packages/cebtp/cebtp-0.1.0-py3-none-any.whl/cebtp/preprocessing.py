
# cebtp/preprocessing.py

from .utils import (
    prepare_ica_data_for_model,
    convert_segmented_data_to_df,
    normalize_ica_features,
    prepare_ica_data_for_dnn,
    prepare_data_for_dnn,
    process_eeg_data,
    compute_feature_weights,
    transform_feature_metrics,
    organize_feature_metrics,
    normalize_features,
    wentropy,
    extract_features,
    load_raw_data,
    convert_to_metric_structure,
    apply_ica,
    segment_data
)



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
