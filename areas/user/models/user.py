import datetime
import uuid
import infrastructure
# import bson.objectid

__author__ = 'cazamagni'


db = infrastructure.db

# see: https://github.com/mrjoes/flask-admin/blob/master/examples/auth-mongoengine/auth.py


class User(db.Document):
    #id = db.ObjectIdField()
    id = db.StringField(primary_key=True, default=str(uuid.uuid4()))
    first_name = db.StringField(max_length=40)
    last_name = db.StringField(max_length=40)
    role = db.StringField(default=str('us'))
    user_name = db.StringField(required=True, unique=True)
    password = db.StringField()
    created_at = db.DateTimeField(required=False, default=datetime.datetime.utcnow())

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<User %r>' % self.name

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        # return self.id
        return str(self.id)

    def get_string_id(self):
        return str(self.id)

    def get_role(self):
        return self.role

    def get_user_home(self):
        # role = db['roles'].find_one({'_id': self.get_role()})
        # return role['home_page']
        # return '/user/home/%s' % (str(self.id))
        return '/user/'