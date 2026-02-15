import streamlit as st

# Custom CSS for a professional look
st.markdown(""" <style> .main { background-color: #f5f7f9; } .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; } </style> """, unsafe_lazy=True)

st.title("🚀 CareerAI: The 2026 Holland Code Assessment")
st.subheader("Discover your AI-proof career path in 5 minutes.")

# The Holland Code Questions (Simplified for MVP)
questions = [
    ("I enjoy fixing mechanical things or working with my hands.", "R"),
    ("I like solving complex math or science problems.", "I"),
    ("I enjoy sketching, drawing, or writing creatively.", "A"),
    ("I like helping people and teaching new skills.", "S"),
    ("I enjoy leading teams and persuading others.", "E"),
    ("I like organizing data and following clear systems.", "C")
]

scores = {"R": 0, "I": 0, "A": 0, "S": 0, "E": 0, "C": 0}

with st.form("assessment"):
    st.info("On a scale of 1 to 5, how much do you agree with these statements?")
    for q_text, code in questions:
        val = st.slider(q_text, 1, 5, 3)
        scores[code] += val
    
    submitted = st.form_submit_button("Generate My Career Report")

if submitted:
    # Identify top 2 traits
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top_trait = sorted_scores[0][0]
    sec_trait = sorted_scores[1][0]
    holland_code = top_trait + sec_trait

    st.success(f"### Your Holland Code is: {holland_code}")
    
    # Logic for the "Free" Result
    matches = {
        "SA": "Art Therapist or UX Researcher",
        "ES": "Customer Success Manager or Team Lead",
        "IR": "Software Engineer or Data Scientist",
        "AI": "Creative Strategist or AI Prompt Engineer",
    }
    
    result = matches.get(holland_code, "Multi-Talented Specialist")
    
    st.write(f"**Primary Career Path:** {result}")
    
    # The "Deep Dive" Upsell
    st.divider()
    st.markdown("### 🔒 Unlock Your 20-Page AI 'Deep Dive' Report")
    st.write("Get a 90-day roadmap, 2026 salary data, and AI-proof skill recommendations.")
    if st.button("Get Deep Dive Report for $10"):
        st.write("Redirecting to Stripe...") # Replace with your Stripe link

    st.sidebar.title("Partner Login")
    st.sidebar.text_input("License Key (B2B)")


# --- FOOTER SECTION ---
st.divider()
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**About CareerAI**")
    st.caption("Empowering the 2026 workforce with AI-driven psychological insights. Built on the validated Holland Code (RIASEC) framework.")

with col2:
    st.markdown("**Legal & Privacy**")
    if st.button("Privacy Policy"):
        st.info("Your data is encrypted. We do not sell individual assessment scores to third parties. Data is used solely for career matching purposes.")

with col3:
    st.markdown("**B2B & Licensing**")
    st.caption("Interested in a white-label version for your school or firm? [Contact Sales](mailto:your@email.com)")

st.markdown("<center style='color: grey; font-size: 0.8em;'>© 2026 CareerAI Technologies. All rights reserved.</center>", unsafe_allow_html=True)