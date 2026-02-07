# Gulzameen (Balochistan) - Design System Documentation

## 🎨 Design Philosophy

**Gulzameen (Balochistan)** embodies the warmth, richness, and cultural depth of Balochistan through:
- **Warm Earth Tones**: Reflecting desert landscapes and heritage
- **Interactive Storytelling**: Making cultural content engaging
- **Responsive Grace**: Beautiful on all devices
- **Cultural Authenticity**: Honoring traditions while embracing modern design

---

## Color System

### Primary Palette

#### Gold (#d4af37)
- **Usage**: Primary accents, headings highlights, badges, CTAs
- **Psychology**: Luxury, prestige, cultural wealth
- **Examples**: 
    - Section highlights: "Gulzameen (Balochistan)"
  - Badge backgrounds: "156 items"
  - Button backgrounds
  - Border accents

#### Primary Dark Brown (#8B4513)
- **Usage**: Main headings, body text, cards
- **Psychology**: Earth, stability, heritage
- **Examples**:
  - H1, H2, H3 headings
  - Card titles
  - Toolbar text
  - Button hover states

#### Secondary Rust (#b85c3c)
- **Usage**: Gradient components, navigation, hover states
- **Psychology**: Warmth, passion, tradition
- **Examples**:
  - Gradient backgrounds (with brown)
  - Navbar background
  - Hover color transitions
  - Button hover effects

#### Light Background (#f5f0eb)
- **Usage**: Card backgrounds, page backgrounds
- **Psychology**: Parchment, aged paper, warmth
- **Examples**:
  - Card backgrounds
  - Treasure card gradients
  - Secondary section backgrounds

### Neutral Palette

#### White (#ffffff)
- **Usage**: Primary content areas, contrast
- **Examples**:
  - Hero section text
  - Card backgrounds
  - Modal backgrounds
  - Text on dark backgrounds

#### Dark Text (#333333)
- **Usage**: Body copy, card content
- **Contrast**: 8.1:1 with white (AAA compliant)

#### Gray Text (#666666)
- **Usage**: Secondary text, descriptions, metadata
- **Contrast**: 4.5:1 with white (AA compliant)

---

## Typography System

### Font Family
```css
Primary: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif
Backup: System fonts for reliability
```

### Type Scale

#### Display (Hero Level)
```css
.hero-title {
    font-size: 5rem;      /* 80px */
    font-weight: 900;
    letter-spacing: 2px;
    line-height: 1.1;
}
```
**Use**: Main page titles, hero sections

#### Heading 1
```css
h1 {
    font-size: 3.5rem;    /* 56px */
    font-weight: 700;
    line-height: 1.2;
}
```
**Use**: Section headers, major titles

#### Heading 2
```css
h2 {
    font-size: 3rem;      /* 48px */
    font-weight: 700;
    line-height: 1.2;
}
```
**Use**: Section titles, content headers

#### Heading 3
```css
h3 {
    font-size: 1.5rem;    /* 24px */
    font-weight: 600;
    line-height: 1.3;
}
```
**Use**: Card titles, subsections

#### Body Text
```css
p {
    font-size: 1rem;      /* 16px */
    font-weight: 400;
    line-height: 1.6;
}
```
**Use**: Main content, descriptions

#### Small Text
```css
small, .small-text {
    font-size: 0.95rem;   /* 15px */
    font-weight: 400;
    line-height: 1.5;
}
```
**Use**: Metadata, secondary information

### Font Weights
- **400**: Regular (body text)
- **500**: Medium (labels, buttons)
- **600**: Semibold (card titles)
- **700**: Bold (section headings)
- **900**: Black (hero titles)

---

## Spacing System

### Base Unit: 8px
All spacing follows multiples of 8px for harmony

### Common Spacing Values
```css
8px    → 0.5rem   (minimal)
12px   → 0.75rem  (button padding)
16px   → 1rem     (standard)
20px   → 1.25rem  (medium)
24px   → 1.5rem   (card padding)
32px   → 2rem     (section spacing)
40px   → 2.5rem   (padding large)
60px   → 3.75rem  (section gap)
80px   → 5rem     (major spacing)
```

### Container Widths
```css
Max-width: 1400px    /* Main content max-width */
Padding: 40px        /* Container padding */
Mobile Padding: 20px /* Mobile containers */
```

---

## Component Library

### Buttons

#### Primary Button
```css
.btn-primary {
    background: #d4af37;
    color: #333333;
    padding: 14px 35px;
    border-radius: 50px;
    font-weight: 600;
    transition: all 0.3s ease;
}

.btn-primary:hover {
    background: #ffffff;
    transform: translateY(-3px);
    box-shadow: 0 10px 30px rgba(212,175,55,0.4);
}
```

#### Secondary Button
```css
.btn-secondary {
    background: transparent;
    color: white;
    border: 2px solid white;
    padding: 14px 35px;
    border-radius: 50px;
    font-weight: 600;
    transition: all 0.3s ease;
}

.btn-secondary:hover {
    background: white;
    color: #8B4513;
    transform: translateY(-3px);
}
```

### Cards

#### Region Card
```css
.region-card {
    background: white;
    border-radius: 12px;
    padding: 40px 30px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    border-left: 4px solid transparent;
    transition: all 0.4s ease;
}

.region-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 20px 50px rgba(0,0,0,0.2);
    border-left-color: #d4af37;
}
```

#### Treasure Card
```css
.treasure-card {
    background: linear-gradient(135deg, #f5f0eb 0%, #ede8e0 100%);
    border-radius: 12px;
    padding: 40px 30px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    transition: all 0.4s ease;
    text-align: center;
}

.treasure-card:hover {
    transform: translateY(-12px);
    box-shadow: 0 20px 50px rgba(0,0,0,0.2);
}
```

### Badges & Tags

#### Item Count Badge
```css
.item-badge {
    background: #d4af37;
    color: #333333;
    padding: 8px 16px;
    border-radius: 20px;
    font-size: 0.9rem;
    font-weight: bold;
}
```

#### Featured Tag
```css
.tag {
    background: #d4af37;
    color: white;
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
}

.tag:hover {
    background: #8B4513;
    transform: scale(1.05);
}
```

---

## Layout Grid System

### Responsive Grid Breakpoints

#### Desktop (1024px+)
```css
.regions-grid {
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 30px;
}
```
**Columns**: 3-4 columns depending on screen

#### Tablet (768px-1023px)
```css
@media (max-width: 1024px) {
    .regions-grid {
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 25px;
    }
}
```
**Columns**: 2-3 columns

#### Mobile (480px-767px)
```css
@media (max-width: 768px) {
    .regions-grid {
        grid-template-columns: 1fr;
        gap: 20px;
    }
}
```
**Columns**: 1 column

#### Small Mobile (<480px)
```css
@media (max-width: 480px) {
    /* Further compression */
}
```

---

## Animation System

### Animation Timing
```css
/* Standard timings */
Fast:    0.3s    /* Hover effects, simple transitions */
Medium:  0.6s    /* Element appearances, hover elevations */
Slow:    0.8s    /* Scroll animations, major transitions */
```

### Easing Functions
```css
ease-out     /* Elements entering (starting fast, ending slow) */
ease         /* Smooth general transitions */
linear       /* Constant speed (rotations, spins) */
ease-in-out  /* Both directions (modals, panels) */
```

### Core Animations

#### Fade In (Down)
```css
@keyframes fadeInDown {
    from {
        opacity: 0;
        transform: translateY(-20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
/* Duration: 0.8-1s | Easing: ease-out */
```

#### Fade In (Up)
```css
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
/* Duration: 0.8s | Easing: ease-out */
/* Most used animation - scroll triggers */
```

#### Slide In (Left)
```css
@keyframes slideInLeft {
    from {
        opacity: 0;
        transform: translateX(-30px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}
```

#### Pulse
```css
@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.7; }
}
```

#### Rotate
```css
@keyframes rotate {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}
/* Used for pattern preview animations */
/* Duration: 20s | Easing: linear | Infinite */
```

### Animation Best Practices
1. Use `transform` and `opacity` for performance
2. Avoid `left`, `top`, `width` (causes reflows)
3. Use `will-change` sparingly for heavy animations
4. Keep animations under 1s for interactions
5. Use `animation-fill-mode: both` to maintain end state

---

## Shadows & Depth

### Shadow Tokens
```css
--shadow-soft:    0 5px 15px rgba(0,0,0,0.1);
--shadow-medium:  0 10px 30px rgba(0,0,0,0.15);
--shadow-strong:  0 20px 50px rgba(0,0,0,0.2);
```

### Elevation System
- **Level 1** (Cards): `0 5px 15px rgba(0,0,0,0.1)`
- **Level 2** (Hover): `0 10px 30px rgba(0,0,0,0.15)`
- **Level 3** (Modals): `0 20px 50px rgba(0,0,0,0.2)`

---

## Gradients

### Primary Gradient
```css
linear-gradient(135deg, #8B4513 0%, #b85c3c 100%)
/* Brown to Rust - used in navbar, hero section */
```

### Secondary Gradient
```css
linear-gradient(135deg, #b8860b 0%, #d4af37 100%)
/* Gold gradient - used for accents */
```

### Light Gradient
```css
linear-gradient(135deg, #f5f0eb 0%, #ede8e0 100%)
/* Light background - used in card backgrounds */
```

---

## Icons & Imagery

### Icon Library
- **Font Awesome 6.4** - CDN hosted
- **Size Scale**: 
  - Hero: 2-4rem
  - Card headers: 1.5-2rem
  - Inline: 1rem
  - Badges: 0.9-1.2rem

### Icon Colors
- Primary: `#d4af37` (gold)
- Dark: `#8B4513` (brown)
- White: `#ffffff` (on dark backgrounds)

### Image Guidance
- **Hero Background**: Dark, textured, Balochistan-inspired
- **Card Images**: Cultural, warm-toned, authentic
- **Pattern Images**: Geometric, embroidery-inspired
- **Format**: WebP (modern), JPEG (fallback), PNG (graphics)

---

## Accessibility Standards

### Color Contrast
- **Level AAA**: 7:1 ratio (ideal)
- **Level AA**: 4.5:1 ratio (minimum)
- **Gold on White**: 3.8:1 (use for non-critical text)
- **Brown on White**: 8.1:1 ✅

### Typography
- **Minimum font size**: 14px (small text)
- **Line height**: 1.5+ for body text
- **Letter spacing**: 2px+ for large headings
- **Max line length**: 60-70 characters (readability)

### Interactive Elements
- **Button size**: Minimum 44x44px (touch)
- **Click target**: Minimum 48x48px
- **Focus state**: Always visible (blue outline)
- **Link underlines**: Always visible on hover

---

## Dark Mode (Future)

### Dark Mode Palette
```css
--dark-bg: #1a1a1a;
--dark-card: #2a2a2a;
--dark-text: #f5f0eb;
--dark-accent: #d4af37;  /* Same gold */
```

Implementation strategy:
```css
@media (prefers-color-scheme: dark) {
    body {
        background: var(--dark-bg);
        color: var(--dark-text);
    }
}
```

---

## Print Styles (Optional)

```css
@media print {
    .navbar, .footer { display: none; }
    body { background: white; color: black; }
    a { text-decoration: underline; }
}
```

---

## Mobile First Approach

1. **Base Styles**: Mobile-optimized by default
2. **Breakpoints**: Add complexity as screen grows
3. **Touch**: All targets 44x44px minimum
4. **Performance**: Lighter images for mobile
5. **Navigation**: Simplified menu on small screens

---

## Design Tokens JSON Export

```json
{
  "colors": {
    "primary": {
      "gold": "#d4af37",
      "dark": "#8B4513",
      "rust": "#b85c3c"
    },
    "neutral": {
      "white": "#ffffff",
      "light": "#f5f0eb",
      "dark_text": "#333333",
      "gray_text": "#666666"
    }
  },
  "typography": {
    "display": "5rem",
    "h1": "3.5rem",
    "h2": "3rem",
    "h3": "1.5rem",
    "body": "1rem",
    "small": "0.95rem"
  },
  "spacing": {
    "xs": "8px",
    "sm": "12px",
    "md": "16px",
    "lg": "24px",
    "xl": "40px",
    "xxl": "60px"
  }
}
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Feb 2026 | Initial design system, 5 regions, complete styling |

---

**Design System Last Updated**: February 2026  
**Maintained by**: Gulzameen (Balochistan) Project Team  
**Status**: Complete & Production Ready ✅
