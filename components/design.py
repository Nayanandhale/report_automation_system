import streamlit as st

def show_design():

    # SIDEBAR
    st.sidebar.image(
        "assets/ngo_logo.png",
        width=180
    )

    st.sidebar.markdown("""
    <h2 style='text-align:center;color:black;'>
    Unnatva Foundation
    </h2>
    """, unsafe_allow_html=True)

    st.sidebar.markdown("""
    <div style="
    background-color: rgba(255,255,255,0.75);
    padding: 18px;
    border-radius: 15px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    ">

    <h2 style="
    color:#2E8B57;text-align:center;margin-bottom:10px;">
    🌱 Our Mission
    </h2>
    <p style="font-size:14px;text-align:justify;color:#333333;">
    Empowering underserved communities through
    sustainable livelihood initiatives and practical,
     demand-driven development programs.
    </p>
    <hr>
    <h4 style="color:#2E8B57;">
    🚀 Focus Areas
    </h4>
    <ul style="font-size:14px;color:#333333;line-height:1.8;">
    <li>Skill Development</li>
    <li>Entrepreneurship Development</li>
    <li>Women Empowerment</li>
    <li>Education & STEM</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # HEADER
    col1, col2 = st.columns([1,5])
    with col1:
        st.image(
            "assets/ngo_logo.png",
            width=100
        )
    with col2:
        st.markdown("""
        <h1 style='color:black;'>
        Unnatva Foundation
        </h1>
        <p style='color:black;font-size:18px;'>
        Empowering India through Sustainable Livelihood Initiatives
        </p>
        """, unsafe_allow_html=True)