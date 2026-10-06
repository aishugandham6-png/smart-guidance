import streamlit as st
import os
from dotenv import load_dotenv

# Optional Gemini import
try:
    from google import genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Career AI",
    page_icon="🎓",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>


.stApp {
    background: linear-gradient(135deg, #eef2ff, #ffffff, #f5f3ff);
}

/* Main title */
.main-title {
    font-size: 45px;
    font-weight: bold;
    text-align: center;
    color: #000000 !important;
    margin-bottom: 5px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 20px;
    color: #000000 !important;
    margin-bottom: 30px;
}

/* All normal text */
.stApp p,
.stApp span,
.stApp label,
.stApp div {
    color: #000000;
}

/* Headings */
.stApp h1,
.stApp h2,
.stApp h3,
.stApp h4,
.stApp h5,
.stApp h6 {
    color: #000000 !important;
}

/* Sidebar text */
[data-testid="stSidebar"] {
    background-color: #ffffff;
}

[data-testid="stSidebar"] * {
    color: #000000 !important;
}

/* Cards */
.card {
    padding: 20px;
    border-radius: 15px;
    background: #ffffff;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 20px;
    color: #000000 !important;
}

.section-title {
    color: #000000 !important;
    font-size: 25px;
    font-weight: bold;
}
.stTextInput input,
.stTextArea textarea {
    color: #000000 !important;
    background-color: #ffffff !important;
}
/* Input boxes */
.stTextInput input,
.stTextArea textarea,
.stSelectbox div {
    color: #000000 !important;
}

/* Button text */
.stButton button {
    color: #000000 !important;
}

/* Metric text */
[data-testid="stMetricValue"],
[data-testid="stMetricLabel"] {
    color: #000000 !important;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# CAREER DATABASE
# --------------------------------------------------

careers = {

    "Python Developer": {
        "skills": [
            "Python",
            "OOP",
            "SQL",
            "Git",
            "Django",
            "REST API"
        ],
        "roadmap": [
            "Learn Python fundamentals",
            "Learn Object-Oriented Programming",
            "Learn SQL and databases",
            "Learn Git and GitHub",
            "Learn Django or Flask",
            "Build real-world projects",
            "Create a portfolio"
        ],
        "description":
            "Python developers build applications, APIs, automation tools and backend systems."
    },

    "Data Scientist": {
        "skills": [
            "Python",
            "Statistics",
            "Pandas",
            "NumPy",
            "Machine Learning",
            "SQL",
            "Data Visualization"
        ],
        "roadmap": [
            "Learn Python",
            "Learn NumPy and Pandas",
            "Learn statistics",
            "Learn data visualization",
            "Learn machine learning",
            "Practice with datasets",
            "Build data science projects"
        ],
        "description":
            "Data scientists analyze data and build models to discover useful insights."
    },

    "Machine Learning Engineer": {
        "skills": [
            "Python",
            "Machine Learning",
            "Deep Learning",
            "NumPy",
            "Pandas",
            "Scikit-learn",
            "TensorFlow/PyTorch"
        ],
        "roadmap": [
            "Learn Python",
            "Learn mathematics and statistics",
            "Learn machine learning",
            "Learn deep learning",
            "Learn Scikit-learn",
            "Learn PyTorch or TensorFlow",
            "Build ML projects"
        ],
        "description":
            "Machine Learning Engineers develop and deploy intelligent machine learning systems."
    },

    "Full Stack Developer": {
        "skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Python",
            "SQL",
            "Git",
            "REST API"
        ],
        "roadmap": [
            "Learn HTML",
            "Learn CSS",
            "Learn JavaScript",
            "Learn React",
            "Learn backend development",
            "Learn databases",
            "Build full-stack applications"
        ],
        "description":
            "Full Stack Developers create both frontend and backend parts of web applications."
    },

    "AI Engineer": {
        "skills": [
            "Python",
            "Machine Learning",
            "Deep Learning",
            "NLP",
            "Transformers",
            "PyTorch",
            "Generative AI"
        ],
        "roadmap": [
            "Learn Python",
            "Learn machine learning",
            "Learn deep learning",
            "Learn NLP",
            "Learn Transformers",
            "Learn Generative AI",
            "Build AI applications"
        ],
        "description":
            "AI Engineers build intelligent applications using machine learning and generative AI."
    }
}

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🎓 Welcome to Career AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Smart Guidance & Skill Recommendation System</div>',
    unsafe_allow_html=True
)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("🎓 Career AI")

page = st.sidebar.radio(
    "Choose an option",
    [
        "🏠 Home",
        "🎯 Career Recommendation",
        "🧠 Skill Gap Analysis",
        "🗺️ Learning Roadmap",
        "🤖 AI Career Assistant"
    ]
)

# --------------------------------------------------
# HOME
# --------------------------------------------------

if page == "🏠 Home":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">How It Works</div>',
        unsafe_allow_html=True
    )

    st.write("1️⃣ Enter your skills and interests.")
    st.write("2️⃣ Select a career you are interested in.")
    st.write("3️⃣ Career AI compares your skills with career requirements.")
    st.write("4️⃣ The system identifies your skill gaps.")
    st.write("5️⃣ Get a personalized learning roadmap.")

    st.markdown("</div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Career Paths", len(careers))

    with col2:
        total_skills = len(
            set(
                skill
                for career in careers.values()
                for skill in career["skills"]
            )
        )
        st.metric("Skills Covered", total_skills)

    with col3:
        st.metric("AI Powered", "Yes")

# --------------------------------------------------
# CAREER RECOMMENDATION
# --------------------------------------------------

elif page == "🎯 Career Recommendation":

    st.header("🎯 Career Recommendation")

    st.write(
        "Enter your current skills. Career AI will calculate "
        "which career matches your skills."
    )

    skill_text = st.text_area(
        "Enter your skills",
        placeholder="Example: Python, SQL, HTML, CSS, Git"
    )

    if st.button("🔍 Find Best Career"):

        if not skill_text.strip():
            st.warning("Please enter at least one skill.")

        else:

            user_skills = {
                skill.strip().lower()
                for skill in skill_text.split(",")
                if skill.strip()
            }

            results = []

            for career, data in careers.items():

                required_skills = {
                    skill.lower()
                    for skill in data["skills"]
                }

                matched = user_skills.intersection(required_skills)

                score = (
                    len(matched) /
                    len(required_skills)
                ) * 100

                results.append(
                    (
                        career,
                        round(score, 2),
                        matched
                    )
                )

            results.sort(
                key=lambda x: x[1],
                reverse=True
            )

            st.subheader("🏆 Recommended Careers")

            for career, score, matched in results:

                st.markdown(
                    f"### {career}"
                )

                st.progress(
                    int(score)
                )

                st.write(
                    f"**Match Score:** {score}%"
                )

                if matched:
                    st.write(
                        "Matched skills:",
                        ", ".join(matched)
                    )

                st.divider()

# --------------------------------------------------
# SKILL GAP ANALYSIS
# --------------------------------------------------

elif page == "🧠 Skill Gap Analysis":

    st.header("🧠 Skill Gap Analysis")

    career = st.selectbox(
        "Select your target career",
        list(careers.keys())
    )

    skill_text = st.text_area(
        "Enter your current skills",
        placeholder="Example: Python, SQL, Git"
    )

    if st.button("📊 Analyze Skill Gap"):

        if not skill_text.strip():

            st.warning("Please enter your skills.")

        else:

            user_skills = {
                skill.strip().lower()
                for skill in skill_text.split(",")
                if skill.strip()
            }

            required = careers[career]["skills"]

            missing = [
                skill
                for skill in required
                if skill.lower() not in user_skills
            ]

            matched = [
                skill
                for skill in required
                if skill.lower() in user_skills
            ]

            st.subheader("✅ Skills You Have")

            if matched:
                for skill in matched:
                    st.success(skill)
            else:
                st.info("No matching skills found.")

            st.subheader("📚 Skills You Need")

            if missing:
                for skill in missing:
                    st.warning(skill)
            else:
                st.success(
                    "🎉 You have all the required skills!"
                )

# --------------------------------------------------
# LEARNING ROADMAP
# --------------------------------------------------

elif page == "🗺️ Learning Roadmap":

    st.header("🗺️ Personalized Learning Roadmap")

    career = st.selectbox(
        "Choose your career",
        list(careers.keys())
    )

    data = careers[career]

    st.subheader(f"🚀 Roadmap for {career}")

    for i, step in enumerate(
        data["roadmap"],
        start=1
    ):

        st.write(
            f"### Step {i}: {step}"
        )

        if i < len(data["roadmap"]):
            st.write("↓")

    st.info(
        data["description"]
    )

# --------------------------------------------------
# AI CAREER ASSISTANT
# --------------------------------------------------

elif page == "🤖 AI Career Assistant":

    st.header("🤖 AI Career Assistant")

    st.write(
        "Ask questions about careers, skills, projects, "
        "learning paths or interviews."
    )

    question = st.text_area(
        "Ask your question",
        placeholder="Example: What skills should I learn to become an AI Engineer?"
    )

    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")

    if st.button("🤖 Ask AI"):

        if not question.strip():

            st.warning("Please enter a question.")

        elif not GEMINI_AVAILABLE:

            st.error(
                "Google GenAI package is not installed."
            )

        elif not api_key:

            st.warning(
                "GEMINI_API_KEY is not configured."
            )

            st.info(
                "Create a .env file and add your Gemini API key."
            )

        else:

            try:

                client = genai.Client(
                    api_key=api_key
                )

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=question
                )

                st.subheader("💡 AI Response")

                st.write(
                    response.text
                )

            except Exception as e:

                st.error(
                    f"AI Error: {e}"
                )