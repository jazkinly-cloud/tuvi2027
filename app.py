import streamlit as st

st.set_page_config(
    page_title="Phong Thủy AI 2027",
    page_icon="logo_phong_thuy_ai.png",
    layout="wide"
)
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Phong Thủy 2027",
    layout="wide"
)

html_file = Path(__file__).parent / (
    "Phong_Thuy_AI_SaigonDoor_tich_hop_theo_doi_click.html"
)

if html_file.exists():
    html = html_file.read_text(encoding="utf-8")
    components.html(html, height=1200, scrolling=True)
else:
    st.error(f"Không tìm thấy file: {html_file.name}")
