# 06 — QUICK REFERENCE CHEATSHEET

> File ngắn gọn — dán vào đầu mỗi chat với AI agent để set context nhanh.

---

## PROJECT IN ONE PARAGRAPH

Green Experience là website Flask + SQLite về du lịch bền vững Việt Nam. 12 trang: Home, Destinations (3 điểm đến: Lô Lô Chải/Măng Đen/Tiền Giang-Bến Tre), Destination Detail, Tour Detail, Homestays, Community, CO₂ Calculator, Login/Register, Dashboard (Green Points), Booking, Certificate, About. Design: premium eco-tourism, fonts Playfair Display + Be Vietnam Pro, màu xanh lá (#4a6b40), off-white background (#f5f2ec), cards border-radius 20px. SQLite lưu: users + bookings + green_points_log + contact_leads. Static data (tours/homestays) hardcode trong Python dict.

---

## KEY DECISIONS

| Quyết định | Lý do |
|---|---|
| Flask, không phải Django | Nhẹ hơn, đủ dùng cho site này |
| HTML/CSS thuần, không React | Kiểm soát design tốt hơn, không overhead |
| SQLite, không phải PostgreSQL | Free, zero config, đủ cho traffic thấp |
| Deploy Render.com | Free tier + persistent disk cho SQLite |
| Static data trong Python dict | Tour data không thay đổi thường xuyên |

---

## 5 COLORS CẦN NHỚ

```
--green-primary: #4a6b40   ← Màu chủ đạo (nav, CTA, headings)
--green-pine:    #2c4a22   ← Hover, dark sections
--off-white:     #f5f2ec   ← Background toàn site
--sun-gold:      #d4a84b   ← Green Points badges
--earth-brown:   #8b6f47   ← Accent Lô Lô Chải theme
```

---

## ROUTES MAP

```
GET  /                    → home.html
GET  /destinations        → destinations.html (list)
GET  /destinations/<id>   → destination_detail.html
GET  /tours/<id>          → tour_detail.html
GET  /homestays           → homestays.html
GET  /community           → community.html
GET  /co2-calculator      → co2_calculator.html (JS logic)
GET  /about               → about.html
GET  /login               → login.html
POST /login               → auth logic → redirect /dashboard
GET  /register            → register.html
POST /register            → create user → redirect /login
GET  /logout              → clear session → redirect /
GET  /dashboard           → dashboard.html (login required)
GET  /booking             → booking.html (step 1)
POST /booking/confirm     → save to DB → redirect /booking/success
GET  /booking/success     → success page
GET  /certificate/<code>  → certificate.html
GET  /admin/bookings      → admin table (is_admin required)
GET  /admin/leads         → contact leads table
```

---

## SQLITE TABLES (4 tables)

```
users            → id, name, email, password_hash, green_points, level, is_admin
bookings         → id, booking_code, tour_*, customer_*, user_id, status, travel_date
green_points_log → id, user_id, action, points, reference, created_at
contact_leads    → id, name, email, phone, interest, message, source, contacted
```

---

## DESTINATIONS DATA SUMMARY

```
lo-lo-chai:         Miền Bắc | 4-5 ngày | 4.500.000₫ | +150GP | −45kg CO₂
mang-den:           Tây Nguyên | 3-4 ngày | 3.800.000₫ | +180GP | −38kg CO₂
tien-giang-ben-tre: Miền Tây | 3 ngày | 2.900.000₫ | +140GP | −32kg CO₂
```

---

## CSS CLASS CONVENTIONS

```css
.btn-primary     → CTA chính (xanh)
.btn-secondary   → Outline xanh
.btn-accent      → Vàng (CO₂, secondary CTA)
.card            → Border-radius 20px, shadow-card
.gp-badge        → Green Points badge (vàng)
.co2-badge       → CO₂ badge (xanh nhạt)
.tag             → Topic tag (pill shape)
.reveal          → Scroll animation (add .visible via JS)
.section-header  → label + title + desc combo
.theme-lo-lo-chai / .theme-mang-den / .theme-tien-giang → Destination colors
```

---

## KHI CẦN THÊM FEATURE MỚI

Checklist:
1. Thêm route vào blueprint phù hợp
2. Tạo template kế thừa base.html
3. Nếu cần DB: thêm table vào schema.sql, tạo migration đơn giản
4. Thêm link vào nav.html nếu cần
5. Thêm CSS page-specific, không sửa global.css (trừ khi là design token mới)
