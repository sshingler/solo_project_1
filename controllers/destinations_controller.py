from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.trek import Trek
from models.destination import Destination 
import repositories.destination_repository as destination_repository
import repositories.trek_repository as trek_repository

destinations_blueprint = Blueprint("destinations", __name__)

@destinations_blueprint.route("/")
def destinations():
    destinations = destination_repository.select_all()
    return render_template("destinations/index.html", all_destinations = destinations)

@destinations_blueprint.route("/destinations/<id>/delete", methods = ['POST'])
def delete_destination(id):
    destination_repository.delete(id)
    return redirect ('/')

@destinations_blueprint.route("/destinations/new")
def new_destination():
    return render_template("destinations/new.html")



