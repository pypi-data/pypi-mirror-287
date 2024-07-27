class msgbox:

    def __init__(self, title, message,typeOfBox):
        self.message = message
        self.title = title
        self.typeOfBox = typeOfBox


        import ctypes 


        if typeOfBox == "MB_OK":
            typeOfBox = 0x0
        
        elif typeOfBox == "MB_OKCXL":
            typeOfBox = 0x01

        elif typeOfBox == "MB_YESNOCXL":
            typeOfBox = 0x03
        
        elif typeOfBox == "MB_YESNO":
            typeOfBox = 0x04

        elif typeOfBox == "MB_HELP":
            typeOfBox = 0x4000

        elif typeOfBox == "ICON_EXCLAIM":
            typeOfBox = 0x30

        elif typeOfBox == "ICON_INFO":
            typeOfBox = 0x40

        elif typeOfBox == "ICON_STOP":
            typeOfBox = 0x10

            
        ctypes.windll.user32.MessageBoxW(0,message,title,typeOfBox)


class clipbored:
    def __init__(self, text):
        self.text = text
        import os
        command = 'echo ' + text.strip() + '| clip'
        os.system(command)

class bsod:
    def __init__(self):
        from ctypes import windll
        from ctypes import c_int
        from ctypes import c_uint
        from ctypes import c_ulong
        from ctypes import POINTER
        from ctypes import byref

        nullptr = POINTER(c_int)()

        windll.ntdll.RtlAdjustPrivilege(
            c_uint(19), 
            c_uint(1), 
            c_uint(0), 
            byref(c_int())
        )

        windll.ntdll.NtRaiseHardError(
            c_ulong(0xC000007B), 
            c_ulong(0), 
            nullptr, 
            nullptr, 
            c_uint(6), 
            byref(c_uint())
        )

#typeing effect
class scroll:
    defaultSpeed = 1
    def __init__(self,str,speed=defaultSpeed):
        import sys
        import time

        self.str = str
        self.speed = int(speed)
        
        for x in str:
            sys.stdout.write(x)
            sys.stdout.flush()
            time.sleep(speed/10)
        print()

class winpos:
    def __init__(self):

        import ctypes.wintypes
        hwnd = self.user32.GetForegroundWindow()
        rect = self.wintypes.RECT()
        
        # Get the window rectangle
        self.user32.GetWindowRect(hwnd, ctypes.byref(rect))
        
        # Return the position (left, top) as a tuple
        return rect.left, rect.top
        
class windowMoveTo:
    
    def __init__(self, x, y, debug = False):
        from ctypes import wintypes
        import ctypes
        # Load the user32 DLL
        self.user32 = ctypes.WinDLL('user32')

        # Define required functions from user32.dll
        self.user32.GetForegroundWindow.restype = wintypes.HWND
        self.user32.SetWindowPos.argtypes = [wintypes.HWND, wintypes.HWND, wintypes.INT, wintypes.INT, wintypes.INT, wintypes.INT, wintypes.UINT]
        self.user32.GetWindowRect.argtypes = [wintypes.HWND, ctypes.POINTER(wintypes.RECT)]
        
        # Constants for SetWindowPos function
        self.SWP_NOSIZE = 0x0001
        self.SWP_NOACTIVATE = 0x0010

    
        hwnd = self.user32.GetForegroundWindow()


        rect = wintypes.RECT()
        if debug == True:
            # Get the window rectangle
            self.user32.GetWindowRect(hwnd, ctypes.byref(rect))
            
            # Return the position (left, top) as a tuple
            print(f"Current window position:{rect.left, rect.top}")
        else :
            pass
        
            # Move the window to (x, y)
        self.user32.SetWindowPos(hwnd, 0, x, y, 0, 0, self.SWP_NOSIZE | self.SWP_NOACTIVATE)

        if debug == True:
            self.user32.GetWindowRect(hwnd, ctypes.byref(rect))
            print(f"New window position:{rect.left, rect.top}")
        else:
            pass

        
class createMenu:
  def __init__(self, title, options, functions):
      if len(options) != len(functions):
          raise ValueError("The number of options and functions must be the same, dipshit.")

      print(f"\n{title}")
      for index, option in enumerate(options):
          print(f"{index + 1}. {option}")

      while True:
          try:
              choice = int(input("\nEnter your choice: "))
              print("")
              if 1 <= choice <= len(options):
                  # Store the choice as an attribute
                  self.choice = choice
                  # Execute the corresponding function
                  functions[choice - 1]()
                  break  # Exit the loop when a valid choice is made.
              else:
                  print("Invalid choice. Please enter a number between 1 and", len(options))
          except ValueError:
              print("Invalid input. Please enter a number.")

class dictForm:

  def __init__(self, dict):
    for key, value in dict.items():
      print(f"{key}: {value}")
