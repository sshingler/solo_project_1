from flask import Flask, render_template, request, redirect
from flask import Blueprint


treks_blueprint = Blueprint("treks", __name__)