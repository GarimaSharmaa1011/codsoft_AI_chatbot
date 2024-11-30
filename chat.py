

print("ChatBot: Hi there! I'm your friendly chatbot. Ask me anything or type 'exit' to end the chat.")

while True:
 
    user_input = input("You: ").strip().lower()

  
    if user_input == "exit":
        print("ChatBot: Goodbye! Have a great day!")
        break


    elif "hello" in user_input or "hi" in user_input:
        print("ChatBot: Hello! How can I assist you today?")
    elif "how are you" in user_input:
        print("ChatBot: I'm just a bot, but I'm functioning as expected! How about you?")
    elif "your name" in user_input:
        print("ChatBot: I'm called ChatBot. What about you?")
    elif "weather" in user_input:
        print("ChatBot: I can't check the weather right now, but you can look out the window!")
    elif "joke" in user_input:
        print("ChatBot: Why don't scientists trust atoms? Because they make up everything!")
    elif "help" in user_input:
        print("ChatBot: Sure! I'm here to answer your questions. Ask me anything specific.")
    elif "bye" in user_input:
        print("ChatBot: Bye! It was nice talking to you.")
    else:
        print("ChatBot: Hmm, I don't understand that. Could you ask something else?")
