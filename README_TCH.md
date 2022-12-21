[English](README_TCH.md) | 繁體中文

# Python-KeyBoard-Sound
一個可以改變鍵盤聲音的程式。

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
