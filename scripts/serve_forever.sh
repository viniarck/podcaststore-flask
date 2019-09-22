#!/bin/sh

echo "Starting gunicorn over HTTP..."
gunicorn -w 4 -b 0.0.0.0:8000 podcaststore.app
