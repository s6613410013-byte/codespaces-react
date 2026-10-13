import streamlit as st
import pandas as pd

def run():
    # ตรวจสอบการ Login
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    # ==================== PAGE 1: LOGIN ====================[cite: 8]
    if not st.session_state.logged_in:
        st.markdown("<br><br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1.2, 1])
        with col2:
            st.image("https://img.icons8.com/illustrations/1000/boat.png", width=180) # รูปไอคอนเรือ[cite: 8]
            st.markdown("<h2 style='text-align: center; color: white;'>Login</h2>", unsafe_allow_html=True)[cite: 8]
            
            username = st.text_input("Username", placeholder="Username")[cite: 8]
            password = st.text_input("Password", type="password", placeholder="Password")[cite: 8]
            
            if st.button("Login", use_container_width=True):[cite: 8]
                st.session_state.logged_in = True
                st.rerun()
        return

    # ==================== NAVIGATION BAR (ดีไซน์ใหม่) ====================[cite: 9, 10, 11]
    nav_col1, nav_col2 = st.columns([1, 2])
    with nav_col2:
        menu = st.radio(
            "",
            ["ภาพรวม", "พลังงานสะสมและกราฟ", "กล้องและระบบถามตอบ", "ออกจากระบบ"],[cite: 9, 10, 11]
            horizontal=True,
            label_visibility="collapsed"
        )

    if menu == "ออกจากระบบ":[cite: 9, 10, 11]
        st.session_state.logged_in = False
        st.rerun()

    st.markdown("<h1 class='main-title'>ระบบตรวจวัดค่าพารามิเตอร์ภายในเรือ</h1>", unsafe_allow_html=True)[cite: 9, 10, 11]

    # ==================== PAGE 2: ภาพรวม ====================[cite: 9]
    if menu == "ภาพรวม":[cite: 9]
        c1, c2 = st.columns(2)
        
        # แบตเตอรี่ระบบเครื่องยนต์[cite: 9]
        with c1:
            st.markdown("""
            <div class='card-outer'>
                <span class='card-badge'>12V</span>
                <div class='card-header-title'>⚡ แบตเตอรี่ระบบเครื่องยนต์</div>
                <div class='card-header-sub'>แบตเตอรี่สำหรับสตาร์ทเครื่องยนต์และระบบจ่ายไฟเริ่มต้นเครื่อง</div>
                <br>
            </div>
            """, unsafe_allow_html=True)[cite: 9]
            
            r1, r2 = st.columns(2)
            with r1:
                st.markdown("<div class='sub-box'><div class='sub-title'>แรงดัน</div><div class='sub-value'>12.4 V</div><div class='sub-desc'>ตัวอย่าง</div></div>", unsafe_allow_html=True)[cite: 9]
                st.markdown("<div class='sub-box'><div class='sub-title'>กำลังใช้งาน</div><div class='sub-value'>—</div><div class='sub-desc'>รอข้อมูลแบตเตอรี่ระบบเครื่องยนต์</div></div>", unsafe_allow_html=True)[cite: 9]
                st.markdown("<div class='sub-box'><div class='sub-title'>กำลังไฟฟ้า</div><div class='sub-value'>—</div><div class='sub-desc'>รอข้อมูลแบตเตอรี่ระบบเครื่องยนต์</div></div>", unsafe_allow_html=True)[cite: 9]
            with r2:
                st.markdown("<div class='sub-box'><div class='sub-title'>อัปเดตล่าสุด</div><div class='sub-value'>09:41 น.</div><div class='sub-desc'>ตัวอย่าง</div></div>", unsafe_allow_html=True)[cite: 9]
                st.markdown("<div class='sub-box'><div class='sub-title'>กระแส</div><div class='sub-value'>—</div><div class='sub-desc'>รอข้อมูลแบตเตอรี่ระบบเครื่องยนต์</div></div>", unsafe_allow_html=True)[cite: 9]
                st.markdown("<div class='sub-box'><div class='sub-title'>พลังงานสะสม</div><div class='sub-value'>—</div><div class='sub-desc'>รอข้อมูลแบตเตอรี่ระบบเครื่องยนต์</div></div>", unsafe_allow_html=True)[cite: 9]

        # แบตเตอรี่ระบบไฟภายในเรือ[cite: 9]
        with c2:
            st.markdown("""
            <div class='card-outer'>
                <span class='card-badge'>24V</span>
                <div class='card-header-title'>⚡ แบตเตอรี่ระบบไฟภายในเรือ</div>
                <div class='card-header-sub'>แบตเตอรี่สำหรับระบบไฟแสงสว่างและอุปกรณ์ภายในเรือ</div>
                <br>
            </div>
            """, unsafe_allow_html=True)[cite: 9]
            
            r1, r2 = st.columns(2)
            with r1:
                st.markdown("<div class='sub-box'><div class='sub-title'>แรงดัน</div><div class='sub-value'>24 V</div><div class='sub-desc'>ตัวอย่าง</div></div>", unsafe_allow_html=True)[cite: 9]
                st.markdown("<div class='sub-box'><div class='sub-title'>กำลังใช้งาน</div><div class='sub-value'>—</div><div class='sub-desc'>รอข้อมูลแบตเตอรี่ระบบไฟภายในเรือ</div></div>", unsafe_allow_html=True)[cite: 9]
                st.markdown("<div class='sub-box'><div class='sub-title'>กำลังไฟฟ้า</div><div class='sub-value'>—</div><div class='sub-desc'>รอข้อมูลแบตเตอรี่ระบบไฟภายในเรือ</div></div>", unsafe_allow_html=True)[cite: 9]
            with r2:
                st.markdown("<div class='sub-box'><div class='sub-title'>อัปเดตล่าสุด</div><div class='sub-value'>09:41 น.</div><div class='sub-desc'>ตัวอย่าง</div></div>", unsafe_allow_html=True)[cite: 9]
                st.markdown("<div class='sub-box'><div class='sub-title'>กระแส</div><div class='sub-value'>—</div><div class='sub-desc'>รอข้อมูลแบตเตอรี่ระบบไฟภายในเรือ</div></div>", unsafe_allow_html=True)[cite: 9]
                st.markdown("<div class='sub-box'><div class='sub-title'>พลังงานสะสม</div><div class='sub-value'>—</div><div class='sub-desc'>รอข้อมูลแบตเตอรี่ระบบไฟภายในเรือ</div></div>", unsafe_allow_html=True)[cite: 9]

    # ==================== PAGE 3: พลังงานสะสมและกราฟ ====================[cite: 10]
    elif menu == "พลังงานสะสมและกราฟ":[cite: 10]
        c1, c2 = st.columns(2)
        
        # กราฟกระแสไฟฟ้า[cite: 10]
        with c1:
            st.markdown("""
            <div class='card-outer'>
                <span class='card-badge'>I</span>
                <div class='card-header-title'>⚡ กราฟกระแสไฟฟ้า</div>
                <div class='card-header-sub'>กระแสแบตเตอรี่ 12V และ 24V เมื่อเวลาผ่านไป</div>
            </div>
            """, unsafe_allow_html=True)[cite: 10]
            
            data_i = pd.DataFrame({
                'เวลา': ['08:00', '08:20', '08:40', '09:00', '09:20', '09:41'],
                'แบตเตอรี่ 12V': [10, 12, 14, 13, 12, 12.4],
                'แบตเตอรี่ 24V': [20, 22, 23, 22, 24, 24.0]
            })
            st.line_chart(data_i.set_index('เวลา'))[cite: 10]

        # กราฟแรงดันไฟฟ้า[cite: 10]
        with c2:
            st.markdown("""
            <div class='card-outer'>
                <span class='card-badge'>V</span>
                <div class='card-header-title'>⚡ กราฟแรงดันไฟฟ้า</div>
                <div class='card-header-sub'>แรงดันแบตเตอรี่ 12V และ 24V เมื่อเวลาผ่านไป</div>
            </div>
            """, unsafe_allow_html=True)[cite: 10]
            
            data_v = pd.DataFrame({
                'เวลา': ['08:00', '08:20', '08:40', '09:00', '09:20', '09:41'],
                'แบตเตอรี่ 12V': [12.2, 12.3, 12.4, 12.4, 12.3, 12.4],
                'แบตเตอรี่ 24V': [24.1, 24.0, 24.2, 24.1, 24.0, 24.0]
            })
            st.line_chart(data_v.set_index('เวลา'))[cite: 10]

    # ==================== PAGE 4: กล้องและระบบถามตอบ ====================[cite: 11]
    elif menu == "กล้องและระบบถามตอบ":[cite: 11]
        st.markdown("""
        <div class='status-banner'>
            <span>สถานะการเชื่อมต่อ: การเชื่อมต่อจำลอง • 12.4 เมกะบิตต่อวินาที • อัปเดต 09:41 น.</span>
            <span>ตัวอย่าง / เชื่อมต่อแล้ว</span>
        </div>
        """, unsafe_allow_html=True)[cite: 11]
        
        c1, c2 = st.columns(2)
        
        # กล้องในเรือ[cite: 11]
        with c1:
            st.markdown("""
            <div class='card-outer'>
                <span class='card-badge'>ยังไม่เปิด</span>
                <div class='card-header-title'>📷 กล้องในเรือ</div>
                <div class='card-header-sub'>กล้องในเรือ • ยังไม่ได้เปิดใช้งาน</div>
            </div>
            """, unsafe_allow_html=True)[cite: 11]
            st.image("https://via.placeholder.com/600x320/000000/FFFFFF?text=Pi+Camera+3+MJPEG+Stream", caption="พื้นที่แสดงภาพจากกล้อง")[cite: 11]
            
            btn_col1, btn_col2 = st.columns(2)
            btn_col1.button("ภาพนิ่ง", use_container_width=True)[cite: 11]
            btn_col2.button("เปิดเต็มจอ", use_container_width=True)[cite: 11]

        # ถามระบบ[cite: 11]
        with c2:
            st.markdown("""
            <div class='card-outer'>
                <span class='card-badge'>ระบบ</span>
                <div class='card-header-title'>💬 ถามระบบ</div>
                <div class='card-header-sub'>สอบถามข้อมูลระบบและสถานะเรือ</div>
            </div>
            """, unsafe_allow_html=True)[cite: 11]
            
            chat_container = st.container(height=250)
            with chat_container:
                st.chat_message("user").write("วันนี้ใช้งานไปกี่ชั่วโมง?")[cite: 11]
                st.chat_message("assistant").write("ระบบใช้งานไปแล้วประมาณ 4.2 ชั่วโมง (ตัวอย่าง)")[cite: 11]
                st.chat_message("user").write("แบตเตอรี่ปัจจุบันเหลือ กี่ %?")[cite: 11]
                st.chat_message("assistant").write("ข้อมูลเปอร์เซ็นต์แบตเตอรี่ไม่พร้อมใช้งานในตัวอย่างนี้")[cite: 11]
            
            st.chat_input("พิมพ์คำถาม...")[cite: 11]