from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.dbibnqaixuihilmanvwq:auroraprimegroup3@aws-0-eu-central-1.pooler.supabase.com:6543/postgres'
    app.config['JWT_SECRET_KEY'] = 'your-jwt-secret-key'

    
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    from .auth_route import auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .product_route import product_blueprint
    app.register_blueprint(product_blueprint)

    from .order_route import order_routes
    app.register_blueprint(order_routes)

    from .cart_route import cart_routes
    app.register_blueprint(cart_routes)

    from .favourite_route import favourite_blueprint
    app.register_blueprint(favourite_blueprint)
    

    return app