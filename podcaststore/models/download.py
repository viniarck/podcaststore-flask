#!/usr/bin/env python
# -*- coding: utf-8 -*-


from podcaststore.app import db, ma
from .track import Track


class Download(db.Model):

    """Download record."""

    id = db.Column(db.Integer, primary_key=True)
    track_id = db.Column(db.Integer, db.ForeignKey("track.id"))
    track = db.relationship(Track, backref=db.backref("downloads"))
    date = db.Column(db.DateTime)

    def __repr__(self) -> str:
        """Download __repr__."""
        return f"Download({self.id}, {self.track.id}, {self.date})"


class PodcastSchema(ma.Schema):
    class Meta:
        fields = ("id", "track_id", "date")
