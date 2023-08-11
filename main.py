import time
import cv2
import numpy as np

reset_key = 82
reconding_key = 83
exit_key = 27
play_key = 32

play = False

bg_color = (203, 192, 255)
height = 300
width = 400

present_time = 0.0
start_time = 0
saved_time = 0

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
    min = sec//60
    sec = sec%60
    return "%02d:%02d.%s" % (min, sec, sosu[:3])

def watch_start():
    global start_time, play
    start_time = time.time()
    play = True
    
def watch_stop():
    global play, present_time, saved_time
    saved_time = present_time
    play = False
    
def watch_reset():
    global present_time, saved_time
    saved_time = 0
    present_time = 0.0
    watch_stop()

def time_recording():
    global present_time
    print(sec_to_text(present_time))

while True:
    if play:
        present_time = time.time() - start_time + saved_time
        
    scr = np.full((height,width,3), bg_color, dtype=np.uint8)
    cv2.putText(scr, sec_to_text(present_time), (50,100), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255 ), 3)
    
    cv2.imshow('stop_watch', scr)
    command = cv2.waitKey(5) & 0xFF
    if command == play_key:
        if play:
            watch_stop()
        else:
            watch_start()
    elif command == reset_key+32 or command == reset_key:
        watch_reset()
    elif command == reconding_key or command == reconding_key+32:
        time_recording()
    elif  command == exit_key:
        break
    
cv2.destroyAllWindows()