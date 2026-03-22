# explain-to-exec — Claude Code Skill

A Claude Code skill that translates technical content into clear executive communication.

## What it does

Engineers are great at solving problems. Communicating them to leadership is a different skill entirely.

`/explain-to-exec` takes any technical input — bug reports, pull requests, architecture proposals, incidents, stack traces — and transforms it into a clean executive briefing with:

- **Plain English situation summary** — no jargon
- **Business impact** — customers affected, revenue risk, cost exposure
- **Timeline** — concrete dates, not sprint numbers
- **Decision needed** — one clear ask, easy to act on

## Install

### Option A — Personal (works in all your projects)
```bash
mkdir -p ~/.claude/skills/explain-to-exec
curl -o ~/.claude/skills/explain-to-exec/SKILL.md \
  https://raw.githubusercontent.com/wahabali/claude-skills/main/explain-to-exec/SKILL.md
```

### Option B — Project only
```bash
mkdir -p .claude/skills/explain-to-exec
curl -o .claude/skills/explain-to-exec/SKILL.md \
  https://raw.githubusercontent.com/wahabali/claude-skills/main/explain-to-exec/SKILL.md
```

## Usage

```
/explain-to-exec NullPointerException in PaymentService at line 247...
```

Or just type your technical content after the slash command. Claude handles the rest.

## Examples

See the [`examples/`](./examples/) folder for real input/output pairs:
- [`bug-report.md`](./examples/bug-report.md) — production bug with downtime impact
- [`pull-request.md`](./examples/pull-request.md) — security migration PR
- [`architecture-proposal.md`](./examples/architecture-proposal.md) — microservices proposal with cost breakdown

## Output structure

```
SITUATION         — what is happening, plain English
IMPACT            — business / customer / revenue effect
WHAT WE'RE DOING  — team response (for incidents/bugs)
COST              — time, money, resources (for proposals)
TIMELINE          — concrete dates
DECISION NEEDED   — one clear ask, or "informational only"
```

## Who it's for

- Engineers who need to write up-to-management summaries
- Tech leads preparing board or leadership updates
- Product managers translating engineering work for stakeholders
- Anyone bridging the technical ↔ business communication gap

## Compatible with

Claude Code · Claude.ai · ChatGPT · Codex · Any tool supporting the [Agent Skills open standard](https://agentskills.io)

---

Built by [Syed Wahab Ali](https://linkedin.com/in/wahabali) · [More Claude skills coming](https://github.com/wahabali/claude-skills)
