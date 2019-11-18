# Configuration for the Web Application

# ==================== #
#     Requirements     #
# ==================== #
import os

basedir = os.path.abspath(os.path.dirname(__file__))
database = 'app.db'

# Configuration
class Config:
    SECRET_KEY = 'aa03bf97f3ff64982f6bc9a6cc0f10fb5d79d718e2f55071259400971e4fdaac'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, database)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/'+database
    SQLALCHEMY_TRACK_MODIFICATIONS = False