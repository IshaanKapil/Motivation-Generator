🌟 Daily Motivation Generator – AI-Powered Quote App

The Daily Motivation Generator is an uplifting web application that uses the ultra-fast Groq API to generate motivational quotes based on the user’s current mood. Whether you’re feeling anxious, unfocused, or just need a boost, this app delivers personalized encouragement instantly.

🚀 Features
✅ AI-Generated Motivation: Uses cutting-edge, lightning-fast LLMs (like Llama 3) via the Groq API to generate original, mood-based quotes.
✅ Customizable Mood Input: Choose from a list of moods:

Anxious
Need focus
Low energy
Overwhelmed
Looking for inspiration
And more moods available!
✅ Fast & Free-Tier Friendly: Powered by Groq, which offers an incredibly generous free tier for developers, making it ideal for quick prototyping. No need to download large models locally!
✅ Simple and Clean UI: Built with Streamlit for instant interaction and visual feedback.

💻 Setup and Installation

🧰 Prerequisites

Python 3.10+
pip (Python package manager)
A free API key from Groq
 (Sign up for an API key here!)

📦 Local Installation

Clone the repository

git clone https://github.com/IshaanKapil/Motivation-Generator.git 
cd Motivation-Generator

Install dependencies

pip install -r requirements.txt

Set up your Groq API Key
Create a .streamlit folder and a secrets.toml file inside it:

mkdir .streamlit
touch .streamlit/secrets.toml

Add your Groq API key to the secrets.toml file:

GROQ_API_KEY = "your-groq-api-key-here"

Run the app

streamlit run app.py 

📁 Project Structure

daily_motivation_project/ 
├── app.py              # Main Streamlit app 
├── requirements.txt    # Dependencies list 
├── README.md           # Project documentation 
└── .streamlit/ 
    └── secrets.toml    # Your Groq API Key

⚙️ Configuration
You can tweak the model parameters directly in app.py:

model: Change the Groq model (e.g., llama3-8b-8192 or mixtral-8x7b-32768)
temperature: Control the creativity of the quotes (e.g., 0.8)
max_tokens: Limit the length of the generated message

🧠 How It Works

User selects a mood from the dropdown.
The app forms a prompt tailored to the mood.
The prompt is sent to the Groq API.
Groq's lightning-fast inference generates a unique, encouraging sentence almost instantly.
The output is displayed in the Streamlit UI.

☁️ Deploy on Streamlit Cloud

Push your code to GitHub.
Go to Streamlit Cloud
.
Create a new app linked to your repo.
Go to Advanced Settings and add your GROQ_API_KEY to the Secrets section.
Set the main file to app.py and deploy!

📚 Usage Guide

Run the app locally or on Streamlit Cloud.
Select your mood.
Click “Generate Motivation”.
Read your personalized message.
Refresh for a new quote or repeat for more inspiration!
 
  OUTPUTS
  
<img width="1915" height="986" alt="Screenshot 2026-04-28 180338" src="https://github.com/user-attachments/assets/25b845b5-c811-4540-bc80-b210c1f6ce23" />
<img width="1919" height="792" alt="Screenshot 2026-04-28 180408" src="https://github.com/user-attachments/assets/9c751c4e-889a-4ed8-a46c-ca2aea95f634" />
<img width="1691" height="829" alt="image" src="https://github.com/user-attachments/assets/4312cbe6-ea95-4024-95ee-8842e1bce0d7" />

🔮 Future Improvements

Save/download favorite quotes
Multi-language support (Hindi, Tamil, etc.)
Voice output (text-to-speech)
Mobile app integration
Daily quote scheduling/reminders



