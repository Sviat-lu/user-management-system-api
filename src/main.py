import uvicorn
from fastapi import FastAPI

from api.v1.router import api_v1_router
from configs import app_settings

app = FastAPI()
app.include_router(api_v1_router)

if __name__ == "__main__":
    uvicorn.run(
        "__main__:app",
        host=app_settings.APP_HOST,
        port=app_settings.APP_PORT,
        reload=True,
    )
