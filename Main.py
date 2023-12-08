from langchain.chat_models import ChatOpenAI
import os
from speech import text_to_speech
import speech_recognition as sr
from langchain import ConversationChain
from langchain import PromptTemplate
from duckgo import summarizier
from open import open
from note import notereturn
from foldername import getFoldername
from folder import foldercreate
from sound import playwakemp3
import datetime
from news import news

def date():
    return datetime.date.today()

#Here change the context to addresses you by replacing HB with your name   
multiple_input_prompt = PromptTemplate(input_variables=["question","context"], template="You are a personal assistant named Lucas, current date is "+str(date())+" and you respond to question: {question},from the user based on this {context}, don't mention the date unless ask to do so, the user will be addressed as HB")

#Add OpenAI API
os.environ['OPENAI_API_KEY'] = "" 

llm = ChatOpenAI(temperature=0.9, max_tokens=120,model_name = "gpt-3.5-turbo")
conversation = ConversationChain(llm=llm, verbose=False)


a=True
thing = sr.Recognizer()
run = True

# You may need to give access to microphone in privacy settings on mac
while run:
    with sr.Microphone() as source:
        print("Working")
        audio_text = thing.listen(source, timeout=15, phrase_time_limit=15)
        print("Done")

    
    try:
        contextneed="no additional context needed you should be able to answer this question"
        text = thing.recognize_google(audio_text)
        print("Recognized Text:")
        text=text.lower()
        print(text)
        name=''
        if "hi lucas" in text and a:
            playwakemp3()
        if 'create' in text and 'folder' in text:
            name=getFoldername(text)
            foldercreate(name)
            contextneed="just say ' yes I can do that and the folder is created' "
        if "search for" in text:
            sum1=summarizier(text)
            contextneed=sum1+"[note don't say information I have provide just say the information found online]"
        if "top news" in text:
            contextneed=news() 
        if 'note'in text and 'create' in text:
            notereturn(ctext)
            contextneed="just say yes I can do that and ask not futher questions, respond like note is made"
        if 'note'in text and 'make' in text:
            notereturn(ctext)
            contextneed="in essence just really only say that yes I can and the note is made"
        if "open" in text:
            open(text)
            contextneed="in essence just really only say that yes I can and don't say do you want me to open it just say I opened app"
        if "help" in text:
            contextneed=""" Say that can do the follow 1) create folder by you saying 'create folder named [name of folder]' 
            2) I can search for anything on the internet by you saying 'search for [query]' 
            3) Give top news by you saying 'top news'
            4) I can create note in notes by you saying 'create note'
            5) I can open linkedin and youtube by saying 'open [youtube or linkedin]'
            6) I can quit by saying 'quit' or 'bye'
            """

        if "quit" in text or "bye" in text:
            print("Bye see you next time")
            text_to_speech("Bye see you next time sir")
            break
        #text_to_speech say
        
        print('Chat:')
        ctext=conversation.predict(input=multiple_input_prompt.format(question=text,context=contextneed))

        print(ctext)
        tempt=ctext
        text_to_speech(ctext)
        a=False

            
    except:
        print("No speech detected. Please speak again.")
            