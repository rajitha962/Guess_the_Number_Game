import streamlit as st
import random

# Page Configuration
st.set_page_config(
    page_title="Guess the Number Game",
    page_icon="🎮",
    layout="centered"
)

# Student Name
st.markdown("## 👩‍🎓 Developed by: **Rajitha**")

# Title
st.title("🎮 Guess the Number Game")

st.write("Try to guess the secret number between **1 and 10**.")

# Generate a random number
secret = random.randint(1, 10)

# User Input
guess = st.number_input(
    "Enter your guess (1-10)",
    min_value=1,
    max_value=10,
    step=1
)

# Check Guess
if st.button("Check"):
    if guess == secret:
        st.success("🎉 Congratulations! You guessed the correct number.")
    else:
        st.error(f"❌ Wrong Guess! The correct number was **{secret}**.")

# Footer
st.markdown("---")
st.markdown("**Created by Rajitha | B.Tech 3rd Year**")