import streamlit as st
from PIL import Image


def LearningDevelopment():
    image = Image.open("./logo/lyzr-logo.png")
    st.image(image, width=150)
    st.title("Learning & Development")
    st.write("**Personalized Learning Pathways:** Recommend training modules based on individual career goals and current skills.")
    st.write("**Content Creation:** Develop interactive training materials and quizzes.")
    st.write("**Knowledge Base Assistant:** Provide explanations and answers to employee questions on various topics.")
