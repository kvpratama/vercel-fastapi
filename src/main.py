from fastapi import FastAPI
from api.hello import router

app = FastAPI()
app.include_router(router)
