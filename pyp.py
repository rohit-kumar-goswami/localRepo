from flask import Flask, render_template, request

app = Flask(__name__)

# Chatbot logic (very simple)
def get_response(user_input):
    if "hello" in user_input.lower():
        return "Hi there!"
    elif "how are you" in user_input.lower():
        return "I'm good, thanks!"
    elif "bye" in user_input.lower():
        return "Goodbye!"
    else:
        return "Sorry, I don't understand."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.form["message"]
    bot_response = get_response(user_input)
    return bot_response

if __name__ == "__main__":
    app.run(debug=True)
