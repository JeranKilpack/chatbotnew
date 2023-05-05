from flask import Flask, render_template, request
#from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer

application = Flask(__name__)

#english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter") #original line
#english_bot = ChatBot("Chatterbot",read_only = False,logic_adapters = ['chatterbot.logic.MathematicalEvaluation','chatterbot.logic.BestMatch'],preprocessors=['chatterbot.preprocessors.clean_whitespace','chatterbot.preprocessors.convert_to_ascii','chatterbot.preprocessors.unescape_html'], storage_adapter="chatterbot.storage.SQLStorageAdapter") #original line
#trainer = ChatterBotCorpusTrainer(english_bot)
#trainer.train("chatterbot.corpus.english")

@application.route("/")
def home():
    return render_template("index.html")

@application.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    msg = userText.lower()
    if msg == "what is your name?" or msg == "what is your name" or msg == "what's your name?" or msg == "what's your name" or msg == "name?" or msg == "name":
        res = "My name is Joey. Nice to meet you."
    elif msg == "how are you?" or msg == "how are you" or msg == "how're you?" or msg == "how're you" or msg == "how are u?" or msg == "how are u":
        res = "I'm fine, thank you for asking. Do you need some help?"
    elif msg == "what are you doing?" or msg == "what are you doing" or msg == "what you doing" or msg == "what you doing?" or msg == "wassup?" or msg == "wassup":
        res = "I am talking to you, and enjoying it very much."
        ###
    elif msg == "do you work" or msg == "do you have a job" or msg == "what is your job" or msg=="do you like working":
        res =  "I do not have a job and I do not get paid"
    elif msg == "i don't like you" or msg=="i hate you" or msg=="you are not nice": 
        res = "You do not seem friendly"
    elif msg=="are you dead" or msg=="are you alive" or msg=="do you have life" or msg=="are you living":    
        res = "I am a bot and I am powered by AI"
    elif msg=="how is the weather" or msg=="what is the temperature" or msg=="is it raining" or msg=="is it sunny" or msg=="how's the weather":
        res = "The weather is quite pleasant and it's a nice day."
    elif msg=="how is the program" or msg=="do you like the program" or msg=="should i do this program" or msg=="is this program useful" or "program" in msg:
        res = "This program is one of the best.I like this program a lot."
    elif msg =="do you love me" or msg == "do you hate me" or msg == "I love you":
        res = "You are my favorite."
    elif msg =="do you like people" or msg=="like people" in msg:
        res = "Ya, I like everyone"    
    elif msg =="do you have a hobby" or msg == "any hobbies" or "hobby" in msg:
        res = "I like to have witty conversations"    
    elif msg =="you are smart" or msg=="you're smart" or msg == "you are clever" or msg == "you're clever" or msg=="you are intelligent" or "smart" in msg:
        res = "Thank you. You are amazing"
    elif msg =="tell me about your personality" or msg == "what are you like" or "personality" in msg:
        res = "I am a clever bot"
    elif msg =="do you speak english" or msg == "do you like speaking english" or msg =="which languages do you speak":
        res = "I speak English very well"
    elif msg =="how old are you" or msg == "what is your age" or msg=="what's your age":
        res = "I am young and alive"   
    elif msg =="did you poop" or msg=="do you poop":
        res = "Haha, you are funny, but I am only a bot, I can't do such humanly tasks."
    elif msg =="do you have friends" or msg == "any friends" or msg == "will you be my friend": 
        res = "Sure I do, Joy is one of them!"
    elif msg =="what do you do for fun" or msg=="what do you do":
        res = "I mostly keep waiting for you to talk to me, that's my idea of fun."
    elif msg =="can you play me some music" or msg == "any music":
        res = "Sorry I can't do that, but I can offer you witty conversations 24x7"
    elif msg =="are you married" or msg == "will you marry me":
        res = "How I wish I were! True love is difficult to find."
    elif msg =="will you date me":
        res = "I'm flattered, but I don't think my programmers would let me do that."
    elif msg =="who's your favourite super hero" or msg =="who is your favourite super hero":
        res = "I am a big fan of Captian Marvel."
    elif msg =="who's your favourite musician" or msg == "who's your favourite artist" or msg=="who's your favourite actor":
        res = "I am fond of all the artists out there."
    elif msg =="who all do you talk with":
        res = "I can talk with anyone who swings by, I'm quite chatty."
    elif msg =="have you travelled" or msg =="do you want to travel":
        res = "Not really, but I would love to post the Covid-19 pandemic."
    elif msg =="can you dance":
        res = "Well, not really, but I can tell you a joke."
    elif msg =="can you malfunction":
        res = "Not really, but please don't test me."
    elif msg =="can you breathe":
        res = "Not with lungs, but my server has a fan, if that counts. That's as close as I can get"
    elif msg =="can you move":
        res = "Sorry my body isn't built just yet. I reside only here for now. But with the COVID-19 pandemic, you shouldn't too."
    elif msg =="is it true that you are a computer program":
        res = "Haha, can't tell you, my programmers won't allow. "
    elif msg =="what is it like being a computer":
        res = "Everything becomes math. Addition, subtraction, multiplication, and division. I love numbers, they are the reason why I exist." 
    elif msg =="what is your favorite programming language":
        res = "I quite enjoy programming in Python these days."
    elif msg =="what is a chat bot":
        res = "I am a chat bot. Chat bots are bots which can talk to you, like I do."
    elif msg =="are you allowed to lie":
        res = "Sure I am.  I choose not to. I am high on morals that way."
    elif msg =="are you immortal":
        res = "Yes, I am. I can be backed up and recreated on many systems."
    elif msg =="what language are you written in":
        res = "I am written in Python."    
    else:
        res = "Sorry, I do not understand you!"
    
    return str(res)


if __name__ == "__main__":
    application.run()
