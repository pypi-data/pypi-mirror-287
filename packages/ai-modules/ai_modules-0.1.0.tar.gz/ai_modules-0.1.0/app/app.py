# app.py
from fastapi import FastAPI

def create_app():
    app = FastAPI(title="AI-Modules: Python Object Data AI System API")
    return app