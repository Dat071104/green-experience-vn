# 03 — PAGES SPECIFICATION

> Spec chi tiết từng trang: sections, content, data, interactions.
> Tất cả URLs ảnh Unsplash đã có sẵn từ mockData gốc.

---

## PAGE 1: HOME (`/`)

### Hero Section
```
Layout: Full-width, min-height 90vh, background gradient var(--gradient-hero)
Overlay: ảnh background (blur nhẹ, opacity 0.3):
  https://images.unsplash.com/photo-1695094412603-3340f1e72232?w=1920

Headline: "Green Experience – Responsible Journey"
  → font: Playfair Display, clamp(3rem, 7vw, 5.5rem), color white
Subheadline: "Đi xanh hơn, hiểu sâu hơn, để lại tác động tốt hơn"
  → font: Be Vietnam Pro 300, font-size 1.25rem, color white/90

CTA Primary: "🌿 Khám phá hành trình xanh" → href /destinations
CTA Secondary: "Tính CO₂ chuyến đi →" → href /co2-calculator (outline, màu trắng)

Stats bar bên dưới hero (3 con số mockup):
  - "1,200+ Du khách xanh"
  - "3 Vùng điểm đến"
  - "8,500 kg CO₂ đã tiết kiệm"
```

### Destination Cards (3 cards)
```
Title section: "Khám phá điểm đến xanh"
Layout: Grid 3 columns (desktop), 1 column (mobile)

Card 1 — Lô Lô Chải:
  Image: https://images.unsplash.com/photo-1609412058473-c199497c3c5d?w=1080
  Tag: "Miền Bắc • Văn hoá bản địa"
  Name: "Lô Lô Chải"
  Tagline: "Xanh gắn với trải nghiệm văn hoá"
  Desc: "Khám phá vẻ đẹp nguyên sơ của vùng núi đá Hà Giang..."
  Stats: "4-5 ngày | Từ 4.500.000 ₫ | +150 GP"
  CTA: "Xem hành trình →" → /destinations/lo-lo-chai
  Theme class: theme-lo-lo-chai

Card 2 — Măng Đen:
  Image: https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?w=1080
  Tag: "Tây Nguyên • Thiện nguyện"
  Name: "Măng Đen"
  Tagline: "Xanh gắn với hành trình thiện nguyện"
  Stats: "3-4 ngày | Từ 3.800.000 ₫ | +180 GP"
  Theme class: theme-mang-den

Card 3 — Tiền Giang – Bến Tre:
  Image: https://images.unsplash.com/photo-1543411789-1a67a2ac05c6?w=1080
  Tag: "Miền Tây • Bảo vệ thiên nhiên"
  Name: "Tiền Giang – Bến Tre"
  Tagline: "Xanh gắn với bảo vệ thiên nhiên"
  Stats: "3 ngày | Từ 2.900.000 ₫ | +140 GP"
  Theme class: theme-tien-giang
```

### Why Green Section
```
Title: "Tại sao chọn du lịch xanh?"
Layout: 3 columns icon + text

Item 1: 🌱 icon → "Hỗ trợ cộng đồng địa phương"
  "100% chi phí homestay và workshop đến tay người dân địa phương"

Item 2: 🌍 icon → "Giảm thiểu tác động môi trường"
  "Chọn phương tiện xanh, không nhựa dùng một lần, trồng cây trong mỗi hành trình"

Item 3: 🏆 icon → "Nhận Green Points & Chứng nhận"
  "Tích điểm từ mỗi hoạt động xanh, đổi quà và nhận certificate du lịch bền vững"
```

### Green Points Teaser
```
Background: var(--green-primary), padding generous
Title: "Hệ thống Green Points" (white)
Desc: "Mỗi hành động xanh đều được ghi nhận và thưởng điểm"
Point items grid (2x3):
  +100 GP — Đặt tour xanh
  +70 GP  — Trồng cây
  +50 GP  — Tham gia cộng đồng
  +40 GP  — Chọn phương tiện xanh
  +30 GP  — Check-in homestay xanh
  +20 GP  — Không dùng nhựa một lần
CTA: "Tạo tài khoản để tích điểm →" → /register
```

### CO₂ Calculator Teaser
```
Background: var(--off-white)
Split layout: left text + right illustration/screenshot
Title: "Bạn đã tiết kiệm bao nhiêu CO₂?"
Desc: "Nhập điểm xuất phát, phương tiện thường và phương tiện xanh — chúng tôi tính cho bạn"
CTA: "Thử ngay máy tính CO₂ →" → /co2-calculator
```

---

## PAGE 2: DESTINATIONS (`/destinations`)

### Hero
```
Background: var(--gradient-hero), padding-y: 80px
Title: "Điểm đến xanh"
Desc: "Khám phá 3 vùng miền với trải nghiệm du lịch bền vững độc đáo"
Filter tabs: "Tất cả | Miền Bắc | Tây Nguyên | Miền Tây"
```

### Destination Cards Grid
```
Loop qua 3 destinations, hiển thị card lớn (ratio 3/2):
- Ảnh hero + gradient overlay
- Region badge (góc trên phải)
- Destination name (Playfair, trắng, bottom)
- Tagline
- Row stats: N ngày | Từ X ₫ | CO₂: −Xkg | GP: +X
- CTA: "Xem hành trình"
```

---

## PAGE 3: DESTINATION DETAIL (`/destinations/<id>`)

### Hero (full-screen, 70vh)
```
Background: hero image của destination (Unsplash URL từ mockData)
Gradient overlay đậm bottom-up
Content: Region badge | Name | Tagline | Stats row
```

### Story Section
```
Layout: text trái (60%) + ảnh phải (40%)
Tiêu đề: "Câu chuyện điểm đến"
Content: description đầy đủ + 5 highlights dạng list với checkmark icon
```

### Tour Highlights
```
Title: "Các hành trình nổi bật"
Cards: 1-2 tours của destination này
Mỗi card: ảnh | tên tour | duration | giá | Green Points | CTA Đặt tour
```

### Green Homestays Section
```
Title: "Homestay đạt chuẩn xanh"
Cards homestay thuộc destination này
Mỗi card: ảnh | tên | giá/đêm | Green Score (%) | certifications list
```

### No-Plastic Spots
```
Title: "Điểm không nhựa dùng một lần"
List/grid: type badge | name | location | description
```

### Community Activities
```
Title: "Hoạt động cộng đồng bạn có thể tham gia"
Cards: title | type | duration | price | Green Points | impact text
```

### Gallery
```
Masonry grid 3 columns, 6 ảnh (Unsplash URLs theo theme destination)
```

### Reviews (Mock)
```
3 review cards: avatar placeholder | tên | rating ⭐ | text | ngày
```

### CTA Booking
```
Banner full-width: "Sẵn sàng cho hành trình xanh?"
Subtext + CTA "Đặt tour ngay" → /booking?tour=<tour-id>
```

---

## PAGE 4: TOUR DETAIL (`/tours/<id>`)

### Header
```
Title: tên tour | Badge: duration | difficulty | max guests
Price: hiển thị lớn "4.500.000 ₫/người"
Green badges: "+150 Green Points" | "−45 kg CO₂"
CTA sticky sidebar (desktop): "Đặt tour ngay"
```

### Itinerary (Theo ngày)
```
Accordion hoặc timeline vertical:
Mỗi ngày: Day N | Title | Activities list | Meals | Accommodation
```

### Included / Not Included
```
2 columns: ✅ Bao gồm | ❌ Không bao gồm
```

### Green Activities
```
Title: "Hoạt động xanh trong hành trình"
List với leaf icon, màu green-mint background
```

### Booking Form (sidebar hoặc bottom)
```
Fields: Chọn ngày khởi hành | Số khách (1-20) | Phương tiện xanh (select)
Tổng giá (tính real-time với JS): = giá × số khách
CTA: "Tiến hành đặt tour" → /booking với params
```

---

## PAGE 5: HOMESTAYS (`/homestays`)

### Hero
```
Title: "Homestay đạt chuẩn xanh"
Desc: "Nghỉ lại nơi mỗi giấc ngủ đều có ý nghĩa"
```

### Green Criteria Explanation
```
5 tiêu chí xanh (icon + title + desc):
1. Tiết kiệm điện/nước — Hệ thống năng lượng mặt trời, thu nước mưa
2. Hạn chế nhựa dùng một lần — Bình nước refill, đồ dùng tre/gỗ
3. Nguyên liệu địa phương — Ăn uống từ vườn nhà và chợ địa phương
4. Phân loại rác — Compost, tái chế tại chỗ
5. Hỗ trợ cộng đồng — Thu nhập trực tiếp cho gia đình
```

### Homestay Cards Grid
```
3 homestay cards:
- Ảnh, tên, location
- Green Score: progress bar (0-100%)
- Giá/đêm
- Certifications: pills
- Highlights: 4 bullets
- CTA: "Xem homestay" (link đến destination detail section)
```

---

## PAGE 6: COMMUNITY (`/community`)

### Hero
```
Title: "Hoạt động cộng đồng"
Desc: "Mỗi hành trình là cơ hội để tạo tác động tích cực"
```

### Activity Cards
```
5 activities:
1. Workshop Thổ Cẩm — Lô Lô Chải | 3h | 200k | +50 GP
2. Lớp Học Tình Nguyện — Măng Đen | 1 ngày | Miễn phí | +100 GP
3. Trồng Cây Bản Địa — Tiền Giang | 2h | 150k | +70 GP
4. Dọn Rác Ven Sông — Tiền Giang | 2h | Miễn phí | +80 GP
5. Hỗ Trợ Nông Hộ — Lô Lô Chải | Linh hoạt | 300k | +60 GP

Mỗi card: type badge | title | destination | duration | price | Green Points | description | impact text
```

### Impact Counter Section
```
Animated counters (mockup):
- 2,450 du khách đã tham gia
- 15,000 cây đã trồng
- 2.3 tấn rác đã dọn
- 850 học sinh được hỗ trợ
```

---

## PAGE 7: CO₂ CALCULATOR (`/co2-calculator`)

### Calculator Form
```
Input 1: Điểm xuất phát (text, suggestions: Hà Nội, TP.HCM, Đà Nẵng)
Input 2: Điểm đến (text, suggestions: Hà Giang, Kon Tum, Bến Tre)
Input 3: Số người (number, min 1 max 20)
Select 4: Phương tiện thường (xe máy / ô tô / máy bay)
Select 5: Phương tiện xanh đề xuất (xe khách / xe điện / xe đạp)

CTA: "Tính toán ngay 🌿"
```

### Result Display (ẩn ban đầu, hiện sau khi tính)
```
Card kết quả:
- "Bạn đã giảm khoảng X kg CO₂" (số lớn, màu green-primary)
- "Tương đương X cây xanh không cần trồng"
- "Nhận thêm +X Green Points khi chọn phương tiện xanh"

Visual: so sánh bar chart (normal vs green transport)
CTA: "Đặt tour với phương tiện xanh →"
```

### Logic (JS, xem chi tiết trong mockData)
```javascript
// Emission factors (gCO2/km)
const factors = { car: 120, motorbike: 80, plane: 250, public: 40, bicycle: 0 };

// Mockup distances (km)
const distances = {
  'Hà Nội-Hà Giang': 300,
  'TP.HCM-Kon Tum': 450,
  'TP.HCM-Bến Tre': 80,
  // default: 200km
};

co2Saved = (normalFactor - greenFactor) * distance * travelers / 1000; // kg
trees = Math.floor(co2Saved / 21);
gp = Math.floor(co2Saved * 2);
```

---

## PAGE 8: LOGIN (`/login`) & REGISTER (`/register`)

### Login Form
```
Card centered, max-width 420px:
- Logo + "Chào mừng trở lại"
- Input: Email
- Input: Mật khẩu (show/hide toggle)
- Checkbox: Ghi nhớ đăng nhập
- CTA: "Đăng nhập"
- Link: "Chưa có tài khoản? Đăng ký →"
- Flash messages: lỗi sai mật khẩu, etc.
```

### Register Form
```
- Input: Họ và tên
- Input: Email
- Input: Mật khẩu + Xác nhận mật khẩu
- Checkbox: Đồng ý điều khoản
- CTA: "Tạo tài khoản xanh 🌿"
- Link: "Đã có tài khoản? Đăng nhập →"
```

### Flask Route Logic
```python
# /login POST:
user = User.query.filter_by(email=email).first()
if user and check_password_hash(user.password_hash, password):
    session['user_id'] = user.id
    redirect('/dashboard')

# /register POST:
new_user = User(name=name, email=email,
                password_hash=generate_password_hash(password))
db.session.add(new_user)
db.session.commit()
redirect('/login')
```

---

## PAGE 9: DASHBOARD (`/dashboard`) — requires login

### Header
```
Avatar circle (initials) | "Chào, {name}!" | Level badge
Green Traveler Level: "🌿 Green Explorer" (dựa theo points)
Progress bar đến level tiếp theo
```

### Stats Grid (2x2)
```
- Tổng Green Points: X (số lớn, màu gold)
- Tours đã đặt: X
- CO₂ đã tiết kiệm: X kg
- Cây đã trồng: X
```

### Points History
```
Table: ngày | hoạt động | điểm nhận | tổng
(Mock data từ user.bookings + activities)
```

### Badges
```
Grid badges earned (màu mờ nếu chưa đạt):
🌱 Eco Beginner | 🌿 Green Explorer | 🌳 Eco Warrior | 🏆 Champion | 🌍 Legend
```

### Rewards Catalog
```
6 phần thưởng mockup, nút "Đổi X GP" (disabled nếu không đủ điểm):
- Voucher Tour 500k — 300 GP
- Túi Vải Canvas — 150 GP
- Bình Nước Inox — 120 GP
- Sản Phẩm Thổ Cẩm — 200 GP
- Certificate Digital — 100 GP
- Voucher Homestay 300k — 200 GP
```

### My Bookings
```
List: tour name | ngày đặt | trạng thái | link Certificate
```

---

## PAGE 10: BOOKING (`/booking`) — 3-step flow

### Step 1: Xác nhận tour
```
Hiển thị: tour name, dates, số người, phương tiện xanh
Tổng giá = giá × số người
CTA: "Tiếp tục →"
```

### Step 2: Thông tin cá nhân
```
Form: Họ tên | Email | SĐT | Ghi chú
Nếu đã đăng nhập: auto-fill từ session user
CTA: "Xác nhận đặt tour"
```

### Step 3: Xác nhận thành công
```
Booking code: GE{timestamp}
Summary: tour, ngày, khách, tổng tiền
"Green Points vừa cộng: +150 GP"
CTA: "Xem Dashboard" | "Tải Certificate"
```

### Flask Route
```python
# /booking POST step 2:
booking = Booking(
    user_id=session.get('user_id'),
    tour_id=form.tour_id,
    tour_name=form.tour_name,
    guests=form.guests,
    total_price=form.total_price,
    green_points=form.green_points,
    customer_name=form.name,
    customer_email=form.email,
    customer_phone=form.phone,
    notes=form.notes,
    booking_code=generate_code(),
    status='confirmed'
)
# Update user points nếu đã login
if session.get('user_id'):
    user.green_points += booking.green_points
```

---

## PAGE 11: CERTIFICATE (`/certificate/<booking_code>`)

### Layout
```
Background: trắng (dành cho print)
Border: double border, xanh lá
Logo + "Green Experience – Responsible Journey" top center
Seal/stamp: circular badge góc (SVG)

"Chứng nhận Du lịch Xanh"
"Cấp cho: {customer_name}"
"Tour: {tour_name}"
"Điểm đến: {destination}"
"Ngày: {booking_date}"

Activities đã tham gia (từ tour.greenActivities):
  ✅ Homestay cộng đồng
  ✅ Không nhựa một lần
  ✅ Trồng cây / Thiện nguyện

"Green Points nhận được: +150 GP"
"CO₂ tiết kiệm ước tính: −45 kg"
"Tương đương X cây xanh"

QR Code mockup (placeholder image hoặc ASCII)
Mã: {booking_code}

Nút: "🖨️ In chứng nhận" (window.print())
Nút: "📤 Chia sẻ hành trình xanh" (Web Share API hoặc copy link)
```

---

## PAGE 12: ABOUT (`/about`)

### Hero + Mission
```
Hero: gradient xanh, logo lớn
Sứ mệnh: 3 pillars — Môi trường | Văn hoá | Cộng đồng
```

### Team / Partners (Mock)
```
4-6 partner logos placeholder + tên tổ chức
```

### Timeline (Câu chuyện)
```
2022: Khởi động chiến dịch
2023: Hợp tác với 15 homestay
2024: 1,000 du khách xanh đầu tiên
2025: Mở rộng 3 vùng miền
```

### CTA Final
```
"Cùng chúng tôi tạo nên sự thay đổi"
Button: "Khám phá tour xanh ngay →"
```
