from flask import Blueprint, render_template, request, abort
from db.helpers import get_db
from data.static_data import TOURS_BY_ID

certificate_bp = Blueprint('certificate', __name__)

@certificate_bp.route('/certificate/<booking_code>')
def view_certificate(booking_code):
    db = get_db()
    booking = db.execute("SELECT * FROM bookings WHERE booking_code=?", (booking_code,)).fetchone()
    
    if not booking:
        abort(404)
        
    tour = TOURS_BY_ID.get(booking['tour_id'])
    co2_saved = booking['guests'] * 45 # Mock value based on 45kg/guest average
    trees = int(co2_saved / 21)
    
    return render_template('certificate.html', booking=booking, tour=tour, co2_saved=co2_saved, trees=trees)
