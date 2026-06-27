# Swarakshit Home-First Content Alignment

Date: 2026-06-20

## Goal

Align the site content around the real product position:

- Swarakshit is a portable, rechargeable gas monitor
- The primary use case is homes and kitchens
- Broader environments can be mentioned carefully, but must not define the product

## Source Of Truth

The approved direction for this pass is:

- portable/rechargeable gas monitor for homes and kitchens first
- use home-first cleanup rather than consumer-only deletion or enterprise expansion

## Problems In Current Content

The current theme content mixes grounded product details with claims that feel invented, overstated, or outside the validated product scope.

Examples:

- named reports and exact risk-reduction percentages
- “world’s most advanced” style superlatives
- industrial deployment language such as ruggedized variants, mesh networks, BMS/SCADA integration, and facility-wide automation
- commercial compliance or enterprise-readiness claims that are not clearly supported
- Carbon Monoxide messaging in places where the product content elsewhere says the device is not designed for CO detection
- shipping, warranty, and payment claims that may not match the real business setup

## Positioning To Apply

### Primary Story

Swarakshit is a practical home safety device for Indian households using LPG or PNG. It helps users check for combustible gas leaks around kitchens, cylinders, pipelines, regulators, burner joints, and other common household gas points.

### Audience

- families
- parents
- households with elderly family members
- households with children
- people checking LPG cylinders, regulator joints, rubber pipes, PNG fittings, and gas geyser connections

### Secondary Story

The product may be usable in selected non-home environments where similar gas checks are needed, but these mentions must stay cautious, non-technical, and clearly secondary.

Allowed style:

- “also useful in selected small commercial kitchen setups”
- “contact us for bulk or specialized requirements”

Disallowed style:

- enterprise deployment claims
- industrial automation claims
- compliance promises unless confirmed
- infrastructure integration claims

## Content Principles

### Keep

- portable and rechargeable positioning
- kitchen safety and household gas leak prevention
- LERC trust language where already part of the brand story
- home-use scenarios like LPG cylinders, PNG pipelines, gas stoves, and gas geysers
- simple, direct, Indian-market-friendly copy

### Remove Or Rewrite

- invented authority references
- exact statistics unless verified and intentionally approved
- exaggerated testimonials
- glamorous or sexualized product language
- unsupported smart-platform language
- CO detection references that conflict with the product FAQ
- unsupported global shipping, warranty, and payment claims

## Page-Level Plan

### 1. `templates/page.application.json`

Purpose after rewrite:

- become the main kitchen solutions page
- explain realistic ways a home customer can bring Swarakshit into their kitchen

Planned changes:

- rename and rewrite hero copy so it feels like a kitchen/home solution page, not a vague “personalized set”
- remove the named study and 80 percent reduction claim
- rewrite the three kit descriptions around realistic home usage:
  - portable handheld/rechargeable checking
  - fixed placement near regular testing points
  - optional expanded setup only if phrased generically and safely
- keep contact CTA focused on home kitchen safety consultation or purchase help

### 2. `templates/page.usecase-kitchen.json`

Purpose after rewrite:

- remain the flagship use-case page
- present the strongest and most believable home safety story

Planned changes:

- keep the kitchen vulnerability framing, but make it tighter and less dramatic
- keep elderly/children safety angle because it fits the audience
- soften or remove exaggerated style-focused testimonial language
- replace “world’s most advanced gas detection technology” with grounded home-safety copy

### 3. `templates/index.json`

Purpose after rewrite:

- make the homepage consistent with the home-first product story

Planned changes:

- cards slider:
  - keep LPG cylinders, PNG pipelines, gas geysers
  - tone down “Hotels & Restaurants” so it becomes secondary, not core
  - adjust section heading/subtitle to sound home-first
- stats section:
  - remove or soften any exact numbers that are not clearly verified
  - keep the emotional and practical message, but avoid precise unsupported claims
- use cases section:
  - remove duplicate “Commercial Offices”
  - replace broad industrial/commercial emphasis with home-relevant use cases
  - rewrite intro text away from “industrial monitoring”
- testimonials:
  - keep calm, believable family-use feedback
  - remove flashy wording like “sleek, sexy”
- FAQ:
  - keep combustible-gas detection and battery guidance if it matches product reality
  - rewrite commercial-kitchen answer cautiously
  - preserve the clear warning that the device is not for CO if that remains the true product limitation

### 4. `templates/product.json`

Purpose after rewrite:

- make the product page accurate and trustworthy

Planned changes:

- device parameters:
  - keep combustible-gas coverage if accurate
  - rewrite “works everywhere” into home/kitchen-first wording
- shipping and warranty:
  - remove worldwide/free express/5-year promises unless confirmed
  - use safer wording based on known support and warranty info only
- payment options:
  - remove platform/payment claims unless confirmed by the store setup

### 5. `templates/page.usecase-commercial.json`

Purpose after rewrite:

- remain available only as a cautious secondary page

Planned changes:

- remove enterprise-grade, multi-user, auto-shutoff, and hospitality-leader language
- recast page as “small commercial kitchen and food-service discussion” if retained
- use simple wording around regular gas-check routines, staff safety, and contacting the team for suitability

### 6. `templates/page.usecase-industrial.json`

Purpose after rewrite:

- avoid misrepresenting the product as an industrial system

Planned changes:

- either heavily soften or reduce this page to a minimal inquiry-oriented page
- remove ruggedized hardware, mesh networking, BMS/SCADA integration, and enterprise audit claims
- if retained, position it as “contact us to discuss special environments” rather than a defined industrial offering

### 7. `templates/page.usecase-basement.json`

Purpose after rewrite:

- resolve the CO contradiction

Planned changes:

- remove CO-focused positioning if the product is not meant for CO
- reframe only around LPG/combustible gas accumulation in enclosed utility spaces, if still relevant
- otherwise consider de-emphasizing this page

### 8. `sections/svarakshit-app-text-block.liquid`

Purpose after rewrite:

- update the default schema content so future uses do not reintroduce incorrect messaging

Planned changes:

- remove Wi-Fi/server/shared-platform/CO language from defaults
- rewrite defaults around portable, rechargeable, home and kitchen gas-check usage
- remove “homes, offices, schools and industrial premises” from the default content

## Voice And Messaging Rules

- sound practical, calm, and safety-focused
- write for Indian homes and real household habits
- prefer “kitchen”, “family”, “cylinder”, “regulator”, “pipe”, “gas connection”, and “home safety”
- avoid sounding like a venture-backed industrial IoT platform
- avoid fear-mongering and avoid inflated luxury language

## Implementation Boundaries

- this pass is content alignment, not layout redesign
- update JSON template content and schema defaults only where needed
- avoid changing component structure unless a content change requires it
- preserve Shopify theme compatibility

## Risks To Watch

- theme editor may overwrite JSON template content later
- changing CO language must stay consistent across homepage, product page, and use-case pages
- removing unsupported commercial language may affect current SEO targeting, but accuracy is more important than breadth in this pass

## Verification Plan

- inspect changed JSON and Liquid content for consistency
- search repo for leftover unsupported phrases:
  - “CO”
  - “SCADA”
  - “BMS”
  - “mesh”
  - “enterprise”
  - “world’s most advanced”
  - “Safety First study”
  - “80%”
- verify the homepage, product page, kitchen/application pages, and secondary use-case pages now tell the same product story

## Open Notes

- This repo is not currently a Git repository from the working directory, so the spec cannot be committed from here unless the theme is later placed inside a Git repo root.
