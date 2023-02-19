from flask import Flask, render_template

from controllers.destinations_controller import destinations_blueprint
from controllers.treks_controller import treks_blueprint

app = Flask(__name__)

app.register_blueprint(destinations_blueprint)
app.register_blueprint(treks_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
