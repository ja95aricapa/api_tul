import matplotlib.pyplot as plt
import os
import numpy as np
import tensorflow as tf
from data.curd import get_info
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from tensorflow import keras


def get_prediction(index: int, check_all: bool, check_eval: bool):
    try:
        index = int(index)
        # load data and labels
        list_info = get_info()
        images_array = list_info[0]
        test_labels = list_info[1]
        model = list_info[2]
        # prepare data
        test_images = images_array / 255.0
        test_images = test_images.reshape(test_images.shape[0], 28, 28, 1)
        # prepare model
        model.compile(
            optimizer="adam",
            loss="sparse_categorical_crossentropy",
            metrics=["accuracy"],
        )
        model.fit(test_images, test_labels, epochs=10)
        test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
        print(f"\nTest accuracy: {test_acc} \nTest loss: {test_loss}")
        # make prediction
        predictions = make_prediction(index, model, test_images, check_all)
        # send info to client
        if check_eval:
            json_to_show = {
                "predictions": predictions,
                "test_loss": test_loss,
                "test_acc": test_acc,
            }
        else:
            json_to_show = {
                "predictions": predictions,
            }
        return JSONResponse(
            status_code=status.HTTP_200_OK, content=json_to_show
        )
    except HTTPException as e:
        return JSONResponse(
            status_code=status.HTTP_424_FAILED_DEPENDENCY, content={"error": e.detail}
        )


def show_image(i: int, images, labels):
    print(f"This image is from class: {labels[i]}")
    plt.figure()
    plt.imshow(images[i])
    plt.colorbar()
    plt.grid(False)
    plt.show()


def make_prediction(i: int, model, images, all_images: bool):
    """
    Calculate a prediction for a given image by index or all the images.

    Args:
        i (int): Desired image index.
        model (_type_): Model to use for prediction.
        images (_type_): Array of images.
        all_images (bool): Check if all images should be predicted.

    Returns:
        A single prediction as a int number or all the predictions as a list of int numbers.
    """
    if all_images:
        result_array = []
        for i in range(len(images)):
            pred_val = np.argmax(model.predict(np.array([images[i]])))
            pred_val = pred_val.item()
            print(f"\n Index: {i} \n Prediction: {pred_val}")
            result_array.append(pred_val)
        return result_array
    else:
        val = np.argmax(model.predict(np.array([images[i]])))
        return val.item()


# Reference: https://www.tensorflow.org/tutorials/keras/classification?hl=es-419
