from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.trek import Trek
from models.destination import Destination 
import repositories.destination_repository as destination_repository
import repositories.trek_repository as trek_repository

treks_blueprint = Blueprint("treks", __name__)

@treks_blueprint.route("/treks")
def treks():
    treks = trek_repository.select_all()
    return render_template ("treks/index.html", all_treks = treks)

@treks_blueprint.route("/treks/<id>/delete", methods = ['POST'])
def delete_trek(id):
    trek_repository.delete(id)
    return redirect ('/treks')

@treks_blueprint.route("/treks/<id>", methods = ["GET"])
def show_trek(id):
    trek = trek_repository.select(id)
    return render_template("treks/show.html", trek = trek)