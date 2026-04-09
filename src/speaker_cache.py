import pickle

def save_prompt(prompt, path="speaker.pkl"):
    with open(path, "wb") as f:
        pickle.dump(prompt, f)

def load_prompt(path="speaker.pkl"):
    with open(path, "rb") as f:
        return pickle.load(f)