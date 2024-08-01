
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.dbibnqaixuihilmanvwq:auroraprimegroup3@aws-0-eu-central-1.pooler.supabase.com:6543/postgres'
    app.config['JWT_SECRET_KEY'] = 'your-jwt-secret-key'

    
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    from .auth_route import auth_blueprint
    app.register_blueprint(auth_blueprint)

    

    return app