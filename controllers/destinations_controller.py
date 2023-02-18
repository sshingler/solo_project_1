from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.destination import Destination 
from models.trek import Trek
import repositories.destination_repository as destination_repository
import repositories.trek_repository as trek_repository

treks_blueprint = Blueprint("treks", __name__)

@treks_blueprint.route("/destinations")
def destinations():
    destinations = destination_repository.select_all()
    return render_template ("destinations/index.html", all_destinations = destinations)
    