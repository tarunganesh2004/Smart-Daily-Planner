from flask import Flask
from app.routes import setup_routes
from app.models import db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database
db.init_app(app)

# Create database tables
with app.app_context():
    db.create_all()

# Initialize routes
setup_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
