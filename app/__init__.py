from pathlib import Path

from flask import Flask, render_template

from config import CONFIG_MAP, Config

BASE_DIR = Path(__file__).resolve().parent.parent


def _resolve_config(config_name_or_class):
    if isinstance(config_name_or_class, str):
        return CONFIG_MAP.get(config_name_or_class.lower(), Config)
    return config_name_or_class or Config


def _init_db(app):
    import sqlite3

    db_path = Path(app.config["DATABASE"])
    db_path.parent.mkdir(parents=True, exist_ok=True)
    schema_path = BASE_DIR / "db" / "schema.sql"

    with sqlite3.connect(db_path) as conn:
        conn.executescript(schema_path.read_text(encoding="utf-8"))
        conn.commit()


def create_app(config_name_or_class=Config):
    app = Flask(
        __name__,
        template_folder=str(BASE_DIR / "templates"),
        static_folder=str(BASE_DIR / "static"),
        instance_path=str(BASE_DIR / "instance"),
    )
    app.config.from_object(_resolve_config(config_name_or_class))

    Path(app.instance_path).mkdir(parents=True, exist_ok=True)
    _init_db(app)

    from app.routes.admin import admin_bp
    from app.routes.auth import auth_bp
    from app.routes.booking import booking_bp
    from app.routes.certificate import certificate_bp
    from app.routes.dashboard import dashboard_bp
    from app.routes.main import main_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(booking_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(certificate_bp)

    @app.template_filter("vnd")
    def vnd_filter(value):
        try:
            return f"{int(value):,}".replace(",", ".") + " ₫"
        except (TypeError, ValueError):
            return str(value) + " ₫"

    @app.errorhandler(404)
    def not_found(_error):
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def server_error(_error):
        return render_template("500.html"), 500

    return app
# Thêm hàm này vào app/__init__.py, gọi trong create_app()

def seed_db_if_empty(app):
    """Chạy mỗi khi app start — safe vì dùng INSERT OR IGNORE"""
    import sqlite3, os
    db_path = os.path.join(app.instance_path, 'green_experience.db')
    conn = sqlite3.connect(db_path)
    # Tạo admin mặc định nếu chưa có
    conn.execute("""
        INSERT OR IGNORE INTO users (name, email, password_hash, role, is_admin, green_points)
        VALUES (
            'Lâm Bảo Ngọc',
            'lambaongoc5487@gmail.com',
            'scrypt:32768:8:1$salt$hash_placeholder',
            'staff', 1, 9999
        )
    """)
    conn.commit()
    conn.close()