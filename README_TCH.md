[English](README.md) | 繁體中文

# Python-KeyBoard-Sound
一個可以改變鍵盤聲音的程式。

## 可以在 [itch.io](https://jingshing.itch.io/keyboard-sound-player) 取得這個程式了！

## 所需的模組
有兩種不同的方式(腳本)開啟這個程式

1. 其一僅使用 ```Pygame```
2. 其二使用 ```keyboard``` 和 ```playsounds```
需要額外安裝

版本 1.0:
* 按 'esc' 停止程式
* 請放 mp3 進入 sound 資料夾

版本 1.1:
* playsound 模塊有 bug:
  * 請進入模塊腳本將此行 ```py command = ' '.join(command).encode('utf-16')``` 更改成 ```py command = ' '.join(command)``` 因為 python3 使用 utf-8 編碼

版本 1.2:
* 新增自定義模式
* 程式會讀取 ```setting.txt```
  * 設定目前可以更改模式和鍵盤按鍵的音效
    * 設定模式需要用這個格式 $\rightarrow$ ```mode=custom``` 或 ```mode=random```
      * custom 模式可以用來更改鍵位的音效，而 random 模式則是隨機撥放 sound 資料夾的音效
    * 設定鍵盤按鍵的音效需要用這個格式 $\rightarrow$ ```key:sample.mp3``` key 的位置要放英文的小寫
      * 只有有設定的按鍵在 custom 模式下，才能夠更改成按鍵的音效
版本 1.2.1
* 我更改了 ```playsound.py``` 從 行60 開始:
```py
try:
     exceptionMessage = ('\n    Error ' + str(errorCode) + ' for command:'
                         '\n        ' + command.decode('utf-16') +
                         '\n    ' + errorBuffer.raw.decode('utf-16').rstrip('\0'))
     logger.error(exceptionMessage)
     raise PlaysoundException(exceptionMessage)
 except:
     pass
```
* 這個可以修復多線程的bug，原本會導致字串和位元組轉換的類型錯誤修正
