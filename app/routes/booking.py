import sqlite3

from flask import Blueprint, flash, redirect, render_template, request, session

from data.static_data import TOURS_BY_ID
from db.helpers import generate_booking_code, get_db

booking_bp = Blueprint('booking', __name__)


@booking_bp.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'GET':
        tour_id = request.args.get('tour_id')
        date = request.args.get('date')
        guests = int(request.args.get('guests', 1))

        tour = TOURS_BY_ID.get(tour_id)
        if not tour:
            flash('Tour khong ton tai.', 'error')
            return redirect('/destinations')

        total_price = tour['price'] * guests
        total_gp = tour['greenPoints'] * guests

        user_info = {}
        if 'user_id' in session:
            db = get_db()
            user = db.execute("SELECT * FROM users WHERE id=?", (session['user_id'],)).fetchone()
            if user:
                user_info = {'name': user['name'], 'email': user['email']}

        return render_template(
            'booking.html',
            tour=tour,
            date=date,
            guests=guests,
            total_price=total_price,
            total_gp=total_gp,
            user_info=user_info,
        )

    user_id = session.get('user_id')
    tour_id = request.form.get('tour_id')
    tour_name = request.form.get('tour_name')
    booking_date = request.form.get('date')
    guests = int(request.form.get('guests', 1))
    total_price = float(request.form.get('total_price', 0))
    green_points = int(request.form.get('green_points', 0))

    customer_name = request.form.get('name')
    customer_email = request.form.get('email')
    customer_phone = request.form.get('phone')
    notes = request.form.get('notes', '')

    booking_code = generate_booking_code()

    db = get_db()
    try:
        db.execute(
            """
            INSERT INTO bookings (
                user_id, tour_id, tour_name, booking_date, guests,
                total_price, green_points, customer_name, customer_email,
                customer_phone, notes, booking_code, status
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                user_id,
                tour_id,
                tour_name,
                booking_date,
                guests,
                total_price,
                green_points,
                customer_name,
                customer_email,
                customer_phone,
                notes,
                booking_code,
                'confirmed',
            ),
        )

        if user_id:
            db.execute(
                "UPDATE users SET green_points = green_points + ? WHERE id = ?",
                (green_points, user_id),
            )
            db.execute(
                """
                INSERT INTO green_points_log (
                    user_id, action, activity_type, description, points, reference
                ) VALUES (?, ?, ?, ?, ?, ?)
                """,
                (user_id, 'booking', 'booking', f'Dat tour: {tour_name}', green_points, booking_code),
            )

        db.commit()
        return redirect(f'/booking/success?code={booking_code}')

    except sqlite3.Error as e:
        flash(f'Loi khi luu booking: {e}', 'error')
        return redirect('/destinations')


@booking_bp.route('/booking/success')
def booking_success():
    code = request.args.get('code')
    db = get_db()
    booking = db.execute("SELECT * FROM bookings WHERE booking_code=?", (code,)).fetchone()

    if not booking:
        flash('Khong tim thay thong tin dat tour.', 'error')
        return redirect('/')

    return render_template('booking_success.html', booking=booking)
