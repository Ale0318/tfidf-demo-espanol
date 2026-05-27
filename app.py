import streamlit as st

# CONFIGURACIÓN
st.set_page_config(
    page_title="Demo TF-IDF en Español",
    layout="wide"
)

# ESTILOS
st.markdown("""
<style>

.stApp {
    background-color: #f5f5f5;
}

h1 {
    font-size: 58px !important;
    font-weight: 800 !important;
}

textarea {
    border-radius: 12px !important;
}

div.stButton > button {
    background-color: #ff5757;
    color: white;
    border: none;
    border-radius: 14px;
    padding: 12px 24px;
    font-size: 28px;
    font-weight: 600;
}

div.stButton > button:hover {
    background-color: #ff3b3b;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# TÍTULO
st.markdown("# 🔎 Demo TF-IDF en Español")

# COLUMNAS
col1, col2 = st.columns([2,1])

# ---------------- IZQUIERDA ----------------

with col1:

    st.markdown("### 📑 Documentos (uno por línea):")

    documentos = st.text_area(
        "",
        height=180,
        value="""Y cada vez
Despiertas
Buscando salir
Al viento
Sin nada que decir"""
    )

    st.markdown("### ❓ Escribe tu pregunta:")

    pregunta = st.text_input(
        "",
        value="¿Dónde juegan el perro y el gato?"
    )

    st.write("")
    st.write("")
    st.write("")

    st.button("🔎 Analizar")

# ---------------- DERECHA ----------------

with col2:

    st.markdown("""
    ## 💡 Preguntas sugeridas:
    """)

    st.button("¿De que trata la canción?")
    st.button("Que flor menciona la canción")
    st.button("Porque perdimos el tiempo")
    st.button("A que realidad volvimos")
    st.button("Que emoción tiene la canción")
