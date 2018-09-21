from flask import render_template
from . import blogBlue

@blogBlue.app_errorhandler(404)
def page_not_found(e):
    render_template("404.html"),404