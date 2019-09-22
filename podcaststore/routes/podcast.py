#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from flask import jsonify, request
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from podcaststore.app import db, app, api_version
from podcaststore.models.podcast import Podcast, PodcastSchema


@app.route(f"/{api_version}/podcast", methods=["GET"])
def podcast_get():
    podcasts = Podcast.query.all()
    podcast_schema = PodcastSchema(many=True)
    return jsonify(podcast_schema.dump(podcasts))


@app.route(f"/{api_version}/podcast", methods=["POST"])
def podcast_post():

    try:
        serd = PodcastSchema().load(json.loads(request.data))
        podcast = Podcast(**serd)
        db.session.add(podcast)
        db.session.commit()
        return "", 201
    except ValidationError as err:
        return f"error: {err.messages}", 400
    except IntegrityError as err:
        return f"error: {str(err)}", 409
