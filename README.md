# CoinGame
A Little Game where you need to collect all Coins

Ziel des Spiels ist es, alle goldenen Münzen in jedem Level einzusammeln, um zum nächsten Level zu gelangen.

Bewegen: Nutze die Pfeiltasten oder WASD (W, A, S, D).

Dash (Sprint): Drücke die Leertaste, um einen schnellen Satz in deine aktuelle Blickrichtung zu machen. Damit kommst du schneller durch Labyrinthe oder entkommst Sackgassen.

Level-Ende: Sobald die letzte Münze verschwindet, lädt das Spiel nach einer kurzen Pause automatisch das nächste Level.

Beenden: Drücke jederzeit ESC, um das Spiel zu schließen.

Kopiere diesen Block komplett in deine PowerShell. Er lädt alle deine Level in der richtigen Reihenfolge (vom einfachsten zum schwersten):

PowerShell

uv run python -m src.coin_collector `
  src/coin_collector/levels/level_example.json `
  src/coin_collector/levels/erstes_level.json `
  src/coin_collector/levels/level_02_parkour.json `
  src/coin_collector/levels/level_03_zigzag.json `
  src/coin_collector/levels/maze_level.json `
  src/coin_collector/levels/final_boss.json
(Hinweis: Falls du eine Fehlermeldung bekommst, prüfe kurz, ob deine Datei wirklich erstes_level.json oder noch erstes_level.jason heißt und passe den Namen im Befehl ggf. an.)
