from fastapi import APIRouter, Body
from services.grid import search_path_list
from schemas.grid import Model

router = APIRouter(prefix="/test", tags=["Test"])


@router.post("/grid/{grid}")
def get_cost_and_path(grid: int, schema: Model = Body()):
    """
    Search for a path from start_point to end_point in a grid of size n x n.

    Args:
        grid (int): Indicates the size of the grid. The grid has size n x n.
        schema (JSON): A JSON with the coordinates of the start and end point.

        Note: The coordinates are represented as a list of two integers, because the FASTAPI param validator of controllers dont allow use tuples.

    Algorithm:
        1. step over start_point and add it to the path
        2. move about the x-axis until the x-coordinate of my current position is the same as the x-coordinate of the end point
            2.1 if x-cordinate is diferrent, move to the next nearest x-coordinate and add it to the path
        3. move about the y-axis until the y-coordinate of my current position is the same as the y-coordinate of the end point
            3.1 if y-cordinate is diferrent, move to the next nearest y-coordinate and add it to the path
        4. if the current position is the same as the end point, add it and to the path
        5. remove start and end point from the path
        6. calculate the distance of the path
        7. return the path and the cost distance

    Returns:
        A JSON with the cost and the path used as a list of coordinates.
    """
    try:
        schema.start_point = tuple(schema.start_point)
        schema.end_point = tuple(schema.end_point)
        return search_path_list(grid=grid, start_point=schema.start_point, end_point=schema.end_point)
    except ValueError as e:
        print(e)
        return {"error": str(e)}