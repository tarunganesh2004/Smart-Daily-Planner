from flask import Flask
from app.routes import setup_routes
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize routes
setup_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
