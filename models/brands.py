from config import db

class Brand(db.Model):
    __tablename__ = 'brands'

    id = db.Column(db.Integer, primary_key=True)
    logo = db.Column(db.String(255))
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    internal_id = db.Column(db.String(50), unique=True)

    manufacturers = db.relationship('Manufacturer', secondary='brand_manufacturer', back_populates='brands')

    def as_dict(self):
        return {
            "id": self.id,
            "logo": self.logo,
            "name": self.name,
            "description": self.description,
            "internal_id": self.internal_id,
        }

class BrandManufacturer(db.Model):
    __tablename__ = 'brand_manufacturer'
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'), primary_key=True)
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturers.id'), primary_key=True)
