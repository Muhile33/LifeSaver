import random 
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "You're becoming the version of you they never expected."
]
def get_quote():
    #Returns a random motivational quote.
    return "\n 💬 " + random.choice(quotes)