#!/usr/bin/env python
# -*- coding: utf-8 -*-

from podcaststore.app import db, ma


class User(db.Model):

    """User record."""

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    is_active = db.Column(db.Boolean, default=True)
    # TODO hash the password
    password = db.Column(db.String(255))
    # TODO make both created_on and updated_on generic for any model
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now()
    )

    def __repr__(self) -> str:
        """User __repr__."""
        return f"User({self.id}, {self.email})"


class UserSchema(ma.Schema):
    class Meta:
        fields = ("email", "password")
