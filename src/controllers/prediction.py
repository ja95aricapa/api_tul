from fastapi import APIRouter
from services.utils import get_prediction

router = APIRouter(prefix="/test", tags=["Test"])


@router.get("/{index}")
def get_predicction_by_index(index: int, all_images: bool = False):
    """
    Estimate a prediction for a given image by index or all the images.

    Args:
        index (_type_): Desired image index.
        all_images (bool, optional): Check if all images should be predicted. False by default, if false only check one image, if true check all the images.

    Returns:
        A single prediction as a int number or all the predictions as a list of int numbers.

    Evaluation:
        During the execution of the model, a training was done using the .fit() method, and later,
        the evaluate() method was used. This last method takes test data and establishes
        how accurate it can be under the given conditions (such as optimization and loss function)
        in the build.
    """
    return get_prediction(index=index, check_all=all_images)
