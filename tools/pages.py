#!/usr/bin/env python3
"""Each game's help page (aha.html, cozy.html, antfarm.html, messenger.html), with the site's header and menu.
The privacy lines follow each game's Privacy Policy (made by safaoz90.github.io tools/legal.py): change both together.

    python3 tools/pages.py
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
EMAIL = "support@wozzly.com"
REFUND = '<a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>'

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{name} · Help · Wozzly</title>
<meta name="description" content="Help and support for {name}: answers to common questions, privacy and how to reach us.">
<meta name="theme-color" content="#15132b">
<link rel="icon" href="{icon}">
<link rel="stylesheet" href="site.css">
</head>
<body>
<header class="top"><div class="wrap">
  <a class="brand" href="./"><img src="img/mochi.png" alt="Mochi, the Wozzly mascot"><span><b>Wozzly</b><small>Calm &amp; cheerful games</small></span></a>
  <nav class="menu" aria-label="Sections">
    <a href="./#games" class="on">Games</a><a href="./#featured">Featured</a><a href="./#why">Why Wozzly</a><a href="./#press">Press</a><a href="./#contact">Contact</a>
  </nav>
</div></header>
<main class="wrap page">
<div class="head"><img src="{icon}" alt=""><div><p class="kicker" style="margin-bottom:6px">Help and support</p><h1 style="font-size:clamp(30px,6vw,44px)">{name}</h1><p class="muted" style="margin:6px 0 0">{tag}</p></div></div>
"""

FOOT = """<footer><div class="wrap"><span>© 2026 Wozzly</span><span><a href="./">All games</a><a href="{privacy}">Privacy Policy</a><a href="{terms}">Terms of Use</a></span></div></footer>
</body>
</html>
"""

PRIVACY_COMMON = [
    "No account, no name, no email: the game never asks who you are.",
    "Videos are optional. Ads are personalised only if you allow tracking in Apple’s question; you can change it in iOS Settings at any time.",
    "Meta’s SDK tells Meta when the game is installed and opened, and about purchases, so we can measure our ads on Facebook and Instagram.",
    "Payments are handled by Apple. We never see your card or Apple Account, and we don’t sell personal information.",
]

GAMES = [
    dict(file="antfarm.html", name="Ant Farm: Sort Puzzle", tag="Cute ants, fruity sort puzzles", icon="img/antfarm-icon.png",
         privacy="antfarm-privacy.html", terms="antfarm-terms.html", qa=[
        ("Stuck on a level?", "Plan your taps before you start: the shelf only has five spots. A fruit with nowhere to go waits on the shelf and hops into its chamber as soon as there’s room. Boosters help on the hardest levels."),
        ("Out of lives?", "Lives grow back over time. You can also watch an optional video for one."),
        ("New phone?", "Your progress is kept in your own iCloud account: sign in with the same Apple Account and it comes back."),
        ("A purchase went wrong?", f"Payments are handled by Apple. You can ask for a refund at {REFUND}."),
    ], privacy_lines=[
        "Your progress is saved on your device and in your own iCloud account; we never receive it.",
        "Anonymous gameplay statistics (Google Firebase, without the advertising identifier) help us improve the levels.",
    ]),
    dict(file="messenger.html", name="Messenger: Last Warning", tag="Tower defense with a story", icon="img/messenger-icon.png",
         privacy="messenger-privacy.html", terms="messenger-terms.html", qa=[
        ("Stuck on a level?", "Build near the bends of the path, where enemies stay in range longest, and upgrade your best buildings with crystals. Boosters (Crystal Rush, Freeze, Overclock, Airstrike) help on the hardest waves."),
        ("Out of lives?", "Lives grow back over time. You can also refill them with coins, or watch an optional video for one."),
        ("New phone?", "Your coins and progress are kept with your own iCloud account: signed in with the same Apple Account, they come back after a reinstall and on your other devices."),
        ("A purchase went wrong?", f"Payments are handled by Apple. You can ask for a refund at {REFUND}."),
    ], privacy_lines=[
        "Your progress is saved on your device and in your own iCloud account; we never receive it.",
        "Anonymous gameplay statistics (Google Firebase, without the advertising identifier) help us improve the levels.",
    ]),
    dict(file="cozy.html", name="Cozy Puzzles - 4 Seasons", tag="Jigsaws of the world’s loveliest places", icon="img/cozy-icon.png",
         privacy="cozy-privacy.html", terms="cozy-terms.html", qa=[
        ("Can’t find where a piece goes?", "Hold the eye to see the whole picture, or turn on the faint picture on the board. The edge and colour filters keep the piece tray tidy, and a wrong piece stays loose so you always know what fits."),
        ("How do I open more puzzles?", "The first puzzle of every season is free; solve one to open the next. You can also open a whole season at once in the shop. There are no subscriptions."),
        ("Bought something on another phone?", "Sign in with the same Apple Account and tap <b>Restore purchases</b> in the shop. Seasons you opened come back; hints you used up don’t."),
        ("A purchase went wrong?", f"Payments are handled by Apple. You can ask for a refund at {REFUND}."),
    ], privacy_lines=[
        "Anonymous play statistics (Google Firebase, without the advertising identifier) help us improve the puzzles. Your photos are never part of them.",
        "Photos you turn into puzzles stay on your device and are never uploaded.",
    ], credits=True),
    dict(file="aha.html", name="Aha! Brain Puzzles", tag="Little puzzles with a clever twist", icon="img/aha-icon.svg",
         privacy="privacy.html", terms="terms.html", qa=[
        ("Stuck on a puzzle?", "Tap <b>Hint</b> for a gentle nudge; a second hint shows the answer. You can also tap <b>Ask someone for help</b> to send the puzzle to a friend."),
        ("Bought something on another phone?", "Sign in with the same Apple Account, then open the shop or Settings and tap <b>Restore purchases</b>. Stage packs, “Everything” and special stages come back; lamp packs are used up and don’t."),
        ("A purchase went wrong?", f"Payments are handled by Apple. You can ask for a refund at {REFUND}."),
    ], privacy_lines=[
        "Anonymous play statistics (Google Analytics for Firebase, without the advertising identifier) help us improve the puzzles.",
        "If a grown-up chooses <b>Under 13</b> in Settings, the game sends no statistics and shows no ads.",
    ]),
]


def page(g):
    out = [HEAD.format(**g)]
    out.append('<section class="card" style="padding-block:clamp(22px,4vw,36px)">\n<h2>Common questions</h2>\n')
    for q, a in g["qa"]:
        out.append(f"<h3>{q}</h3>\n<p>{a}</p>\n")
    out.append(f'<h3>Anything else</h3>\n<p>Write to <a href="mailto:{EMAIL}">{EMAIL}</a>. Please include your iPhone or iPad model and what happened.</p>\n</section>\n')
    lines = PRIVACY_COMMON[:1] + g["privacy_lines"] + PRIVACY_COMMON[1:]
    out.append('<section class="card" style="padding-block:clamp(22px,4vw,36px)">\n<h2>Privacy</h2>\n<ul>\n')
    out += [f"<li>{l}</li>\n" for l in lines]
    extra = ' · <a href="cozy-credits.html">Photo credits</a>' if g.get("credits") else ""
    out.append(f'</ul>\n<p><a href="{g["privacy"]}">Read the full Privacy Policy</a> · <a href="{g["terms"]}">Terms of Use</a>{extra}</p>\n</section>\n</main>\n')
    out.append(FOOT.format(**g))
    (ROOT / g["file"]).write_text("".join(out), encoding="utf-8")


for g in GAMES:
    page(g)
print("wrote", ", ".join(g["file"] for g in GAMES))
