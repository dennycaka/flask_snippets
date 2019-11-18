# Declaring models to be defined in the database

# ==================== #
#     Requirements     #
# ==================== #

# Import datetime module
from datetime import datetime

# Imprt current app
from flask import current_app

# Import UserMixin object
from flask_login import UserMixin

# Import objects from lpd Application
from app import db, login_manager, marsh


# Define a base model for other database tables to inherit
class Base(db.Model):
    __abstract__ = True
    __table_args__ = {'extend_existing': True}
    # Attribute
    id = db.Column(db.Integer, primary_key=True)
    # Timestamps
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_modified = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# ================================ #
#     Handle load user session     #
# ================================ #
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ============================= #
#     User model and schema     #
# ============================= #
class User(Base, UserMixin):
    # Table name
    __tablename__ = 'user'

    # Attributes
    username = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    
    # Relationship
    # posts = db.relationship('Post', backref='author', lazy=True)

    # Constructor
    def __init__(self, username, name, email, password):
        self.username = username
        self.name = name
        self.email = email
        self.password = password

    # Representation
    def __repr__(self):
        return (f"User {self.username} ('{self.name}', {self.email})")


# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     content = db.Column(db.Text, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#     def __repr__(self):
#         return f"Post('{self.title}', '{self.date_posted}')"