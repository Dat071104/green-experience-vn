from flask import Blueprint, render_template, session, redirect, flash, request
from db.helpers import get_db
import sqlite3

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.before_request
def check_admin():
    if not session.get('is_admin'):
        flash('Bạn không có quyền truy cập trang này.', 'error')
        return redirect('/')

@admin_bp.route('/bookings')
def bookings():
    db = get_db()
    bookings = db.execute("SELECT * FROM bookings ORDER BY created_at DESC").fetchall()
    return render_template('admin/bookings.html', bookings=bookings)

@admin_bp.route('/bookings/update/<int:booking_id>', methods=['POST'])
def update_status(booking_id):
    status = request.form.get('status')
    if status in ['confirmed', 'completed', 'cancelled']:
        db = get_db()
        try:
            db.execute("UPDATE bookings SET status=? WHERE id=?", (status, booking_id))
            db.commit()
            flash('Cập nhật trạng thái thành công.', 'success')
        except sqlite3.Error as e:
            flash(f'Lỗi: {e}', 'error')
    return redirect('/admin/bookings')
