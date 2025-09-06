from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# Advanced College-level FAQ and smart search
FAQ = [
    # Specific faculty-related queries (prioritized)
    {"keywords": ["faculty", "teachers", "professors", "staff"], "answer": "🎓 RATM has highly qualified and experienced faculty members across all departments. Our professors hold advanced degrees and have industry experience. Faculty members regularly conduct research, publish papers, and provide mentorship to students. Visit our Faculty page to view detailed profiles and qualifications."},
    
    # Course and program queries
    {"keywords": ["course", "program", "degree", "departments"], "answer": "📚 RATM offers: \n• MBA (Management)\n• MCA (Computer Applications)\n• BBA, BCA, B.ECom\n• BSc (Computer Science)\n• MLib, BLib (Library Sciences)\n• B.Ed, M.Ed (Education)\n\nDepartments: Management, Computer Applications, Basic Sciences, Library & Information Sciences, and Education."},
    
    # Admission queries
    {"keywords": ["admission", "apply", "registration", "eligibility", "how to join"], "answer": "📝 Admissions Process:\n• Online Registration available\n• Contact: +91 9997398811, +91 9997596633\n• Email: [email protected]\n• Eligibility criteria varies by course\n• Visit Admission Guidelines page for detailed requirements\n• Documents required: Academic transcripts, ID proof, photos"},
    
    # Placement queries
    {"keywords": ["placement", "recruiters", "jobs", "career", "companies"], "answer": "💼 RATM Placement Highlights:\n• Strong industry connections\n• Top recruiters: HCL, Accenture, Dabur, Hyundai, NIIT, IDBI\n• Regular training & workshops\n• Guest lectures by industry experts\n• Career counseling sessions\n• Industrial visits\n• 100% placement assistance"},
    
    # Campus and facilities
    {"keywords": ["campus", "facilities", "hostel", "library", "infrastructure"], "answer": "🏫 RATM Campus Features:\n• Modern classrooms with digital equipment\n• Well-equipped computer labs\n• Comprehensive library with vast collection\n• Hostel facilities for outstation students\n• Sports and recreational facilities\n• Wi-Fi enabled campus\n• Cafeteria and medical facilities"},
    
    # Events and activities
    {"keywords": ["event", "news", "workshop", "fest", "gallery", "activities"], "answer": "🎉 Recent RATM Events:\n• Tree Plantation Drive (July 2025)\n• BCA & B.Com Farewell Party (June 2025)\n• Tablets Distribution Program\n• LinkedIn Optimization Workshop\n• Cricket League 2025\n• Cultural festivals and tech events\n• Regular guest lectures and seminars"},
    
    # Contact information
    {"keywords": ["contact", "email", "phone", "helpline", "reach"], "answer": "📞 Contact RATM:\n• Helpline: +91 9997398811, +91 9997596633\n• Email: [email protected]\n• Location: Mathura, Uttar Pradesh\n• Website: ratm.in\n• Office hours: 9 AM - 5 PM (Mon-Sat)\n• For urgent queries, call helpline numbers"},
    
    # Location queries
    {"keywords": ["location", "address", "where", "mathura"], "answer": "📍 RATM Location:\n• Located in Mathura, Uttar Pradesh, India\n• The holy city known for Lord Krishna\n• Well-connected by road and rail\n• Easy access from Delhi NCR region\n• Visit our Contact Us page for detailed directions and map"},
    
    # Innovation and technology
    {"keywords": ["modern", "innovative", "digital", "technology"], "answer": "💡 RATM's Modern Approach:\n• Digital classrooms with smart boards\n• Industry-oriented curriculum\n• Regular workshops and training\n• Guest lectures by industry experts\n• Technology-enabled learning\n• Innovation labs and research facilities\n• Collaboration with leading companies"},
    
    # About college queries (moved to end to prevent early matching)
    {"keywords": ["about college", "college info", "ratm info", "history", "established"], "answer": "🏛️ Rajiv Academy for Technology & Management (RATM) is a premier educational institution established in 1998 in the holy city of Mathura. With 27 years of excellence, RATM offers professional education across diverse fields including Management, Technology, Basic Sciences, Library Sciences, and Education under R.K. Education Hub."},
]

def get_bot_response(message):
    msg = message.lower().strip()
    
    # Priority matching - check for specific keywords first
    priority_keywords = ["faculty", "teachers", "professors", "staff", "placement", "admission", "course", "campus"]
    
    # Check for high-priority matches first
    for item in FAQ:
        for keyword in item["keywords"]:
            if keyword in priority_keywords and keyword in msg:
                return item["answer"]
    
    # Then check for general matches
    for item in FAQ:
        matching_keywords = [kw for kw in item["keywords"] if kw in msg]
        if matching_keywords:
            return item["answer"]
    
    # Handle enquiry requests
    if any(word in msg for word in ["enquiry", "admission form", "apply now", "want to join"]):
        return "📋 Start Your RATM Journey!\nYou can submit your admission enquiry:\n• Visit our Online Registration page\n• Call: +91 9997398811\n• Email: [email protected]\n• Fill the admission form on our website\n\nWould you like information about any specific course?"
    
    # Handle greetings
    if any(word in msg for word in ["hello", "hi", "hey", "good morning", "good afternoon"]):
        return "👋 Hello! Welcome to Rajiv Academy for Technology & Management (RATM)!\n\nI'm here to help you with information about:\n• Courses & Programs\n• Admissions Process\n• Faculty & Infrastructure\n• Placements & Career Support\n• Campus Life & Events\n\nWhat would you like to know?"
    
    # Default response
    return "🎓 Welcome to RATM - 27 Years of Excellence!\n\nI can help you with information about:\n• Courses & Admissions\n• Faculty & Campus\n• Placements & Career\n• Events & Activities\n• Contact Information\n\nPlease ask me anything about our college!"

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
