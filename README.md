# 🎉 Invitación de Cumpleaños — Streamlit

App interactiva para invitar a tu cumpleaños, pensada para verse en celular
(formato vertical 1080x1920).

## Flujo de la app

1. **Portada**: video en loop de una cortina cerrada + botón
   "¿Quieres ir a mi cumpleaños?"
2. **Invitación**: video de la cortina abriéndose + detalles del evento +
   2 botones: **Asistiré** y **No podré**
3. **Asistiré**: formulario simple (nombre, acompañantes, mensaje) que se
   guarda en `respuestas_confirmadas.csv`, además de un botón hacia tu
   Google Forms y un botón hacia tu ubicación en Google Maps.
4. **No podré**: reproduce automáticamente un sonido `.mp3` que tú elijas.

## Estructura de carpetas

```
invitacion-cumple/
├── app.py
├── requirements.txt
├── .gitignore
└── assets/
    ├── cortina_cerrada.mp4
    ├── cortina_abriendo.mp4
    └── no_podre.mp3
```

## Cómo editar tus datos

Abre `app.py` y edita la sección superior marcada como
`CONFIGURACIÓN — EDITA AQUÍ TUS DATOS`:

- `NOMBRE_CUMPLEANERO`
- `FECHA_EVENTO`, `HORA_EVENTO`
- `LUGAR_EVENTO`, `DIRECCION_EVENTO`
- `MENSAJE_INVITACION`
- `GOOGLE_FORMS_URL` (pega aquí el link de tu formulario de Google Forms)

El link de Google Maps ya está configurado.

## Cómo subir tus archivos multimedia

Ver la guía paso a paso que te compartió Claude en el chat, o el resumen
rápido:

1. Coloca tus archivos dentro de la carpeta `assets/` con estos nombres
   exactos:
   - `cortina_cerrada.mp4`
   - `cortina_abriendo.mp4`
   - `no_podre.mp3`
2. Sube todo a GitHub (interfaz web o `git push`).
3. Despliega en https://share.streamlit.io/ apuntando a `app.py`.

## Notas técnicas

- Los videos se incrustan en base64 directamente en el HTML para
  garantizar el `autoplay` en navegadores móviles (los navegadores exigen
  que el video esté `muted` para reproducirse automáticamente; por eso
  ambos videos están silenciados).
- Si tus videos son muy pesados (>50-100 MB), el repositorio de GitHub
  puede rechazar el push. Comprime los videos antes de subirlos (recomendado:
  H.264, resolución 1080x1920, bajo bitrate, duración corta para el loop).
- Las respuestas del formulario simple se guardan en un CSV local. En
  Streamlit Community Cloud este archivo **no es permanente**: se borra
  cada vez que la app se reinicia o se redeploya. Para guardar respuestas
  de forma definitiva, usa el botón de Google Forms.
