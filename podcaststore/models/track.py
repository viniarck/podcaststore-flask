from podcaststore.app import db, ma
from .podcast import Podcast


class Track(db.Model):

    """Track record."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    podcast_id = db.Column(db.Integer, db.ForeignKey("podcast.id"))
    podcast = db.relationship(Podcast, backref=db.backref("tracks"))
    media_url = db.Column(db.String(255), nullable=True)
    release_date = db.Column(db.Date, nullable=True)
    duration = db.Column(db.DateTime, nullable=True)

    def __repr__(self) -> str:
        """Podcast __repr__."""
        return f"Track({self.id}, {self.title})"


class TrackSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "podcast_id", "media_url", "duration")
