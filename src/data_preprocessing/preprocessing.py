import os 
import wfdb
import shutil
import scipy.io
import numpy as np
from scipy.signal import resample

def load_ecg_data(mat_file_path):
    """
    Load data from a .mat file.
    Returns the ECG signal data.
    """
    # Load ECG data from .mat file
    mat_data = scipy.io.loadmat(mat_file_path)
    ecg_signal = mat_data['val'][0]

    return ecg_signal

def load_hea_data(hea_file_path):
    """
    Load information from a .hea file.
    Returns the sample name and original sampling rate (fs).
    """
    # Load information from .hea file
    with open(hea_file_path, 'r') as file:
        lines = file.readlines()
        # Extract relevant information from the .hea file
        fields = lines[0].split()
        sample_name, original_fs  = fields[0], fields[3]


    return sample_name, int(original_fs)

def resample_ecg_signal(ecg_signal, original_fs, target_fs):
    """
    Resample the ECG signal to the target sampling rate.
    """
    # Resample ECG signal to the target sampling rate
    resampled_signal = resample(ecg_signal, int(len(ecg_signal) * target_fs / original_fs))

    return resampled_signal

def preprocess_data(input_dir, output_dir, target_fs=1000, resample_data=False):
    """
    Preprocess ECG data from .mat files and save as .npy files.
    Optionally perform resampling.
    """  
    # Join folder paths
    sample_input_dir = os.path.join(input_dir, 'sample/')
    sample_output_dir = os.path.join(output_dir, 'sample/')

    label_input_dir = os.path.join(input_dir, 'label/')
    label_output_dir = os.path.join(output_dir, 'label/')
    
    # Copy exact input label path into output directory 
    shutil.copytree(label_input_dir, label_output_dir)

    # Create output directory if it doesn't exist
    if not os.path.exists(sample_output_dir):
        os.makedirs(sample_output_dir)

    # List all .mat files in the data directory
    mat_files = [file for file in os.listdir(sample_input_dir) if file.endswith('.mat')]

    for mat_file in mat_files:
        # Construct file paths
        mat_file_path = os.path.join(sample_input_dir, mat_file)
        hea_file_path = os.path.join(sample_input_dir, mat_file.replace('.mat', '.hea'))

        # Load ECG signal
        ecg_signal = load_ecg_data(mat_file_path)

        # Load sample name and original sampling rate from .hea file
        sample_name, original_fs = load_hea_data(hea_file_path)

        # Resample ECG signal to the target sampling rate if specified
        if resample_data:
            resampled_ecg = resample_ecg_signal(ecg_signal, original_fs, target_fs)
        else:
            resampled_ecg = ecg_signal

        # Save preprocessed data
        output_file_path = os.path.join(sample_output_dir, f"{sample_name}.npy")
        np.save(output_file_path, resampled_ecg)

if __name__ == "__main__":
    # Set the paths to your raw data directory and the directory where you want to save preprocessed data
    raw_data_dir = "../../data/raw/training2017"
    output_data_dir = "../../data/processed/training2017"

    # Preprocess data with resampling
    preprocess_data(raw_data_dir, output_data_dir, resample_data=True)

    # Alternatively, preprocess data without resampling
    # preprocess_data(raw_data_dir, output_data_dir, resample_data=False)