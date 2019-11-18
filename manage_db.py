# File to manage Database for Web Application
from app import create_app, manager
from sqlalchemy_utils import create_database, database_exists


app = create_app()

class CreateDB():
  url = app.config['SQLALCHEMY_DATABASE_URI']
  
  if not database_exists(url):
      create_database(url)
  else:
    print("Database already exist!")

# Import database model to be migrated
# at the first time
from app.models import User

if __name__ == '__main__':
  CreateDB()
  manager.run()