English | [繁體中文](README_TCH.md)
# Python-KeyBoard-Sound
A program make you custom your own keyboard sound.

## Require modules
There are two method(scripts) to make custom keyboard sound.

1. using ```Pygame```
2. using ```keyboard``` and ```playsounds```

Ver 1.0:
* press 'esc' to stop
* please put mp3 into the sound folder

Ver 1.1:
* playsound module has bug:
  * please enter the module file and edit ```py command = ' '.join(command).encode('utf-16')``` into ```py command = ' '.join(command)``` since python3 is encode with utf-8

Ver 1.2:
* Add custom mode
* it will load ```setting.txt``` to the program.
  * the setting can be contain with key custom sound and mode setting
    * setting mode with this format $\rightarrow$ ```mode=custom``` or ```mode=random```
      * custom can be use for edit key and random is for random play sound in sound folder
    * setting key with this format $\rightarrow$ ```key:sample.mp3``` the key need to be lower case.
      * it will only play sound when you press the key in the setting in custom mode
