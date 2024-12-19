from flask import Flask, request, Blueprint, render_template, jsonify
from utils import add_value

values_bp = Blueprint("values", __name__)

@values_bp.route('/')
def home():
    return render_template('index.html')

@values_bp.route("/value", methods=["POST"])
def handle_request():        
    if request.method == "POST":
        return add_value(request.json["value"])

if __name__ == "__main__":
    app.run()