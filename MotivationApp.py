import streamlit as st
from groq import Groq
import time

st.set_page_config(page_title="Daily Motivation Generator", layout="centered", page_icon="🌟")

custom_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');

/* Main App Background */
.stApp {
    background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
    font-family: 'Outfit', sans-serif;
    color: #f8fafc;
}

/* Main content wrapper (Glassmorphism) */
.block-container {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 24px;
    padding-top: 2rem !important;
    padding-bottom: 3rem !important;
    padding-left: 3rem !important;
    padding-right: 3rem !important;
    margin-top: 4rem;
    margin-bottom: 4rem;
    box-shadow: 0 10px 40px 0 rgba(0, 0, 0, 0.4);
}

/* Hide standard Streamlit header/footer */
header {visibility: hidden;}
footer {visibility: hidden;}

/* Typography */
h1, h2, h3, h4, h5, h6, p, div, span, label {
    font-family: 'Outfit', sans-serif !important;
    color: #f8fafc;
}

/* Headings */
h1 {
    font-weight: 800 !important;
    font-size: 2.8rem !important;
    background: -webkit-linear-gradient(45deg, #a78bfa, #ec4899);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    margin-bottom: 0.5rem;
}

/* Selectbox styling */
div[data-baseweb="select"] > div {
    background: rgba(15, 23, 42, 0.6) !important;
    border: 1px solid rgba(167, 139, 250, 0.3) !important;
    border-radius: 12px !important;
    color: white !important;
    padding: 0.2rem;
}

div[data-baseweb="select"] * {
    color: white !important;
}

/* Dropdown list styling */
ul[data-baseweb="menu"] {
    background-color: #1e293b !important;
    border: 1px solid rgba(167, 139, 250, 0.3) !important;
}

li[role="option"] {
    color: white !important;
}

/* Button styling */
div.stButton > button:first-child {
    background: linear-gradient(90deg, #8b5cf6 0%, #ec4899 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 30px !important;
    padding: 0.6rem 2rem !important;
    font-size: 1.1rem !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(236, 72, 153, 0.4) !important;
    width: 100% !important;
    margin-top: 1rem;
}

div.stButton > button:first-child:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(236, 72, 153, 0.6) !important;
    background: linear-gradient(90deg, #9333ea 0%, #db2777 100%) !important;
}

/* Quote Box Styling (Custom HTML) */
.quote-box {
    background: linear-gradient(135deg, rgba(139, 92, 246, 0.15) 0%, rgba(236, 72, 153, 0.15) 100%);
    border-left: 4px solid #ec4899;
    padding: 2rem;
    border-radius: 0 15px 15px 0;
    margin-top: 2rem;
    font-size: 1.4rem;
    font-style: italic;
    line-height: 1.6;
    color: #fdf2f8;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    position: relative;
    animation: fadeIn 0.8s ease-in-out;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Spinner styling */
.stSpinner > div > div {
    border-color: #ec4899 transparent transparent transparent !important;
}

</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)


st.markdown("<h1>🌟 Daily Motivation</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 1.1rem; margin-bottom: 2rem;'>Select your mood and get an uplifting quote powered by our lightning-fast AI</p>", unsafe_allow_html=True)

try:
    api_key = st.secrets.get("GROQ_API_KEY")
    if not api_key:
        st.error("Please set your GROQ_API_KEY in the `.streamlit/secrets.toml` file.")
    else:
        client = Groq(api_key=api_key)
except FileNotFoundError:
    st.error("Please create a `.streamlit/secrets.toml` file and set your GROQ_API_KEY.")
    api_key = None

moods = [
    "Feeling anxious",
    "Need focus",
    "Low energy",
    "Looking for inspiration",
    "Feeling overwhelmed",
    "Feeling lost",
    "Want to start the day strong"
]

selected_mood = st.selectbox("How are you feeling today?", moods)

if st.button("Generate Motivation 🚀") and api_key:
    with st.spinner("Channeling positive energy..."):
        time.sleep(0.5)
        
        prompt = f"Write a short, highly encouraging and motivational message (1-2 sentences max) for someone who is {selected_mood.lower()}. Do not include any conversational filler, just the quote."

        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are an uplifting and empathetic motivational speaker."
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model="llama-3.1-8b-instant",
                temperature=0.8,
                max_tokens=60,
                top_p=0.9
            )

            message = chat_completion.choices[0].message.content.strip()
            
            st.markdown(f'<div class="quote-box">"{message}"</div>', unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"An error occurred: {e}")
