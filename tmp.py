import os
import scipy.io
import numpy as np
import matplotlib.pyplot as plt

# # Show the .mat file contents
# file_path = 'data/raw/training2017/A00001.mat'
# data = scipy.io.loadmat(file_path)

# for key in data:
#     print(f"Key: {key}\nData:\n{data[key]}\n")



def plot_processed_data(data_dir, sample_name):
    """
    Load and plot one of the processed ECG signals.
    """
    # Construct the file path for the processed data
    processed_file_path = os.path.join(data_dir, f"{sample_name}.npy")

    # Load the processed ECG signal
    processed_ecg = np.load(processed_file_path)

    # Plot the ECG signal
    plt.figure(figsize=(10, 4))
    plt.plot(processed_ecg)
    plt.title(f"Processed ECG Signal: {sample_name}")
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    plt.show()

if __name__ == "__main__":
    # Set the path to your processed data directory
    processed_data_dir = "data/processed/training2017"

    # Specify the sample name you want to visualize
    # You can replace 'A00001' with the actual sample name
    sample_name_to_visualize = 'A00001'

    # Plot the processed data
    plot_processed_data(processed_data_dir, sample_name_to_visualize)
