import os
import eel
import webbrowser

# Initialize Eel with your web folder
eel.init("www")

# Optional: Try to open Microsoft Edge in app mode
try:
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')
except:
    print("Edge not found. Opening default browser instead.")
    webbrowser.open("http://localhost:8000/index.html")

# Start Eel server
eel.start('index.html', mode=None, host='localhost', block=True)
