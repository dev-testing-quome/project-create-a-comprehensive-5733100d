import uvicorn
from fastapi import FastAPI, Request, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import os

from database import engine
from routers import patient_router, appointment_router # Add other routers as needed

#Import models here if needed for database initialization
# from models import Base

app = FastAPI()

# CORS Configuration
origins = ["*"] # Update with your allowed origins in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
)

# Database Initialization
#Base.metadata.create_all(bind=engine)

# Router Registration
app.include_router(patient_router)
app.include_router(appointment_router) # Add other routers here

# Health Check Endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}

# Static Files Serving
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")
    @app.get("/{{"file_path:path}}")
    async def serve_frontend(file_path: str, request: Request):
        if file_path.startswith("api"):
            return None # Let API routes handle it
        static_file = os.path.join("static", file_path)
        if os.path.isfile(static_file):
            return FileResponse(static_file)
        return FileResponse("static/index.html") # SPA routing

# Exception Handling
@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})

#Start the application
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
