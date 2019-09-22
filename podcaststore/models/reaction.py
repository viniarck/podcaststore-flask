#!/usr/bin/env python
# -*- coding: utf-8 -*-


from .user import User
from .track import Track
from podcaststore.app import db, ma


class Reaction(db.Model):

    """Reaction record."""

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship(User, backref=db.backref("users_reactions"))
    track_id = db.Column(db.Integer, db.ForeignKey("track.id"))
    track = db.relationship(Track, backref=db.backref("track_reactions"))
    deleted_on = db.Column(db.DateTime, nullable=True)
    code = db.Column(db.String(16))

    def __repr__(self) -> str:
        """Reaction __repr__."""
        return f"Reaction({self.id}, {self.code})"


class ReactionSchema(ma.Schema):
    class Meta:
        fields = ("id", "user_id", "track_id", "deleted_on", "code")
