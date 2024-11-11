import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Fonts
font = pygame.font.Font(None, 36)

# Start menu
def start_menu():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Space Invaders - Start Menu")
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return "start_game"
                elif event.key == pygame.K_h:
                    return "high_scores"
                elif event.key == pygame.K_s:
                    return "settings"

        screen.fill(BLACK)
        title_text = font.render("Space Invaders", True, WHITE)
        start_text = font.render("Press Enter to Start", True, WHITE)
        high_scores_text = font.render("Press H for High Scores", True, WHITE)
        settings_text = font.render("Press S for Settings", True, WHITE)

        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 4))
        screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2))
        screen.blit(high_scores_text, (SCREEN_WIDTH // 2 - high_scores_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(settings_text, (SCREEN_WIDTH // 2 - settings_text.get_width() // 2, SCREEN_HEIGHT // 2 + 100))

        pygame.display.flip()
        clock.tick(60)

# Pause menu
def pause_menu():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Space Invaders - Pause Menu")
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return "resume_game"
                elif event.key == pygame.K_q:
                    return "quit_game"

        screen.fill(BLACK)
        pause_text = font.render("Game Paused", True, WHITE)
        resume_text = font.render("Press Enter to Resume", True, WHITE)
        quit_text = font.render("Press Q to Quit", True, WHITE)

        screen.blit(pause_text, (SCREEN_WIDTH // 2 - pause_text.get_width() // 2, SCREEN_HEIGHT // 4))
        screen.blit(resume_text, (SCREEN_WIDTH // 2 - resume_text.get_width() // 2, SCREEN_HEIGHT // 2))
        screen.blit(quit_text, (SCREEN_WIDTH // 2 - quit_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))

        pygame.display.flip()
        clock.tick(60)

# Animations and visual effects
def add_animations():
    pass

# Ensure responsiveness
def ensure_responsiveness():
    pass
