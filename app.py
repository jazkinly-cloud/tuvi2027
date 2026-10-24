
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Phong Thủy 2027",
    layout="wide"
)

html_file = Path(__file__).parent / (
    "phong_th_y_ai_b_n_tr_i_nghi_m_ng_i_d_ng_v2_0.html"
)

if html_file.exists():
    html = html_file.read_text(encoding="utf-8")
    components.html(html, height=1200, scrolling=True)
else:
    st.error(f"Không tìm thấy file: {html_file.name}")
