from flask import render_template,session,redirect,url_for
from . import blogBlue


@blogBlue.route("/demo/btn")
def btn():

    return render_template("/demo/btn.html")
@blogBlue.route("/demo/form")
def form():

    return render_template("/demo/form.html")
@blogBlue.route("/demo/table")
def table():

    return render_template("/demo/table.html")
@blogBlue.route("/demo/tab_card")
def tab_card():

    return render_template("/demo/tab_card.html")
@blogBlue.route("/demo/progress_bar")
def progress_bar():

    return render_template("/demo/progress_bar.html")
@blogBlue.route("/demo/folding_panel")
def folding_panel():

    return render_template("/demo/folding_panel.html")
@blogBlue.route("/demo/auxiliar")
def auxiliar():

    return render_template("/demo/auxiliar.html")
@blogBlue.route("/demo/add_edit")
def add_edit():

    return render_template("/demo/add_edit.html")
@blogBlue.route("/demo/data_table")
def data_table():

    return render_template("/demo/data_table.html")