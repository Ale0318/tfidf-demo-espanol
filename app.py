import streamlit as st

# CONFIGURACIÓN
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

.block-container{
    max-width: 1400px;
    padding-top: 2rem;
}

h1 {
    font-size: 52px !important;
    font-weight: 800 !important;
    text-align: center;
    color: #2b2d42;
}

h2 {
    color: #2b2d42;
}

textarea, input {
    border-radius: 12px !important;
}

div.stButton > button {
    border-radius: 16px;
    background-color: #ff5757;
    color: white;
    border: none;
    font-size: 20px;
    padding: 10px 22px;
    width: 100%;
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
st.write("")

# CENTRAR TODO EL BLOQUE
left, center, right = st.columns([0.7, 2, 0.7])

with center:

    # COLUMNAS INTERNAS
    col1, col2 = st.columns([1.3, 1])

    # IZQUIERDA
    with col1:

        st.markdown("## 📑 Documentos (uno por línea):")

        documentos = st.text_area(
            "",
            height=140,
            value="""Amor, no llores, veo luz en tus males
Siguiéndote el corazón, bailando en un canto de zorzales
Niño, soy un hombre con tristeza, sé del peso en tu verdad
Escaparte por robar porque robás para cenar
Vi tus dedos en el barro con olor a libertad
Sé que te querés dormir pa' no volver a despertar"""
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

    # DERECHA
    with col2:

        st.markdown("## 💡 Preguntas sugeridas:")

        st.button("¿De qué trata la canción?")
        st.button("¿Qué emoción expresa?")
        st.button("¿Qué sentimiento transmite?")
        st.button("¿La canción habla de tristeza?")
        st.button("¿Cuál es el tema principal?")
