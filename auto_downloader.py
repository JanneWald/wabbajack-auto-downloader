# This script automates the process of clicking slow download button in wobbajack
# By Janne Wald
# 4/29/2025

from pywinauto.application import Application
import optparse
import time

class ButtonPresser:
    def __init__(self, debug=False):
        self.debug = debug
        self.attempts = 0
        self.max_attempts = 300
        
    def connect_to_program(self, program):
        try:
            print("Connecting to Wabbajack...")
            app = Application(backend="uia")
            app.connect(title_re=program, timeout=5)
            self.main_window = app.top_window()
        
        except Exception as e:
            print(f"Error connecting to {program}: {e}")
            exit(1)
    
    def attempt_to_click(self, button_name):
        if self.debug: print("Available buttons:")
        if self.debug: print(self.main_window.print_control_identifiers())
        
        if self.debug: print(f"Attempt #{self.attempts}")
        try:
            self.main_window.child_window(title=button_name, control_type="Button").invoke()
            self.attempts = 0
            print("Clicked the button")
        
        except Exception as e:
            print(f"Error clicking {button_name}: {e}")
            self.attempts += 1
            if self.attempts >= self.max_attempts:
                print("Max attempts reached. Exiting...")
                exit(1)
    
    def spam_click(self, button_name):
        while True:
            self.attempt_to_click(button_name)
            time.sleep(5)
        
def main():
    parser = optparse.OptionParser()
    # Enables debug mode if -d is passed as an argument
    parser.add_option("-d", "--debug", action="store_true", dest="debug", default=False, help="Enable debug mode")
    (options, args) = parser.parse_args()
    
    downloader = ButtonPresser(debug=options.debug)
    downloader.connect_to_program(".*Wabbajack.*") 
    downloader.spam_click("SLOW DOWNLOAD")
    
    exit(0)

if __name__ == "__main__":
    main()