from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple rule-based chatbot responses
def get_bot_response(message):
    message = message.lower()
    if "course" in message or "program" in message:
        return "RATM offers MBA, MCA, BBA, BCA, B.ECom, BSc (CS), MLib, BLib, B Ed, and M Ed."
    elif "admission" in message:
        return "For admissions, visit the Online Registration page or contact +91 9997398811."
    elif "placement" in message:
        return "RATM has a strong placement record with top recruiters like HCL, Accenture, Dabur, Hyundai, NIIT, and IDBI."
    elif "contact" in message:
        return "You can contact RATM at +91 9997398811 or email [email protected]."
    elif "location" in message or "address" in message:
        return "RATM is located in Mathura, Uttar Pradesh."
    elif "event" in message or "news" in message:
        return "Recent events include Tree Plantation, Farewell Party, Tablets Distribution, and Workshops."
    elif "about" in message:
        return "Rajiv Academy for Technology & Management (RATM) is a premier institute established in 1998, offering professional education in various fields." 
    elif "modern" in message or "innovative" in message:
        return "RATM is committed to modern and innovative education, featuring industry-oriented courses, digital classrooms, regular workshops, guest lectures, and a vibrant campus life. We embrace technology and creativity to prepare students for the future."
    else:
        return "Welcome to RATM! How can I assist you today? Ask me about courses, admissions, placements, or events." 

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    bot_response = get_bot_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
