import pickle

import tensorflow as tf
from tensorflow import keras

def get_info():
    list_name = ['data/images.pickle', "data/labels.pickle", "data/model.pickle"]
    list_obj = []
    for name in list_name:
        with open(name, "rb") as f:
            print(f"{name} loaded")
            list_obj.append(pickle.load(f))
    return list_obj
