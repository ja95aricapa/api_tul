import uvicorn
from controllers import prediction, grid
from fastapi import FastAPI

app = FastAPI()

app.include_router(prediction.router)
app.include_router(grid.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
