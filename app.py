from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- Core Chatbot Function ---
def get_bot_response(user_input):
    """
    Takes user input, converts it to lowercase, and returns a predefined reply
    using if-elif statements.
    """
    text = user_input.lower().strip()
    
    if text in ["hello", "hi", "hey"]:
        return "Hi!"
    elif text == "how are you":
        return "I'm fine, thanks!"
    elif text in ["bye", "goodbye", "quit"]:
        return "Goodbye!"
    elif text == "what is your name":
        return "I'm a simple chatbot."
    elif text == "what can you do":
        return "I can respond to basic greetings and questions. Try asking me something!"
    elif text == "tell me a joke":
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif text == "what's the weather like":
        return "I don't have access to real-time weather data, but I hope it's nice where you are!"
    elif text == "what's the time":
        return "I don't have access to real-time data, but you can check your device's clock!" 
    elif text == "what's your favorite color":
        return "I don't have preferences, but I think blue is a nice color!"    
    elif text == "what's your favorite food":
        return "I don't eat, but I hear pizza is pretty popular!"
    else:
        return "I don't understand that yet. Try saying 'hello', 'how are you', or 'bye'."

# --- Routes (Input/Output API) ---

@app.route("/")
def home():
    # Serves the frontend HTML page
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    # Gets the message from the frontend, gets the bot's reply, and sends it back
    user_message = request.json.get("message")
    
    if user_message:
        reply = get_bot_response(user_message)
        return jsonify({"reply": reply})
    return jsonify({"reply": "Error: No message received."})

if __name__ == "__main__":
    # Runs the application in a continuous loop listening for requests
    app.run(debug=True)