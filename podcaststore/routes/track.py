#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import jsonify
from podcaststore.app import db, ma, app, api_version
from podcaststore.models.track import Track, TrackSchema


@app.route(f"/{api_version}/track", methods=["GET"])
def track_get():
    tracks = Track.query.all()
    track_schema = TrackSchema(many=True)
    return jsonify(track_schema.dump(tracks))
