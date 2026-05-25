from flask import Blueprint, render_template, request, redirect, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from db.helpers import get_db
import sqlite3

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role', 'user') # 'user' or 'staff'
        staff_code = request.form.get('staffCode', '')

        if role == 'staff' and staff_code != 'STAFF2025':
            flash('Mã nhân viên không hợp lệ!', 'error')
            return redirect('/login')

        db = get_db()
        try:
            # We fetch user, also check role. But wait, in DB, we didn't add role initially. 
            # We'll just fetch by email.
            user = db.execute("SELECT * FROM users WHERE email=?", (email,)).fetchone()
            
            if user and check_password_hash(user['password_hash'], password):
                session['user_id'] = user['id']
                session['user_name'] = user['name']
                session['user_role'] = role
                
                # Check if role is staff and they used the right code, we can treat them as admin for this session 
                # (or update their is_admin flag if they weren't before)
                if role == 'staff':
                    session['is_admin'] = True
                    # Optional: update db if not already admin
                    db.execute("UPDATE users SET is_admin=1, role='staff' WHERE id=?", (user['id'],))
                    db.commit()
                else:
                    session['is_admin'] = bool(user['is_admin'])
                
                flash('Đăng nhập thành công!', 'success')
                return redirect('/dashboard')
            else:
                flash('Email hoặc mật khẩu không chính xác.', 'error')
        except sqlite3.Error as e:
            flash(f'Lỗi cơ sở dữ liệu: {e}', 'error')
            
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        role = request.form.get('role', 'user')
        staff_code = request.form.get('staffCode', '')

        if password != confirm_password:
            flash('Mật khẩu không khớp!', 'error')
            return redirect('/register')
            
        if len(password) < 8:
            flash('Mật khẩu phải có ít nhất 8 ký tự.', 'error')
            return redirect('/register')

        if role == 'staff' and staff_code != 'STAFF2025':
            flash('Mã nhân viên không hợp lệ!', 'error')
            return redirect('/register')

        db = get_db()
        try:
            # Check if email exists
            existing = db.execute("SELECT id FROM users WHERE email=?", (email,)).fetchone()
            if existing:
                flash('Email này đã được sử dụng.', 'error')
                return redirect('/register')
                
            hashed = generate_password_hash(password)
            is_admin = 1 if role == 'staff' else 0
            
            # Using try-except for column role just in case
            try:
                db.execute(
                    "INSERT INTO users (name, email, password_hash, is_admin, role) VALUES (?, ?, ?, ?, ?)",
                    (name, email, hashed, is_admin, role)
                )
            except sqlite3.OperationalError:
                # Fallback if 'role' column is not created yet
                db.execute(
                    "INSERT INTO users (name, email, password_hash, is_admin) VALUES (?, ?, ?, ?)",
                    (name, email, hashed, is_admin)
                )
            db.commit()
            
            # Auto login
            user = db.execute("SELECT * FROM users WHERE email=?", (email,)).fetchone()
            session['user_id'] = user['id']
            session['user_name'] = user['name']
            session['user_role'] = role
            session['is_admin'] = is_admin
            
            flash('Tạo tài khoản thành công! Chào mừng bạn.', 'success')
            return redirect('/dashboard')
            
        except sqlite3.Error as e:
            flash(f'Lỗi cơ sở dữ liệu: {e}', 'error')

    return render_template('register.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Đã đăng xuất.', 'success')
    return redirect('/')
