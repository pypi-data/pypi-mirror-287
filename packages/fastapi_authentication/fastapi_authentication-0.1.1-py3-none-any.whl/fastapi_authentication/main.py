from fastapi import FastAPI
from fastapi_auth import models
from fastapi_auth.routes import auth_with_otp
from fastapi_auth.con import engine
app = FastAPI()

models.Base.metadata.create_all(bind=engine)
@app.get("/")
async def root():
    return {"message":"helth check working.............."}


app.include_router(auth_with_otp.router)
