# Python-KeyBoard-Sound
A program make you custom your own keyboard sound.

There are two method(scripts) to make custom keyboard sound.

1. using ```Pygame```
2. using ```keyboard``` and ```playsounds```

Ver 1.0:
* press 'esc' to stop
* please put mp3 into the sound folder

Ver 1.1:
* playsound module has bug:
  * please enter the module file and edit ```py command = ' '.join(command).encode('utf-16')``` into ```py command = ' '.join(command)``` since python3 is encode with utf-8
