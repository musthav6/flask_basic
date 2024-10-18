
from config import db


class Manufacturer(db.Model):
    __tablename__ = 'manufacturers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    country = db.Column(db.String(50))
    certificates = db.Column(db.Text)
    internal_id = db.Column(db.String(50), unique=True)

    brands = db.relationship('Brand', secondary='brand_manufacturer', back_populates='manufacturers')

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "country": self.country,
            "certificates": self.certificates
        }