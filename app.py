import streamlit as st
import time
import json
from datetime import datetime

# Configure page
st.set_page_config(
    page_title="PHL 201 - Test Version",
    page_icon="🏛️",
    layout="wide"
)

# Test if basic Streamlit works
st.title("🏛️ PHL 201 Philosophy Program")
st.write("If you can see this, Streamlit is working!")

# Initialize session state
if 'test_counter' not in st.session_state:
    st.session_state.test_counter = 0

# Simple test button
if st.button("Test Button"):
    st.session_state.test_counter += 1
    st.success(f"Button clicked {st.session_state.test_counter} times!")

# Sidebar test
st.sidebar.title("Navigation Test")
mode = st.sidebar.radio("Choose mode:", ["Test 1", "Test 2", "Test 3"])

if mode == "Test 1":
    st.header("Test Mode 1")
    st.write("This is a simple test to verify Streamlit functionality.")
    
elif mode == "Test 2":
    st.header("Quiz Test")
    
    question = "What is 2 + 2?"
    answer = st.radio("Select answer:", ["3", "4", "5", "6"])
    
    if answer:
        if answer == "4":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect")
            
elif mode == "Test 3":
    st.header("Content Test")
    
    st.markdown("""
    ## Sample Philosophy Content
    
    This is a test of markdown rendering and content display.
    
    ### Key Points:
    - Point 1
    - Point 2 
    - Point 3
    
    **Bold text** and *italic text* should work.
    """)

# Footer
st.markdown("---")
st.caption("Test version - if you see this, the basic app is working")
