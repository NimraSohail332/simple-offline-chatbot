def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great. Thanks!"
    elif "your name" in user_input:
        return "I'm a simple chatbot made by Nimra :)"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day."
    else:
        return "I'm sorry, I don't understand that yet."

def chat():
    print("Chatbot is running! (type 'exit' to stop)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = chatbot_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    chat()
