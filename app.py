from __future__ import annotations

import random
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Inhalte auch serverseitig verfügbar (für API)
WISHES = [
    "Gute Besserung, Kiddo! Nimm pls die Zeit, die dein Körper braucht.",
    "Ich hoffe, du fühlst dich schon ganz bald wieder stabiler, Schritt für Schritt, (Mittelfinger).",
    "Möge die Naivität deinen Kopf verlassen!",
    "Nerv nicht",
    "Du nervst",
    "Ich hasse dich",
    "Du bist klein",
]

TIPS = [
    "Tipp: Stell dir ein Glas Wasser/Tee direkt ans Bett – dann trinkst du automatisch häufiger.",
    "Tipp: Lauwarmer Tee + Honig kann den Hals beruhigen (Honig nicht für Kinder unter 1 Jahr).",
    "Tipp: Kurze, lauwarme Dusche oder Inhalation mit Wasserdampf kann sich gut anfühlen – vorsichtig bei Schwindel.",
    "Tipp: Nasenspray/Salzspray kann die Nase befreien; Nasenspülung hilft vielen ebenfalls.",
    "Tipp: Suppe/Brühe liefert Flüssigkeit + Salz und ist oft leichter runterzubekommen.",
    "Tipp: Wenn Fieber da ist: eher Ruhe + trinken als Sport – und bei anhaltenden Symptomen abklären.",
]

@app.get("/")
def index():
    # Übergib Wishes/Tips an das Template, damit dein JS sie nutzen kann
    return render_template("index.html", wishes=WISHES, tips=TIPS)

@app.get("/checklist")
def checklist():
    items = [
        ("💧 Trinken", "Glas Wasser/Tee in den nächsten 20–30 Minuten"),
        ("🛌 Ruhen", "15–30 Min. Pause ohne Screen"),
        ("🍲 Warm essen", "Suppe/Brühe/Haferbrei, wenn’s geht"),
        ("🌬️ Lüften", "5 Minuten stoßlüften"),
        ("🧣 Warm halten", "Socken/Decke (aber nicht überhitzen)"),
    ]
    return render_template("checklist.html", items=items)

@app.get("/api/wish")
def api_wish():
    return jsonify(wish=random.choice(WISHES))

@app.get("/api/tip")
def api_tip():
    return jsonify(tip=random.choice(TIPS))

@app.get("/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
