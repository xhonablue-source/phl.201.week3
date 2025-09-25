import streamlit as st

# Minimal configuration
st.set_page_config(page_title="PHL 201", page_icon="🏛️")

# Test basic display
st.title("PHL 201 Philosophy Program")
st.write("Debug: Basic Streamlit functionality test")

# Test session state
if 'counter' not in st.session_state:
    st.session_state.counter = 0

st.write(f"Session state test: {st.session_state.counter}")

if st.button("Test Button"):
    st.session_state.counter += 1
    st.success(f"Button works! Count: {st.session_state.counter}")

# Test sidebar
st.sidebar.title("Sidebar Test")
mode = st.sidebar.selectbox("Choose:", ["Option 1", "Option 2", "Option 3"])
st.write(f"Selected: {mode}")

# Test content based on selection
if mode == "Option 1":
    st.header("Philosophy Content Test")
    st.markdown("""
    ## Plato's Cave Allegory
    
    This is a test of basic content display:
    - Point 1: Shadows represent illusions
    - Point 2: The fire represents partial truth  
    - Point 3: Sunlight represents full knowledge
    
    **Bold text** and *italic text* rendering test.
    """)
    
elif mode == "Option 2":
    st.header("Quiz Test")
    
    question = "According to Plato, what do the shadows represent?"
    answer = st.radio("Select:", [
        "Complete reality",
        "Illusions we mistake for reality", 
        "Mathematical concepts",
        "Political ideas"
    ])
    
    if answer:
        if answer == "Illusions we mistake for reality":
            st.success("✅ Correct! The shadows represent illusions.")
        else:
            st.error("❌ Incorrect. The shadows represent illusions we mistake for reality.")

elif mode == "Option 3":
    st.header("Advanced Features Test")
    
    # Progress bar test
    st.write("Progress bar test:")
    st.progress(0.7)
    
    # Columns test
    col1, col2 = st.columns(2)
    with col1:
        st.write("Column 1 content")
    with col2:
        st.write("Column 2 content")
    
    # Expander test
    with st.expander("Click to expand"):
        st.write("Hidden content revealed!")

# Footer
st.markdown("---")
st.caption("Minimal version - troubleshooting display issues")
