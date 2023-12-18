import streamlit as st

# Configure site title and header
st.set_page_config(page_title="Harvard University", layout="wide")
st.title("Crimson Dreams Come True at Harvard")
st.subheader("Unlocking potential, shaping leaders.")

# Navigation bar
menu = st.sidebar.radio("Explore Harvard:", ["About Us", "Academics", "Campus Life", "Admissions", "Connect"])

# Content based on selected menu item
if menu == "About Us":
    # Mission & Vision
    st.write("**Mission:** To educate generations of scholars and leaders who make a difference in the world.")
    st.write("**Vision:** To be a university where curiosity thrives, ideas flourish, and knowledge sparks action.")
    # History & Legacy
    st.write("Founded in 1636, Harvard is the oldest university in the U.S., steeped in rich history and tradition.")
    st.image("naturepic.png", caption="Harvard Yard, the iconic heart of campus.")
    # Faculty & Nobel Laureates
    st.write("Home to 21 Nobel laureates and some of the world's leading scholars, Harvard offers unique learning opportunities.")
    

elif menu == "Academics":
    # Degree Programs
    st.write("Dive into diverse academic fields across 13 schools, including Harvard College, Law School, and Medical School.")
    st.dataframe(data=[
        {"School": "Harvard College", "Highlights": "Humanities, social sciences, natural sciences, arts"},
        {"School": "Law School", "Highlights": "JD, LLM, SJD programs, renowned legal scholars"},
        {"School": "Medical School", "Highlights": "MD, PhD programs, cutting-edge medical research"},
    ])
    # Undergraduate Research & Fellowships
    st.write("Get involved in groundbreaking research alongside professors, with opportunities for grants and fellowships.")
    st.image("naturepic.png", caption="Undergraduate students contributing to real-world research.")

elif menu == "Campus Life":
    # Houses & Residential Life
    st.write("Experience the vibrant community spirit in Harvard's 12 residential Houses, each with its unique traditions.")
    
    # Student Activities & Clubs
    st.write("Engage in over 450 student organizations, from a cappella groups to robotics clubs, finding your passion.")
    

elif menu == "Admissions":
    # Application Process & Deadlines
    st.write("Learn about the holistic admissions process, with deadlines for early and regular action applications.")
    
    # Student Testimonials & Tips
    st.write("Hear from admitted students about their journeys and helpful application tips.")
    

elif menu == "Connect":
    # Virtual Tour & Information Session
    st.write("Take a virtual tour of campus and attend an online information session to learn more about Harvard.")
    # Contact Admissions & Financial Aid
    st.write("Reach out to the admissions office or learn about financial aid options and scholarships.")
    

# Additional interactive elements (optional)
# st.image("harvard_crimson_logo.png")
# st.write("Follow us on Instagram: @harvarduniversity")

# Footer with copyright information
st.write("<small>Copyright © 2023 Presidents and Fellows of Harvard College</small>", unsafe_allow_html=True)

