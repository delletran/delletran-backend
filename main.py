import json
import os

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['get'],
    allow_headers=["*"],
)


class APIQueryParams(BaseModel):
    _status: str
    
    
@app.get("/")
async def root():
    return JSONResponse({
        "message": "Details",
        "status": 200,
        "routes": {
            "root": {
                "path": '/',
                "querY_params": None,
            },
            "api": {
                "path": '/api',
                "querY_params": None,
            }
            
        }
    })

@app.get('/api/')
async def api_root( _status:str = Query(None)):
    response = {
        "message": "OK",
        "status": 200,
        "route": "/api"
    }
    
    return JSONResponse(response)


@app.get('/api/test_query')
async def api_test_query( q:str = Query(None)):
    response = {
        "message": "OK",
        "status": 200,
        "route": "/api",
        "queries": q
    }
    
    return JSONResponse(response)


# if __name__ == "__main__":
#   uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)