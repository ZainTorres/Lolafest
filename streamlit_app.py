import base64
from pathlib import Path
from datetime import datetime

import streamlit as st

# ======================================================================
#  CONFIGURACIÓN — EDITA AQUÍ TUS DATOS
# ======================================================================
#NOMBRE_CUMPLEANERO = "LOLITA"          # Ej: "Valentina"
#FECHA_EVENTO = "Sábado 15 de Agosto, 2026"             # Ej: "Sábado 15 de Agosto, 2026"
#HORA_EVENTO = "7:00 PM"                                # Ej: "7:00 PM"
#LUGAR_EVENTO = "ESCRIBE AQUÍ EL LUGAR"                 # Ej: "Salón Los Jardines"
#DIRECCION_EVENTO = "ESCRIBE AQUÍ LA DIRECCIÓN COMPLETA"
#MENSAJE_INVITACION = "¡Será una noche inolvidable y quiero celebrarla contigo!"

# Link de tu Google Maps (ya configurado con el que enviaste)
GOOGLE_MAPS_LINK = "https://maps.app.goo.gl/wh5xMjmkSFv2aa2P6"

# Pega aquí tu link de Google Forms cuando lo crees
GOOGLE_FORMS_URL = "PEGA_AQUI_TU_LINK_DE_GOOGLE_FORMS"

# Archivos multimedia (deben estar en la carpeta assets/)
VIDEO_CORTINA_CERRADA = "assets/cortina_cerrada.mp4"
VIDEO_CORTINA_ABRIENDO = "assets/cortina_abriendo.mp4"
SONIDO_NO_PODRE = "assets/no_podre.mp3"

# ======================================================================
#  CONFIGURACIÓN DE PÁGINA
# ======================================================================
st.set_page_config(
    page_title=f"Invitación de Cumpleaños - {NOMBRE_CUMPLEANERO}",
    page_icon="🎉",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ======================================================================
#  ESTILOS GLOBALES (mobile-first, 1080x1920 vertical feel)
# ======================================================================
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .stApp {
        background: #0b0b12;
    }

    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
        max-width: 480px;
        margin: 0 auto;
    }

    .video-container {
        position: relative;
        width: 100%;
        border-radius: 18px;
        overflow: hidden;
        box-shadow: 0 8px 40px rgba(0,0,0,0.6);
        margin-bottom: 1.2rem;
    }

    .titulo-invitacion {
        text-align: center;
        color: #f5d676;
        font-family: 'Georgia', serif;
        font-size: 2.1rem;
        font-weight: 700;
        margin: 0.6rem 0 0.3rem 0;
        text-shadow: 0 2px 10px rgba(245, 214, 118, 0.4);
    }

    .subtitulo-invitacion {
        text-align: center;
        color: #e8e6f0;
        font-size: 1.05rem;
        margin-bottom: 1.2rem;
        line-height: 1.5;
    }

    .detalle-card {
        background: linear-gradient(135deg, #1c1c2b, #2a2440);
        border: 1px solid rgba(245, 214, 118, 0.35);
        border-radius: 16px;
        padding: 1.1rem 1.3rem;
        margin-bottom: 1rem;
        color: #f0eefc;
    }

    .detalle-card b { color: #f5d676; }

    div.stButton > button {
        width: 100%;
        border-radius: 14px;
        padding: 0.85rem 1rem;
        font-size: 1.05rem;
        font-weight: 600;
        border: none;
        transition: transform 0.15s ease;
    }

    div.stButton > button:hover {
        transform: scale(1.02);
    }

    .btn-principal button {
        background: linear-gradient(135deg, #f5d676, #e0b84a) !important;
        color: #1c1505 !important;
    }

    .btn-asistir button {
        background: linear-gradient(135deg, #4caf7d, #2f8f5c) !important;
        color: white !important;
    }

    .btn-no-podre button {
        background: linear-gradient(135deg, #6b6b7a, #44444f) !important;
        color: #f0eefc !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ======================================================================
#  UTILIDADES
# ======================================================================
def video_base64(path: str) -> str | None:
    """Lee un video local y lo devuelve en base64 para incrustarlo en HTML."""
    p = Path(path)
    if not p.exists():
        return None
    with open(p, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def mostrar_video_loop(path: str, key_msg: str):
    """Muestra un video en loop, autoplay, silenciado (requerido por navegadores)."""
    b64 = video_base64(path)
    if b64 is None:
        st.warning(
            f"⚠️ No encontré el video en `{path}`. "
            f"Sube tu archivo a esa ruta dentro del repositorio."
        )
        return
    html = f"""
    <div class="video-container">
        <video autoplay loop muted playsinline style="width:100%; display:block;">
            <source src="data:video/mp4;base64,{b64}" type="video/mp4">
        </video>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def mostrar_video_una_vez(path: str):
    """Muestra un video una sola vez (sin loop), autoplay, silenciado."""
    b64 = video_base64(path)
    if b64 is None:
        st.warning(
            f"⚠️ No encontré el video en `{path}`. "
            f"Sube tu archivo a esa ruta dentro del repositorio."
        )
        return
    html = f"""
    <div class="video-container">
        <video autoplay muted playsinline style="width:100%; display:block;">
            <source src="data:video/mp4;base64,{b64}" type="video/mp4">
        </video>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def reproducir_sonido(path: str):
    """Reproduce un mp3 automáticamente una vez, oculto."""
    p = Path(path)
    if not p.exists():
        st.warning(f"⚠️ No encontré el audio en `{path}`. Sube tu archivo mp3 a esa ruta.")
        return
    with open(p, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    html = f"""
    <audio autoplay style="display:none;">
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """
    st.markdown(html, unsafe_allow_html=True)


def guardar_respuesta_local(nombre: str, acompanantes: int, mensaje: str):
    """Guarda confirmaciones en un CSV local dentro del proyecto."""
    archivo = Path("respuestas_confirmadas.csv")
    nueva = not archivo.exists()
    with open(archivo, "a", encoding="utf-8") as f:
        if nueva:
            f.write("fecha_registro,nombre,acompanantes,mensaje\n")
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        nombre_limpio = nombre.replace(",", " ")
        mensaje_limpio = mensaje.replace(",", " ").replace("\n", " ")
        f.write(f"{fecha},{nombre_limpio},{acompanantes},{mensaje_limpio}\n")


# ======================================================================
#  ESTADO DE NAVEGACIÓN
# ======================================================================
if "escena" not in st.session_state:
    st.session_state.escena = "portada"   # portada -> invitacion -> (asistire | no_podre)


def ir_a(escena: str):
    st.session_state.escena = escena


# ======================================================================
#  ESCENA 1: PORTADA — cortina cerrada en loop
# ======================================================================
if st.session_state.escena == "portada":
    mostrar_video_loop(VIDEO_CORTINA_CERRADA, "portada")

    st.markdown(
        "<div class='subtitulo-invitacion'>Tienes algo especial esperándote...</div>",
        unsafe_allow_html=True,
    )

    st.markdown("<div class='btn-principal'>", unsafe_allow_html=True)
    if st.button("¿Quieres ir a mi cumpleaños? 🎂", key="btn_abrir"):
        ir_a("invitacion")
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)


# ======================================================================
#  ESCENA 2: INVITACIÓN — cortina abriéndose + detalles + botones
# ======================================================================
elif st.session_state.escena == "invitacion":
    mostrar_video_una_vez(VIDEO_CORTINA_ABRIENDO)

    st.markdown(f"<div class='titulo-invitacion'>¡Estás invitado/a!</div>", unsafe_allow_html=True)
    st.markdown(
        f"<div class='subtitulo-invitacion'>{MENSAJE_INVITACION}</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="detalle-card">
            🎉 <b>Festejado/a:</b> {NOMBRE_CUMPLEANERO}<br>
            📅 <b>Fecha:</b> {FECHA_EVENTO}<br>
            🕖 <b>Hora:</b> {HORA_EVENTO}<br>
            📍 <b>Lugar:</b> {LUGAR_EVENTO}<br>
            🗺️ <b>Dirección:</b> {DIRECCION_EVENTO}
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='btn-asistir'>", unsafe_allow_html=True)
        if st.button("✅ Asistiré", key="btn_asistire"):
            ir_a("asistire")
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='btn-no-podre'>", unsafe_allow_html=True)
        if st.button("😢 No podré", key="btn_no_podre"):
            ir_a("no_podre")
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)


# ======================================================================
#  ESCENA 3A: ASISTIRÉ — formulario + Google Forms + mapa
# ======================================================================
elif st.session_state.escena == "asistire":
    st.markdown("<div class='titulo-invitacion'>¡Qué alegría! 🥳</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='subtitulo-invitacion'>Confirma tu asistencia con tus datos abajo.</div>",
        unsafe_allow_html=True,
    )

    with st.form("form_confirmacion", clear_on_submit=False):
        nombre = st.text_input("Tu nombre completo *")
        acompanantes = st.number_input("¿Cuántos acompañantes traerás?", min_value=0, max_value=20, value=0)
        mensaje = st.text_area("Mensaje para el/la festejado/a (opcional)")
        enviado = st.form_submit_button("Enviar confirmación")

        if enviado:
            if nombre.strip() == "":
                st.error("Por favor escribe tu nombre antes de enviar.")
            else:
                guardar_respuesta_local(nombre, int(acompanantes), mensaje)
                st.success(f"¡Gracias {nombre}! Tu asistencia quedó confirmada 🎉")
                st.balloons()

    st.markdown("---")
    st.markdown(
        "<div class='subtitulo-invitacion'>"
        "¿Prefieres confirmar por Google Forms? También puedes hacerlo aquí:"
        "</div>",
        unsafe_allow_html=True,
    )
    st.link_button("📋 Abrir formulario de Google Forms", GOOGLE_FORMS_URL, use_container_width=True)

    st.markdown("---")
    st.markdown("<div class='titulo-invitacion' style='font-size:1.4rem;'>📍 Cómo llegar</div>", unsafe_allow_html=True)
    st.link_button("🗺️ Abrir ubicación en Google Maps", GOOGLE_MAPS_LINK, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("⬅️ Volver a la invitación", key="volver_1"):
        ir_a("invitacion")
        st.rerun()


# ======================================================================
#  ESCENA 3B: NO PODRÉ — sonido + mensaje
# ======================================================================
elif st.session_state.escena == "no_podre":
    reproducir_sonido(SONIDO_NO_PODRE)

    st.markdown("<div class='titulo-invitacion'>Te vamos a extrañar 💔</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='subtitulo-invitacion'>"
        "Gracias por avisar. ¡Ojalá puedas la próxima vez!"
        "</div>",
        unsafe_allow_html=True,
    )

    if st.button("⬅️ Volver a la invitación", key="volver_2"):
        ir_a("invitacion")
        st.rerun()
