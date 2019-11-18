# Error handler for AYDA Application

# ==================== #
#     Requirements     #
# ==================== #

# Import dependencies from flask module
from flask import Blueprint, render_template

# ==================== #


# Define the blueprint: 'errors'
error_module = Blueprint('errors', __name__)


# Set the error handlers

# ========================= #
#     Error 403 Handler     #
# ========================= #
@error_module.app_errorhandler(403)
def error_403(error):
    return 'Error 403', 403
    # return render_template('errors/403.html', title='403'), 403


# ========================= #
#     Error 404 Handler     #
# ========================= #
@error_module.app_errorhandler(404)
def error_404(error):
    return 'Error 404', 404
    # return render_template('errors/404.html', title='404'), 404


# ========================= #
#     Error 500 Handler     #
# ========================= #
@error_module.app_errorhandler(500)
def error_500(error):
    return 'Error 500', 500
    # return render_template('errors/500.html', title='500'), 500
