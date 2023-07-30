import time
import cv2
import numpy as np

play = False

bg_color = (203, 192, 255)
height = 300
width = 400

present_time = 0.0
start_time = 0

def making_button(img:np.ndarray, h, w, x=0.5,y=0.5):
    shape = img.shape
    x = int(shape[1] * x)
    y = int(shape[0] * y)
    hw = w//2
    hh = h//2
    cv2.rectangle(img,(x-hw,y-hh), (x+hw,y+hh), (0,0,0), 4)
    print((x-hw,y-hh), (x+hw,y+hh),'||', x,y,hw,hh)
    return img

def sec_to_text(time):
    sec = int(time)
    sosu = str(time).split('.')[1]
    sec = sec%60
    min = sec//60
    return "%02d:%02d.%s" % (min, sec, sosu[:3])

def watch_start():
    global start_time, play
    start_time = time.time()
    play = True
    
def watch_end():
    global play
    play = False

while True:
    if play:
        present_time = time.time() - start_time
    else:
        pass
    scr = np.full((height,width,3), bg_color, dtype=np.uint8)
    cv2.putText(scr, sec_to_text(present_time), (50,100), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255 ), 3)
    
    cv2.imshow('stop_watch', scr)
    command = cv2.waitKey(5)
    if command & 0xFF == 32:
        if play:
            watch_end()
        else:
            watch_start()
    elif  command & 0xFF == 27:
        break
    
cv2.destroyAllWindows()