import matplotlib.pyplot as plt
import numpy as np

"""
Para que las funciones retornen el resultado esperado,
usted debe cargar los datos con los siguientes nombres:
images, labels, model 
"""


def show_image(i: int):
    print(f"This image is from class: {labels[i]}")
    plt.figure()
    plt.imshow(images[i])
    plt.colorbar()
    plt.grid(False)
    plt.show()


def make_prediction(i: int, all_images: bool = False):
    if all_images:
        return model.predict(images)
    else:
        return np.argmax(model.predict(np.array([images[i]])))
