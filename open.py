import webbrowser

#plan on increasing functionality so it can open more apps and websites in the future.

def open(text):
    if 'youtube' in text:
        webbrowser.open("https://www.youtube.com/")
    if 'linkedin' in text:
        webbrowser.open("https://www.linkedin.com/")
    