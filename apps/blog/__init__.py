from flask import Blueprint
blogBlue = Blueprint("blog",__name__)
from . import views,errors