streamlit run birthday_app.py
import streamlit as st
import time

# Seite konfigurieren
st.set_page_config(page_title="🎂 Birthday Moments", page_icon="🎂")

# Titel
st.title("🎉 Alles Gute zum Geburtstag! 🎉")

st.write("Eine kleine Überraschung wartet auf dich… 🎁")
for i in range(5, 0, -1):
    st.write(f"⏳ Überraschung in {i} Sekunden...")
    time.sleep(1)
# Startbutton
if st.button("👉 Überraschung starten"):

    st.success("Los geht's... 💫")
    time.sleep(2)

    # Nachricht 1
    st.subheader("💬 Nachricht 1")
    st.write("Wir wünschen dir alles Gute zum Geburtstag!")
    time.sleep(3)

    # Nachricht 2
    st.subheader("💬 Nachricht 2")
    st.write("Viel Glück, Erfolg und Gesundheit für dein neues Jahr!")
    time.sleep(3)

    # Bild (optional)
    st.subheader("📸 Erinnerung")
    st.image("bild.jpg", caption="Gemeinsame Momente ❤️")
    time.sleep(3)

    # Video
    st.subheader("🎥 Überraschungsvideo")
    st.video("video.mp4")
    time.sleep(5)

    # Musik
    st.subheader("🎶 Song für dich")
    st.audio("song.mp3")
    time.sleep(3)

    # Finale
    st.success("🎁 Finale Überraschung!")
    st.balloons()
    st.header("❤️ Wir haben dich lieb! ❤️")

name = st.text_input("Christian")

if name:
    st.write(f"🎉 Alles Gute, {name}!")    