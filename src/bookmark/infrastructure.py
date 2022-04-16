from cerberus import Validator
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
cors = CORS()
migrate = Migrate()
validator = Validator()
