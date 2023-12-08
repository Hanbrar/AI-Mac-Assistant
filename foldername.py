

def getFoldername(text):
    t=False
    text=text.split()
    text1=""
    for word in text:
       
        if(t):
            text1=word
            break
        if(word=="named"):
            t=True
    return text1