# RULES.md — Green Experience Agent Rules
> Version: 1.0 | Last updated: see IMPLEMENTATION_LOG.md
> ⚠️ AI agent PHẢI đọc file này TRƯỚC KHI làm bất cứ điều gì.

---

## R1 — ĐỌC TRƯỚC, CODE SAU

Trước mỗi task, đọc theo thứ tự:
1. `RULES.md` (file này)
2. `IMPLEMENTATION_LOG.md` → tìm dòng `### CURRENT PHASE` và `### LAST CHECKPOINT`
3. File spec liên quan trong `docs/` (01–06)
4. Chỉ sau đó mới bắt đầu code

**Không được bắt đầu code khi chưa đọc log** — vì session trước có thể đã làm một phần.

---

## R2 — GHI LOG BẮT BUỘC

Sau MỖI hành động đáng kể (tạo file, fix bug, quyết định kỹ thuật), ghi vào `IMPLEMENTATION_LOG.md`:

```markdown
### [YYYY-MM-DD HH:MM] Phase X — Tên task
**Done:** Mô tả ngắn đã làm gì
**Files:** List files đã tạo/sửa
**Decision:** Lý do chọn approach này (nếu có nhiều lựa chọn)
**Bug (nếu có):** Mô tả lỗi → nguyên nhân → cách fix
**Next:** Việc tiếp theo cần làm
```

---

## R3 — SELF-VERIFICATION LOOP

Sau khi hoàn thành MỖI file, chạy mental checklist:
- [ ] File có kế thừa `base.html` không? (với templates)
- [ ] Có dùng đúng CSS variables từ `02_DESIGN_SYSTEM.md` không?
- [ ] Font có phải Playfair Display + Be Vietnam Pro không?
- [ ] Border-radius cards có phải 20-24px không?
- [ ] Text tiếng Việt có encoding đúng không?
- [ ] Flask route có return template đúng không?
- [ ] Nếu có form: có CSRF token + validation không?
- [ ] Ảnh có `loading="lazy"` + `alt` tiếng Việt không?

Nếu bất kỳ check nào fail → **sửa ngay, không tiếp tục** → ghi bug vào log.

---

## R4 — KHÔNG ĐỂ PLACEHOLDER

Tuyệt đối không viết:
- `<!-- TODO: add content here -->`
- `# TODO: implement this`
- `pass  # implement later`
- Content giả như "Lorem ipsum"

Mọi section phải có nội dung thật (tiếng Việt, đúng ngành du lịch xanh).
Nếu cần data thật → dùng web search (R7).

---

## R5 — KHÔNG PHÁ VỠ DESIGN SYSTEM

Các giá trị KHÔNG được tự ý thay đổi:
- ❌ `border-radius: 8px` → ✅ `border-radius: var(--radius-card)` = 20px
- ❌ Font `Inter`, `Roboto`, `Arial` → ✅ `Playfair Display` + `Be Vietnam Pro`
- ❌ Color `#007bff`, `#28a745` (Bootstrap colors) → ✅ dùng CSS variables
- ❌ `box-shadow: 0 2px 4px rgba(0,0,0,0.1)` generic → ✅ `var(--shadow-card)`

---

## R6 — CHECKPOINT SAU MỖI PHASE

Sau khi hoàn thành một phase, PHẢI:
1. Chạy checklist của phase đó (trong ULTIMATE_PROMPT.md)
2. Với mỗi item chưa done: làm xong rồi mới tiếp
3. Ghi checkpoint vào log: `### CHECKPOINT Phase X — PASSED [date]`
4. Chỉ sau đó mới chuyển phase tiếp theo

---

## R7 — WEB SEARCH PERMISSION

Agent được phép và PHẢI dùng web search cho:
- Tìm thông tin thực tế về điểm du lịch (Lô Lô Chải, Măng Đen, Tiền Giang–Bến Tre)
- Ảnh Unsplash theo từ khóa cụ thể (tìm URL thật)
- Homestay thực tế ở các địa điểm đó
- Hoạt động cộng đồng thực tế ở vùng đó
- Giá tour thị trường hiện tại (để mockup sát thực tế)
- Thông tin CO₂ emission factors chính xác hơn
- Bất kỳ thông tin nào giúp content trông authentic hơn

**Query format gợi ý:**
```
"du lịch Lô Lô Chải Hà Giang homestay 2024"
"Măng Đen Kon Tum tour xanh thiện nguyện"
"Tiền Giang Bến Tre eco tour trồng cây"
"unsplash ha giang mountain tribe vietnam"
```

---

## R8 — TOKEN SAFETY

Nếu context window gần đầy (ước tính 70%+ đã dùng):
1. Ghi ngay checkpoint vào log
2. Ghi rõ `### NEXT SESSION START HERE` trong log
3. List tất cả files đã tạo, files còn thiếu
4. Ghi trạng thái hiện tại của từng file (done/partial/not started)

---

## R9 — FILE NAMING CONVENTION

```
templates/          → snake_case.html (home.html, tour_detail.html)
static/css/         → snake_case.css (global.css, tour_detail.css)
static/js/          → snake_case.js (main.js, co2_calculator.js)
routes/             → snake_case.py (main.py, auth.py)
docs/               → XX_TITLE.md (số thứ tự 2 chữ số)
```

---

## R10 — DEMO-ONLY FEATURES

Các feature sau chỉ là DEMO (không cần backend thật):
- Green Points rewards redemption → hiển thị modal "Tính năng sắp ra mắt"
- QR Code trên Certificate → placeholder SVG
- Payment gateway → hiển thị "Thanh toán sẽ được xử lý qua đối tác"
- Map tương tác → static image hoặc Google Maps embed link
- Email confirmation → flash message "Email xác nhận đã được gửi"

Login/Register cho Staff vs User → cùng một form, chỉ khác badge hiển thị sau login.

---

## R11 — DEPLOY CHECKLIST (cuối cùng)

Trước khi push GitHub:
- [ ] `requirements.txt` đầy đủ, đúng version
- [ ] `Procfile` có `web: gunicorn run:app`
- [ ] `render.yaml` có persistent disk config
- [ ] `.gitignore` exclude: `instance/`, `*.db`, `.env`, `__pycache__/`, `venv/`
- [ ] `SECRET_KEY` không hardcode, đọc từ env var
- [ ] Không có `debug=True` trong production code
- [ ] README.md có hướng dẫn deploy

---

## R12 — QUALITY STANDARD

Website phải đạt được khi nhìn vào:
- Người lạ thấy đây là website **thật**, không phải demo sinh viên
- Design premium, không có element nào trông "free Bootstrap theme"
- Content đủ để khách hàng hiểu tour và muốn đặt
- Mobile responsive (breakpoint 768px minimum)
- Không có broken layout, overflow ngang, text bị cắt
