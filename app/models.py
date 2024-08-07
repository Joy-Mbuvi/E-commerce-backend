from . import db

class User(db.Model):
    __tablename__='user'

    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    hash_password=db.Column(db.String(140),unique=True,nullable=False)
    orders = db.relationship('Order', backref='user', lazy=True)
    cart = db.relationship('Cart', backref='user', uselist=False)

    def __repr__(self):
        return f'<User {self.username}>'


class Product(db.Model):
    __tablename__='product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    image_url= db.Column(db.Text,nullable=True)

class CartItem(db.Model):
    __tablename__ = 'cart_item'
    
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)

    cart = db.relationship('Cart', back_populates='items')
    product = db.relationship('Product')

class Cart(db.Model):
    __tablename__='cart'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id= db.Column(db.Integer,db.ForeignKey('product.id'))
    quantity= db.Column(db.Integer)
    items = db.relationship('CartItem', back_populates='cart', cascade='all, delete-orphan')

class Order(db.Model):
    __tablename__='order'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='Pending')
    total_price = db.Column(db.Float, nullable=False)

