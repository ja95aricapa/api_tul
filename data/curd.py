import pickle

import tensorflow as tf
from tensorflow import keras

from google_drive_downloader import GoogleDriveDownloader as gdd

list1 = ['1rud19sdNaHHiu4003ri1Tng8SU_RODek', '1qPtc2xsrkWRvK-2JBB4kfP7oXQa2aU6T', '17kAMuASme_sYOTUpOswrYa5b2PDFGRb0']
list2 = ['data/images.pickle', "data/labels.pickle", "data/model.pickle"]

idx1 = 0

while idx1 < len(list1):
    gdd.download_file_from_google_drive(file_id=list1[idx1], dest_path=list2[idx1], unzip=False)
    print(f"{list2[idx1]} downloaded")
    idx1 += 1

def get_info():
    list_name = ['data/images.pickle', "data/labels.pickle", "data/model.pickle"]
    list_obj = []
    for name in list_name:
        with open(name, "rb") as f:
            print(f"{name} loaded")
            list_obj.append(pickle.load(f))
    return list_obj
