import streamlit as st

st.title("👋 My Bio")
#---------Bio-------------
NAME = "Preston Konkel"
PROGRAM = "B.S. / Computer Science / MSU Denver"
INTRO = (
    "I am a Computer Science Student and work part time in IT. Data visualization is a fun branch of study especially in "
    "regards to geographic systems and information."
)
FUN_FACTS = [
    "I love food",
    "I’m learning all the time",
    "I want to build things",
]
PHOTO_PATH = "hubble-captures-vivid-auroras-in-jupiters-atmosphere_28000029525_o~small.jpg"  # Put a file in repo root or set a URL

# ---------- Layout ----------
col1, col2 = st.columns([1, 2], vertical_alignment="center")

with col1:
    try:
        st.image(PHOTO_PATH, caption=NAME, use_container_width=True)
    except Exception:
        st.info("Add a photo named `your_photo.jpg` to the repo root, or change PHOTO_PATH.")
with col2:
    st.subheader(NAME)
    st.write(PROGRAM)
    st.write(INTRO)

st.markdown("### Fun facts")
for i, f in enumerate(FUN_FACTS, start=1):
    st.write(f"- {f}")

st.divider()
st.caption("Edit `pages/1_Bio.py` to customize this page.")
