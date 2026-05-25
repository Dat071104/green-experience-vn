# 01 — PROJECT CONTEXT

## Tên dự án
**Green Experience – Responsible Journey**

## Mô tả
Website du lịch bền vững quảng bá tour xanh tại 3 vùng miền Việt Nam: Miền Bắc (Lô Lô Chải – Hà Giang), Tây Nguyên (Măng Đen – Kon Tum), Miền Tây (Tiền Giang – Bến Tre). Mục tiêu: bán tour online, thu lead khách hàng, truyền thông ý thức môi trường.

## Nguồn gốc
Bắt đầu từ Figma design → AI generate React app (TypeScript + Tailwind + shadcn/ui + React Router + Framer Motion). Nay cần rebuild thành Flask + HTML/CSS + SQLite để deploy thật trên Render.com.

---

## VISUAL IDENTITY & PHONG CÁCH

### Định hướng thiết kế
- **Premium eco-tourism**: Không quá học thuật, không cheap. Cân bằng giữa cảm xúc và chuyển đổi.
- **Organic + Modern**: Layout sạch, ảnh lớn, nhiều white space, nhưng có tính cách.
- **Trustworthy + Inspiring**: Khách hàng phải vừa tin tưởng vừa muốn đặt tour ngay.

### Cảm xúc từng điểm đến
| Điểm đến | Cảm xúc chủ đạo | Visual tone |
|---|---|---|
| Lô Lô Chải | Xanh văn hoá bản địa, thổ cẩm, sương sớm | Xanh rêu + nâu đất, pattern thổ cẩm |
| Măng Đen | Xanh thiện nguyện, ánh sáng cộng đồng | Xanh thông + cam đất |
| Tiền Giang – Bến Tre | Xanh bảo vệ thiên nhiên, sông nước | Xanh lá non + xanh nước |

---

## USER PERSONAS

### Primary: Du khách trẻ có ý thức (22–35 tuổi)
- Quan tâm đến môi trường, muốn du lịch có ý nghĩa
- Quen đặt tour online, tìm trải nghiệm độc đáo không phải tourist trap
- Ngân sách: 3–6 triệu/tour ngắn ngày

### Secondary: Nhóm công ty, team building xanh
- Booking nhóm 10–20 người
- Cần hóa đơn, thông tin đầy đủ, quy trình booking chuyên nghiệp

### Admin (bạn - chủ website)
- Xem danh sách booking từ SQLite
- Xem thông tin khách hàng (tên, email, SĐT, tour đã đặt)
- Export data đơn giản (không cần CMS phức tạp)

---

## TÍNH NĂNG CHÍNH

| Tính năng | Priority | Cần SQLite? |
|---|---|---|
| Xem tour + điểm đến | P0 | Không (mock data) |
| CO₂ Calculator | P0 | Không (JS only) |
| Đăng ký / Đăng nhập | P1 | Có |
| Đặt tour (Booking) | P1 | Có |
| Green Points Dashboard | P2 | Có |
| Certificate digital | P2 | Có |
| Admin view bookings | P2 | Có |

---

## TECH STACK QUYẾT ĐỊNH

```
Backend:    Flask 3.x (Python 3.11+)
Database:   SQLite (file: green_experience.db)
ORM:        SQLAlchemy 2.x (hoặc raw sqlite3 nếu muốn nhẹ hơn)
Auth:       Flask-Login + werkzeug password hashing
Templates:  Jinja2 (bundled với Flask)
Frontend:   HTML5 + CSS3 (custom properties) + Vanilla JS (ES6+)
Icons:      Lucide Icons (CDN)
Fonts:      Google Fonts (Playfair Display + Be Vietnam Pro)
Images:     Unsplash URLs (không host local)
Deploy:     Render.com (free tier, Python runtime)
```

### Lý do KHÔNG dùng React/Streamlit
- **Không React**: Cần HTML/CSS thật để kiểm soát design chi tiết; React overhead không cần thiết cho site này
- **Không Streamlit**: Streamlit không hỗ trợ custom styling ở level này; design sẽ bị giới hạn
- **Flask**: Đủ nhẹ, deploy Render free, dễ học, Jinja2 templates linh hoạt

---

## CẤU TRÚC THƯ MỤC ĐỀ XUẤT

```
green_experience/
├── app/
│   ├── __init__.py          # App factory
│   ├── models.py            # SQLAlchemy models
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── main.py          # Home, About, Destinations
│   │   ├── auth.py          # Login, Register
│   │   ├── booking.py       # Booking flow
│   │   ├── dashboard.py     # User dashboard
│   │   └── admin.py         # Admin panel (simple)
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── destinations.html
│   │   ├── destination_detail.html
│   │   ├── tour_detail.html
│   │   ├── homestays.html
│   │   ├── community.html
│   │   ├── co2_calculator.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── booking.html
│   │   ├── dashboard.html
│   │   ├── certificate.html
│   │   ├── about.html
│   │   └── admin/
│   │       └── bookings.html
│   └── static/
│       ├── css/
│       │   ├── global.css
│       │   ├── home.css
│       │   ├── destinations.css
│       │   └── ... (per page)
│       ├── js/
│       │   ├── main.js
│       │   ├── co2_calculator.js
│       │   └── booking.js
│       └── img/             # Chỉ icon/logo local, ảnh từ Unsplash URL
├── instance/
│   └── green_experience.db  # SQLite file (git-ignored)
├── config.py
├── requirements.txt
├── Procfile                 # Render deploy
└── render.yaml
```
