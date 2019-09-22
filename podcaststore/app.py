#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config["DEBUG"] = True
DB_NAME = os.environ.get("DB_NAME", "podcast_api")
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PW = os.environ.get("DB_PW", "db_pass")
DB_USER = os.environ.get("DB_USER", "db_user")
DB_PORT = os.environ.get("DB_PORT", 5432)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://{DB_USER}:{DB_PW}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
db = SQLAlchemy(app)
ma = Marshmallow(app)
api_version = "v1"

from . import models, routes

models.init_app(app)
routes.init_app(app)


def create_all() -> None:
    """Create all tables."""
    db.create_all()


create_all()
