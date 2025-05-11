from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from crunchyroll import Crunchyroll
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LoginRequest(BaseModel):
    email: str
    password: str

@app.post("/login")
async def login(data: LoginRequest):
    try:
        session = await Crunchyroll.login(data.email, data.password)
        return JSONResponse(
            content={
                "success": True,
                "username": session.user.name
            },
            status_code=200
        )
    except Exception as e:
        return JSONResponse(
            content={
                "success": False,
                "error": str(e)
            },
            status_code=200
        )

if __name__ == "__main__":
    import os
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
