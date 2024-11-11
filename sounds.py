import pygame

# Initialize Pygame mixer
pygame.mixer.init()

# Load sound effects
shoot_sound = pygame.mixer.Sound("sounds/shoot.wav")
explosion_sound = pygame.mixer.Sound("sounds/explosion.wav")
power_up_sound = pygame.mixer.Sound("sounds/power_up.wav")

# Load background music
pygame.mixer.music.load("sounds/background_music.mp3")

# Play background music
pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely

# Function to play sound effects
def play_sound(sound):
    sound.play()
