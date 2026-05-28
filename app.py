import streamlit as st
from components.styles import show_style
from components.design import show_design
from components.upload import show_upload
from components.dashboard import show_dashboard
from components.history import show_history

show_style()
show_design()

import streamlit as st
import sqlite3
import bcrypt

# DATABASE
conn = sqlite3.connect(
    "database.db",
    check_same_thread=False
)

cursor = conn.cursor()

# SESSION
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# ----------------------------
# LOGIN FUNCTION
# ----------------------------

def login_user(username, password):

    cursor.execute(
        """
        SELECT password, status
        FROM users
        WHERE username = ?
        """,
        (username,)
    )

    user = cursor.fetchone()

    if user:

        stored_password, status = user

        # Check approval
        if status != "approved":
            return "pending"

        # Verify password
        if bcrypt.checkpw(
            password.encode(),
            stored_password.encode()
        ):

            st.session_state.logged_in = True
            st.session_state.username = username

            return "success"

    return "failed"

# ----------------------------
# LOGOUT
# ----------------------------

def logout():

    st.session_state.logged_in = False
    st.session_state.username = ""

# ============================
# LOGIN PAGE
# ============================

if not st.session_state.logged_in:

    st.title("Login")

    username = st.text_input(
        "Username",
        key="login_username"
    )

    password = st.text_input(
        "Password",
        type="password",
        key="login_password"
    )

    if st.button("Login"):

        result = login_user(
            username.strip(),
            password
        )

        if result == "success":
            st.success("Login successful!")
            st.rerun()

        elif result == "pending":
            st.warning("Waiting for admin approval")

        else:
            st.error("Invalid username or password")

    # ============================
    # SIGNUP
    # ============================

    st.subheader("Create New Account")

    new_username = st.text_input(
        "New Username",
        key="signup_username"
    )

    new_password = st.text_input(
        "New Password",
        type="password",
        key="signup_password"
    )

    if st.button("Signup"):

        hashed_password = bcrypt.hashpw(
            new_password.encode(),
            bcrypt.gensalt()
        ).decode()

        try:

            cursor.execute(
                """
                INSERT INTO users
                (username, password, status)
                VALUES (?, ?, ?)
                """,
                (
                    new_username.strip(),
                    hashed_password,
                    "pending"
                )
            )

            conn.commit()

            st.success(
                "Signup request sent to admin!"
            )

        except Exception as e:
            st.error("Username already exists")

    st.stop()
# ----------------------------
# CHANGE PASSWORD
# ----------------------------

with st.sidebar:

    st.subheader("Change Password")

    current_password = st.text_input(
        "Current Password",
        type="password",
        key="current_pass"
    )

    new_password = st.text_input(
        "New Password",
        type="password",
        key="new_pass"
    )

    if st.button("Update Password"):

        cursor.execute(
            """
            SELECT password
            FROM users
            WHERE username = ?
            """,
            (st.session_state.username,)
        )

        user = cursor.fetchone()

        if user:

            stored_password = user[0]

            if bcrypt.checkpw(
                current_password.encode(),
                stored_password.encode()
            ):

                hashed_new_password = bcrypt.hashpw(
                    new_password.encode(),
                    bcrypt.gensalt()
                ).decode()

                cursor.execute(
                    """
                    UPDATE users
                    SET password = ?
                    WHERE username = ?
                    """,
                    (
                        hashed_new_password,
                        st.session_state.username
                    )
                )

                conn.commit()

                st.success("Password updated!")

            else:
                st.error("Wrong current password")

# ============================
# ADMIN PANEL
# ============================

with st.sidebar:

    if st.session_state.username == "admin":

        st.header("Admin Panel")

        cursor.execute(
            """
            SELECT id, username
            FROM users
            WHERE status = 'pending'
            """
        )

        pending_users = cursor.fetchall()

        if pending_users:

            for user in pending_users:

                user_id, username = user

                st.write(f"🟡 {username}")

                if st.button(
                    f"Approve {username}",
                    key=f"approve_{user_id}"
                ):

                    cursor.execute(
                        """
                        UPDATE users
                        SET status = 'approved'
                        WHERE id = ?
                        """,
                        (user_id,)
                    )

                    conn.commit()

                    st.success(f"{username} approved!")

                    st.rerun()

        else:
            st.info("No pending users")

with st.sidebar:

    if st.button("Logout"):

        logout()

        st.rerun()

tab1, tab2, tab3 = st.tabs([
    "📤 Upload Report",
    "📊 Dashboard",
    "📜 History"
])

with tab1:
    show_upload()
with tab2:
    show_dashboard()
with tab3:
    show_history()