print("👋 Hello! I’m CareerBuddy – your AI career advisor!")
print("Type 'exit' to end the chat.\n")

import time

def slow_type(text):
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(0.01)
    print()

def suggest_path(user_input):
    user_input = user_input.lower()

    if any(keyword in user_input for keyword in ["hello", "hi", "hey"]):
        return "👋 Hey there! I'm here to help you figure out your career path. Just tell me what you’re interested in!"

    elif any(keyword in user_input for keyword in ["thank you", "thanks"]):
        return "😊 You're very welcome! Let me know if you have more questions."

    elif any(keyword in user_input for keyword in ["ok", "okay", "fine", "cool"]):
        return "😄 Alright! Just type something you're curious about, and I'll do my best to guide you!"
    elif any(keyword in user_input for keyword in ["design", "ux", "ui", "figma"]):
        return "🎨 You’d be great as a UI/UX Designer. Learn Figma, Adobe XD, and look for internships on Internshala or LinkedIn."

    elif any(keyword in user_input for keyword in ["data", "analysis", "analyst"]):
        return "📊 Data Analyst could be your path! Learn Excel, Python, SQL, and tools like Power BI or Tableau."

    elif any(keyword in user_input for keyword in ["ml", "ai", "machine", "deep"]):
        return "🤖 You’re an AI enthusiast! Start with Python, Numpy, Pandas, and explore TensorFlow or Scikit-learn."

    elif any(keyword in user_input for keyword in ["code", "developer", "programmer"]):
        return "💻 Software Developer suits you! Practice DSA with Java, build projects using Python or full-stack web dev."

    elif any(keyword in user_input for keyword in ["cyber", "security", "hacking"]):
        return "🔐 You might love Cybersecurity! Learn Linux, Networking, and tools like Wireshark, Burp Suite."

    elif any(keyword in user_input for keyword in ["remote", "freelance", "from home"]):
        return "🌍 Freelancing is great! Learn in-demand skills (design, writing, coding) and explore Upwork, Fiverr."

    else:
        return "🤔 I'm still learning! Try asking about design, AI, coding, data, or cybersecurity."

# Chat loop
while True:
    user = input("You: ")

    if user.lower() in ["exit", "quit", "bye"]:
        print("CareerBuddy: Goodbye and good luck! 🚀")
        break

    reply = suggest_path(user)
    slow_type(f"CareerBuddy: {reply}")