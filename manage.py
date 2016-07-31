#!/usr/bin/env python
import os
from app import create_app, db
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app(os.environ.get('FLASK_CONFIG', 'default'))
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)

from app.authentication.models import User

@manager.command
def adduser(email, username):
    """Register a new User"""
    from getpass import getpass
    name = raw_input('Full Name: ')
    password = getpass()
    password2 = getpass(prompt='Confirm: ')
    if password != password2:
        import sys
        sys.exit('Error: Password do not match')
    db.create_all()
    user = User(name=name, email=email, username=username, password=password)
    db.session.add(user)
    db.session.commit()
    print('User {0} was successfully created'.format(username))

if __name__ == '__main__':
    manager.run()
