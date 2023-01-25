"""
Run this file
"""
import magic
from uuid import uuid4

import uvicorn
from starlette import status
from starlette.responses import HTMLResponse

from settings import config
from settings.app import app, templates
from settings.file_types import SUPPORTED_FILE_TYPE
from src.helpers import s3_upload

from fastapi import UploadFile, HTTPException, Request


@app.get("/")
def test():
    """ Nimble AWS S3 """
    return "Nimble AWS S3 Upload and Download file"


@app.get("/files", response_class=HTMLResponse)
def file_upload(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("upload_file.html", context)


@app.post("/upload")
async def upload(file: UploadFile | None = None):
    """
    Upload main function
    :param file: File
    :return: Status
    """
    if not file:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="File not found!"
        )

    contents = await file.read()
    file_type = magic.from_buffer(buffer=contents, mime=True)

    if file_type not in SUPPORTED_FILE_TYPE:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unsupported file type: {file_type}. Supported file are {SUPPORTED_FILE_TYPE}"
        )

    await s3_upload(contents=contents, key=f"{uuid4()}.{SUPPORTED_FILE_TYPE[file_type]}")

    return {
        "status": "ok",
        "info": "Upload file success"
    }


def start():
    """ Starts webserver with uvicorn """
    uvicorn.run(app, host=config.API_HOST, port=int(config.API_PORT))


if __name__ == '__main__':
    start()
