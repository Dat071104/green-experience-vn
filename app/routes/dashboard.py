from flask import Blueprint, render_template, session, redirect, flash
from db.helpers import get_db, get_user_level
import sqlite3

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Vui lòng đăng nhập để xem Dashboard.', 'error')
        return redirect('/login')
        
    user_id = session['user_id']
    db = get_db()
    
    # Get user info
    user = db.execute("SELECT * FROM users WHERE id=?", (user_id,)).fetchone()
    
    # Calculate level based on green points
    level_info = get_user_level(user['green_points'])
    
    # Get bookings
    bookings = db.execute("SELECT * FROM bookings WHERE user_id=? ORDER BY created_at DESC", (user_id,)).fetchall()
    
    # Calculate stats
    total_tours = len(bookings)
    total_co2_saved = sum(b['guests'] * 45 for b in bookings) # Mock calculation
    total_trees = int(total_co2_saved / 21)
    
    # Get points history
    points_history = db.execute("SELECT * FROM green_points_log WHERE user_id=? ORDER BY created_at DESC LIMIT 5", (user_id,)).fetchall()
    
    # Mock Rewards Catalog
    rewards = [
        {'id': 1, 'name': 'Voucher Tour 500k', 'cost': 300, 'icon': 'ticket'},
        {'id': 2, 'name': 'Túi Vải Canvas', 'cost': 150, 'icon': 'shopping-bag'},
        {'id': 3, 'name': 'Bình Nước Inox', 'cost': 120, 'icon': 'coffee'},
        {'id': 4, 'name': 'Sản Phẩm Thổ Cẩm', 'cost': 200, 'icon': 'gift'},
        {'id': 5, 'name': 'Certificate Digital', 'cost': 100, 'icon': 'award'},
        {'id': 6, 'name': 'Voucher Homestay 300k', 'cost': 200, 'icon': 'home'}
    ]

    return render_template('dashboard.html', 
                           user=user, 
                           level_info=level_info,
                           bookings=bookings,
                           stats={
                               'tours': total_tours,
                               'co2': total_co2_saved,
                               'trees': total_trees
                           },
                           points_history=points_history,
                           rewards=rewards)
