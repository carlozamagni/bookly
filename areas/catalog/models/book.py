import uuid
import datetime
import infrastructure


__author__ = 'carlozamagni'


db = infrastructure.db


class Book(db.Document):
    id = db.StringField(primary_key=True, default=str(uuid.uuid4()))
    isbn = db.StringField(required=True, max_length=40)
    title = db.StringField(max_length=200)
    owner = db.StringField(required=True)
    status = db.IntField(required=True, choices=[1, 2, 3, 4, 5])
    notes = db.StringField(max_length=5000)
    created_at = db.DateTimeField(required=False, default=datetime.datetime.utcnow())

    def __unicode__(self):
        return '%s - %s' % (self.isbn, self.title)