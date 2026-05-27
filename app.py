import streamlit as st

# CONFIG
st.set_page_config(
    page_title="Demo TF-IDF",
    layout="wide"
)

# ESTILOS
st.markdown("""
<style>

.stApp {
    background-color: white;
}

.main {
    max-width: 1100px;
    margin: auto;
}

h1 {
    font-size: 52px !important;
    font-weight: 800 !important;
    text-align: center;
}

textarea, input {
    border-radius: 12px !important;
}

div.stButton > button {
    border-radius: 14px;
    background-color: #ff5757;
    color: white;
    border: none;
    font-size: 22px;
    padding: 10px 20px;
}

div.stButton > button:hover {
    background-color: #ff4040;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# TÍTULO
st.markdown("# 🔎 Demo TF-IDF en Español")

st.write("")

# COLUMNAS PRINCIPALES
col1, col2 = st.columns([2.2, 1])

# IZQUIERDA
with col1:

    st.markdown("### 📑 Documentos (uno por línea):")

    documentos = st.text_area(
        "",
        height=180,
        value="""Amor, no llores, veo luz en tus males
Siguiéndote el corazón, bailando en un canto de zorzales
Niño, soy un hombre con tristeza, sé del peso en tu verdad
Escaparte por robar porque robás para cenar
Vi tus dedos en el barro con olor a libertad
Sé que te querés dormir pa' no volver a despertar"""
    )

    st.markdown("### ❓ Escribe tu pregunta:")

    pregunta = st.text_input(
        "",
        value="¿Qué sentimiento transmite la canción?"
    )

    st.write("")
    st.write("")

    st.button("🔎 Analizar")

# DERECHA
with col2:

    st.markdown("## 💡 Preguntas sugeridas:")

    st.button("¿De qué trata la canción?")
    st.button("¿Qué emoción expresa?")
    st.button("¿Qué sentimiento transmite?")
    st.button("¿La canción habla de tristeza?")
    st.button("¿Cuál es el tema principal?")cipal?")
