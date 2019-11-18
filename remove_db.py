# File to remove database from Web Application
import shutil
import os
from app import create_app
from sqlalchemy_utils import database_exists, drop_database


app = create_app()

class DropDB():
    url = app.config['SQLALCHEMY_DATABASE_URI']
    basedir = os.path.abspath(os.path.dirname(__file__))
    folder = os.path.join(basedir, 'migrations')

    if not database_exists(url):
        print("Database does not exist!")
    else:
        drop_database(url)
        if os.path.isdir(folder):
            shutil.rmtree(folder)
            print('Migrations has been removed!')
        print('Database has been removed!')


if __name__ == '__main__':
  DropDB()