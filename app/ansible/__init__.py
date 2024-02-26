from flask import Blueprint

bp = Blueprint('ansible', __name__)


from app.ansible import routes