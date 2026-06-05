from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import os

from database import get_connection, init_db

app = Flask(__name__)
CORS(app)

init_db()

# ==========================================
# ROTA INICIAL
# ==========================================

@app.route("/")
def home():
    return jsonify({
        "mensagem": "API funcionando",
        "status": "ok"
    })