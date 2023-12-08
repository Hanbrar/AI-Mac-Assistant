import subprocess
#there will be premission settings that you will have to change to allow to create notes
def create_local_note_in_apple_notes(title, body):
    applescript = f'''
        tell application "Notes"
            activate
            tell folder "Notes"
                make new note with properties {{name:"{title}", body:"{body}"}}
            end tell
        end tell
    '''
    subprocess.call(['osascript', '-e', applescript])

# You can replace title with the name of the file you will like
def notereturn(text):
    title = "Note 1"
    body = text[text.index(":") + 1:].strip()
    create_local_note_in_apple_notes(title, body)
