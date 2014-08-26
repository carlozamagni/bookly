import datetime
import infrastructure

__author__ = 'carlozamagni'


db = infrastructure.db


class Message(db.EmbeddedDocument):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    body = db.StringField(verbose_name="review", required=True)
    author = db.StringField(verbose_name="author_id", max_length=255, required=True)
    author_user_name = db.StringField(verbose_name="author_user_name", max_length=255, required=True)

    def __unicode__(self):
        return '%s - %s' % (self.created_at, self.author)