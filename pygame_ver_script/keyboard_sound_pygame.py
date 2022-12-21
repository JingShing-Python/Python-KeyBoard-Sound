import os
import sys
import random
try:
    import pygame
    pygame.init()
    pygame.mixer.init()
except:
    sys.exit()

def resource_path(relative):
	if hasattr(sys, "_MEIPASS"):
		absolute_path = os.path.join(sys._MEIPASS, relative)
	else:
		absolute_path = os.path.join(relative)
	return absolute_path

class KeyBoardSound_pygame:
    def __init__(self):
        self.sounds = os.listdir('sound')
        self.keyboard_sound_program()

    def play_sound(self):
        sound_file = 'sound/' + self.sounds[random.randint(0, len(self.sounds)-1)]
        pygame.mixer.music.load(resource_path(sound_file))
        pygame.mixer.music.play()
        
    def keyboard_sound_program(self):
        screen = pygame.display.set_mode((640, 480))
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    print(event)
                    self.play_sound()

if __name__ == '__main__':
    keyboard_sound = KeyBoardSound_pygame()
