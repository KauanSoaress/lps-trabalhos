from flask import Flask
from blueprint import values_bp

app = Flask(__name__)

app.register_blueprint(values_bp)

if __name__ == "__main__":
    app.run()