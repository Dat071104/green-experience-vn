#!/usr/bin/env python3
"""
check_structure.py — Chạy ngay để diagnose lỗi
python check_structure.py
"""
import os, sys, traceback
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).parent
print(f"{'='*60}")
print(f" GREEN EXPERIENCE — STRUCTURE DIAGNOSTIC")
print(f"{'='*60}")
print(f" Working dir : {ROOT.absolute()}")
print(f"{'='*60}\n")

# ── Critical files ─────────────────────────────────────────
print("📁 CRITICAL FILES:")
critical = [
    'run.py', 'config.py', 'requirements.txt', '.gitignore',
    'app/__init__.py', 'app/routes/__init__.py',
    'app/routes/main.py', 'app/routes/auth.py',
    'app/routes/booking.py', 'app/routes/dashboard.py',
    'app/routes/admin.py',
    'db/__init__.py', 'db/schema.sql', 'db/helpers.py',
    'data/__init__.py', 'data/static_data.py',
    'templates/base.html', 'templates/home.html',
    'templates/partials/nav.html', 'templates/partials/footer.html',
    'static/css/global.css', 'static/js/main.js',
    'Procfile', 'render.yaml',
]
missing = []
for f in critical:
    path = ROOT / f
    if path.exists():
        size = path.stat().st_size
        status = f"✅ ({size:,} bytes)"
    else:
        status = "❌ MISSING"
        missing.append(f)
    print(f"  {status:25s} {f}")

# ── Flask app test ─────────────────────────────────────────
print(f"\n🐍 FLASK APP:")
sys.path.insert(0, str(ROOT))
try:
    from app import create_app
    app = create_app('development')
    print(f"  ✅ create_app() OK")
    print(f"  📂 template_folder : {app.template_folder}")
    print(f"  📂 static_folder   : {app.static_folder}")
    print(f"  📂 instance_path   : {app.instance_path}")

    # Check template folder actually exists
    tf = Path(app.template_folder)
    if tf.exists():
        templates = list(tf.glob('*.html'))
        print(f"  📄 Templates found : {len(templates)} html files")
        print(f"     {[t.name for t in templates[:5]]}")
        home_exists = (tf / 'home.html').exists()
        print(f"  {'✅' if home_exists else '❌'} home.html exists in template folder")
    else:
        print(f"  ❌ Template folder DOES NOT EXIST at: {tf}")
        print(f"     → This is why TemplateNotFound error occurs!")

    # Check static folder
    sf = Path(app.static_folder)
    if sf.exists():
        css = list((sf / 'css').glob('*.css')) if (sf / 'css').exists() else []
        print(f"  📄 CSS files       : {len(css)}")
    else:
        print(f"  ❌ Static folder DOES NOT EXIST at: {sf}")

except ImportError as e:
    print(f"  ❌ Import failed: {e}")
    print(f"     Traceback:")
    traceback.print_exc()
except Exception as e:
    print(f"  ❌ App creation failed: {e}")
    traceback.print_exc()

# ── DB schema ─────────────────────────────────────────────
print(f"\n🗄️  DATABASE SCHEMA:")
schema = ROOT / 'db' / 'schema.sql'
if schema.exists():
    content = schema.read_text(encoding='utf-8')
    for table in ['users', 'bookings', 'green_points_log', 'contact_leads']:
        has = f"CREATE TABLE" in content and table in content
        print(f"  {'✅' if has else '❌'} Table: {table}")
    # Try execute
    try:
        import sqlite3, tempfile
        tmp = tempfile.mktemp(suffix='.db')
        conn = sqlite3.connect(tmp)
        conn.executescript(content)
        conn.commit()
        tables = [r[0] for r in conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        ).fetchall()]
        conn.close()
        os.unlink(tmp)
        print(f"  ✅ Schema executes OK — tables: {tables}")
    except Exception as e:
        print(f"  ❌ Schema execution error: {e}")
else:
    print(f"  ❌ db/schema.sql not found")

# ── Static data ───────────────────────────────────────────
print(f"\n📊 STATIC DATA:")
try:
    from data import static_data as sd
    dests = getattr(sd, 'DESTINATIONS', [])
    tours = getattr(sd, 'TOURS', [])
    homes = getattr(sd, 'HOMESTAYS', [])
    print(f"  {'✅' if len(dests)>=3 else '❌'} DESTINATIONS: {len(dests)} items")
    print(f"  {'✅' if len(tours)>=3 else '❌'} TOURS: {len(tours)} items")
    print(f"  {'✅' if len(homes)>=1 else '❌'} HOMESTAYS: {len(homes)} items")
    print(f"  {'✅' if hasattr(sd,'DESTINATIONS_BY_ID') else '❌'} DESTINATIONS_BY_ID lookup")
    print(f"  {'✅' if hasattr(sd,'TOURS_BY_ID') else '❌'} TOURS_BY_ID lookup")
except Exception as e:
    print(f"  ❌ static_data import failed: {e}")

# ── Summary ───────────────────────────────────────────────
print(f"\n{'='*60}")
if missing:
    print(f"❌ MISSING {len(missing)} files:")
    for f in missing:
        print(f"   → Create: {f}")
else:
    print(f"✅ All critical files present")
print(f"{'='*60}\n")
print("Next: python tests/test_suite.py")
