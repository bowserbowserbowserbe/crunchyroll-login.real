from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from crunchyroll import Crunchyroll
import uvicorn

app = FastAPI()

class LoginRequest(BaseModel):
    email: str
    password: str

@app.post("/login")
async def login(data: LoginRequest):
    try:
        session = await Crunchyroll.login(data.email, data.password)
        return {
            "success": True,
            "username": session.user.name
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

if __name__ == "__main__":
    import os
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
