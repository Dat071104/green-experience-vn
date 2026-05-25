# 02 — DESIGN SYSTEM

> Đây là source of truth cho mọi visual decision. AI agent PHẢI follow file này.

---

## COLOR PALETTE (CSS Variables)

Paste nguyên khối này vào `global.css` trong `:root { }`:

```css
:root {
  /* === PRIMARY GREENS === */
  --green-primary:   #4a6b40;   /* Xanh lá chính — nav active, CTA primary, headings */
  --green-pine:      #2c4a22;   /* Xanh thông đậm — hover states, dark backgrounds */
  --green-moss:      #6b7c5f;   /* Xanh rêu — body text, muted elements */
  --green-sage:      #9aaf8a;   /* Xanh sage — borders, dividers, muted bg */
  --green-fresh:     #7ab870;   /* Xanh lá tươi — accent, badges, icons */
  --green-mint:      #c8dfc4;   /* Xanh mint nhạt — backgrounds, hover fills */

  /* === NEUTRALS === */
  --off-white:       #f5f2ec;   /* Background chính — toàn site */
  --cream:           #ede8df;   /* Cards, sections alternating bg */
  --sand:            #c8b89a;   /* Borders, dividers nhẹ */
  --earth-brown:     #8b6f47;   /* Accent nâu — Lô Lô Chải theme, pattern */
  --warm-white:      #faf9f6;   /* Pure sections bg */

  /* === ACCENTS === */
  --sun-gold:        #d4a84b;   /* Điểm nhấn vàng — Green Points, badges, stars */
  --terracotta:      #c97b4a;   /* Cam đất — Măng Đen theme, CTA secondary */
  --water-blue:      #7ba8a8;   /* Xanh nước — Tiền Giang theme */

  /* === SEMANTIC === */
  --text-primary:    #1e2d1a;   /* Heading text */
  --text-secondary:  #4a5e42;   /* Body text */
  --text-muted:      #7a8a72;   /* Caption, meta */
  --border-light:    rgba(154,175,138,0.25);  /* Card borders */
  --shadow-green:    rgba(74,107,64,0.12);    /* Card shadows */

  /* === GRADIENTS (as backgrounds) === */
  --gradient-hero:   linear-gradient(135deg, #2c4a22 0%, #4a6b40 50%, #6b7c5f 100%);
  --gradient-card:   linear-gradient(180deg, transparent 50%, rgba(30,45,26,0.85) 100%);
  --gradient-mint:   linear-gradient(135deg, #c8dfc4 0%, #f5f2ec 100%);
}
```

### Destination-Specific Color Overrides
```css
/* Lô Lô Chải — Xanh rêu + nâu đất */
.theme-lo-lo-chai {
  --dest-primary:  #6b8e5f;
  --dest-accent:   #8b6f47;
  --dest-bg:       #f0ebe0;
}

/* Măng Đen — Xanh thông + cam đất */
.theme-mang-den {
  --dest-primary:  #2c5f4a;
  --dest-accent:   #d4a574;
  --dest-bg:       #f0f5ee;
}

/* Tiền Giang – Bến Tre — Xanh lá non + xanh nước */
.theme-tien-giang {
  --dest-primary:  #5a9167;
  --dest-accent:   #7ba8a8;
  --dest-bg:       #edf5ee;
}
```

---

## TYPOGRAPHY

```css
/* Google Fonts import — paste vào <head> của base.html */
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Be+Vietnam+Pro:wght@300;400;500;600&display=swap" rel="stylesheet">

/* CSS */
:root {
  --font-display: 'Playfair Display', Georgia, serif;   /* Headlines, hero text */
  --font-body:    'Be Vietnam Pro', -apple-system, sans-serif;  /* Body, UI */
}

body { font-family: var(--font-body); }

h1, h2, .hero-title { font-family: var(--font-display); }
```

### Type Scale
```css
.text-hero     { font-size: clamp(2.5rem, 6vw, 5rem); line-height: 1.1; }
.text-h1       { font-size: clamp(2rem, 4vw, 3.5rem); line-height: 1.2; }
.text-h2       { font-size: clamp(1.5rem, 3vw, 2.5rem); line-height: 1.3; }
.text-h3       { font-size: clamp(1.2rem, 2vw, 1.5rem); line-height: 1.4; }
.text-body     { font-size: 1rem; line-height: 1.7; }
.text-small    { font-size: 0.875rem; line-height: 1.6; }
.text-caption  { font-size: 0.75rem; line-height: 1.5; letter-spacing: 0.05em; text-transform: uppercase; }
```

---

## SPACING & LAYOUT

```css
:root {
  --radius-card:    20px;      /* Cards */
  --radius-btn:     12px;      /* Buttons */
  --radius-badge:   100px;     /* Pills/badges */
  --radius-input:   10px;      /* Form inputs */

  --shadow-card:    0 4px 24px var(--shadow-green);
  --shadow-hover:   0 12px 40px rgba(74,107,64,0.18);
  --shadow-hero:    0 24px 64px rgba(30,45,26,0.3);

  --max-width:      1280px;
  --padding-x:      clamp(1rem, 5vw, 4rem);
  --section-y:      clamp(3rem, 8vw, 6rem);
}

.container {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 0 var(--padding-x);
}
```

---

## COMPONENT SPECS

### Cards (Tour / Destination)
```
- Border radius: 20-24px
- Shadow: var(--shadow-card)
- Hover: translateY(-6px) + var(--shadow-hover) — transition 0.3s ease
- Image: aspect-ratio 4/3, object-fit cover
- Gradient overlay trên ảnh: var(--gradient-card)
- Padding nội dung: 1.25rem 1.5rem
- Tag/badge: background var(--green-mint), color var(--green-primary), radius 100px, font-size 0.75rem
```

### Buttons
```
CTA Primary:
  - bg: var(--green-primary), color: white
  - padding: 0.875rem 2rem
  - radius: var(--radius-btn)
  - hover: bg var(--green-pine), translateY(-2px)
  - font-weight: 600, font-size: 0.95rem

CTA Secondary (outline):
  - border: 2px solid var(--green-primary), color: var(--green-primary)
  - hover: bg var(--green-primary), color white

CTA Ghost:
  - color: var(--green-moss)
  - hover: color var(--green-primary), underline

Accent (Tính CO₂):
  - bg: var(--sun-gold), color: var(--text-primary)
  - hover: bg darken 10%
```

### Green Points Badge
```
- Background: linear-gradient(135deg, #d4a84b, #e8c070)
- Color: white, font-weight 700
- Icon: ⭐ hoặc Lucide `award` icon
- Format: "+150 GP"
```

### CO₂ Saved Badge
```
- Background: var(--green-mint)
- Color: var(--green-pine)
- Icon: Lucide `trending-down`
- Format: "−45 kg CO₂"
```

### Section Headers
```html
<div class="section-header">
  <span class="section-label"><!-- Nhỏ, uppercase, màu green-sage --></span>
  <h2 class="section-title"><!-- Playfair Display, green-primary --></h2>
  <p class="section-desc"><!-- Be Vietnam Pro, green-moss, max-width 600px --></p>
</div>
```

---

## NAVIGATION

```
- Position: sticky top, z-index 100
- Background: rgba(245,242,236,0.95) + backdrop-blur(12px)
- Border-bottom: 1px solid var(--border-light)
- Height: 80px
- Logo: Leaf icon (Lucide) + "Green Experience" / "Responsible Journey"
- Links: font-size 0.9rem, font-weight 500, color var(--green-moss)
- Active link: color var(--green-primary)
- CTA Nav: "Đăng nhập" button, style CTA Primary nhỏ
```

---

## FOOTER

```
- Background: var(--green-primary)
- Color: white / white/70
- 3 columns: Logo + tagline | Links chính | Liên hệ
- Bottom bar: "© 2025 Green Experience. Hành trình xanh, tác động bền vững."
- Accent: border-top 1px solid rgba(255,255,255,0.1)
```

---

## ANIMATIONS (CSS only + JS IntersectionObserver)

```css
/* Fade in up — dùng cho cards, sections */
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(30px); }
  to   { opacity: 1; transform: translateY(0); }
}

.reveal {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}
.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}

/* Stagger children */
.reveal-group .reveal:nth-child(1) { transition-delay: 0s; }
.reveal-group .reveal:nth-child(2) { transition-delay: 0.1s; }
.reveal-group .reveal:nth-child(3) { transition-delay: 0.2s; }
```

```javascript
// main.js — scroll reveal
const observer = new IntersectionObserver(
  (entries) => entries.forEach(e => e.isIntersecting && e.target.classList.add('visible')),
  { threshold: 0.15 }
);
document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
```
