---
name: swimlane-diagram
description: Takes a text description of a process and generates a beautiful swimlane diagram as a PNG file. Supports cross-lane handoffs with numbered steps and vertical connectors.
author: Ali Syed
version: 2.0.0
---

# Swimlane Diagram Generator

Turn a plain text process description into a beautiful swimlane diagram PNG — with cross-lane handoffs, numbered steps, and Anthropic-style colors.

## Input

`$ARGUMENTS` — a text description of a process. Can be a paragraph, bullet points, or a list of steps with roles/participants.

## Your Task

1. **Analyse the input** — extract:
   - Diagram title and subtitle
   - Participants / roles / departments (these become the swim lanes, ordered top to bottom)
   - Steps per participant, numbered in global sequence order (①②③…)
   - Cross-lane handoffs — which step in one lane triggers a step in another lane

2. **Generate a complete HTML file** following the template and rules below.

3. **Save the HTML** to `/tmp/swimlane.html`

4. **Run the screenshot script:**
   ```bash
   python3 /Users/syedwahabali/Documents/Projects/ClaudeCode/skills/swimlane-diagram/screenshot.py /tmp/swimlane.html /tmp/swimlane.png
   ```

5. **Open the PNG:**
   ```bash
   open /tmp/swimlane.png
   ```

---

## Full HTML Template

Use this exact CSS. Fill in title, subtitle, lanes, steps, connector rows, and cross connectors dynamically.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
    background: #FAF8F5;
    padding: 48px;
  }
  .title { font-size: 22px; font-weight: 700; color: #1A1A1A; margin-bottom: 8px; }
  .subtitle { font-size: 13px; color: #8B8480; margin-bottom: 32px; }
  .diagram {
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 8px 32px rgba(0,0,0,0.12), 0 2px 6px rgba(0,0,0,0.07);
    border: 1px solid #D8D0C8;
    display: inline-block;
    min-width: 900px;
  }
  .lane {
    display: flex;
    align-items: center;
    border-bottom: 1px solid #EDE8E0;
    min-height: 90px;
  }
  .lane:last-child { border-bottom: none; }
  .connector-row {
    display: flex;
    align-items: center;
    background: #F7F4F0;
    border-bottom: 1px solid #EDE8E0;
    min-height: 36px;
  }
  .lane-label {
    width: 140px; min-width: 140px;
    display: flex; align-items: center; justify-content: center;
    padding: 20px 14px;
    font-size: 11px; font-weight: 700; color: white;
    text-align: center; letter-spacing: 0.8px; text-transform: uppercase;
    line-height: 1.5; align-self: stretch;
  }
  .connector-label { width: 140px; min-width: 140px; background: #F0EDE8; }
  .lane-body {
    flex: 1; display: flex; align-items: center;
    padding: 16px 24px; gap: 8px; background: #FFFEFB;
  }
  .connector-body {
    flex: 1; display: flex; align-items: center;
    padding: 0 24px; gap: 8px; min-height: 36px;
  }
  .step {
    background: white; border: 1.5px solid; border-radius: 10px;
    padding: 10px 16px; font-size: 12px; font-weight: 500; color: #1A1A1A;
    text-align: center; min-width: 120px; line-height: 1.4;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08); white-space: nowrap;
  }
  .step .badge {
    display: block; font-size: 10px; font-weight: 700;
    margin-bottom: 4px; opacity: 0.6;
  }
  .step.start, .step.end { border-radius: 50px; font-weight: 600; }
  .step.decision { border-radius: 4px; background: #FDF8F2; font-style: italic; }
  .arrow { font-size: 16px; color: #BDB5AC; flex-shrink: 0; }
  .cross {
    display: flex; flex-direction: column; align-items: center;
    gap: 2px; min-width: 120px;
  }
  .cross .line { width: 1.5px; height: 18px; background: #BDB5AC; }
  .cross .down { font-size: 14px; color: #BDB5AC; }
  .cross .label { font-size: 10px; color: #8B8480; font-style: italic; }
</style>
</head>
<body>

<div class="title">TITLE HERE</div>
<div class="subtitle">SUBTITLE HERE</div>

<div class="diagram">

  <!-- Lane 1 -->
  <div class="lane">
    <div class="lane-label" style="background: #CF6749;">Lane 1</div>
    <div class="lane-body">
      <div class="step start" style="border-color: #CF6749;">
        <span class="badge" style="color:#CF6749;">① START</span>
        First Step
      </div>
      <div class="arrow">→</div>
      <div class="step" style="border-color: #CF6749;">
        <span class="badge" style="color:#CF6749;">③</span>
        Another Step
      </div>
    </div>
  </div>

  <!-- Connector row between Lane 1 and Lane 2 -->
  <!-- Position .cross elements under the steps that hand off -->
  <div class="connector-row">
    <div class="connector-label"></div>
    <div class="connector-body">
      <div class="cross">
        <div class="line"></div>
        <div class="down">↓</div>
        <div class="label">trigger label</div>
      </div>
      <!-- Use spacer divs to align connectors under correct steps -->
    </div>
  </div>

  <!-- Lane 2 -->
  <div class="lane">
    <div class="lane-label" style="background: #7B9E87;">Lane 2</div>
    <div class="lane-body">
      <div class="step" style="border-color: #7B9E87;">
        <span class="badge" style="color:#7B9E87;">②</span>
        Received Step
      </div>
      <div class="arrow">→</div>
      <div class="step end" style="border-color: #7B9E87;">
        <span class="badge" style="color:#7B9E87;">④ END</span>
        Final Step
      </div>
    </div>
  </div>

</div>

</body>
</html>
```

---

## Color Palette (use in order)

| Lane | Color |
|------|-------|
| 1 | `#CF6749` — Anthropic coral |
| 2 | `#7B9E87` — sage green |
| 3 | `#5B7FA6` — muted blue |
| 4 | `#9B7BB8` — soft purple |
| 5 | `#C4853A` — warm amber |
| 6 | `#7A9E9F` — teal |

---

## Rules

- Number ALL steps globally in sequence order (①②③④…) across all lanes — the numbers tell the story.
- Use `start` class on the very first step, `end` class on the very last step.
- Use `decision` class on steps that are decisions or approvals.
- Add a `connector-row` between two lanes ONLY when a handoff happens between them.
- Use `<div style="flex:1"></div>` to push steps to the right within a lane when they start later in the timeline.
- Use spacer `<div style="width:Xpx"></div>` in connector rows to align `.cross` elements under the correct steps above.
- Keep step labels short — 3–5 words max.
- Connector `.label` text should describe the handoff trigger (e.g. "notified", "accepted", "approved", "triggered").
- Do not add any explanation — just generate the HTML, run the screenshot command, and open the PNG.
