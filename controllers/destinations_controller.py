from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.trek import Trek
from models.destination import Destination 
import repositories.destination_repository as destination_repository
import repositories.trek_repository as trek_repository

destinations_blueprint = Blueprint("destinations", __name__)

@destinations_blueprint.route("/destinations")
def destinations():
    destinations = destination_repository.select_all()
    return render_template("destinations/index.html", all_destinations = destinations)

@destinations_blueprint.route("/destinations/<id>/delete", methods = ['POST'])
def delete_destination(id):
    destination_repository.delete(id)
    return redirect ('/destinations')

@destinations_blueprint.route("/destinations/new", methods = ['GET'])
def new_destination():
    treks = trek_repository.select_all
    return render_template("destinations/new.html", all_treks = treks)

@destinations_blueprint.route("/destinations", methods = ['POST'])
def create_destination():
    destination_name = request.form['destination_name']
    country = request.form['country']
    continent = request.form['continent']
    destination = Destination (destination_name, country, continent)
    destination_repository.save(destination)
    return redirect ('/destinations')

@destinations_blueprint.route("/destinations/<id>", methods = ["GET"])
def show_destination(id):
    all_treks = trek_repository.select_all()
    destination = destination_repository.select(id)
    return render_template("destinations/show.html", destination = destination, all_treks = all_treks )

@destinations_blueprint.route("/destinations/<id>/edit", methods = ["GET"])
def edit_destination(id):
    destination = destination_repository.select(id)
    return render_template("destinations/edit.html", destination = destination)

@destinations_blueprint.route("/destinations/<id>", methods = ['POST'])
def update_destination(id):
    destination_name = request.form['destination_name']
    country = request.form['country']
    continent = request.form['continent']
    destination = Destination(destination_name, country, continent, id)
    destination_repository.update(destination)
    return redirect ("/destinations")