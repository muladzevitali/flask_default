from typing import (Optional, List)

from flask_security import RoleMixin

from apps import db
from src.config import database

table_prefix = database.table_prefix


class Role(db.Model, RoleMixin):
    __tablename__ = f'{table_prefix}_roles'

    id = db.Column(db.Integer, db.Sequence(f'{table_prefix}_roles_id_seq', start=10000, increment=1), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
    parent_id = db.Column(db.Integer, db.ForeignKey(f'{__tablename__}.id'))
    parent = db.relationship("Role", remote_side=[id])
    users = db.relationship('User', secondary=f'{table_prefix}_users_roles_rel',
                            backref=db.backref(f'{table_prefix}_roles.role_id'), lazy='dynamic')

    def __str__(self):
        return self.name

    @staticmethod
    def get_parent_default(role: 'Role', roles_list: List['Role']):
        """Recursive function for obtaining parent roles"""
        parent_roles: Optional[List['Role']] = Role.query.filter(Role.id == role.parent_id).all()
        # If deputies run recursion for each deputy
        if parent_roles:
            roles_list.extend(parent_roles)
            for parent_role in parent_roles:
                Role.get_parent_default(parent_role, roles_list)

        return roles_list

    @property
    def get_parents(self) -> Optional[List['Role']]:
        """Get all parent roles for current role"""
        parent_roles: Optional[List['Role']] = self.get_parent_default(self, [])
        parent_roles.append(self)

        return parent_roles

    @property
    def get_functions(self) -> List[str]:
        return [f'{function.hash}' for function in self.application_functions]
