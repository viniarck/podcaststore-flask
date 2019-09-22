#!/usr/bin/env python
# -*- coding: utf-8 -*-

from podcaststore.app import db, ma


class Podcast(db.Model):

    """Podcast record."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    title = db.Column(db.String(255), nullable=True)
    start_date = db.Column(db.Date, nullable=True)

    def __repr__(self) -> str:
        """Podcast __repr__."""
        return f"Podcast({self.id}, {self.name})"


class PodcastSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "title", "start_date")
