from flask import Flask


def init_app(app: Flask) -> None:
    """init app."""
    from . import podcast
    from . import track
