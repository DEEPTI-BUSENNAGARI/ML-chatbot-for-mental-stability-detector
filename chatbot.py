from textblob import TextBlob

class MentalHealthChatbot:
    def __init__(self):
        self.sentiment_analyzer = TextBlob()

    def analyze_sentiment(self, text):
        analysis = self.sentiment_analyzer(text)
        polarity = analysis.sentiment.polarity
        if polarity > 0.2:
            return "Positive"
        elif polarity < -0.2:
            return "Negative"
        else:
            return "Neutral"

    def interact(self):
        print("Welcome to the Mental Health Chatbot!")
        print("Please enter your message:")
        while True:
            user_input = input("> ")
            if user_input.lower() == "exit":
                print("Goodbye!")
                break
            sentiment = self.analyze_sentiment(user_input)
            print(f"Detected sentiment: {sentiment}")

if __name__ == "__main__":
    chatbot = MentalHealthChatbot()
    chatbot.interact()
