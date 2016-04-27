# manage.py

from flask.ext.script import Manager

from app.application import create_app
app = create_app()

from app.models import User, Role, ROLE_DATA
from app.views.user import get_all

manager = Manager(app)

@manager.command
def hello():
  print "hello"

@manager.command
def num_users():
  print "NUM USERS: %s " % User.objects.count()

@manager.command
def call_route_test():
  print "ALL USERS: %s " % get_all()


@manager.command
def add_user_role(username, role_name):
  print "username, role_name:",username, role_name
  new_role = Role.objects(name=role_name).get()
  print "Role %s" % new_role.name
  user = User.objects(username=username).first()
  if not user:
    print "Could not find user with username: %s" % username
    return
  for role in user.roles:
    if role.name == role_name:
      print "User %s already has %s role" % (username, role_name)
      return
  user.update(push__roles=new_role)
  print "Added %s role to %s" % (role_name, username)


@manager.command
def revoke_user_role(username, role_name):
  print "username, role_name:",username, role_name
  role = Role.objects(name=role_name).get()
  print "Role %s" % role
  user = User.objects(username=username).first()
  if not user:
    print "Could not find user with username: %s" % username
    return
  has_role = False
  for role in user.roles:
    if role.name == role_name:
      has_role = True
  if not has_role:
    print "User %s does not have %s role" % (username, role_name)
  else:
    user.update(pull__roles=role)
    print "Revoked role %s from %s" % (role_name, username)


@manager.command
def seed_roles():
  for name, description in ROLE_DATA:
    try:
      Role.objects(name=name).get()
    except Exception as e:
      print "No role for name %s, exception: %s" % (name, e)
      Role(name=name, description=description).save()
      print "Created Role %s" % name

if __name__ == "__main__":
  manager.run()