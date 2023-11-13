from fastapi import FastAPI
import uvicorn
from config.database import engine
from todo import models

from todo.routers import user, item

app = FastAPI()
app.include_router(item.router)
app.include_router(user.router)
models.Base.metadata.create_all(engine)


@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run(app, port=8080)
