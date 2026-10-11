import streamlit as st
import os
from utils.db_handler import authenticate_user, register_user

def show_login_page():
    # Hide sidebar during login for a focused, clean login experience
    st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        display: none;
    }
    .main .block-container {
        max-width: 460px;
        padding-top: 3.5rem;
        padding-bottom: 3.5rem;
    }
    .portal-title {
        color: #005A36;
        font-size: 22px;
        font-weight: 800;
        text-align: center;
        margin: 6px 0 2px 0;
        letter-spacing: -0.2px;
    }
    .portal-subtitle {
        color: #52635B;
        font-size: 13px;
        font-weight: 500;
        text-align: center;
        margin: 0 0 18px 0;
    }
    </style>
    """, unsafe_allow_html=True)

    logo_path = "assets/ngo_logo.png" if os.path.exists("assets/ngo_logo.png") else None

    # Centered Logo
    if logo_path:
        col_l1, col_l2, col_l3 = st.columns([1.5, 1, 1.5])
        with col_l2:
            st.image(logo_path, width=80)

    # Title & Subtitle
    st.markdown("""
    <div class="portal-title">UNNATVA FOUNDATION</div>
    <div class="portal-subtitle">Report Automation & Tracker System • Nashik Center</div>
    """, unsafe_allow_html=True)

    tab_login, tab_signup = st.tabs(["🔐 Sign In", "📝 Create Account"])

    with tab_login:
        st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)
        username = st.text_input("Username", key="login_username_field", placeholder="Enter your username")
        password = st.text_input("Password", type="password", key="login_password_field", placeholder="Enter your password")

        st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)
        if st.button("Log In to Portal", key="btn_portal_login", use_container_width=True):
            if not username.strip() or not password:
                st.warning("Please enter both username and password.")
            else:
                status = authenticate_user(username, password)
                if status == "success":
                    st.session_state.logged_in = True
                    st.session_state.username = username.strip()
                    st.success("Login successful!")
                    st.rerun()
                elif status == "pending":
                    st.warning("⚠️ Account created but pending administrator approval.")
                else:
                    st.error("Invalid username or password.")

    with tab_signup:
        st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)
        new_user = st.text_input("Desired Username", key="signup_user_field", placeholder="Choose username")
        new_pass = st.text_input("Desired Password", type="password", key="signup_pass_field", placeholder="Choose password")
        
        st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)
        if st.button("Submit Account Request", key="btn_submit_signup", use_container_width=True):
            if not new_user.strip() or not new_pass:
                st.warning("Please fill in both fields.")
            else:
                ok, msg = register_user(new_user, new_pass)
                if ok:
                    st.success(f"✅ {msg}")
                else:
                    st.error(f"⚠️ {msg}")

        st.markdown("""
        <div style="font-size:12px; color:#6B7C72; margin-top:12px; text-align:center;">
            New staff registrations require administrator approval before logging in.
        </div>
        """, unsafe_allow_html=True)
