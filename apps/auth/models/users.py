from datetime import timedelta
from hashlib import sha256
from typing import (List, Optional)

from flask_login import (AnonymousUserMixin, login_user, logout_user)
from flask_security import (UserMixin)

from apps import db
from src.config import database

table_prefix = database.table_prefix


class User(db.Model, UserMixin):
    __tablename__ = f'{table_prefix}_users'

    id = db.Column(db.Integer, db.Sequence(f'{table_prefix}_users_id_seq', start=10000), primary_key=True)
    authenticated = db.Column(db.Boolean(), default=0)
    active = db.Column(db.Boolean(), default=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(64), nullable=False)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    manager_id = db.Column(db.Integer, db.ForeignKey(f'{table_prefix}_users.id'))
    manager = db.relationship("User", remote_side=[id])
    roles = db.relationship('Role', secondary=f'{table_prefix}_users_roles_rel',
                            backref=db.backref(f'{table_prefix}_users.user_id'), lazy='dynamic')

    def create_user(self, username: str, first_name: str, last_name: str, email: str, password: str):
        """Create user and insert into database"""
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = self.hash_password(password)

        db.session.add(self)
        db.session.commit()

    @staticmethod
    def hash_password(password: str) -> hex:
        """Password hashing handler"""

        return sha256(password.encode()).hexdigest()

    def __repr__(self):
        return '%s' % self.username

    def __str__(self):
        return '%s' % self.username

    def get_id(self):
        return self.username

    def has_role(self, role_name: str) -> bool:
        """Check if the user has given role"""
        if any([role.name == role_name for role in self.roles]):
            return True

        return False

    @staticmethod
    def get_by_id(id_: int) -> 'User':
        """Get user by id"""
        user: 'User' = User.query.filter(User.id == id_).first()

        return user

    def is_authenticated(self):
        return self.authenticated

    @staticmethod
    def get_deputies(current_user: 'User', users_list: List['User']):
        """Recursive function for obtaining deputy users"""
        deputies: Optional[List['User']] = User.query.filter(User.manager_id == current_user.id).all()
        # If deputies run recursion for each deputy
        if deputies:
            users_list.extend(deputies)
            for deputy in deputies:
                User.get_deputies(deputy, users_list)

        return users_list

    def get_deputy_tree(self) -> Optional[List['User']]:
        """Get all deputies for current user INCLUDING SELF"""
        deputies_tree: Optional[List['User']] = self.get_deputies(self, [])
        deputies_tree.append(self)

        return deputies_tree

    @property
    def serialize(self):
        data = {'email': self.email, 'first_name': self.first_name,
                'last_name': self.last_name, 'username': self.username}

        return data

    def login(self):
        """Login user respect to flask_login"""
        self.authenticated = True
        db.session.add(self)
        db.session.commit()
        login_user(self, remember=False, duration=timedelta(hours=6))

    def logout(self):
        """Logout user respect to flask_login"""
        self.authenticated = False
        db.session.add(self)
        db.session.commit()
        logout_user()


class AnonymousUser(AnonymousUserMixin, UserMixin):
    def __init__(self):
        self.first_name = "Guest"
        self.username = "Anonymous"
        self.email = "anonymous@bog.ge"
        self.authenticated = False
        self.id = -1
        self.phone_validated = 0
        self.is_anonymous = True
        self.password = "anonymous"
        self.active = False
        self.roles = []

    def get_user_id(self):
        return self.id

    def has_role(self, role):
        return False

    def is_anonymous(self):
        return True
