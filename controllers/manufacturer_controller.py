from models.manufacturer import Manufacturer
from config import db


def get_all_manufacturers():
    return Manufacturer.query.all()


def get_manufacturer_by_id(manufacturer_id):
    return Manufacturer.query.get(manufacturer_id)


def add_manufacturer(manufacturer_data):
    new_manufacturer = Manufacturer(**manufacturer_data)
    db.session.add(new_manufacturer)
    db.session.commit()
    return new_manufacturer
