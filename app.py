import streamlit as st
import os

from components.styles import show_style
from components.design import show_design
from components.auth import show_login_page
from components.upload import show_upload
from components.dashboard import show_dashboard
from components.history import show_history
from utils.db_handler import (
    get_pending_users,
    approve_user,
    update_password
)

# 1. APPLY GLOBAL PAGE STYLES
show_style()

# 2. SESSION INITIALIZATION
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

def logout():
    st.session_state.logged_in = False
    st.session_state.username = ""

# ============================
# LOGIN FLOW (CLEAN, FOCUSED)
# ============================
if not st.session_state.logged_in:
    show_login_page()
    st.stop()

# ============================
# MAIN AUTHENTICATED PORTAL
# ============================

# DISPLAY SIDEBAR & MAIN HEADER
show_design()

# SIDEBAR UTILITIES
with st.sidebar:
    st.markdown(f"**Logged in as:** `{st.session_state.username}`")

    # ADMIN PANEL (VISIBLE ONLY TO ADMIN)
    if st.session_state.username == "admin":
        st.markdown("---")
        st.markdown("##### 🛡️ Admin Approval Panel")
        pending_users = get_pending_users()

        if pending_users:
            for u_id, u_name in pending_users:
                col_u1, col_u2 = st.columns([2, 1])
                col_u1.write(f"🟡 `{u_name}`")
                if col_u2.button("Approve", key=f"approve_{u_id}"):
                    approve_user(u_id)
                    st.success(f"{u_name} approved!")
                    st.rerun()
        else:
            st.info("No pending user approvals.")

    # PASSWORD CHANGE
    st.markdown("---")
    with st.expander("🔑 Change Password"):
        curr_pass = st.text_input("Current Password", type="password", key="side_curr_pass")
        new_pass = st.text_input("New Password", type="password", key="side_new_pass")
        if st.button("Update Password"):
            ok, msg = update_password(st.session_state.username, curr_pass, new_pass)
            if ok:
                st.success(msg)
            else:
                st.error(msg)

    # LOGOUT BUTTON
    st.markdown("---")
    if st.button("🚪 Logout", use_container_width=True):
        logout()
        st.rerun()

# MAIN NAVIGATION TABS
tab1, tab2, tab3 = st.tabs([
    "📤 Ingest Report",
    "📊 Analytics Dashboard",
    "📜 Master History"
])

with tab1:
    show_upload()

with tab2:
    show_dashboard()

with tab3:
    show_history()
