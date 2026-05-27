import streamlit as st

st.set_page_config(
    page_title="Demo TF-IDF",
    layout="wide"
)

# =========================
# ESTILOS
# =========================

st.markdown("""
<style>

.stApp {
    background-color: #f5f5f5;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

h1 {
    text-align: center;
    color: #2b2d42;
    font-size: 42px !important;
    margin-bottom: 50px;
}

h2 {
    color: #2b2d42;
    font-size: 28px !important;
}

textarea {
    border-radius: 12px !important;
}

.stTextInput input {
    border-radius: 12px !important;
}

div.stButton > button {
    background-color: #ff5757;
    color: white;
    border-radius: 14px;
    border: none;
    padding: 12px 28px;
    font-size: 22px;
    font-weight: bold;
}

div.stButton > button:hover {
    background-color: #ff3f3f;
    color: white;
}

.pregunta-btn {
    background-color: #ff5757;
    color: white;
    padding: 10px;
    border-radius: 14px;
    text-align: center;
    margin-bottom: 12px;
    font-size: 16px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# =========================
# CENTRAR TODO EL CONTENIDO
# =========================

left, center, right = st.columns([1.2, 4, 1.2])

with center:

    # =========================
    # TITULO
    # =========================

    st.markdown(
        "<h1>🔎 Demo TF-IDF en Español</h1>",
        unsafe_allow_html=True
    )

    # =========================
    # COLUMNAS
    # =========================

    col1, col2 = st.columns([1.7, 1])

    # =========================
    # COLUMNA IZQUIERDA
    # =========================

    with col1:

        st.markdown("## 📑 Documentos (uno por línea):")

        texto = st.text_area(
            "",
            value="""Amor, no llores, veo luz en tus males
Siguiéndote el corazón, bailando en un canto de zorzales
Niño, soy un hombre con tristeza, sé del peso en tu verdad
Escaparte por robar porque robás para cenar
Vi tus dedos en el barro con olor a libertad
Sé que te querés dormir pa' no volver a despertar""",
            height=180
        )

        st.write("")

        st.markdown("## ❓ Escribe tu pregunta:")

        pregunta = st.text_input(
            "",
            value="¿Qué sentimiento transmite la canción?"
        )

        st.write("")
        st.write("")

        st.button("🔎 Analizar")

    # =========================
    # COLUMNA DERECHA
    # =========================

    with col2:

        st.markdown("## 💡 Preguntas sugeridas:")

        preguntas = [
            "¿De qué trata la canción?",
            "¿Qué emoción expresa?",
            "¿Qué sentimiento transmite?",
            "¿La canción habla de tristeza?",
            "¿Cuál es el tema principal?"
        ]

        for p in preguntas:
            st.markdown(
                f"<div class='pregunta-btn'>{p}</div>",
                unsafe_allow_html=True
            )
