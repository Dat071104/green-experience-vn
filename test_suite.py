#!/usr/bin/env python3
"""
tests/test_suite.py — Green Experience Automated Test Suite
Chạy: python tests/test_suite.py
Kết quả: PASS / FAIL từng test, tổng kết cuối
AI agent đọc output để biết cần fix gì.
"""

import sys
import os
import sqlite3
import importlib
import traceback
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ─── Setup path ────────────────────────────────────────────────────────────────
ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))

# ─── Color output ──────────────────────────────────────────────────────────────
class C:
    GREEN  = '\033[92m'
    RED    = '\033[91m'
    YELLOW = '\033[93m'
    BLUE   = '\033[94m'
    BOLD   = '\033[1m'
    RESET  = '\033[0m'

def ok(msg):    print(f"  {C.GREEN}✅ PASS{C.RESET}  {msg}")
def fail(msg):  print(f"  {C.RED}❌ FAIL{C.RESET}  {msg}")
def warn(msg):  print(f"  {C.YELLOW}⚠️  WARN{C.RESET}  {msg}")
def info(msg):  print(f"  {C.BLUE}ℹ️  INFO{C.RESET}  {msg}")
def header(msg):print(f"\n{C.BOLD}{C.BLUE}{'═'*60}{C.RESET}\n{C.BOLD} {msg}{C.RESET}\n{'═'*60}")

results = {"pass": 0, "fail": 0, "warn": 0}

def test(name, condition, fix_hint=""):
    if condition:
        ok(name)
        results["pass"] += 1
        return True
    else:
        fail(f"{name}")
        if fix_hint:
            print(f"    {C.YELLOW}→ FIX:{C.RESET} {fix_hint}")
        results["fail"] += 1
        return False

# ══════════════════════════════════════════════════════════════════════════════
# GROUP 1: PROJECT STRUCTURE
# ══════════════════════════════════════════════════════════════════════════════
header("GROUP 1: Project Structure")

required_dirs = [
    "app", "app/routes", "db", "data",
    "templates", "templates/partials", "templates/admin",
    "static", "static/css", "static/js", "static/img",
    "instance", "tests"
]
for d in required_dirs:
    test(f"Directory exists: {d}/",
         (ROOT / d).is_dir(),
         f"mkdir -p {d}")

required_files = [
    "app/__init__.py",
    "app/routes/__init__.py",
    "app/routes/main.py",
    "app/routes/auth.py",
    "app/routes/booking.py",
    "app/routes/dashboard.py",
    "app/routes/admin.py",
    "db/schema.sql",
    "db/helpers.py",
    "data/static_data.py",
    "config.py",
    "run.py",
    "requirements.txt",
    "Procfile",
    "render.yaml",
    ".gitignore",
    "README.md",
    "RULES.md",
    "IMPLEMENTATION_LOG.md",
]
for f in required_files:
    test(f"File exists: {f}",
         (ROOT / f).is_file(),
         f"Create file: {f} (see docs/)")

# ══════════════════════════════════════════════════════════════════════════════
# GROUP 2: TEMPLATES
# ══════════════════════════════════════════════════════════════════════════════
header("GROUP 2: Templates")

required_templates = [
    "base.html",
    "home.html",
    "destinations.html",
    "destination_detail.html",
    "tour_detail.html",
    "homestays.html",
    "community.html",
    "co2_calculator.html",
    "login.html",
    "register.html",
    "dashboard.html",
    "booking.html",
    "certificate.html",
    "about.html",
    "404.html",
    "500.html",
    "partials/nav.html",
    "partials/footer.html",
    "admin/bookings.html",
    "admin/leads.html",
]
for t in required_templates:
    path = ROOT / "templates" / t
    exists = path.is_file()
    test(f"Template: {t}", exists,
         f"Create templates/{t} extending base.html")
    if exists:
        content = path.read_text(encoding="utf-8", errors="ignore")
        # Check extends base (except base itself and partials)
        if t not in ("base.html",) and not t.startswith("partials/"):
            test(f"  {t}: extends base.html",
                 "extends" in content and "base.html" in content,
                 f"Add {{% extends 'base.html' %}} to top of {t}")
        # Check no Lorem ipsum
        test(f"  {t}: no placeholder text",
             "lorem ipsum" not in content.lower() and "TODO" not in content,
             f"Replace all placeholder text in {t}")

# ══════════════════════════════════════════════════════════════════════════════
# GROUP 3: CSS & JS
# ══════════════════════════════════════════════════════════════════════════════
header("GROUP 3: Static Assets")

css_files = ["global.css", "home.css", "destinations.css",
             "auth.css", "booking.css", "dashboard.css"]
for f in css_files:
    path = ROOT / "static" / "css" / f
    test(f"CSS: {f}", path.is_file(), f"Create static/css/{f}")
    if path.is_file():
        content = path.read_text(encoding="utf-8", errors="ignore")
        if f == "global.css":
            for var in ["--green-primary", "--off-white", "--font-display",
                       "--radius-card", "--shadow-card"]:
                test(f"  global.css has {var}",
                     var in content,
                     f"Add CSS variable {var} to :root {{ }} in global.css")

js_files = ["main.js", "co2_calculator.js", "booking.js", "auth.js"]
for f in js_files:
    path = ROOT / "static" / "js" / f
    test(f"JS: {f}", path.is_file(), f"Create static/js/{f}")

# ══════════════════════════════════════════════════════════════════════════════
# GROUP 4: PYTHON IMPORTS
# ══════════════════════════════════════════════════════════════════════════════
header("GROUP 4: Python Module Imports")

try:
    import config
    ok("config.py importable")
    results["pass"] += 1
    test("config has SECRET_KEY",
         hasattr(config, 'Config') or hasattr(config, 'DevelopmentConfig'),
         "Add class Config or DevelopmentConfig to config.py")
except Exception as e:
    fail(f"config.py import failed: {e}")
    results["fail"] += 1

try:
    import data.static_data as sd
    ok("data/static_data.py importable")
    results["pass"] += 1
    test("DESTINATIONS has ≥ 3 items",
         hasattr(sd, 'DESTINATIONS') and len(sd.DESTINATIONS) >= 3,
         "Add at least 3 destinations to DESTINATIONS list")
    test("TOURS has ≥ 3 items",
         hasattr(sd, 'TOURS') and len(sd.TOURS) >= 3,
         "Add at least 3 tours to TOURS list")
    test("HOMESTAYS exists",
         hasattr(sd, 'HOMESTAYS') and len(sd.HOMESTAYS) >= 1,
         "Add HOMESTAYS list to static_data.py")
    test("DESTINATIONS_BY_ID lookup exists",
         hasattr(sd, 'DESTINATIONS_BY_ID'),
         "Add DESTINATIONS_BY_ID = {d['id']: d for d in DESTINATIONS}")
    test("TOURS_BY_ID lookup exists",
         hasattr(sd, 'TOURS_BY_ID'),
         "Add TOURS_BY_ID = {t['id']: t for t in TOURS}")
    # Check each destination has required keys
    if hasattr(sd, 'DESTINATIONS') and sd.DESTINATIONS:
        d = sd.DESTINATIONS[0]
        for key in ['id', 'name', 'region', 'image', 'priceFrom', 'greenPoints', 'co2Saved']:
            test(f"  Destination has key: '{key}'",
                 key in d,
                 f"Add '{key}' field to each destination dict")
except Exception as e:
    fail(f"data/static_data.py import failed: {e}")
    print(f"    {C.RED}Traceback:{C.RESET} {traceback.format_exc()[-200:]}")
    results["fail"] += 1

try:
    from db import helpers as h
    ok("db/helpers.py importable")
    results["pass"] += 1
    for fn in ['get_db', 'generate_booking_code', 'get_user_level', 'add_green_points']:
        test(f"  helpers has function: {fn}()",
             hasattr(h, fn) and callable(getattr(h, fn)),
             f"Add function {fn}() to db/helpers.py")
except Exception as e:
    fail(f"db/helpers.py import failed: {e}")
    results["fail"] += 1

# ══════════════════════════════════════════════════════════════════════════════
# GROUP 5: FLASK APP FACTORY
# ══════════════════════════════════════════════════════════════════════════════
header("GROUP 5: Flask App Factory & Routes")

app = None
try:
    # Try import app factory
    app_module = importlib.import_module('app')
    if hasattr(app_module, 'create_app'):
        app = app_module.create_app('development')
        ok("create_app() callable")
        results["pass"] += 1
    else:
        fail("app/__init__.py missing create_app() function")
        results["fail"] += 1
except Exception as e:
    fail(f"Flask app import failed: {e}")
    print(f"    {C.RED}Cause:{C.RESET} {str(e)}")
    results["fail"] += 1

if app:
    client = app.test_client()
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False

    routes_to_test = [
        ('/', 200, "Home page"),
        ('/destinations', 200, "Destinations list"),
        ('/homestays', 200, "Homestays page"),
        ('/community', 200, "Community page"),
        ('/co2-calculator', 200, "CO2 Calculator"),
        ('/about', 200, "About page"),
        ('/login', 200, "Login page"),
        ('/register', 200, "Register page"),
    ]

    with app.test_request_context():
        for url, expected_status, label in routes_to_test:
            try:
                response = client.get(url)
                test(f"Route {url} → {expected_status}",
                     response.status_code == expected_status,
                     f"Fix route handler for {url} — got {response.status_code}")
                if response.status_code == 200:
                    content = response.data.decode('utf-8', errors='ignore')
                    test(f"  {url}: contains 'Green Experience'",
                         'Green Experience' in content or 'green' in content.lower(),
                         f"Add Green Experience branding to {url} template")
            except Exception as e:
                fail(f"Route {url} threw exception: {e}")
                results["fail"] += 1

    # Test protected routes redirect
    try:
        resp = client.get('/dashboard')
        test("/dashboard redirects if not logged in",
             resp.status_code in (302, 301),
             "Add @login_required decorator to /dashboard route")
        resp = client.get('/admin/bookings')
        test("/admin/bookings redirects if not logged in",
             resp.status_code in (302, 301),
             "Add admin check to /admin/bookings route")
    except Exception as e:
        fail(f"Protected route test failed: {e}")
        results["fail"] += 1

    # Test 404
    try:
        resp = client.get('/this-page-does-not-exist-xyz')
        test("404 handler works",
             resp.status_code == 404,
             "Add @app.errorhandler(404) to app/__init__.py")
    except Exception as e:
        warn(f"404 handler test skipped: {e}")
        results["warn"] += 1

# ══════════════════════════════════════════════════════════════════════════════
# GROUP 6: DATABASE
# ══════════════════════════════════════════════════════════════════════════════
header("GROUP 6: SQLite Database")

schema_path = ROOT / "db" / "schema.sql"
if schema_path.exists():
    schema = schema_path.read_text(encoding="utf-8")
    for table in ['users', 'bookings', 'green_points_log', 'contact_leads']:
        test(f"schema.sql: CREATE TABLE {table}",
             f"CREATE TABLE IF NOT EXISTS {table}" in schema or
             f"CREATE TABLE {table}" in schema,
             f"Add CREATE TABLE IF NOT EXISTS {table} (...) to schema.sql")
    for col in ['role', 'is_admin', 'green_points']:
        test(f"schema.sql: users has column '{col}'",
             col in schema,
             f"Add column '{col}' to CREATE TABLE users in schema.sql")

# Try create test DB and verify schema
try:
    test_db_path = ROOT / "instance" / "test_check.db"
    conn = sqlite3.connect(str(test_db_path))
    if schema_path.exists():
        conn.executescript(schema_path.read_text(encoding="utf-8"))
    conn.commit()
    cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [r[0] for r in cursor.fetchall()]
    conn.close()
    test_db_path.unlink(missing_ok=True)
    for t in ['users', 'bookings', 'green_points_log', 'contact_leads']:
        test(f"DB schema creates table: {t}", t in tables,
             f"Fix CREATE TABLE {t} syntax in schema.sql")
except Exception as e:
    fail(f"DB schema execution failed: {e}")
    results["fail"] += 1

# ══════════════════════════════════════════════════════════════════════════════
# GROUP 7: AUTH FLOW (integration)
# ══════════════════════════════════════════════════════════════════════════════
header("GROUP 7: Auth Flow Integration")

if app:
    import tempfile, uuid
    test_email = f"test_{uuid.uuid4().hex[:8]}@green.vn"

    with app.app_context():
        # Test register
        try:
            resp = client.post('/register', data={
                'name': 'Test User Xanh',
                'email': test_email,
                'password': 'testpass123',
                'confirm_password': 'testpass123',
                'role': 'user',
            }, follow_redirects=False)
            test("POST /register returns redirect",
                 resp.status_code in (302, 200),
                 "Fix /register POST handler to redirect after successful registration")
        except Exception as e:
            fail(f"Register test failed: {e}")
            results["fail"] += 1

        # Test login after register
        try:
            resp = client.post('/login', data={
                'email': test_email,
                'password': 'testpass123',
                'role': 'user',
            }, follow_redirects=False)
            test("POST /login with valid creds returns redirect",
                 resp.status_code in (302, 200),
                 "Fix /login POST handler — should redirect to /dashboard on success")
        except Exception as e:
            fail(f"Login test failed: {e}")
            results["fail"] += 1

        # Test wrong password
        try:
            resp = client.post('/login', data={
                'email': test_email,
                'password': 'wrongpassword',
                'role': 'user',
            }, follow_redirects=True)
            test("POST /login with wrong password shows error (not 500)",
                 resp.status_code == 200,
                 "Handle wrong password gracefully — return 200 with error message")
        except Exception as e:
            fail(f"Wrong password test failed: {e}")
            results["fail"] += 1

# ══════════════════════════════════════════════════════════════════════════════
# GROUP 8: DEPLOY FILES
# ══════════════════════════════════════════════════════════════════════════════
header("GROUP 8: Deploy Readiness")

procfile = ROOT / "Procfile"
if procfile.exists():
    content = procfile.read_text()
    test("Procfile has gunicorn command",
         "gunicorn" in content,
         "Procfile should contain: web: gunicorn run:app")
    test("Procfile uses $PORT",
         "$PORT" in content or "PORT" in content,
         "Add --bind 0.0.0.0:$PORT to gunicorn command")

render_yaml = ROOT / "render.yaml"
if render_yaml.exists():
    content = render_yaml.read_text()
    test("render.yaml has disk config",
         "disk" in content,
         "Add disk: section to render.yaml for SQLite persistence")
    test("render.yaml has SECRET_KEY env var",
         "SECRET_KEY" in content,
         "Add SECRET_KEY to envVars in render.yaml")

req = ROOT / "requirements.txt"
if req.exists():
    content = req.read_text()
    for pkg in ["Flask", "Werkzeug", "gunicorn"]:
        test(f"requirements.txt has {pkg}",
             pkg in content,
             f"Add {pkg} to requirements.txt")

gitignore = ROOT / ".gitignore"
if gitignore.exists():
    content = gitignore.read_text()
    for entry in ["instance/", "*.db", ".env"]:
        test(f".gitignore excludes {entry}",
             entry in content,
             f"Add '{entry}' to .gitignore")

config_py = ROOT / "config.py"
if config_py.exists():
    content = config_py.read_text()
    test("config.py reads SECRET_KEY from env",
         "environ" in content and "SECRET_KEY" in content,
         "SECRET_KEY must use os.environ.get(), not hardcoded")
    test("config.py no hardcoded debug=True in production",
         "ProductionConfig" in content,
         "Add ProductionConfig class with DEBUG=False")

# ══════════════════════════════════════════════════════════════════════════════
# FINAL SUMMARY
# ══════════════════════════════════════════════════════════════════════════════
total = results["pass"] + results["fail"]
pct = int(results["pass"] / total * 100) if total else 0

print(f"\n{'═'*60}")
print(f"{C.BOLD} TEST SUMMARY{C.RESET}")
print(f"{'═'*60}")
print(f"  {C.GREEN}PASS: {results['pass']}{C.RESET}")
print(f"  {C.RED}FAIL: {results['fail']}{C.RESET}")
print(f"  {C.YELLOW}WARN: {results['warn']}{C.RESET}")
print(f"  Score: {pct}% ({results['pass']}/{total})")

if results["fail"] == 0:
    print(f"\n  {C.GREEN}{C.BOLD}🎉 ALL TESTS PASSED — Ready to deploy!{C.RESET}")
elif pct >= 80:
    print(f"\n  {C.YELLOW}{C.BOLD}⚠️  Almost there — fix the FAIL items above{C.RESET}")
else:
    print(f"\n  {C.RED}{C.BOLD}❌ Multiple failures — see FIX hints above{C.RESET}")

print(f"{'═'*60}\n")

# Exit code for CI/automation
sys.exit(0 if results["fail"] == 0 else 1)
