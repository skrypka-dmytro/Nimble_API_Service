"""
Setting up fastapi app
"""
import fastapi
from fastapi.templating import Jinja2Templates

from settings import config


app = fastapi.FastAPI(
    title=config.APP_NAME,
)

templates = Jinja2Templates(directory="templates")
