# Main module for AYDA Application

# ==================== #
#     Requirements     #
# ==================== #

# Import dependencies from flask module
from flask import Blueprint, current_app, jsonify, redirect, render_template, url_for
# Import requirement of session management
from flask_login import current_user, login_required

# ==================== #

# Define the blueprint: 'main', set its url prefix: app.url/
main_module = Blueprint('main', __name__, url_prefix='/')

# Set the routes and accepted methods

# ================== #
#     Home Route     #
# ================== #
@main_module.route("/", methods=['GET', 'POST'])
# @login_required
def home():
    data = current_app.config['SECRET_KEY']
    return f"{data}"

# ==================== #
#     Public Route     #
# ==================== #
@main_module.route("/public", methods=['GET', 'POST'])
def public():
    return "Hello Stranger"