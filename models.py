from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# назва, ціна, опис, картинка (str)
class Tour(db.Model):
    __tablename__ = "tour"
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, default="https://picsum.photos/200/300?grayscale")
    is_booked = db.Column(db.Boolean, default=False)
