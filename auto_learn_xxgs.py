import pyautogui as pg
import random

# pg.FAILSAFE = False

def get_img_center_point(img_path):
    bounding_box = pg.locateOnScreen(img_path, confidence=0.8)
    if bounding_box:
        center_point = pg.center(bounding_box)
        print("found bounding box: ", bounding_box)
        return center_point
    print("bounding box not found")
    return None

btn_img = "C:\\Users\\JIANG\\Pictures\\matching\\btn.png"
progress_bar = "C:\\Users\\JIANG\\Pictures\\matching\\bar.png"
complete_img = "C:\\Users\JIANG\\Pictures\\matching\\replay.png"
sleep_interval = 60

# focus on chrome window
# pg.click(x=1191, y=1414)

W, H = pg.size()

while True:
    # detect pause
    center_point = get_img_center_point(btn_img)
    if center_point:
        pg.click(center_point, duration=0.5)


    # prevent lock screen
    pg.moveTo(x=random.randint(W//4, W-W//4), y=random.randint(H//4, H-H//4), duration=1)
    pg.sleep(3)

    # play next section video
    if pg.locateOnScreen(complete_img, confidence=0.6):
        pg.hotkey('ctrl', 'shift', 'tab')
        pg.sleep(1)
        pg.hotkey('ctrl', 'r')
        pg.sleep(3)
        print("play next section video")
        while True:
            center_point = get_img_center_point(progress_bar)
            if center_point:
                pg.click(center_point[0]+130, center_point[1], duration=0.5)
                break

    pg.sleep(sleep_interval) # sleep N seconds
