# import streamlit as st
# from dotenv import load_dotenv
# import os
# from google import genai
# load_dotenv()
# api_key = os.getenv("GENAI_API_KEY")
# client = genai.Client(api_key=api_key)
# st.set_page_config(
#     page_title="Gemini ai chatbot",
#     layout="centered"
# )
# st.title("gemini ai chatbot")
# st.write("ask gemini anything!")
# prompt = st.text_area("Enter your prompt here:",
#                       placeholder="explain arttificial intelligence in simple terms")
# if st.button("generate response"):
#     if prompt:
#         with st.spinner("gemini is thinking..."):
#             response=client.models.generate_content(
#                 model="gemini-3.5-flash-lite",
#                 contents=prompt
                
#             )
#         st.success("response generated!!!")
#         st.write(response.text)
#     else:
#         st.warning("please enter a prompt:")




import streamlit as st
from dotenv import load_dotenv
import os
from google import genai

# -----------------------------
# Load API key
# -----------------------------
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Gemini AI Chatbot",
    page_icon="🌌",
    layout="centered"
)

# -----------------------------
# GALAXY CSS
# -----------------------------
st.markdown("""
<style>

/* ---------- MAIN BACKGROUND ---------- */

.stApp {
    background:
        radial-gradient(circle at 20% 20%, rgba(91, 33, 182, 0.25), transparent 25%),
        radial-gradient(circle at 80% 30%, rgba(37, 99, 235, 0.20), transparent 25%),
        radial-gradient(circle at 50% 80%, rgba(147, 51, 234, 0.18), transparent 30%),
        linear-gradient(135deg, #020617, #09001a, #020617);

    color: #f8fafc;
}

/* ---------- GALAXY STARS ---------- */

.stApp::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;

    background-image:
        radial-gradient(2px 2px at 20px 30px, white, transparent),
        radial-gradient(1px 1px at 100px 150px, white, transparent),
        radial-gradient(2px 2px at 200px 80px, #c4b5fd, transparent),
        radial-gradient(1px 1px at 300px 200px, white, transparent),
        radial-gradient(2px 2px at 400px 120px, #93c5fd, transparent),
        radial-gradient(1px 1px at 500px 250px, white, transparent),
        radial-gradient(2px 2px at 600px 70px, #ddd6fe, transparent),
        radial-gradient(1px 1px at 700px 180px, white, transparent),
        radial-gradient(2px 2px at 800px 100px, #bfdbfe, transparent);

    background-size: 900px 400px;

    opacity: 0.5;
    pointer-events: none;
    z-index: 0;
}

/* ---------- CONTENT ---------- */

.block-container {
    position: relative;
    z-index: 1;
    max-width: 850px;
    padding-top: 60px;
}

/* ---------- TITLE ---------- */

h1 {
    text-align: center;

    font-size: 3.2rem !important;
    font-weight: 800 !important;

    background: linear-gradient(
        90deg,
        #c4b5fd,
        #818cf8,
        #38bdf8,
        #c084fc
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    text-shadow:
        0 0 20px rgba(139, 92, 246, 0.35);
}

/* ---------- DESCRIPTION ---------- */

.stMarkdown p {
    color: #cbd5e1;
    text-align: center;
    font-size: 1.05rem;
}

/* ---------- TEXT AREA ---------- */

.stTextArea textarea {

    background: rgba(15, 23, 42, 0.75) !important;

    color: #f8fafc !important;

    border: 1px solid rgba(139, 92, 246, 0.5) !important;

    border-radius: 18px !important;

    padding: 18px !important;

    font-size: 16px !important;

    box-shadow:
        0 0 20px rgba(124, 58, 237, 0.12),
        inset 0 0 20px rgba(15, 23, 42, 0.5);

    transition: all 0.3s ease;
}

/* Text area focus */

.stTextArea textarea:focus {

    border: 1px solid #8b5cf6 !important;

    box-shadow:
        0 0 10px rgba(139, 92, 246, 0.5),
        0 0 30px rgba(59, 130, 246, 0.2) !important;
}

/* Placeholder */

.stTextArea textarea::placeholder {
    color: #64748b !important;
}

/* ---------- BUTTON ---------- */

.stButton > button {

    width: 100%;

    background: linear-gradient(
        90deg,
        #7c3aed,
        #4f46e5,
        #2563eb
    );

    color: white;

    border: none;

    border-radius: 14px;

    padding: 14px 20px;

    font-size: 17px;

    font-weight: 700;

    box-shadow:
        0 0 15px rgba(124, 58, 237, 0.45),
        0 0 35px rgba(37, 99, 235, 0.2);

    transition: all 0.3s ease;
}

/* Button hover */

.stButton > button:hover {

    transform: translateY(-2px);

    background: linear-gradient(
        90deg,
        #9333ea,
        #6366f1,
        #3b82f6
    );

    box-shadow:
        0 0 20px rgba(168, 85, 247, 0.7),
        0 0 45px rgba(59, 130, 246, 0.35);
}

/* ---------- SUCCESS MESSAGE ---------- */

.stAlert {

    background: rgba(15, 23, 42, 0.75) !important;

    border: 1px solid rgba(139, 92, 246, 0.35) !important;

    border-radius: 15px !important;

    color: #e2e8f0 !important;
}

/* ---------- RESPONSE AREA ---------- */

div[data-testid="stMarkdownContainer"] {

    color: #e2e8f0;
}

/* ---------- SPINNER ---------- */

.stSpinner > div {
    border-top-color: #8b5cf6 !important;
}

/* ---------- WARNING ---------- */

div[data-baseweb="notification"] {

    background: rgba(30, 27, 75, 0.85) !important;

    border-radius: 14px !important;
}

/* ---------- REMOVE STREAMLIT TOP SPACE ---------- */

header {
    background: transparent !important;
}

/* ---------- FOOTER ---------- */

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# MAIN UI
# -----------------------------

st.title("🌌 Gemini AI Chatbot")

st.write("✨ Ask Gemini anything and explore the universe of knowledge.")

prompt = st.text_area(
    "Enter your prompt here:",
    placeholder="Explain artificial intelligence in simple terms...",
    height=180
)

if st.button("🚀 Generate Response"):

    if prompt:

        with st.spinner("🌌 Gemini is thinking..."):

            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt
            )

        st.success("✨ Response generated!")

        st.markdown("### 🌠 Gemini's Response")

        st.write(response.text)

    else:

        st.warning("⚠️ Please enter a prompt.")
