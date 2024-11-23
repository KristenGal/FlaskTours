from models import db, Tour
from main import app

with app.app_context():
    db.drop_all()
    db.create_all()

    tour1 = Tour(title="t1", price=111, description="d11", is_booked=True)
    tours = [Tour(title=f"title{x}", price=x*2, description=f"description{x}") for x in range(1, 11)]
    db.session.add(tour1)
    db.session.add_all(tours)
    db.session.commit()

    # tour = Tour(title="t1", price=111, description="d1")

# title
# price
# description
# image_url
# is_booked