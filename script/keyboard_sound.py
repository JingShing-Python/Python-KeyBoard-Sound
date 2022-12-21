import os
import random
import threading
import sys
try:
    import playsound
    import keyboard
except:
        sys.exit()

# for packing program
def resource_path(relative):
	if hasattr(sys, "_MEIPASS"):
		absolute_path = os.path.join(sys._MEIPASS, relative)
	else:
		absolute_path = os.path.join(relative)
	return absolute_path

class KeyBoardSound:
    def __init__(self, mode='random_sound'):
        self.mode = mode
        self.sound_list = os.listdir('sound')
        keyboard.hook(self.keyboard_sound_program)
        # stop when press 'esc'
        keyboard.wait('esc')
    def play_sound(self):
        sound_file = 'sound/' + self.sound_list[random.randint(0, len(self.sound_list)-1)]
        playsound.playsound(resource_path(sound_file))
        
    def keyboard_sound_program(self, event):
        if event.event_type == 'down':
            print(event)
            threading.Thread(target=self.play_sound).start()

if __name__ == '__main__':
      key_board_sound = KeyBoardSound()
