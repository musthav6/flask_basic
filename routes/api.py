from flask import Blueprint, jsonify
from controllers.brand_controller import get_all_brands, get_brand_by_id
from controllers.manufacturer_controller import get_all_manufacturers, get_manufacturer_by_id

api_bp = Blueprint('api', __name__)


@api_bp.route('/brands', methods=['GET'])
def brands():
    brands = get_all_brands()
    return jsonify([brand.as_dict() for brand in brands])


@api_bp.route('/brands/<int:brand_id>', methods=['GET'])
def brand(brand_id):
    brand = get_brand_by_id(brand_id)
    return jsonify(brand.as_dict()) if brand else ('', 404)


@api_bp.route('/manufacturers', methods=['GET'])
def manufacturers():
    manufacturers = get_all_manufacturers()
    return jsonify([manufacturer.as_dict() for manufacturer in manufacturers])


@api_bp.route('/manufacturers/<int:manufacturer_id>', methods=['GET'])
def manufacturer(manufacturer_id):
    manufacturer = get_manufacturer_by_id(manufacturer_id)
    return jsonify(manufacturer.as_dict()) if manufacturer else ('', 404)
