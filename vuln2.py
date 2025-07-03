# File: vulnerable_deserialization.py

"""
⚠️ WARNING: Insecure deserialization for demonstration only.
Never unpickle untrusted input in real applications.
"""

import pickle

def load_model_from_file(path):
    with open(path, "rb") as f:
        return pickle.load(f)  # Insecure: vulnerable to arbitrary code execution


if __name__ == "__main__":
    model = load_model_from_file("data/vulnerable_model.pkl")
    print("Loaded model:", model)
