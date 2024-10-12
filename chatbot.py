import time

ds = {
    "hi": "hello",
    "how are you": "I'm fine. Tell me about you!",
    "how old are you": "I'm 20 years old.",
    "what is your name": "My name is Helper.",
    "bye": "Goodbye! See you soon!",
}

while True:
    # User input
    g = input("You: ").lower()  # Convert input to lowercase but don't remove spaces
    
    if g == "quit":
        print("Chatbot: Goodbye! Have a great day!")
        break
    elif g == "what is the time now":
        print("Chatbot:", time.ctime())  # Fetch the current time each time this input is received
    elif g in ds:
        print("Chatbot:", ds[g])
    else:
        print("Chatbot: I don't understand that.")
