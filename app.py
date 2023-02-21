from flask import Flask, render_template

from controllers.destinations_controller import destinations_blueprint
from controllers.treks_controller import treks_blueprint

import repositories.trek_repository as trek_repository

app = Flask(__name__)

app.register_blueprint(destinations_blueprint)
app.register_blueprint(treks_blueprint)

@app.route('/')
def home():
    completed_treks = trek_repository.select_completed()
    uncompleted_treks = trek_repository.select_uncompleted()
    total_distance = trek_repository.total_distance()
    total_days = trek_repository.total_days()
    return render_template('index.html', completed_treks = completed_treks, uncompleted_treks = uncompleted_treks, total_distance = total_distance, total_days = total_days)

if __name__ == '__main__':
    app.run(debug=True)
