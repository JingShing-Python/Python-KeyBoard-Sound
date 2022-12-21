import os
import random
import threading
import sys
try:
    import playsound
    import keyboard
except:
    # if can not import main module it will exit
    sys.exit()

# for packing program
# if you need to pack file in the program
# I recommend this func to redirect your path to right path
def resource_path(relative):
	if hasattr(sys, "_MEIPASS"):
		absolute_path = os.path.join(sys._MEIPASS, relative)
	else:
		absolute_path = os.path.join(relative)
	return absolute_path

class KeyBoardSound:
    def __init__(self, path='setting.txt'):
        self.sound_list = os.listdir('sound')
        if len(self.sound_list)<0:
            sys.exit()
        # record pressed key for play sound
        self.pressed_key = None
        # load setting path can be init at the first
        self.setting_path = path
        self.setting = dict()
        # this func will load setting and init mode
        self.load_setting()

        keyboard.hook(self.keyboard_sound_program)
        # stop when press 'esc' or it will repeated upon line
        keyboard.wait('esc')

    def load_setting(self):
        try:
            with open(self.setting_path) as f:
                 for line in f.readlines():
                    line = line.replace('\n', '').replace('\r','')
                    if 'mode=' in line:
                        self.mode = line.split('=')[-1]
                    elif ':' in line:
                        line = line.split(':')
                        self.setting[line[0]]=line[-1]
        except:
            print('can not read setting!')
            self.mode = 'random'
                

    def play_sound(self):
        if self.mode == 'random':
            # random mode will randomly play any sound in sound folder
            sound_file = 'sound/' + self.sound_list[random.randint(0, len(self.sound_list)-1)]
            playsound.playsound(sound_file)
        elif self.mode == 'custom':
            # custom mode
            try:
                sound_file = 'sound/' + self.setting[self.pressed_key]
                playsound.playsound(sound_file)
            except:
                pass
        
    def keyboard_sound_program(self, event):
        if event.event_type == 'down':
            # set key to the pressed key
            self.pressed_key = event.name
            # using thread to play multiple sound at same time
            threading.Thread(target=self.play_sound).start()

if __name__ == '__main__':
      key_board_sound = KeyBoardSound()
