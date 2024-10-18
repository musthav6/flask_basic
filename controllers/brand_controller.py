from models.brands import Brand
from config import db


def get_all_brands():
    return Brand.query.all()


def get_brand_by_id(brand_id):
    return Brand.query.get(brand_id)


def add_brand(brand_data):
    new_brand = Brand(**brand_data)
    db.session.add(new_brand)
    db.session.commit()
    return new_brand
