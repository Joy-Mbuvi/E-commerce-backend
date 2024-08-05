from app import create_app,db
from app.models import Product

app = create_app()
app.app_context().push()

products=[]

products.append(Product(name="complete skateboard",description="High-quality complete skateboard ",price=5000,stock=50))
products.append(Product(name="skateboard decks",description=" Skateboard decks with customizable designs and sizes.",price=4500,stock=180))
products.append(Product(name="longboards",description="Smooth-riding longboards perfect for cruising around the city.",price=11000,stock=50))
products.append(Product(name="penny boards",description=" Compact and colorful penny boards for easy transportation",price= 4000,stock=150))
products.append(Product(name="Skateboard Trucks",description="Durable skateboard trucks for stability and control.",price=2500,stock=20))
products.append(Product(name="Skateboard wheels",description="High-performance skateboard wheels in various sizes and hardness.",price=2000,stock=250))
products.append(Product(name="Skateboard Bearings",description=" Smooth and fast skateboard bearings.",price=1000,stock=160,))
products.append(Product(name="Grip Tape",description="High-quality grip tape with various designs",price=700,stock=50))
products.append(Product(name="Helemts",description="Stylish and safe helmets ",price=3000,stock=100))
products.append(Product(name="Knee Pads",description="comfortable and protective knee pads",price=2000,stock=70))
products.append(Product(name="elbow pads",description="durable elbow pads for added protection",price=2000,stock=60))
products.append(Product(name="wrist guards",description="essential wrist guards to prevent injuries",price=300,stock=80))
products.append(Product(name="full protective gear",description="complete set including helmet,knee pads,elbow pads and wrist guards",price=7000,stock=150))
products.append(Product(name="skate shoes",description="High-quality skate shoes designed for durability and style",price=5000,stock=150))
products.append(Product(name="Trendy Tees",description="high fashion skater Tees",price=1500,stock=45))
products.append(Product(name="Hoodies",description="keeping it clean with high quality hoddies",price=3000,stock=45))
products.append(Product(name="Skate Pants",description="stylish and durable pants",price=3000,stock=45))
products.append(Product(name="Caps and Beanies",description="protection from the Nairobi sun",price=500,stock=45))
products.append(Product(name="Backpacks",description="The bearer that carrys skateboards and gear",price=1000,stock=20))
products.append(Product(name="The skateboard toolkit",description="multi-functional tools for skateboard maintenance",price=2500,stock=30))
products.append(Product(name="Phone holders",description="Phone holders that can be attached to skateboards for capturing rides.",price=1500,stock=50))
products.append(Product(name="Socks",description="Comfortable and stylish socks for skateboarders",price=500,stock=80,))
products.append(Product(name="Water Bottles",description="Durable water bottles with skateboarding designs.",price= 800,stock= 60))
products.append(Product(name="Skateboard Wall Mounts",description="Wall mounts to display skateboards at home.",price=2000,stock=70))
products.append(Product(name=" Stickers",description="Stickers for personalizing skateboards",price=50,stock=500))

db.session.add_all(products)

db.session.commit()