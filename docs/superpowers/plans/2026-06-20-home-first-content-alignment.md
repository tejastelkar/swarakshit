# Home-First Content Alignment Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Align Swarakshit theme content with the approved home-and-kitchen-first product positioning.

**Architecture:** Update theme JSON templates and a small number of Liquid schema defaults so homepage, product, application, and use-case pages all describe the same product story. Keep all changes content-only and preserve the existing Shopify section structure.

**Tech Stack:** Shopify theme JSON templates, Liquid sections, repo text search, JSON validation

## Global Constraints

- portable/rechargeable gas monitor for homes and kitchens first
- use home-first cleanup rather than consumer-only deletion or enterprise expansion
- sound practical, calm, and safety-focused
- write for Indian homes and real household habits
- avoid sounding like a venture-backed industrial IoT platform
- this pass is content alignment, not layout redesign
- preserve Shopify theme compatibility

---

### Task 1: Write The Execution Map

**Files:**
- Modify: `templates/index.json`
- Modify: `templates/product.json`
- Modify: `templates/page.application.json`
- Modify: `templates/page.usecase-kitchen.json`
- Modify: `templates/page.usecase-commercial.json`
- Modify: `templates/page.usecase-industrial.json`
- Modify: `templates/page.usecase-basement.json`
- Modify: `sections/svarakshit-app-text-block.liquid`

**Interfaces:**
- Consumes: approved spec at `docs/superpowers/specs/2026-06-20-home-first-content-alignment-design.md`
- Produces: a consistent set of page-level content updates and safer default schema copy

- [ ] **Step 1: Re-open the approved spec**

Run: `sed -n '1,260p' docs/superpowers/specs/2026-06-20-home-first-content-alignment-design.md`
Expected: the approved home-first positioning and page-level plan are visible

- [ ] **Step 2: Re-open the target templates**

Run: `sed -n '1,260p' templates/page.application.json && sed -n '1,260p' templates/page.usecase-kitchen.json && sed -n '1,260p' templates/page.usecase-commercial.json && sed -n '1,260p' templates/page.usecase-industrial.json && sed -n '1,260p' templates/page.usecase-basement.json`
Expected: all current content is visible and ready for rewrite

- [ ] **Step 3: Re-open homepage, product, and schema defaults**

Run: `sed -n '1,620p' templates/index.json && sed -n '1,260p' templates/product.json && sed -n '1,220p' sections/svarakshit-app-text-block.liquid`
Expected: all content sources that need alignment are visible

### Task 2: Rewrite Primary Home And Kitchen Content

**Files:**
- Modify: `templates/page.application.json`
- Modify: `templates/page.usecase-kitchen.json`

**Interfaces:**
- Consumes: current kitchen/application JSON structures
- Produces: accurate home-first kitchen copy with no unsupported claims

- [ ] **Step 1: Update the application page content**

Edit `templates/page.application.json` so it follows this content shape:

```json
{
  "hero": {
    "settings": {
      "title": "Kitchen Safety Solutions",
      "text": "Choose the Swarakshit setup that fits your home kitchen and daily gas safety routine."
    }
  },
  "intro": {
    "settings": {
      "heading": "Bring Swarakshit Into Your Kitchen",
      "text": "<p>Swarakshit helps households check for combustible gas leaks around stoves, cylinders, regulators, pipes, and other common kitchen gas points. It is portable, rechargeable, and easy to use as part of a regular home safety routine.</p>",
      "author": "~ Swarakshit Home Safety"
    }
  }
}
```

- [ ] **Step 2: Update the three kitchen kit descriptions**

Edit the `kits` blocks in `templates/page.application.json` so the descriptions follow this content direction:

```json
{
  "kit_1": {
    "settings": {
      "title": "Kitchen Kit No.1",
      "description": "<p>A portable rechargeable Swarakshit gas monitor for routine checks around LPG cylinders, PNG joints, regulators, burner connections, and other everyday kitchen gas points.</p>"
    }
  },
  "kit_2": {
    "settings": {
      "title": "Kitchen Kit No.2",
      "description": "<p>A Swarakshit gas monitor with a dedicated placement option for households that want a convenient fixed spot near their main kitchen testing area.</p>"
    }
  },
  "kit_3": {
    "settings": {
      "title": "Kitchen Kit No.3",
      "description": "<p>A broader kitchen safety setup for larger homes or multi-point checking routines, designed for families that want easier coverage across more than one gas connection area.</p>"
    }
  }
}
```

- [ ] **Step 3: Update kitchen use-case copy**

Edit `templates/page.usecase-kitchen.json` so the key copy follows this direction:

```json
{
  "hero": {
    "settings": {
      "subtitle": "Protect your family by checking for combustible gas leaks where daily cooking happens most."
    }
  },
  "intro_text": {
    "blocks": {
      "heading": {
        "settings": {
          "heading": "Everyday Cooking Spaces Need Everyday Gas Safety"
        }
      }
    }
  },
  "product": {
    "settings": {
      "left_text": "Bring home the Swarakshit portable gas monitor for regular kitchen safety checks around your stove, cylinder, pipe connections, and regulator."
    }
  }
}
```

- [ ] **Step 4: Soften kitchen testimonials**

Edit the testimonial copy in `templates/page.usecase-kitchen.json` so it stays believable and removes exaggerated styling language.

- [ ] **Step 5: Validate both JSON files**

Run: `node -e "JSON.parse(require('fs').readFileSync('templates/page.application.json','utf8')); JSON.parse(require('fs').readFileSync('templates/page.usecase-kitchen.json','utf8')); console.log('ok')"`
Expected: `ok`

### Task 3: Align Homepage And Product Messaging

**Files:**
- Modify: `templates/index.json`
- Modify: `templates/product.json`

**Interfaces:**
- Consumes: current homepage and product-page block content
- Produces: home-first messaging across hero, cards, use cases, testimonials, FAQ, and product tabs

- [ ] **Step 1: Rewrite homepage cards and use-case framing**

Edit `templates/index.json` to:

```json
{
  "svarakshit_cards_slider_G9qiDA": {
    "settings": {
      "heading": "Where Families Use Swarakshit",
      "subtitle": "From kitchen cylinders to PNG joints and gas geysers, Swarakshit helps households check the gas points they rely on every day."
    }
  },
  "svarakshit_use_cases": {
    "settings": {
      "heading": "Home Safety Use Cases",
      "text": "<p>Explore the everyday places where Indian households can use Swarakshit to check for combustible gas leaks and build safer daily habits at home.</p>"
    }
  }
}
```

- [ ] **Step 2: Remove unsupported homepage breadth**

Edit `templates/index.json` to remove duplicate or over-broad use cases like duplicate commercial offices and industrial-first emphasis. Keep home-relevant items and only light secondary mentions where needed.

- [ ] **Step 3: Soften homepage testimonials and FAQ**

Edit `templates/index.json` so:
- testimonials sound calm and believable
- “Can I use it for commercial kitchens?” becomes a cautious secondary-use answer
- unsupported exact statistics or overly confident commercial claims are softened

- [ ] **Step 4: Rewrite product detail tabs**

Edit `templates/product.json` so the product tabs follow this direction:

```json
{
  "param": {
    "settings": {
      "content": "<p><strong>Multi-Gas Detection:</strong> Detects LPG, PNG, CNG, methane and other combustible gases.</p><p><strong>LCD Display with 'Hi' Alert:</strong> Digital screen shows gas level information during use.</p><p><strong>LERC Certified:</strong> Built around trusted gas-safety positioning for Indian households.</p><p><strong>USB Rechargeable:</strong> Portable design for regular checks around the home and kitchen.</p><p><strong>Best Suited For:</strong> Home kitchens, LPG cylinder checks, PNG joints, gas regulator points, and similar household gas connections.</p>"
    }
  }
}
```

- [ ] **Step 5: Clean shipping and payment language**

Edit `templates/product.json` to remove unsupported claims like worldwide shipping, 5-year warranty, PayPal, Apple Pay, and Google Pay unless the store explicitly supports them.

- [ ] **Step 6: Validate both JSON files**

Run: `node -e "JSON.parse(require('fs').readFileSync('templates/index.json','utf8')); JSON.parse(require('fs').readFileSync('templates/product.json','utf8')); console.log('ok')"`
Expected: `ok`

### Task 4: Soften Secondary Use-Case Pages And Defaults

**Files:**
- Modify: `templates/page.usecase-commercial.json`
- Modify: `templates/page.usecase-industrial.json`
- Modify: `templates/page.usecase-basement.json`
- Modify: `sections/svarakshit-app-text-block.liquid`

**Interfaces:**
- Consumes: existing secondary-use JSON pages and Liquid schema defaults
- Produces: cautious secondary-use content and safe default copy for future pages

- [ ] **Step 1: Rewrite commercial page as secondary-use content**

Edit `templates/page.usecase-commercial.json` to remove enterprise, Wi-Fi alert, auto-shutoff, and hospitality-leader claims. Replace them with cautious wording about discussing suitability for selected small commercial kitchen environments.

- [ ] **Step 2: Rewrite industrial page into inquiry-led copy**

Edit `templates/page.usecase-industrial.json` to remove ruggedized hardware, mesh networking, BMS, SCADA, and industrial-system claims. Keep only minimal exploratory messaging if the page remains.

- [ ] **Step 3: Remove CO contradictions from basement page**

Edit `templates/page.usecase-basement.json` to remove CO claims and refocus only on enclosed household areas where combustible gas may collect, if that use case still makes sense.

- [ ] **Step 4: Update Liquid schema defaults**

Edit `sections/svarakshit-app-text-block.liquid` so the `content` default becomes:

```liquid
"default": "<p>Swarakshit is a portable rechargeable gas monitor designed to help households check for combustible gas leaks around kitchens and other home gas connection points.</p><p>Use it as part of a regular safety routine near LPG cylinders, PNG joints, regulators, burner connections, and gas appliances where early detection matters most.</p>"
```

- [ ] **Step 5: Validate JSON and scan defaults**

Run: `node -e "JSON.parse(require('fs').readFileSync('templates/page.usecase-commercial.json','utf8')); JSON.parse(require('fs').readFileSync('templates/page.usecase-industrial.json','utf8')); JSON.parse(require('fs').readFileSync('templates/page.usecase-basement.json','utf8')); console.log('ok')"`
Expected: `ok`

### Task 5: Verify Content Consistency

**Files:**
- Modify: `templates/index.json`
- Modify: `templates/product.json`
- Modify: `templates/page.application.json`
- Modify: `templates/page.usecase-kitchen.json`
- Modify: `templates/page.usecase-commercial.json`
- Modify: `templates/page.usecase-industrial.json`
- Modify: `templates/page.usecase-basement.json`
- Modify: `sections/svarakshit-app-text-block.liquid`

**Interfaces:**
- Consumes: all updated content files
- Produces: verified, internally consistent home-first messaging

- [ ] **Step 1: Run the unsupported-phrase search**

Run: `rg -n "Safety First study|80%|world's most advanced|SCADA|BMS|mesh|enterprise-grade|Carbon Monoxide|sleek, sexy|worldwide|PayPal|Apple Pay|Google Pay" templates sections`
Expected: no relevant unsupported marketing claims remain in the edited content

- [ ] **Step 2: Run a home-first phrase sanity check**

Run: `rg -n "portable|rechargeable|kitchen|LPG|PNG|cylinder|regulator|home" templates/index.json templates/product.json templates/page.application.json templates/page.usecase-kitchen.json sections/svarakshit-app-text-block.liquid`
Expected: key home-first terms appear across the primary pages

- [ ] **Step 3: Review the changed file diffs**

Run: `git diff -- templates/index.json templates/product.json templates/page.application.json templates/page.usecase-kitchen.json templates/page.usecase-commercial.json templates/page.usecase-industrial.json templates/page.usecase-basement.json sections/svarakshit-app-text-block.liquid`
Expected: content-only diffs with no accidental structural breakage

