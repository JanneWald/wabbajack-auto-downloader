# wabbajack auto downloader
Do you have a gigantic modpack you saw on nexus? And are you tired of manually downloading each mod in wabbajack and don't want to spent $8 on premium nexus, you've come to the right spot!

Here are 2 different tools to solve this.
**NOTE: This speeds up and automates the install process but is still going to be much slower than paying for premium**

## AutoDownloader
This tool utilitizes UIA (UI Automation) which should owrk on most windows apps, including wabbajack. Requiring minimal setup and won't kidnap the mouse on your desktop.
#### Setup
You will need to install the following `$ pip install pywinauto`
#### Running
Simply have wabbajack open on the screen where it asks you to download. Run the program and confirm it is automatically invoking the download.

A friend tried this and said it was possible to have this running a seperate virtual desktop while using his PC normally.

It will try to click a new "SLOW DOWNLOAD" button for ~25 min before exiting automatically
## Autoclicker (Primitive)
This tool takes your physical mouse and automatically clicks the download button. This is the first design and should work on most distros and be consistent.
#### Setup
You will need to install the following `$ pip install pyautogui opencv-python pyscreeze pillow`
This script requires a target, in this case a screenshot of the 'slow download' button. Save this image as `target.png` in the same directory.
*Optionally you can also add a `pause.png`, picture of the download queue screen, so that you max attempts don't count*
#### Running
Keep wabbajack on same window that the script runs on. To be safe run on main window. Make sure that the wabbajack window is fully visible on your screen.

It will try to click a new download button for ~5 min before exiting automatically