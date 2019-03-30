# !/usr/bin/python3
# -*- coding: Utf-8 -*
from Classes import Display


# Main program
def main():
    # Instatiation display
    pygame = Display.Display()
    clock = pygame.pygame_display_time()
    done = False

    while not done:
        done = pygame.event_manager()
        pygame.pygame_display_flip()

    pygame.quit_pygame()


if __name__ == "__main__":
    main()
