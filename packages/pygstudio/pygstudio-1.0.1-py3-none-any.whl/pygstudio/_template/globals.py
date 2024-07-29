# // Pygstudio template file created by pygstudio script (Version 1.1)
# ? You are free to edit this script

from typing import Optional
import pygame

running: bool = False

clock: pygame.time.Clock = pygame.time.Clock()
screen: Optional[pygame.Surface] = None

def on_event(event: pygame.event.Event) -> None:
    # This bindable function is called in every event.
    pass

def on_render(screen: pygame.Surface) -> None:
    # This bindable function is executed in every rendered step.
    pass

def on_init():
    # This bindable function is executed after the window initialization
    pass

def on_exit():
    # This bindable function is executed when the game exits
    pass