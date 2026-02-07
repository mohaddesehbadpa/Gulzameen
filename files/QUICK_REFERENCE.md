# Gulzameen (Balochistan) - Quick Reference Guide

## 🚀 Quick Start

### Install & Run
```bash
cd c:\Users\DeLL\Desktop\files
pip install -r requirements.txt
python app.py
# Visit: http://localhost:5000
```

---

## 📁 File Structure at a Glance

```
files/
├── app.py                    ← Main Flask application
├── data_enhanced.py         ← Regional data (5 regions)
├── requirements.txt         ← Python dependencies
├── README.md               ← Full documentation
├── IMPLEMENTATION_GUIDE.md ← Detailed guide
├── templates/
│   ├── base.html          ← Base template (nav + footer)
│   ├── index.html         ← Home page
│   ├── region.html        ← Region detail page
│   └── 404.html           ← Error page
└── static/
    ├── style.css          ← All CSS (2000+ lines)
    └── main.js            ← JavaScript features
```

---

## 🎨 Visual Features

| Feature | Location | Details |
|---------|----------|---------|
| Hero Section | index.html | Full-screen, animated, responsive |
| Region Cards | index.html | Hover effects, icons, descriptions |
| Cultural Treasures | index.html | 6 category cards with badges |
| Contribution CTA | index.html | Two-column layout, call-to-action |
| Region Details | region.html | Stories, songs, patterns in grids |
| Footer | base.html | Multi-column, social links |
| Animations | style.css | Fade-in, slide, parallax effects |
| Responsive | style.css | Mobile, tablet, desktop breakpoints |

---

## 🔧 How to Customize

### Change Colors
**File**: `style.css` → `:root` section
```css
--primary-color: #d4af37;        /* Gold accents */
--primary-dark: #8B4513;         /* Main dark brown */
--secondary-color: #b85c3c;      /* Rust for gradients */
```

### Add a New Region
**File**: `data_enhanced.py`
```python
"new_region": {
    "name": "Region Name",
    "description": "Description here",
    "stories": ["Story 1", "Story 2", ...],
    "songs": ["Song 1", "Song 2", ...],
    "patterns": ["Pattern 1", "Pattern 2", ...]
}
```

### Modify Hero Section
**File**: `index.html` → Find `<!-- Hero Section -->`
- Edit title, description, badges
- Change background image
- Adjust button text

### Add Animation Effects
**File**: `style.css` → `@keyframes` section
- Define new animation
- Apply to elements with `animation:` property

### Change Navigation Links
**File**: `base.html` → `.nav-menu` section
```html
<li><a href="/your-link" class="nav-link">Label</a></li>
```

---

## 📱 Responsive Breakpoints

| Device | Width | CSS Media Query |
|--------|-------|-----------------|
| Mobile | <480px | `@media (max-width: 480px)` |
| Tablet | 480-768px | `@media (max-width: 768px)` |
| Desktop | 768-1024px | `@media (max-width: 1024px)` |
| Large | >1024px | Default (no media query) |

---

## 🎯 Key Classes & IDs

### Navigation
- `.navbar` - Navigation container
- `.nav-logo` - Logo element
- `.nav-menu` - Menu list
- `.nav-link` - Menu links

### Hero Section
- `.hero` - Main hero container
- `.hero-content` - Content wrapper
- `.hero-title` - Title text
- `.hero-buttons` - Button group
- `.hero-stats` - Statistics display

### Cards
- `.region-card` - Region cards
- `.treasure-card` - Treasure category cards
- `.story-card` - Story cards
- `.song-card` - Song cards
- `.pattern-card` - Pattern cards

### Sections
- `.regions-section` - Regions area
- `.treasures-section` - Treasures area
- `.contribute-section` - Contribution area

### Utilities
- `.btn` - Button base class
- `.btn-primary` - Primary button style
- `.btn-secondary` - Secondary button style
- `.highlight` - Text highlight (gold)
- `.section-header` - Section titles

---

## 🔌 JavaScript Functions

### Animation Functions
- `initializeAnimations()` - Scroll-triggered animations
- `initializeScrollEffects()` - Parallax and navbar effects
- `initializeInteractiveElements()` - Button interactions
- `addSmoothScrolling()` - Anchor link smoothing

### Utility Functions
- `showNotification(message)` - Toast notifications
- `animateCountUp(element, target)` - Number animations
- `addRippleEffect(element)` - Click ripple effect
- `loadDynamicContent(url, target)` - Dynamic loading

---

## 🎬 Animation Reference

### Built-in Animations
```css
@keyframes fadeInDown      /* Top to bottom fade */
@keyframes fadeInUp        /* Bottom to top fade */
@keyframes slideInLeft     /* Left to right slide */
@keyframes pulse           /* Pulse effect */
@keyframes rotate          /* 360° rotation */
@keyframes ripple-animation /* Ripple effect */
```

### Apply Animation
```css
element {
    animation: fadeInUp 0.8s ease-out 0.5s both;
    /* animation-name duration easing delay fill-mode */
}
```

---

## 🎨 Color Palette Quick Reference

```
Gold:        #d4af37  (Primary accent, badges)
Dark Brown:  #8B4513  (Headings, main text)
Rust:        #b85c3c  (Gradients, borders)
Light BG:    #f5f0eb  (Card backgrounds)
White:       #ffffff  (Content areas)
Dark Text:   #333333  (Body text)
Gray Text:   #666666  (Secondary text)
```

---

## 🚨 Common Issues & Fixes

| Issue | Solution |
|-------|----------|
| Site won't load | Check Flask is running, visit http://localhost:5000 |
| CSS not applying | Clear cache (Ctrl+F5), check file paths |
| Animations stuttering | Check browser performance, reduce animations |
| Mobile layout broken | Test with browser dev tools, check media queries |
| Region not found | Add to data_enhanced.py, URL must match key |

---

## 📊 Content Statistics

```
Regions:           5
  - Stories:       20+
  - Songs:         20+
  - Patterns:      20+

Total Items:
  - Folk Stories:  156+
  - Songs:         89+
  - Patterns:      234+
  - Recipes:       67+
  - Festivals:     24+
  - Wisdom:        412+
```

---

## 🔐 Security Notes

- No user input validation needed (content-only site)
- No database credentials exposed
- Static file serving through Flask
- CSRF protection ready for forms (add when needed)
- XSS protection through Jinja2 auto-escaping

---

## 📈 Performance Tips

1. **Images**: Use optimized formats (WebP, JPEG)
2. **CSS**: Minify for production
3. **JS**: Load after content (already done)
4. **Fonts**: Use system fonts or efficient CDNs
5. **Caching**: Enable browser caching on server

---

## 🎓 Learning Resources

- **Flask Docs**: https://flask.palletsprojects.com
- **CSS Grid**: https://css-tricks.com/snippets/css/complete-guide-grid/
- **Animations**: https://developer.mozilla.org/en-US/docs/Web/CSS/animation
- **Responsive**: https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design

---

## 📝 Common Customizations

### Change Site Title
`templates/base.html` → `<title>` tag

### Add a New Section
1. Create HTML in `index.html`
2. Add CSS in `style.css`
3. Add content in `data_enhanced.py` if needed

### Change Font
`style.css` → `body` selector → `font-family`

### Modify Button Styles
`style.css` → `.btn`, `.btn-primary`, `.btn-secondary`

### Adjust Spacing
`style.css` → `padding`, `margin`, `gap` properties

---

## 🌐 Deployment Checklist

- [ ] Remove `debug=True` from `app.py`
- [ ] Minify CSS and JavaScript
- [ ] Optimize images
- [ ] Set up HTTPS
- [ ] Configure caching headers
- [ ] Test on production database
- [ ] Set up monitoring
- [ ] Configure backups

---

## 📞 Support

- **Project Creator**: Mohaddeseh Badpa
- **Instagram**: @mohaddeseh.badpa
- **About**: Digital celebration of Balochi culture

---

**Last Updated**: February 2026  
**Version**: 1.0 Complete  
**Status**: Ready for Use & Extension 🚀
