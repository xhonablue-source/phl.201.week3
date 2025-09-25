"""
PHL 201 Enhanced Philosophy Program - Ancient Philosophy & Human Nature
Interactive Philosophy Lesson - Xavier Honablue, M.Ed.

Enhanced with comprehensive content on Plato's Forms, Human Nature theories,
and Aristotelian philosophy with expanded 80-question assessment.
"""

import streamlit as st
import time
import json
import random
from datetime import datetime
from typing import List, Dict, Optional

# Configure page
st.set_page_config(
    page_title="PHL 201 - Ancient Philosophy & Human Nature",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'current_slide' not in st.session_state:
    st.session_state.current_slide = 0
if 'timer_active' not in st.session_state:
    st.session_state.timer_active = False
if 'timer_end' not in st.session_state:
    st.session_state.timer_end = None
if 'student_responses' not in st.session_state:
    st.session_state.student_responses = {}
if 'quiz_attempts' not in st.session_state:
    st.session_state.quiz_attempts = {}
if 'comprehensive_quiz_results' not in st.session_state:
    st.session_state.comprehensive_quiz_results = []

# Enhanced slide data incorporating text content
SLIDES = [
    {
        "id": "welcome",
        "title": "Ancient Philosophy & Human Nature",
        "content": """
        # 🏛️ Ancient Philosophy & Human Nature
        
        ## PHL 201 — Enhanced Course Module
        **Professor Xavier Honablue, M.Ed.**
        
        ### Core Themes:
        - **Plato's Theory of Forms** - The world beyond appearances
        - **Human Nature Theories** - What makes us human?
        - **The Cave Allegory** - Philosophical enlightenment
        - **Aristotelian Responses** - Material vs. immaterial soul
        - **Traditional Western Views** - Rationalism & religious perspectives
        
        ### Learning Objectives:
        - Distinguish between appearance and reality in Platonic metaphysics
        - Analyze competing theories of human nature (rationalist, materialist, religious)
        - Evaluate the immaterial soul thesis and its critics
        - Connect ancient philosophy to contemporary questions
        - Practice philosophical argumentation and critical thinking
        """,
        "presenter_notes": "Emphasize that philosophy deals with fundamental questions that remain relevant today."
    },
    {
        "id": "plato_forms_theory",
        "title": "Plato's Theory of Forms",
        "content": """
        # 🌟 Plato's Theory of Forms: Two Worlds
        
        ## The Fundamental Distinction
        
        ### World of Appearances (Sensible Realm)
        - **Characteristics:** Always changing, imperfect, accessible through senses
        - **Examples:** This particular chair, that specific horse, individual acts of justice
        - **Epistemic Status:** Opinion (doxa) - unreliable knowledge
        - **Problem:** We mistake copies for reality
        
        ### World of Forms (Intelligible Realm)  
        - **Characteristics:** Eternal, unchanging, perfect, accessible through reason
        - **Examples:** The Form of Chair, Horse, Justice, Beauty, Good
        - **Epistemic Status:** Knowledge (episteme) - reliable truth
        - **Reality:** More real than physical world
        
        ## Key Insight: Participation Theory
        **All material objects "participate in" or are imperfect copies of perfect Forms.**
        
        > "The physical things we see in the world around us, for example, are always imperfect and constantly changing copies or likenesses of those perfect ideals, while the perfect ideals themselves are always the same."
        
        ## The Form of the Good
        - **Ultimate Form:** Source of all truth and knowledge
        - **Metaphor:** Like the sun illuminating physical world
        - **Function:** Makes other Forms knowable to reason
        """,
        "presenter_notes": "Use concrete examples. The perfect triangle exists as a Form even though we can only draw imperfect triangles."
    },
    {
        "id": "cave_allegory_detailed",
        "title": "The Cave Allegory: A Complete Analysis",
        "content": """
        # 🕳️ Plato's Cave Allegory: Levels of Reality
        
        ## The Allegory Decoded
        
        | Element | Symbolizes | Philosophical Meaning |
        |---------|------------|---------------------|
        | **Cave** | Physical world | Realm of appearances and illusion |
        | **Prisoners** | Ordinary people | Those who mistake sensory experience for reality |
        | **Chains** | Ignorance/prejudice | What prevents us from seeing truth |
        | **Shadows** | Sensory objects | Imperfect copies we take for reality |
        | **Fire** | Physical sun | Source of illumination in material world |
        | **Real objects** | Mathematical/moral concepts | Higher forms of knowledge |
        | **Outside world** | Realm of Forms | True reality beyond physical |
        | **Sun** | Form of the Good | Ultimate source of truth and knowledge |
        | **Escaped prisoner** | Philosopher | One who achieves enlightenment |
        | **Return journey** | Teaching duty | Philosopher's obligation to educate others |
        
        ## Four Levels of Knowledge (Divided Line)
        
        **Level 1: Images (Eikasia)** - Shadows, reflections, illusions  
        **Level 2: Physical Objects (Pistis)** - Actual material things  
        **Level 3: Mathematical Objects (Dianoia)** - Geometry, logic, reasoning  
        **Level 4: The Forms (Noesis)** - Pure knowledge through philosophical dialectic  
        
        ## Why Do People Reject Truth?
        - **Comfort of familiar illusions** - Truth can be painful and disruptive
        - **Social pressure** - Others prefer their illusions
        - **Difficulty of learning** - Philosophical education requires effort
        - **Fear of change** - New knowledge transforms how we see everything
        """,
        "presenter_notes": "Connect to modern examples: social media echo chambers, confirmation bias, resistance to scientific facts."
    },
    {
        "id": "human_nature_overview",
        "title": "What Makes Us Human? Competing Theories",
        "content": """
        # 🧠 Theories of Human Nature
        
        ## Why Does Your View Matter?
        
        Your theory of human nature profoundly affects:
        - **Relationships** - Do you trust others or assume self-interest?
        - **Politics** - What kind of government do humans need?
        - **Ethics** - Are we naturally good, evil, or neutral?
        - **Education** - How should we develop human potential?
        - **Personal identity** - What makes you "you"?
        
        ## Three Major Western Approaches
        
        ### 1. Rationalist View (Plato)
        - **Core claim:** Humans are essentially rational souls
        - **Key features:** Reason should rule over appetite and emotion
        - **Immortality:** Soul survives bodily death
        - **Purpose:** Achieve knowledge of eternal Forms
        
        ### 2. Materialist View (Hobbes, modern science)
        - **Core claim:** Humans are complex physical machines
        - **Key features:** All behavior explained by material causes
        - **Mortality:** Death ends personal existence
        - **Purpose:** Survival and satisfaction of desires
        
        ### 3. Judeo-Christian View (Augustine)
        - **Core claim:** Humans made in God's image
        - **Key features:** Rational soul created by God
        - **Destiny:** Eternal existence with God
        - **Purpose:** Love God and neighbor
        
        ## Critical Questions
        - Are humans naturally selfish or capable of genuine altruism?
        - Is there something non-physical about human consciousness?
        - What distinguishes humans from other animals?
        - Can human nature be fundamentally changed?
        """,
        "presenter_notes": "Encourage students to consider how their own beliefs about human nature affect their daily interactions."
