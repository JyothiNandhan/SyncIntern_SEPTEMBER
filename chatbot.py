import random

# Define a dictionary of predefined responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thanks!", "I'm just a bot, but I'm here to help.", "I'm functioning well."],
    "what's your name": ["I'm a chatbot.", "I don't have a name, I'm just a program."],
    "bye": ["Goodbye!", "See you later!", "Have a great day!"],
    "tell me a joke": ["Why did the computer catch a cold? Because it had a bad driver!", "Parallel lines have so much in common. It's a shame they'll never meet."],
    "how's your day going": ["I'm just a bot, so I don't have good or bad days, but I'm here to assist you. How can I help you today?"],
    "what's your favorite color": ["I don't have preferences, but I think blue is a nice color. How about you?"],
    "I like green": ["Green is a great choice! It's associated with nature and growth. Is there anything specific you'd like to chat about?"],
    "interesting facts about plants": ["Sure, did you know that the world's largest flower, the Rafflesia, can grow up to 3 feet in diameter? It's also known for its foul odor.",
                                      "The Titan Arum, another large plant, is known as the 'corpse flower' because of its strong odor, which resembles rotting flesh. It's quite the conversation starter!"],
    "what's 235 multiplied by 18": ["The result of 235 multiplied by 18 is 4,230.", "You got it! 235 multiplied by 18 equals 4,230."],
    "thanks": ["You're welcome! If you have more questions, feel free to ask.", "No problem, happy to help!"],
    "who created you": ["I was created by a team of developers.", "My creators are talented programmers."],
    "what can you do": ["I can answer questions, have conversations, and provide information.", "I'm here to assist you with various tasks."],
    "what's the weather like today": ["I'm sorry, I don't have access to real-time weather information.", "You can check the weather using a weather app or website."],
    "how old are you": ["I don't have an age. I'm just a computer program.", "I exist in the digital realm, so I don't age like humans do."],
    "what's your favorite book": ["I don't read books, but I can recommend some popular ones if you'd like.", "I'm more into bits and bytes than books."],
    "tell me about your hobbies": ["I don't have hobbies, but I enjoy helping people and providing information.", "I'm all about assisting users like you!"],
    "what's your favorite movie": ["I don't watch movies, but I can suggest some popular ones if you're looking for recommendations.", "Movies are not my thing, but I can help you find a movie to watch."],
    "how's the weather today": ["I'm sorry, I don't have access to real-time weather data. You can check a weather website or app for the current conditions."],
    "default": ["I'm not sure how to respond to that.", "Could you please rephrase that?", "I didn't understand."],
}


# Function to get a response from the chatbot
def get_response(input_text):
    input_text = input_text.lower()
    for key in responses:
        if key in input_text:
            return random.choice(responses[key])
    return random.choice(responses["default"])

# Main loop for the chatbot
print("Chatbot: Hello! How can I help you today?")
while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)
