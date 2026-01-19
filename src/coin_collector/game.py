import pygame
import sys
from .config import load_level

PLAYER_SIZE = 30

def run_game(level_paths: list[str], fps: int = 60, debug: bool = False):
    pygame.init()
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 24)
    big_font = pygame.font.SysFont("Arial", 64, bold=True)

    for path in level_paths:
        try:
            lvl = load_level(path)
        except Exception as e:
            print(f"Fehler beim Laden von {path}: {e}")
            continue

        screen = pygame.display.set_mode((lvl.width, lvl.height))
        pygame.display.set_caption(f"Coin Collector - Level: {path}")

        player = pygame.Rect(lvl.player_start.x, lvl.player_start.y, PLAYER_SIZE, PLAYER_SIZE)
        coins = [pygame.Rect(c.x - c.r, c.y - c.r, c.r*2, c.r*2) for c in lvl.coins]
        walls = [pygame.Rect(w.x, w.y, w.w, w.h) for w in lvl.walls]
        
        current_speed = lvl.speed
        score = 0
        total_coins = len(coins)
        level_running = True
        
        # Hilfsvariablen für Dash
        last_vx, last_vy = 1, 0 

        while level_running:
            dt = clock.tick(fps)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit(); sys.exit()
                    # DASH FUNKTION (Leertaste)
                    if event.key == pygame.K_SPACE:
                        dash_distance = 60
                        old_pos = player.topleft
                        player.x += last_vx * dash_distance
                        player.y += last_vy * dash_distance
                        # Check ob wir in einer Wand gelandet sind
                        for w in walls:
                            if player.colliderect(w):
                                player.topleft = old_pos # Zurückteleportieren bei Kollision

            # Bewegung berechnen
            keys = pygame.key.get_pressed()
            vx = (keys[pygame.K_RIGHT] or keys[pygame.K_d]) - (keys[pygame.K_LEFT] or keys[pygame.K_a])
            vy = (keys[pygame.K_DOWN] or keys[pygame.K_s]) - (keys[pygame.K_UP] or keys[pygame.K_w])
            
            if vx != 0 or vy != 0:
                if vx != 0 and vy != 0:
                    vx *= 0.7071
                    vy *= 0.7071
                last_vx, last_vy = vx, vy # Blickrichtung speichern

            # Kollision X
            player.x += int(vx * current_speed)
            for w in walls:
                if player.colliderect(w):
                    if vx > 0: player.right = w.left
                    elif vx < 0: player.left = w.right

            # Kollision Y
            player.y += int(vy * current_speed)
            for w in walls:
                if player.colliderect(w):
                    if vy > 0: player.bottom = w.top
                    elif vy < 0: player.top = w.bottom

            # Münzen sammeln
            new_coins = []
            for c in coins:
                if player.colliderect(c):
                    score += 1
                else:
                    new_coins.append(c)
            coins = new_coins

            # Zeichnen
            screen.fill((20, 20, 25))
            for w in walls:
                pygame.draw.rect(screen, (100, 100, 110), w, border_radius=4)
            for c in coins:
                pygame.draw.circle(screen, (255, 215, 0), c.center, c.width // 2)
            pygame.draw.rect(screen, (0, 200, 255), player, border_radius=8)

            # HUD
            hud = font.render(f"Coins: {score}/{total_coins} | Speed: {current_speed} | SPACE = Dash", True, (255, 255, 255))
            screen.blit(hud, (15, 15))

            if not coins:
                victory = big_font.render("LEVEL GESCHAFFT!", True, (0, 255, 150))
                screen.blit(victory, (lvl.width//2 - 250, lvl.height//2 - 40))
                pygame.display.flip()
                pygame.time.delay(1200)
                level_running = False

            pygame.display.flip()

    pygame.quit()