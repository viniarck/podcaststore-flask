#!/usr/bin/env python
# -*- coding: utf-8 -*-

from podcaststore.app import db, ma
from .track import Track


class Tag(db.Model):

    """Tag record."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    track_id = db.Column(db.Integer, db.ForeignKey("track.id"))
    track = db.relationship(Track, backref=db.backref("tags"))

    def __repr__(self) -> str:
        """Tag __repr__."""
        return f"Tag({self.id}, {self.name})"


class TagSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "track_id")
