#!/usr/bin/env python
# -*- coding: utf-8 -*-

from podcaststore.app import app


@app.route("/")
def index() -> None:
    """docstring."""
    return "nice"
