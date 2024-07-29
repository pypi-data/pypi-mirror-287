# // Pygstudio template file created by pygstudio script (Version 1.0) 

# Notes:
# - You can delete these comments if you don't want them.
# - You can do basic configuration here for the game
# - This script is your main script and to be executed

# This code is for importing pygame to be used by other configurations:
# import pygame

# === This section is responsible for the screen ===
SCREEN_SIZE = (680, 420)
SCREEN_BACKGROUND = (255, 255, 255)

# === This section is responsible for the window ===
WINDOW_TITLE = "$MYPYGSTUDIOGAME"

# Use pygame.load.image() for setting window_icon. 
# Ex: WINDOW_ICON = pygame.image.load("mygame.png")
WINDOW_ICON = None      

# To use this config, you must import pygame and perform or operation on flags
# Example: pygame.RESIZABLE | pygame.OPENGL | ...
WINDOW_FLAGS = 0

# You can also use vsync by turning on the vsync flag
VSYNC = True

# Determines the frames per second. Use 0 for no limit
FPS = 60

import engine
engine.start(SCREEN_SIZE, SCREEN_BACKGROUND, WINDOW_FLAGS, WINDOW_TITLE, WINDOW_ICON, FPS, VSYNC)