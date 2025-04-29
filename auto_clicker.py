# This script uses your cursor to automatically click a target on the screen
# Make sure target.png is in the same directory
# Also the target has to exactly the same as the button, screenshot then crop the button,
# Having definable borders/edges in the target picture helps the script to find the button

# By Janne Wald
# 4/28/2025

import pyautogui
import time
import os
import random
# user needs to: $ pip install pyautogui opencv-python pyscreeze pillow

end = "\033[0m"
green = "\033[32m"
red = "\033[31m"
yellow = "\033[33m"
target = "target.png" # Image to find
pause = "pause.png"
max_attempts = 300 # Number of attempts to find the image, giving large timer to prevent queue from canceling program
attempts = 0
mouse_speed = 1
has_pause = False

warning = f"""{red}
  __  .__                                                          
_/  |_|  |__   ____     ____  __ _________  _________________      
\   __\  |  \_/ __ \  _/ ___\|  |  \_  __ \/  ___/  _ \_  __ \     
 |  | |   Y  \  ___/  \  \___|  |  /|  | \/\___ (  <_> )  | \/     
 |__| |___|  /\___  >  \___  >____/ |__|  /____  >____/|__|        
           \/     \/       \/                  \/                  
.__         .____    ________   ________    ____________________._.
|__| ______ |    |   \_____  \  \_____  \  /   _____/\_   _____/| |
|  |/  ___/ |    |    /   |   \  /   |   \ \_____  \  |    __)_ | |
|  |\___ \  |    |___/    |    \/    |    \/        \ |        \ \|
|__/____  > |_______ \_______  /\_______  /_______  //_______  / __
        \/          \/       \/         \/        \/         \/  \/                      
{end}"""

def main():
    global attempts, has_pause
    print(warning)
    
    if not os.path.exists(target):
        print(f"{red}Error: {target} not found!{end}")
        print(f"{yellow}Please place the image in the same directory as this script.{end}")
        exit(1)
    
    if os.path.exists(pause):
        has_pause = True
        print(f"{yellow}Pause image found. Will check for pause screen before adjusting attempts{end}")
    
    # Get screen size
    screen_width, screen_height = pyautogui.size()
    print(f"Running on screen size: {screen_width} x {screen_height}")
    
    while True:
        # Set random speed for fun
        mouse_speed = random.uniform(0.03, 3.45)
        # Move mouse to the center of the screen
        pyautogui.moveTo(screen_width / 2, screen_height / 2, duration=mouse_speed)
        
        try_find_image(target, True)
        time.sleep(1)

        if has_pause:
            found = try_find_image(pause, False)
            if found:
                attempts = 0
                print(f"{yellow}Pause screen found. Waiting for 5 seconds to hopefully clean up queue{end}")
                time.sleep(5)
                    
def try_find_image(target, clicking):
    global attempts

    # Look for the button
    try:
        # Button found
        location = pyautogui.locateOnScreen(target, confidence=0.7)
        print(f"{green}{target} found!{end}")
        
        box = (location.left, location.top, location.width, location.height)
        box = tuple(int(x) for x in location)        
        print(box)
        screenshot = pyautogui.screenshot(region=box)
        screenshot.save('what_it_matched.png')
        
        pyautogui.moveTo(box[0] + box[2] // 2, box[1] + box[3] // 2, duration=mouse_speed)
        if clicking: print("Clicking the button...")
        if clicking: pyautogui.click()
        attempts = 0
        return True
    
    except Exception as e:
        # Button not found
        print(f"{yellow}{target} not found. Waiting for 5 seconds before retrying...{end}", e)
        attempts += 1
        if attempts >= max_attempts:
            print(f"{red}Max attempts reached. Exiting...{end},")
            exit(101010)
        
        else:
            print(f"{yellow}Attempt {attempts}/{max_attempts} failed.{end}")
            # Wait for 5 seconds before retrying
            return False

if __name__ == "__main__":
    main()