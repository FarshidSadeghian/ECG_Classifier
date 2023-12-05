import scipy.io

file_path = 'data/raw/training2017/A00001.mat'
data = scipy.io.loadmat(file_path)

for key in data:
    print(f"Key: {key}\nData:\n{data[key]}\n")
