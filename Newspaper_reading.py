import requests
import json

def speak(str):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.SpVoice")

    speak.speak(str)


if __name__ == '__main__':
    speak("This is made by Chetan Rakhra")
    speak("News for today.. Let's begin")
    url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=d960979ddbcb4cf9a694ffae85fd854f"
    news = requests.get(url).text
    news_dict = json.loads(news)
    print(news_dict["articles"])
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        speak("Moving on to the next news.. Listen Carefully")

    speak("Thanks for listening..")
    speak("Regards from Chetan Rakhra")
