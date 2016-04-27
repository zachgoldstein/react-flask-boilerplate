from flask.ext.mongoengine import MongoEngine
import json

db = MongoEngine()

ROLE_DATA = [("User", "Default user"),
             ("User Manager", "A user that manages a group of other users"),
             ("Admin", "The root admin, with full access")]


class Role(db.Document):
  name = db.StringField(max_length=80, choices=[x[0] for x in ROLE_DATA], unique=True)
  description = db.StringField(max_length=255)


class User(db.Document):
  username = db.StringField(max_length=255)
  password = db.StringField(max_length=255)
  roles = db.ListField(db.ReferenceField(Role), default=[])

  def id_str(self):
    return str(self.id)

  def has_role(self, role_name):
    print "checking for role_name %s" % role_name
    for role in self.roles:
      print "Role.name  %s" % role.name
      if role.name == role_name:
        return True
    return False
