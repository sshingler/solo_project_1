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

@treks_blueprint.route("/treks/completed")
def completed_treks():
    treks = trek_repository.select_all()
    return render_template ("treks/completed.html", all_treks = treks)

@treks_blueprint.route("/treks/uncompleted")
def uncompleted_treks():
    treks = trek_repository.select_all()
    return render_template ("treks/incomplete.html", all_treks = treks)

@treks_blueprint.route("/treks/<id>/delete", methods = ['POST'])
def delete_trek(id):
    trek_repository.delete(id)
    return redirect ('/treks')

@treks_blueprint.route("/treks/new", methods = ['GET'])
def new_trek():
    destinations = destination_repository.select_all()
    return render_template("/treks/new.html", all_destinations = destinations)


@treks_blueprint.route("/treks", methods = ['POST'])
def create_trek():
    trek_name = request.form['trek_name']
    trek_distance = request.form['trek_distance']
    trek_days = request.form['trek_days']
    trek_headline = request.form['trek_headline']
    trek_completed = True if "trek_completed" in request.form else False 
    trek_notes = request.form['trek_notes']
    destination = destination_repository.select(request.form['destination_id'])
    trek = Trek(trek_name, trek_distance, trek_days, trek_headline, trek_completed, trek_notes, destination)
    trek_repository.save(trek)
    return redirect ('/treks')


@treks_blueprint.route("/treks/<id>", methods = ["GET"])
def show_trek(id):
    trek = trek_repository.select(id)
    return render_template("treks/show.html", trek = trek)

@treks_blueprint.route("/treks/<id>/edit", methods = ["GET"])
def edit_trek(id):
    trek = trek_repository.select(id)
    destinations = destination_repository.select_all()
    return render_template("treks/edit.html", trek = trek, all_destinations = destinations)

@treks_blueprint.route("/treks/<id>", methods = ['POST'])
def update_trek(id): 
    trek_name = request.form['trek_name']
    trek_distance = request.form['trek_distance']
    trek_days = request.form['trek_days']
    trek_headline = request.form['trek_headline']
    trek_completed = True if "trek_completed" in request.form else False
    trek_notes = request.form['trek_notes']
    destination = destination_repository.select(request.form['destination_id'])
    trek = Trek(trek_name, trek_distance, trek_days, trek_headline, trek_completed, trek_notes, destination, id)
    trek_repository.update(trek)
    return redirect ('/treks')

