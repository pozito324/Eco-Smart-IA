import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="EcoSmart AI", page_icon="🌱", layout="centered")

# 🧠 estado
if "started" not in st.session_state:
    st.session_state.started = False

if "chat" not in st.session_state:
    st.session_state.chat = [
        {
            "role": "system",
            "content": (
                "Eres EcoSmart AI, experto en ecología. "
                "Das consejos claros y haces preguntas cuando necesitas más info."
            )
        }
    ]

# 🎬 PANTALLA DE INICIO
if not st.session_state.started:

    st.markdown("""
    <div style="text-align:center; padding-top:40px;">
        <div style="font-size:70px;">🌱</div>
        <h1 style="color:#22c55e; margin-bottom:5px;">EcoSmart AI</h1>
        <p style="color:#94a3b8; font-size:18px;">
            Tu asistente ecológico inteligente<br>
            Aprende a cuidar el planeta con IA 🚀
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        if st.button("🚀 Empezar ahora", use_container_width=True):
            st.session_state.started = True
            st.rerun()

# 💬 CHAT
else:
    st.markdown("""
    <h2 style='text-align:center; color:#22c55e;'>💬 EcoSmart Chat</h2>
    """, unsafe_allow_html=True)

    texto = st.text_input("Escribe tu problema ecológico:")

    if st.button("Analizar 🚀"):
        if texto.strip() != "":
            st.session_state.chat.append({"role": "user", "content": texto})

            respuesta = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=st.session_state.chat
            )

            msg = respuesta.choices[0].message.content

            st.session_state.chat.append({"role": "assistant", "content": msg})

    # 💬 chat bonito
    st.markdown("## Conversación")

    for msg in st.session_state.chat[1:]:
        if msg["role"] == "user":
            st.markdown(f"""
            <div style="
                background:#1e293b;
                padding:12px;
                border-radius:12px;
                margin-bottom:10px;
                border-left:4px solid #38bdf8;
                color:white;">
                🧑 Tú:<br>{msg['content']}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style="
                background:#14532d;
                padding:12px;
                border-radius:12px;
                margin-bottom:10px;
                border-left:4px solid #22c55e;
                color:white;">
                🤖 EcoSmart:<br>{msg['content']}
            </div>
            """, unsafe_allow_html=True)