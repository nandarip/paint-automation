import subprocess
import pyautogui
import time
import os

# Enable fail-safe feature
pyautogui.FAILSAFE = True

def step1_open_paint():
    print("Opening Paint")
    try:
        # Open Paint
        subprocess.Popen('mspaint.exe')
        time.sleep(2)  # Wait for Paint to open
        print("Paint opened successfully")
        return True
    except Exception as e:
        print(f"Error opening Paint: {e}")
        return False

def step2_add_text():
    print("Adding text")
    try:
        # Get Paint window position
        paint_window = pyautogui.getActiveWindow()
        x, y = paint_window.left, paint_window.top
        
        # Click on the text tool using keyboard shortcut 'T'
        pyautogui.press('t')
        time.sleep(1)  # Wait for tool selection
        
        # Calculate center of canvas
        canvas_x = x + paint_window.width // 2
        canvas_y = y + paint_window.height // 2
        
        # Click where to add text (center of canvas)
        pyautogui.click(x=canvas_x, y=canvas_y)
        time.sleep(1)  # Wait for text box to appear
        
        # Press Ctrl+B for bold
        pyautogui.hotkey('ctrl', 'b')
        time.sleep(0.5)
        
        # Press Ctrl+Shift+> to increase font size multiple times
        for _ in range(3):
            pyautogui.hotkey('ctrl', 'shift', '>')
            time.sleep(0.2)
        
        # Type the text
        pyautogui.write("This was drawn automatically!")
        time.sleep(0.5)
        
        # Click outside to finish text editing
        pyautogui.click(x=canvas_x + 200, y=canvas_y + 200)
        time.sleep(0.5)
        
        print("Text added successfully")
        return True
    except Exception as e:
        print(f"Error adding text: {e}")
        return False

def paint_demo():
    if step1_open_paint():
        print("Proceed to Step 2")
        if step2_add_text():
            print("All steps completed successfully!")
        else:
            print("Error in Step 2")
    else:
        print("Error in Step 1")

if __name__ == "__main__":
    paint_demo()