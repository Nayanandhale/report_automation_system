import streamlit as st
import os

def show_design():
    # SIDEBAR BRANDING
    logo_path = "assets/ngo_logo.png" if os.path.exists("assets/ngo_logo.png") else None

    with st.sidebar:
        if logo_path:
            logo_cols = st.columns([1, 2, 1])
            with logo_cols[1]:
                st.image(logo_path, width=95)
        
        st.markdown("""
        <div style="text-align:center; margin-top:4px; margin-bottom:12px;">
            <div style="color:#005A36; font-size:18px; font-weight:800; letter-spacing:-0.2px;">UNNATVA FOUNDATION</div>
            <span style="background:#E2ECE6; color:#005A36; font-size:11px; font-weight:700; padding:3px 10px; border-radius:12px;">
                Nashik Center • Social Initiative
            </span>
        </div>
        """, unsafe_allow_html=True)

        # Sidebar Mission Card
        st.markdown("""
        <div style="
            background: #FFFFFF;
            border: 1px solid #DCE7E0;
            border-radius: 14px;
            padding: 16px;
            margin-bottom: 16px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.03);
        ">
            <h4 style="color:#005A36; margin:0 0 8px 0; font-size:14px; font-weight:700;">
                🌱 Our Mission
            </h4>
            <p style="font-size:12px; color:#4A5E53; line-height:1.5; margin:0 0 10px 0;">
                Empowering underserved communities through sustainable livelihood initiatives and practical development programs.
            </p>
            <div style="border-top:1px dashed #DCE7E0; padding-top:10px;">
                <div style="color:#005A36; font-size:11px; font-weight:700; margin-bottom:6px;">FOCUS INITIATIVES</div>
                <div>
                    <span class="unnatva-pill-badge" style="font-size:10px; padding:3px 8px; margin-bottom:4px; display:inline-block;">Skill Development</span>
                    <span class="unnatva-pill-badge" style="font-size:10px; padding:3px 8px; margin-bottom:4px; display:inline-block;">Entrepreneurship</span>
                    <span class="unnatva-pill-badge" style="font-size:10px; padding:3px 8px; margin-bottom:4px; display:inline-block;">Women Empowerment</span>
                    <span class="unnatva-pill-badge" style="font-size:10px; padding:3px 8px; margin-bottom:4px; display:inline-block;">Education & STEM</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # TOP HERO HEADER (Matching website screenshot)
    col_hero1, col_hero2 = st.columns([1, 10]) if logo_path else (None, None)

    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #005A36 0%, #004529 100%);
        border-radius: 16px;
        padding: 20px 24px;
        margin-bottom: 20px;
        color: white;
        box-shadow: 0 6px 20px rgba(0, 90, 54, 0.15);
    ">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:15px;">
            <div style="display:flex; align-items:center; gap:16px;">
                <div>
                    <div style="display:inline-block; background:rgba(255,255,255,0.15); border:1px solid rgba(255,255,255,0.25); padding:3px 10px; border-radius:20px; font-size:11px; font-weight:600; letter-spacing:0.5px; text-transform:uppercase; margin-bottom:6px;">
                        Report Automation System
                    </div>
                    <h1 style="color:white; margin:0 0 4px 0; font-size:26px; font-weight:800; font-family:'Plus Jakarta Sans', sans-serif;">
                        Unnatva Foundation
                    </h1>
                    <p style="color:#D6EADF; margin:0; font-size:13px; font-weight:500;">
                        Automated report ingestion, OCR extraction, attendance verification, and Google Sheets tracker sync.
                    </p>
                </div>
            </div>
            <div style="background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.18); border-radius:12px; padding:10px 16px; text-align:right;">
                <div style="font-size:11px; color:#CADFD3; font-weight:600; text-transform:uppercase;">Impact Tracker (2023–2026)</div>
                <div style="margin-top:6px; display:flex; gap:8px; justify-content:flex-end; flex-wrap:wrap;">
                    <span style="background:#F5C518; color:#0A2B19; font-weight:800; font-size:12px; padding:3px 9px; border-radius:10px;">11,593 Beneficiaries</span>
                    <span style="background:#F5C518; color:#0A2B19; font-weight:800; font-size:12px; padding:3px 9px; border-radius:10px;">2,390 Women Trained</span>
                    <span style="background:#F5C518; color:#0A2B19; font-weight:800; font-size:12px; padding:3px 9px; border-radius:10px;">78.4% Placement</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)