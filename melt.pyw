from win32gui import *
import random, time, math
from win32con import *
from win32api import *

wide = 10 #based on pixels
magnitude = 10 #the intensity
noAnim = False #melting animation

def melt(w, m, anim):
    x, y = GetSystemMetrics(0), GetSystemMetrics(1)
    
    hwnd = GetDesktopWindow()
    hdc = GetWindowDC(hwnd)
    randx = random.randint(0, x)
    #-round(math.sin(i*5)+10)
    for i in range(w):
        BitBlt(hdc, randx, 0, i-round(w/2), y, hdc, randx, -round(math.sin(i*.205)+m), SRCCOPY)
        if anim:
            Sleep(10)
    ReleaseDC(hwnd, hdc)

while True:
    try:
        melt(wide, magnitude, not noAnim)
    except error:
        pass
    Sleep(500)
