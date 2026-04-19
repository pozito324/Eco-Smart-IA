import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="EcoSmart AI", page_icon="🌱", layout="centered")

# 🎨 ESTILO OSCURO PRO
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom, #0f172a, #111827);
        color: white;
    }

    h1, h2, h3, p {
        color: white;
    }

    .user {
        background-color: #1f2937;
        color: white;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 8px;
        border-left: 4px solid #38bdf8;
    }

    .bot {
        background-color: #14532d;
        color: white;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 8px;
        border-left: 4px solid #22c55e;
    }

    .stTextInput > div > div > input {
        background-color: #111827;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌱 EcoSmart AI")
st.write("Tu asistente ecológico inteligente 🌍")

# 🧠 memoria
if "chat" not in st.session_state:
    st.session_state.chat = [
        {
            "role": "system",
            "content": (
                "Eres EcoSmart AI, experto en ecología. "
                "Das consejos claros, prácticos y haces preguntas cuando necesitas más información del usuario."
            )
        }
    ]

# input
texto = st.text_input("💬 Escribe tu problema ecológico:")

if st.button("🔍 Enviar"):
    if texto.strip() != "":
        # guardar usuario
        st.session_state.chat.append({
            "role": "user",
            "content": texto
        })

        # respuesta IA
        respuesta = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=st.session_state.chat
        )

        msg = respuesta.choices[0].message.content

        # guardar IA
        st.session_state.chat.append({
            "role": "assistant",
            "content": msg
        })

# 💬 chat bonito
st.write("## 💬 Conversación")

for msg in st.session_state.chat[1:]:
    if msg["role"] == "user":
        st.markdown(f"<div class='user'>🧑‍💬 <b>Tú:</b> {msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot'>🤖 <b>EcoSmart:</b> {msg['content']}</div>", unsafe_allow_html=True)