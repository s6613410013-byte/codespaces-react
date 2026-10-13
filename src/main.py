import os
import streamlit as st
import App

# ตั้งค่าหน้าจอ
st.set_page_config(
    page_title="ระบบตรวจวัดค่าพารามิเตอร์ภายในเรือ",
    page_icon="🚤",
    layout="wide"
)

# โหลด CSS ตกแต่ง
css_path = os.path.join(os.path.dirname(__file__), 'index.css')
if os.path.exists(css_path):
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

if __name__ == "__main__":
    App.run()