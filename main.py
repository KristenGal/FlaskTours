from flask import Flask, jsonify, render_template, request
from models import db, Tour

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)


@app.get('/')
def index():
    tours = Tour.query.all()
    return render_template('index.html', tours=tours)


@app.get('/<int:tour_id>/')
def tour(tour_id):
    tour = Tour.query.get_or_404(tour_id)
    return render_template('tour.html', tour=tour)


@app.post('/add_tour/')
def add_tour():
    data = request.get_json()

    if not data.get("title"):
        return jsonify({"error": "Enter the title"})
    elif not data.get("price"):
        return jsonify({"error": "Enter the price (number)"})
    elif not data.get("description"):
        return jsonify({"error": "Enter the description"})
    
    tour = Tour(title=data.get("title"), 
                price=data.get("price"), 
                description=data.get("description"))
    db.session.add(tour)
    db.session.commit()


if __name__ == "__main__":
    app.run(debug=True)
