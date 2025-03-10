import pickle

def load_user_data(file_path):
    with open(file_path, "rb") as f:
        data = pickle.load(f)  # Unsafe deserialization, can lead to remote code execution
    return data