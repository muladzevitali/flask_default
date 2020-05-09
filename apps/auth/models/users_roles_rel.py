from apps import db
from src.config import database

table_prefix = database.table_prefix


class UserRoleRel(db.Model):
    __tablename__ = f'{table_prefix}_users_roles_rel'

    id = db.Column(db.Integer, db.Sequence(f'{table_prefix}_users_roles_rel_id_seq', start=10000), primary_key=True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey(f'{table_prefix}_users.id'))
    role_id = db.Column('role_id', db.Integer, db.ForeignKey(f'{table_prefix}_roles.id'))
