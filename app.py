import streamlit as st
import pandas as pd

# ─── PAGE CONFIG ─────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="NextChapter · Rise Academy",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── GLOBAL STYLES ───────────────────────────────────────────────────────────

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;1,400&family=Source+Sans+3:wght@300;400;600&display=swap');

/* Main Page Overrides */
.stApp {
    background-color: #F9F7F2; /* Soft Cream/Paper Background */
}

html, body, [class*="css"] {
    font-family: 'Lora', Georgia, serif;
    color: #2D2C29; /* Deep Charcoal for readability */
    font-weight: 600; /* further increase for stronger text */
}

/* Hide default streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2rem; padding-bottom: 3rem; max-width: 860px; }

/* Buttons - Elevated Gold */
.stButton > button {
    background-color: #C8A96E !important;
    color: #2D2C29 !important; /* dark text for contrast on gold */
    border: none !important;
    border-radius: 0 !important; /* fully rectangular */
    font-family: 'Source Sans 3', sans-serif !important;
    font-weight: 700 !important; /* stronger weight for contrast */
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
    padding: 0.65rem 2rem !important;
    width: 100%;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}
.stButton > button:hover {
    background-color: #B8996E !important;
    color: #2D2C29 !important;
}

/* Radio buttons & Selection */
.stRadio > div { gap: 0.4rem; }
.stRadio label {
    background: #FFFFFF;
    border: 1px solid #E0DDD5;
    padding: 0.5rem 1.2rem;
    cursor: pointer;
    color: #5D5B55 !important;
    font-family: 'Source Sans 3', sans-serif !important;
    border-radius: 0; /* rectangular shape */
    font-weight: 600; /* improve text contrast */
}

/* Text & Input Areas - Crisp White */
.stTextInput input, .stTextArea textarea {
    background-color: #FFFFFF !important;
    border: 1px solid #E0DDD5 !important;
    border-radius: 4px !important;
    color: #2D2C29 !important;
    font-family: 'Lora', serif !important;
}

/* Select box & Multiselect */
.stSelectbox > div > div, .stMultiSelect > div > div {
    background-color: #FFFFFF !important;
    border: 1px solid #E0DDD5 !important;
    border-radius: 4px !important;
}

/* Slider Track */
.stSlider > div > div > div > div {
    background-color: #C8A96E !important;
}

/* Dataframe Styling */
.stDataFrame { 
    border: 1px solid #E0DDD5; 
    background-color: #FFFFFF;
}

/* Divider */
hr { border-color: #E0DDD5 !important; }

/* Metric & Cards */
[data-testid="metric-container"] {
    background: #FFFFFF;
    border: 1px solid #E0DDD5;
    padding: 1rem;
    border-radius: 8px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.02);
}
[data-testid="stMetricLabel"] { color: #7A7770 !important; font-size: 0.75rem !important; letter-spacing: 0.1em; text-transform: uppercase; }
[data-testid="stMetricValue"] { color: #B8996E !important; font-size: 2rem !important; }

/* Custom Progress Bar Background for Light Mode */
.progress-bg {
    height: 6px;
    background: #E0DDD5; 
    border-radius: 3px;
    margin-top: 4px;
}
</style>
""", unsafe_allow_html=True)

# ─── DATA ─────────────────────────────────────────────────────────────────────

STUDENTS = [
    {"first": "Abryana",   "last": "Davis",        "interest": "Marketing & Sales",              "career": "Art Directors"},
    {"first": "Alex",      "last": "Morton",        "interest": "Supply Chain & Transportation",  "career": "Security and Fire Alarm Systems Installers"},
    {"first": "BJ",        "last": "Summerville",   "interest": "Advanced Manufacturing",         "career": "Hairdressers, Hairstylists, and Cosmetologists"},
    {"first": "Calvin",    "last": "Cox",           "interest": "Management & Entrepreneurship",  "career": "Sales Representatives"},
    {"first": "Cameron",   "last": "Vannor II",     "interest": "Arts, Entertainment, & Design",  "career": "Video Game Designers"},
    {"first": "Ce'Ana",    "last": "Glasspie",      "interest": "Energy & Natural Resources",     "career": "Aerospace Engineering and Operations Technicians"},
    {"first": "Ce'Asia",   "last": "Glasspie",      "interest": "Arts, Entertainment, & Design",  "career": "Wind Energy Engineers"},
    {"first": "Chance",    "last": "Hobbs",         "interest": "Healthcare & Human Services",    "career": "Biochemists and Biophysicists"},
    {"first": "Christopher","last": "Watt",         "interest": "Agriculture",                    "career": "Agents and Business Managers of Artists"},
    {"first": "Coreyona",  "last": "Jenkins",       "interest": "Hospitality, Events, & Tourism", "career": "Funeral Home Managers"},
    {"first": "Danaja",    "last": "Ellis",         "interest": "Hospitality, Events, & Tourism", "career": "Travel Guides"},
    {"first": "Daonte",    "last": "Matthews",      "interest": "Construction",                   "career": "Home Health Aides"},
    {"first": "Daryl",     "last": "Mclaurin",      "interest": "Arts, Entertainment, & Design",  "career": "Costume Attendants"},
    {"first": "David",     "last": "Botkin",        "interest": "Management & Entrepreneurship",  "career": "Supply Chain Managers"},
    {"first": "Dayona",    "last": "Matthews",      "interest": "Financial Services",             "career": "Customer Service Representatives"},
    {"first": "Deshawn",   "last": "Henry",         "interest": "Arts, Entertainment, & Design",  "career": "Art Directors"},
    {"first": "Devonte",   "last": "Parker",        "interest": "Healthcare & Human Services",    "career": "Elementary School Teachers"},
    {"first": "Ivyonna",   "last": "Tolliver",      "interest": "Financial Services",             "career": "Reservation and Transportation Ticket Agents"},
    {"first": "Jamar",     "last": "Mitchell",      "interest": "Financial Services",             "career": "Travel Agents"},
    {"first": "Jasmine",   "last": "Grimaldo",      "interest": "Agriculture",                    "career": "Agents and Business Managers of Artists"},
    {"first": "Jaykyra",   "last": "Brown",         "interest": "Arts, Entertainment, & Design",  "career": "Zoologists and Wildlife Biologists"},
    {"first": "Jayla",     "last": "Lewis-Lomax",   "interest": "Agriculture",                    "career": "Massage Therapists"},
    {"first": "Joshawn",   "last": "Henry",         "interest": "Advanced Manufacturing",         "career": "Cargo and Freight Agents"},
    {"first": "Joshua",    "last": "Rollins",       "interest": "Advanced Manufacturing",         "career": "Brokerage Clerks"},
    {"first": "Jovan",     "last": "Watson",        "interest": "Supply Chain & Transportation",  "career": "First-Line Supervisors"},
    {"first": "Kamar",     "last": "Clark",         "interest": "Public Service & Safety",        "career": "Patternmakers, Metal and Plastic"},
    {"first": "Khai",      "last": "Vannor",        "interest": "Supply Chain & Transportation",  "career": "HVAC Mechanics and Installers"},
    {"first": "Laniya",    "last": "Young",         "interest": "Supply Chain & Transportation",  "career": "Writers and Authors"},
    {"first": "Louis",     "last": "Bailey",        "interest": "Public Service & Safety",        "career": "Dispatchers"},
    {"first": "Malachi",   "last": "Sottile",       "interest": "Energy & Natural Resources",     "career": "Writers and Authors"},
    {"first": "Micah",     "last": "Botkin",        "interest": "Supply Chain & Transportation",  "career": "Sales Representatives"},
    {"first": "Michelle",  "last": "Mendez",        "interest": "Arts, Entertainment, & Design",  "career": "Writers and Authors"},
    {"first": "Myshawn",   "last": "Fuller",        "interest": "Supply Chain & Transportation",  "career": "Recycling Coordinators"},
    {"first": "Mytesha",   "last": "Davis",         "interest": "Supply Chain & Transportation",  "career": "Sales Representatives"},
    {"first": "Precise",   "last": "Hope",          "interest": "Arts, Entertainment, & Design",  "career": "Set and Exhibit Designers"},
    {"first": "Raeon",     "last": "Matthews",      "interest": "Education",                      "career": "Public Relations Specialists"},
    {"first": "Reginald",  "last": "Coleman",       "interest": "Healthcare & Human Services",    "career": "Skincare Specialists"},
    {"first": "Sydni",     "last": "Vickers",       "interest": "Education",                      "career": "Sales Representatives"},
    {"first": "Taniya",    "last": "Powell",        "interest": "Healthcare & Human Services",    "career": "Tutors"},
    {"first": "Tiyanna",   "last": "Williams",      "interest": "Hospitality, Events, & Tourism", "career": "Residential Advisors"},
    {"first": "Trenton",   "last": "Able",          "interest": "Financial Services",             "career": "Real Estate Brokers"},
    {"first": "Twanaya",   "last": "Russell",       "interest": "Arts, Entertainment, & Design",  "career": "Set and Exhibit Designers"},
    {"first": "Zion",      "last": "Surratt",       "interest": "Arts, Entertainment, & Design",  "career": "Writers and Authors"},
    {"first": "Zyaire",    "last": "Hill",          "interest": "Digital Technology",             "career": "Flight Attendants"},
    {"first": "Chance",    "last": "Smith",         "interest": "Education",                      "career": "Personal Care Aides"},
    {"first": "Evan",      "last": "Matthews",      "interest": "Advanced Manufacturing",         "career": "Massage Therapists"},
    {"first": "Ky",        "last": "Smith",         "interest": "Healthcare & Human Services",    "career": "Makeup Artists, Theatrical and Performance"},
]

MASLOW_LEVELS = [
    {
        "id": 1,
        "level": "Foundation",
        "maslow": "Physiological & Safety",
        "icon": "🏠",
        "color": "#C8A96E",
        "desc": "Your basic needs — stability, safety, belonging. These form the ground you stand on.",
        "questions": [
            "I have people in my life who support me.",
            "I feel safe at school and at home.",
            "I have what I need to focus on learning.",
        ],
    },
    {
        "id": 2,
        "level": "Community",
        "maslow": "Love & Belonging",
        "icon": "🤝",
        "color": "#7B9E87",
        "desc": "Your people. Ubuntu — 'I am because we are.' Your community is part of who you are.",
        "questions": [
            "I feel like I belong where I am.",
            "I have people who believe in me.",
            "I take pride in my roots and where I come from.",
        ],
    },
    {
        "id": 3,
        "level": "Self-Regard",
        "maslow": "Esteem",
        "icon": "⭐",
        "color": "#5B8DB8",
        "desc": "How you see your worth — not from others' approval, but from knowing who you are.",
        "questions": [
            "My life matters and I have something important to offer.",
            "I am valuable because of who I am, not just what I do.",
            "No one can take away my sense of self.",
            "I believe in my ability to shape my own future.",
        ],
    },
    {
        "id": 4,
        "level": "Purpose",
        "maslow": "Self-Actualization",
        "icon": "🌟",
        "color": "#8B5E9B",
        "desc": "Your calling. You were born to make a positive difference. What does that look like for you?",
        "questions": [
            "I have a sense of what kind of future I want.",
            "I feel excited about at least one thing I could do in the world.",
            "I believe I was born to make a positive difference.",
        ],
    },
]

INTEREST_AREAS = [
    "Agriculture", "Advanced Manufacturing", "Arts, Entertainment, & Design",
    "Construction", "Digital Technology", "Education",
    "Energy & Natural Resources", "Financial Services",
    "Healthcare & Human Services", "Hospitality, Events, & Tourism",
    "Management & Entrepreneurship", "Marketing & Sales",
    "Public Service & Safety", "Supply Chain & Transportation",
]

INTEREST_COLORS = {
    "Arts, Entertainment, & Design":   "#C27BAD",
    "Supply Chain & Transportation":   "#5B8DB8",
    "Healthcare & Human Services":     "#7B9E87",
    "Financial Services":              "#C8A96E",
    "Advanced Manufacturing":          "#B0714E",
    "Management & Entrepreneurship":   "#8B5E9B",
    "Education":                       "#4E9B9B",
    "Hospitality, Events, & Tourism":  "#D4856A",
    "Agriculture":                     "#6B9B6B",
    "Energy & Natural Resources":      "#B8A84E",
    "Public Service & Safety":         "#7B85B8",
    "Marketing & Sales":               "#B85E8B",
    "Construction":                    "#9B7B4E",
    "Digital Technology":              "#4E8BB8",
}

# ─── SESSION STATE INIT ───────────────────────────────────────────────────────

def init_state():
    defaults = {
        "mode": "student",          # student | counselor
        "step": "intro",            # intro | maslow | interests | affirm | results
        "student_name": "",
        "maslow_step": 0,
        "responses": {},            # {level_idx: [q1_score, q2_score, ...]}
        "selected_interests": [],
        "affirm": "",
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

# ─── HELPERS ──────────────────────────────────────────────────────────────────

def maslow_score(level_idx):
    scores = st.session_state.responses.get(level_idx, [])
    if not scores:
        return 0
    max_score = len(MASLOW_LEVELS[level_idx]["questions"]) * 5
    return round((sum(scores) / max_score) * 100)

def dominant_level():
    best_idx = max(range(4), key=lambda i: maslow_score(i))
    return MASLOW_LEVELS[best_idx]

def progress_bar_html(pct, color):
    return f"""
    <div style="height:6px;background:#1A1916;border-radius:3px;margin-top:4px;">
      <div style="height:100%;width:{pct}%;background:{color};border-radius:3px;"></div>
    </div>"""

def badge_html(text, color):
    return f'<span style="display:inline-block;padding:3px 12px;background:{color}22;color:{color};border:1px solid {color}55;font-size:0.82rem;margin:3px;">{text}</span>'

def reset():
    for k in ["step","student_name","maslow_step","responses","selected_interests","affirm"]:
        del st.session_state[k]
    init_state()

# ─── MODE TOGGLE ─────────────────────────────────────────────────────────────

col_left, col_right = st.columns([5, 1])
with col_right:
    mode_choice = st.radio(
        "", ["Student", "Counselor"],
        index=0 if st.session_state.mode == "student" else 1,
        horizontal=True, label_visibility="collapsed", key="mode_toggle"
    )
    st.session_state.mode = mode_choice.lower()

# ═══════════════════════════════════════════════════════════════════════════════
# STUDENT VIEW
# ═══════════════════════════════════════════════════════════════════════════════

if st.session_state.mode == "student":

    # ── INTRO ──────────────────────────────────────────────────────────────────
    if st.session_state.step == "intro":
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown('<div style="text-align:center;font-size:2.8rem;">✦</div>', unsafe_allow_html=True)
        st.markdown('<h1 style="text-align:center;font-weight:400;font-size:3rem;letter-spacing:-0.02em;margin-bottom:0.5rem;">NextChapter</h1>', unsafe_allow_html=True)
        st.markdown('<p style="text-align:center;color:#A09D95;font-size:1.1rem;">A self-discovery journey for Rise Academy students.</p>', unsafe_allow_html=True)
        st.markdown('<p style="text-align:center;color:#7A7770;font-style:italic;font-size:0.95rem;margin-bottom:2.5rem;">"Umuntu ngumuntu ngabantu" — you are who you are because of others.<br>But you also carry something unique. Let\'s find it.</p>', unsafe_allow_html=True)

        _, col, _ = st.columns([2, 2, 2])
        with col:
            if st.button("BEGIN →"):
                st.session_state.step = "name"
                st.rerun()

    # ── NAME ───────────────────────────────────────────────────────────────────
    elif st.session_state.step == "name":
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<p style="color:#7A7770;letter-spacing:0.1em;font-size:0.78rem;text-transform:uppercase;">Step 1 of 4</p>', unsafe_allow_html=True)
        st.markdown('<h2 style="font-weight:400;font-size:2rem;margin-bottom:1.5rem;">What do we call you?</h2>', unsafe_allow_html=True)

        name_input = st.text_input("", placeholder="Your first name", label_visibility="collapsed", key="name_input")

        _, col, _ = st.columns([1, 2, 1])
        with col:
            if st.button("CONTINUE →"):
                if name_input.strip():
                    st.session_state.student_name = name_input.strip()
                    st.session_state.step = "maslow"
                    st.rerun()
                else:
                    st.warning("Please enter your name to continue.")

    # ── MASLOW ASSESSMENT ──────────────────────────────────────────────────────
    elif st.session_state.step == "maslow":
        idx = st.session_state.maslow_step
        level = MASLOW_LEVELS[idx]

        # Progress dots
        dots = " ".join([
            f'<span style="display:inline-block;width:32px;height:3px;background:{MASLOW_LEVELS[i]["color"] if i <= idx else "#2A2820"};margin:0 2px;"></span>'
            for i in range(4)
        ])
        st.markdown(f'<div style="margin-bottom:1.5rem;">{dots}</div>', unsafe_allow_html=True)

        st.markdown(f'<p style="color:#7A7770;font-size:0.75rem;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:0;">Level {level["id"]} · {level["maslow"]}</p>', unsafe_allow_html=True)
        st.markdown(f'<h2 style="font-weight:400;color:{level["color"]};font-size:2rem;margin-top:0.2rem;">{level["icon"]} {level["level"]}</h2>', unsafe_allow_html=True)
        st.markdown(f'<p style="color:#A09D95;font-style:italic;font-size:0.95rem;margin-bottom:2rem;">{level["desc"]}</p>', unsafe_allow_html=True)

        st.markdown('<p style="color:#7A7770;font-size:0.78rem;letter-spacing:0.08em;">Rate each statement: 1 = Not at all &nbsp;·&nbsp; 5 = Very much</p>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

        scores = []
        all_answered = True
        for q_idx, question in enumerate(level["questions"]):
            st.markdown(f'<p style="color:#D5D0C8;font-size:1rem;margin-bottom:0.3rem;">{question}</p>', unsafe_allow_html=True)
            val = st.select_slider(
                f"q_{idx}_{q_idx}",
                options=[1, 2, 3, 4, 5],
                value=st.session_state.responses.get(idx, [3] * len(level["questions"]))[q_idx]
                      if idx in st.session_state.responses else 3,
                label_visibility="collapsed",
                key=f"slider_{idx}_{q_idx}"
            )
            scores.append(val)
            st.markdown("<br>", unsafe_allow_html=True)

        # Save scores live
        st.session_state.responses[idx] = scores

        _, col, _ = st.columns([1, 2, 1])
        with col:
            label = "NEXT LEVEL →" if idx < 3 else "CONTINUE →"
            if st.button(label):
                if idx < 3:
                    st.session_state.maslow_step += 1
                else:
                    st.session_state.step = "interests"
                st.rerun()

    # ── INTERESTS ──────────────────────────────────────────────────────────────
    elif st.session_state.step == "interests":
        st.markdown('<p style="color:#7A7770;letter-spacing:0.1em;font-size:0.78rem;text-transform:uppercase;">Step 3 of 4</p>', unsafe_allow_html=True)
        st.markdown('<h2 style="font-weight:400;font-size:2rem;margin-bottom:0.5rem;">What pulls you in?</h2>', unsafe_allow_html=True)
        st.markdown('<p style="color:#7A7770;font-size:0.9rem;margin-bottom:1.5rem;">Pick up to 3 interest areas that feel most like you.</p>', unsafe_allow_html=True)

        selected = st.multiselect(
            "",
            options=INTEREST_AREAS,
            default=st.session_state.selected_interests,
            max_selections=3,
            label_visibility="collapsed",
            key="interest_select"
        )
        st.session_state.selected_interests = selected

        # Color badges preview
        if selected:
            badges = " ".join([badge_html(a, INTEREST_COLORS.get(a, "#C8A96E")) for a in selected])
            st.markdown(f'<div style="margin:1rem 0;">{badges}</div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        _, col, _ = st.columns([1, 2, 1])
        with col:
            if st.button("CONTINUE →"):
                if selected:
                    st.session_state.step = "affirm"
                    st.rerun()
                else:
                    st.warning("Select at least one interest area.")

    # ── AFFIRMATION ────────────────────────────────────────────────────────────
    elif st.session_state.step == "affirm":
        st.markdown('<p style="color:#7A7770;letter-spacing:0.1em;font-size:0.78rem;text-transform:uppercase;">Final Step</p>', unsafe_allow_html=True)
        st.markdown('<h2 style="font-weight:400;font-size:2rem;margin-bottom:0.75rem;">Complete this sentence.</h2>', unsafe_allow_html=True)
        st.markdown('<p style="color:#7A7770;font-style:italic;font-size:1rem;margin-bottom:1.5rem;">"I was born to make a positive difference by..."</p>', unsafe_allow_html=True)

        affirm_text = st.text_area(
            "",
            value=st.session_state.affirm,
            placeholder="helping people, creating things, leading, protecting my community...",
            height=100,
            label_visibility="collapsed",
            key="affirm_input"
        )
        st.session_state.affirm = affirm_text

        st.markdown("<br>", unsafe_allow_html=True)
        _, col, _ = st.columns([1, 2, 1])
        with col:
            if st.button("SEE MY RESULTS →"):
                if affirm_text.strip():
                    st.session_state.step = "results"
                    st.rerun()
                else:
                    st.warning("Complete the sentence to continue.")

    # ── RESULTS ────────────────────────────────────────────────────────────────
    elif st.session_state.step == "results":
        name = st.session_state.student_name
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f'<div style="text-align:center;font-size:2.2rem;margin-bottom:0.5rem;">✦</div>', unsafe_allow_html=True)
        st.markdown(f'<h2 style="text-align:center;font-weight:400;font-size:2.4rem;">{name}\'s NextChapter</h2>', unsafe_allow_html=True)
        st.markdown('<p style="text-align:center;color:#7A7770;font-style:italic;margin-bottom:2.5rem;">"I am the leader of my destiny."</p>', unsafe_allow_html=True)

        st.markdown("---")

        # Needs landscape
        st.markdown('<p style="color:#5A5850;font-size:0.72rem;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:1rem;">Your Needs Landscape</p>', unsafe_allow_html=True)

        for level in reversed(MASLOW_LEVELS):
            score = maslow_score(level["id"] - 1)
            bar = progress_bar_html(score, level["color"])
            st.markdown(f"""
            <div style="margin-bottom:1rem;">
              <div style="display:flex;justify-content:space-between;">
                <span style="color:#D5D0C8;font-size:0.9rem;">{level['icon']} {level['level']}</span>
                <span style="color:{level['color']};font-weight:600;font-size:0.9rem;">{score}%</span>
              </div>
              {bar}
            </div>""", unsafe_allow_html=True)

        st.markdown("---")

        # Interests
        st.markdown('<p style="color:#5A5850;font-size:0.72rem;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:0.75rem;">Your Interest Areas</p>', unsafe_allow_html=True)
        badges = " ".join([badge_html(a, INTEREST_COLORS.get(a, "#C8A96E")) for a in st.session_state.selected_interests])
        st.markdown(f'<div style="margin-bottom:1.5rem;">{badges}</div>', unsafe_allow_html=True)

        st.markdown("---")

        # Purpose statement
        affirm = st.session_state.affirm.strip().rstrip(".")
        st.markdown(f"""
        <div style="border-left:3px solid #C8A96E;padding-left:1.5rem;margin-bottom:2rem;">
          <p style="color:#7A7770;font-size:0.75rem;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:0.4rem;">Your Purpose Statement</p>
          <p style="font-size:1.1rem;line-height:1.7;color:#F0EDE6;font-style:italic;">
            "I was born to make a positive difference by {affirm.lower()}."
          </p>
        </div>""", unsafe_allow_html=True)

        # Dominant strength
        dom = dominant_level()
        st.markdown(f"""
        <div style="background:#1A1916;padding:1.5rem;border-top:3px solid {dom['color']};margin-bottom:2rem;">
          <p style="color:{dom['color']};font-size:0.72rem;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:0.4rem;">Your Strongest Foundation</p>
          <h4 style="font-weight:400;font-size:1.3rem;margin-bottom:0.4rem;">{dom['icon']} {dom['level']}</h4>
          <p style="color:#A09D95;font-size:0.9rem;line-height:1.6;margin:0;">{dom['desc']}</p>
        </div>""", unsafe_allow_html=True)

        _, col, _ = st.columns([2, 1, 2])
        with col:
            if st.button("Start Over"):
                reset()
                st.rerun()

# ═══════════════════════════════════════════════════════════════════════════════
# COUNSELOR DASHBOARD
# ═══════════════════════════════════════════════════════════════════════════════

else:
    df = pd.DataFrame(STUDENTS)
    df["name"] = df["first"] + " " + df["last"]

    # Header
    col1, col2 = st.columns([5, 1])
    with col1:
        st.markdown('<p style="color:#5A5850;font-size:0.7rem;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:0;">NextChapter · Counselor View</p>', unsafe_allow_html=True)
        st.markdown('<h2 style="font-weight:400;font-size:1.5rem;margin-top:0.1rem;">Rise Academy · Post-Secondary Pathways</h2>', unsafe_allow_html=True)
    with col2:
        st.metric("Students", len(df))

    st.markdown("---")

    # Interest distribution chart
    st.markdown('<p style="color:#5A5850;font-size:0.72rem;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:1rem;">Interest Area Distribution</p>', unsafe_allow_html=True)

    counts = df["interest"].value_counts().reset_index()
    counts.columns = ["interest", "count"]
    max_count = counts["count"].max()

    for _, row in counts.iterrows():
        color = INTEREST_COLORS.get(row["interest"], "#C8A96E")
        pct = (row["count"] / max_count) * 100
        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:1rem;margin-bottom:0.5rem;">
          <div style="width:210px;text-align:right;font-size:0.78rem;color:#A09D95;flex-shrink:0;">{row['interest']}</div>
          <div style="flex:1;height:18px;background:#1A1916;position:relative;">
            <div style="height:100%;width:{pct}%;background:{color}55;border-right:2px solid {color};"></div>
          </div>
          <div style="width:24px;font-size:0.85rem;font-weight:600;color:{color};flex-shrink:0;">{row['count']}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ASRS research callout
    st.markdown("""
    <div style="background:#15140F;border:1px solid #2A2820;border-left:3px solid #8B5E9B;padding:1.25rem 1.5rem;margin-bottom:2rem;">
      <p style="color:#8B5E9B;font-size:0.7rem;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:0.4rem;">
        Framework Note · Lateef &amp; Boahen-Boaten (2024)
      </p>
      <p style="color:#A09D95;font-size:0.88rem;line-height:1.7;margin:0;">
        Afrocentric self-regard (ASRS) correlates significantly with career aspirations
        (<em>r</em> = .49, <em>p</em> &lt; .01) and flourishing (<em>r</em> = .60, <em>p</em> &lt; .01)
        among Black emerging adults. Students' interest data should be read alongside
        self-regard indicators — high interest alignment with low self-regard scores signals
        a counseling priority. Ubuntu-centered interventions that reinforce community
        belonging strengthen both wellbeing and career trajectory.
      </p>
    </div>""", unsafe_allow_html=True)

    st.markdown("---")

    # Roster filters
    st.markdown('<p style="color:#5A5850;font-size:0.72rem;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:0.75rem;">Student Roster</p>', unsafe_allow_html=True)

    col_search, col_filter = st.columns([2, 2])
    with col_search:
        search = st.text_input("", placeholder="Search by name or career...", label_visibility="collapsed", key="search")
    with col_filter:
        interest_filter = st.selectbox("", ["All Interests"] + INTEREST_AREAS, label_visibility="collapsed", key="interest_filter")

    # Apply filters
    filtered = df.copy()
    if search:
        filtered = filtered[
            filtered["name"].str.lower().str.contains(search.lower()) |
            filtered["career"].str.lower().str.contains(search.lower())
        ]
    if interest_filter != "All Interests":
        filtered = filtered[filtered["interest"] == interest_filter]

    # Style the dataframe
    display_df = filtered[["name", "interest", "career"]].rename(columns={
        "name": "Student",
        "interest": "Interest Area",
        "career": "Career Match"
    }).reset_index(drop=True)

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True,
        height=min(600, 40 + len(display_df) * 37),
    )

    if len(display_df) == 0:
        st.markdown('<p style="text-align:center;color:#4A4840;font-style:italic;padding:1rem;">No students match this filter.</p>', unsafe_allow_html=True)

    st.markdown(f'<p style="color:#5A5850;font-size:0.8rem;margin-top:0.5rem;">Showing {len(display_df)} of {len(df)} students</p>', unsafe_allow_html=True)
