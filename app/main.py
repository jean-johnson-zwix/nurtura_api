from fastapi import FastAPI
import model
from config import engine
from router import router
import config
from functools import lru_cache

model.Base.metadata.create_all(bind=engine)
app = FastAPI()

@lru_cache
def get_settings():
    return config.Settings()

@app.get('/')
async def hello_world():
    return {"message":"Hello World"}

app.include_router(router,prefix="/auth", tags=["user management"])