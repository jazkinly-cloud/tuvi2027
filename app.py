
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Phong Thủy AI",
    page_icon="☯️",
    layout="wide"
)

st.title("☯️ PHONG THỦY AI")

html_file = Path(__file__).parent / "index.html"

if html_file.exists():
    html_content = html_file.read_text(encoding="utf-8")
    components.html(
        html_content,
        height=1000,
        scrolling=True
    )
else:
    st.error("Không tìm thấy file index.html. Anh hãy tải file HTML lên cùng thư mục với app.py.")
