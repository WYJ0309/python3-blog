from flask import Blueprint
blogBlue = Blueprint("blog",__name__,url_prefix="/blog")

from . import views,errors