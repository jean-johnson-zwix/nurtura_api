from fastapi import FastAPI
import model
from config import engine
from router import router
import config
from functools import lru_cache
from fastapi.middleware.cors import CORSMiddleware


model.Base.metadata.create_all(bind=engine)
app = FastAPI()


'''
origins = [
    "http://localhost:3000",
    "https://your-frontend-domain.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
'''

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@lru_cache
def get_settings():
    return config.Settings()

@app.get('/')
async def hello_world():
    return {"message":"Hello World"}

app.include_router(router,prefix="/auth", tags=["user management"])