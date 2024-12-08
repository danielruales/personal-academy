import streamlit as st
import sys
import warnings
import os
from personal_academy.src.personal_academy.crew import PersonalAcademy

# __import__('pysqlite3')
# import sys
# sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
# import sqlite3

# Suppress warnings
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Title of the app
st.title("Personal Academy")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page:", ["Home", "Course Outline", "Course Content", "Homework", "Quizzes"])

# Initialize session state to store results if it doesn't exist
if 'crew_result' not in st.session_state:
    st.session_state.crew_result = None

# Function to run the crew
def run_crew(topic, background):
    inputs = {
        'topic': topic,
        'experience': background
    }
    try:
        result = PersonalAcademy().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        st.error(f"An error occurred while running the crew: {e}")
        return None

# Home Page
if page == "Home":
    # Input fields for user to provide their topic and background
    topic = st.text_input("Enter the topic you want to learn about:", "")
    background = st.text_area("Enter your background or experience:", "")

    # Button to submit the inputs
    if st.button("Submit"):
        if topic and background:
            # Display the inputs
            st.success("Inputs received!")
            st.write(f"**Topic:** {topic}")
            st.write(f"**Background:** {background}")

            # Run the crew and display results
            result = run_crew(topic, background)
            if result:
                st.write("Crew execution completed successfully!")
                st.write(result)  # Display the result of the crew execution
        else:
            st.error("Please fill in both fields.")

# Course Outline Page
elif page == "Course Outline":
    st.header("Course Outline")
    st.write("This page will display the course outline based on the topic and background provided.")
    
    # Path to the outline Markdown file
    outline_file_path = os.path.join("outputs", "outline.md")
    
    # Check if the outline file exists
    if os.path.exists(outline_file_path):
        with open(outline_file_path, "r") as file:
            content = file.read()
            st.markdown(content)  # Render the Markdown content
    else:
        st.write("Outline file not found. Please ensure the file exists in the outputs directory.")


# Course Content Page
elif page == "Course Content":
    st.header("Course Content")
    st.write("This page will display the course content based on the topic and background provided.")
    
   # Path to the outline Markdown file
    course_content_file_path = os.path.join("outputs", "course_content.md")
    
    # Check if the outline file exists
    if os.path.exists(course_content_file_path):
        with open(course_content_file_path, "r") as file:
            content = file.read()
            st.markdown(content)  # Render the Markdown content
    else:
        st.write("Course content file not found. Please ensure the file exists in the outputs directory.")

# Homework Page
elif page == "Homework":
    st.header("Homework")
    st.write("This page will display the homework assignments based on the topic and background provided.")
    
    # Path to the outline Markdown file
    homework_file_path = os.path.join("outputs", "homework.md")
    
    # Check if the outline file exists
    if os.path.exists(homework_file_path):
        with open(homework_file_path, "r") as file:
            content = file.read()
            st.markdown(content)  # Render the Markdown content
    else:
        st.write("Homework file not found. Please ensure the file exists in the outputs directory.")

# Quizzes Page
elif page == "Quizzes":
    st.header("Quizzes")
    st.write("This page will display quizzes based on the topic and background provided.")

    # Path to the outline Markdown file
    quiz_file_path = os.path.join("outputs", "quiz.md")
    
    # Check if the outline file exists
    if os.path.exists(quiz_file_path):
        with open(quiz_file_path, "r") as file:
            content = file.read()
            st.markdown(content)  # Render the Markdown content
    else:
        st.write("Quiz file not found. Please ensure the file exists in the outputs directory.")

# Optional: Add more functionality or instructions
st.sidebar.markdown("""
### Instructions:
1. Use the sidebar to navigate between different sections of the app.
2. Enter the topic and background on the Home page to run the crew.
""")