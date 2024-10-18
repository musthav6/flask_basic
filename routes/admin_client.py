from flask import Blueprint, render_template, redirect, url_for, flash
from forms.brand_form import BrandForm
from forms.manufacturer_form import ManufacturerForm
from controllers.brand_controller import add_brand, get_all_brands
from controllers.manufacturer_controller import add_manufacturer, get_all_manufacturers

admin_bp = Blueprint('admin_client', __name__)


@admin_bp.route('/admin/brands', methods=['GET', 'POST'])
def admin_brands():
    form = BrandForm()
    if form.validate_on_submit():
        brand_data = {key: value for key, value in form.data.items() if (key != 'submit' and key != 'csrf_token')}
        add_brand(brand_data)
        flash('Brand added successfully!', 'success')
        return redirect(url_for('admin_client.admin_brands'))

    brands = get_all_brands()  # Отримуємо всі бренди з контролера
    return render_template('brand.html', form=form, brands=brands)


@admin_bp.route('/admin/manufacturers', methods=['GET', 'POST'])
def admin_manufacturers():
    form = ManufacturerForm()
    if form.validate_on_submit():
        manufacturer_data = {key: value for key, value in form.data.items() if
                             (key != 'submit' and key != 'csrf_token')}
        add_manufacturer(manufacturer_data)
        flash('Manufacturer added successfully!', 'success')
        return redirect(url_for('admin_client.admin_manufacturers'))

    manufacturers = get_all_manufacturers()
    return render_template('manufacturer.html', form=form, manufacturers=manufacturers)
