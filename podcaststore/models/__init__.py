#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask


def init_app(app: Flask) -> None:
    """init app."""
    from . import podcast
    from . import track
    from . import tag
    from . import user
    from . import reaction
    from . import download
