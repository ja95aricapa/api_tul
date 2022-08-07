from typing import Tuple
from fastapi.responses import JSONResponse


def search_path_list(
    grid: int, start_point: Tuple[int, int], end_point: Tuple[int, int]
):
    """
    Search for a path from start_point to end_point in a grid of size n x n.

    Args:
        grid (int): Indicates the size of the grid.
        start_point (tuple(int, int)): Coordinate of the start point.
        end_point (tuple(int, int)): Coordinate of the end point.
    """
    if grid <= 2:
        raise ValueError("Grid size must be greater than 2")
    grid = grid - 1
    check_grid = [
        grid < start_point[0],
        grid < start_point[1],
        grid < end_point[0],
        grid < end_point[1],
    ]
    if True in check_grid:
        raise ValueError("Invalid start or end point, it must be within the grid")
    # Initialize the queue
    current_x = start_point[0]
    current_y = start_point[1]
    list_pos = [(current_x, current_y)]
    # move over x axis
    while current_x != end_point[0]:
        if current_x < end_point[0]:
            current_x = current_x + 1
        if current_x > end_point[0]:
            current_x = current_x - 1
        list_pos.append((current_x, current_y))
    # move over y axis
    while current_y != end_point[1]:
        if current_y < end_point[1]:
            current_y = current_y + 1
        if current_y > end_point[1]:
            current_y = current_y - 1
        list_pos.append((current_x, current_y))
    # remove the start point and end point
    list_pos = list_pos[1:-1]
    # calculate the path cost
    cost = len(list_pos)
    return JSONResponse(content={'cost': cost, 'path': list_pos})
