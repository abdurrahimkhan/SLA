import pdb
from pprint import pprint

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, applications, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html
import fastapi_offline_swagger_ui
from os import path

import Oauth2
from api import crud
from database.database import SessionLocal
from schemas.schemas import User
from sqlalchemy.orm import Session

app = FastAPI()

''' 
This following code block necessary to switch offline cdn files via fastapi_offline_swagger_ui module
'''
assets_path = fastapi_offline_swagger_ui.__path__[0]
print(assets_path)

if path.exists(assets_path + "/swagger-ui.css") and path.exists(assets_path + "/swagger-ui-bundle.js"):
    app.mount("/assets", StaticFiles(directory=assets_path), name="static")


    def swagger_monkey_patch(*args, **kwargs):
        return get_swagger_ui_html(
            *args,
            **kwargs,
            swagger_css_url="/assets/swagger-ui.css",
            swagger_js_url="/assets/swagger-ui-bundle.js",
        )


    applications.get_swagger_ui_html = swagger_monkey_patch

origins = [
    "*",
    "http://localhost:3000",
]

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ALGORITHM = "HS256"


@app.get("/")
async def ping():
    """
    Pings the API.

    Returns:
        dict: A dictionary containing the message.
    """

    return {"message": "SLA Backend is running successfully"}


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/users/", response_model=list[User])
def get_all_users(db: Session = Depends(get_db)):
    users = crud.get_all_users(db)
    # us =
    # user_dicts = [vars(user) for user in users]
    # print(user_dicts)
    print(users)
    # pprint(vars(users[0]))
    # pdb.set_trace()
    return JSONResponse(users)


@app.post("/login/")
def login_for_access_token(email: str, password: str, db: Session = Depends(get_db)):
    return Oauth2.login(email, password, db)
