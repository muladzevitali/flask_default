from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from apps import (create_app, db)
from apps.auth.models import (User, Role, UserRoleRel)
from src.config import application as application_config
from src.scripts import create_users

application = create_app(application_config)
tables = [User.__table__, Role.__table__, UserRoleRel.__table__]
migrate = Migrate(application, db, max_identifier_length=128)

manager = Manager(application)
manager.add_command('db', MigrateCommand)


@manager.command
def reset_database():
    with application.app_context():
        db.metadata.drop_all(db.engine, tables=tables)
        db.metadata.create_all(db.engine, tables=tables)
        create_users(User, Role, db)


if __name__ == '__main__':
    manager.run()
