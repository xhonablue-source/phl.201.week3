"""
PHL 201 Week 3 - Ancient Philosophy: Plato's Theory of Forms
Interactive Philosophy Lesson - Xavier Honablue, M.Ed.
"""

import streamlit as st
import time
import json
import io
from datetime import datetime
from typing import List, Dict, Optional

# Configure page
st.set_page_config(
    page_title="PHL 201 Week 3 - Plato's Theory of Forms",
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
if 'assignment2_progress' not in st.session_state:
    st.session_state.assignment2_progress = {
        'cave_reflection_draft': '',
        'revision_notes': '',
        'final_reflection': '',
        'peer_feedback': '',
        'completed_sections': set()
    }

# Slide data for Week 3
SLIDES = [
    {
        "id": "welcome",
        "title": "Welcome to Ancient Philosophy",
        "content": """
        # 🏛️ Ancient Philosophy: Plato's Theory of Forms
        
        ## PHL 201 — Week 3
        **Professor Xavier Honablue, M.Ed.**
        
        ### Today's Journey:
        - **Tuesday:** Revision Workshop - Improving your Plato's Cave reflection
        - **Thursday:** Plato's Theory of Forms - The world beyond appearances
        
        ### Learning Objectives:
        - Understand Plato's distinction between the world of appearances and the world of Forms
        - Analyze the Allegory of the Cave as a metaphor for philosophical enlightenment
        - Practice philosophical writing and revision skills
        - Connect ancient Greek philosophy to contemporary questions about reality and knowledge
        """,
        "presenter_notes": "Review Assignment 1 submissions briefly. Emphasize that philosophy is a skill that improves with practice and revision."
    },
    {
        "id": "revision_workshop",
        "title": "Revision Workshop: Plato's Cave",
        "content": """
        # ✏️ Revision Workshop: Improving Your Cave Reflection
        
        ## Why Revise Philosophical Writing?
        
        Philosophy is like **learning to see in the dark** - it takes practice, patience, and willingness to revise our understanding.
        
        ### Common Areas for Improvement:
        
        **1. Thesis Clarity**
        - ❌ "Plato's Cave is about people in a cave"
        - ✅ "Plato's Allegory of the Cave illustrates how philosophical education liberates us from mistaking appearances for reality"
        
        **2. Evidence and Analysis**
        - ❌ "The prisoners are chained and see shadows"
        - ✅ "The chained prisoners represent how we mistake sensory experience for ultimate truth, just as we might mistake a reflection in water for the actual object"
        
        **3. Personal Connection**
        - ❌ "This relates to my life"
        - ✅ "Like Plato's prisoners, I initially accepted social media portrayals as reality until I learned to question the 'shadows' on my screen"
        
        ## 🎯 Your Task: Peer Review Activity (15 minutes)
        Work with a partner to improve your Cave reflections using our revision checklist.
        """,
        "timer_minutes": 15,
        "activity_type": "peer_review"
    },
    {
        "id": "plato_biography",
        "title": "Meet Plato",
        "content": """
        # 👨‍🏫 Plato (428/427 - 348/347 BCE)
        
        ## The Man Behind the Ideas
        
        ### Background:
        - **Born:** Aristocratic family in Athens during the Golden Age
        - **Student:** Learned from Socrates for 20 years
        - **Trauma:** Witnessed Athens execute Socrates in 399 BCE
        - **Mission:** Founded the Academy to continue Socratic questioning
        
        ### Why the Cave Allegory?
        
        **Personal Experience:** Plato felt like the escaped prisoner returning to tell others about reality, only to be ridiculed and rejected.
        
        **Political Context:** Athens was struggling with:
        - Democracy vs. Expertise (Who should rule?)
        - Appearance vs. Reality (What can we trust?)
        - Opinion vs. Knowledge (How do we know anything?)
        
        ### 🤔 Think About It:
        What "caves" exist in our society today? Where do we mistake shadows for reality?
        """,
        "presenter_notes": "Connect Plato's historical context to contemporary issues like social media, fake news, or political polarization."
    },
    {
        "id": "forms_introduction",
        "title": "The Theory of Forms",
        "content": """
        # 🌟 Plato's Theory of Forms
        
        ## Two Worlds, Two Kinds of Knowledge
        
        ### The World of Appearances (What We See)
        - **Sensory objects:** This chair, that tree, this person
        - **Always changing:** Growing, aging, moving, decaying
        - **Imperfect copies:** No perfect circle exists in nature
        - **Opinion (doxa):** Based on senses, unreliable
        
        ### The World of Forms (What Is Real)
        - **Perfect essences:** The Form of Chair, Tree, Human
        - **Eternal and unchanging:** Always the same
        - **Perfect standards:** The perfect Circle, Justice, Beauty
        - **Knowledge (episteme):** Based on reason, reliable
        
        ## 🎯 Key Insight:
        **Everything we see is an imperfect copy of a perfect Form.**
        
        Like shadows on the cave wall are copies of real objects, our world is made of copies of perfect Forms.
        """,
        "presenter_notes": "Use concrete examples. Hold up a physical object and ask students to think about what makes it that type of thing."
    },
    {
        "id": "forms_examples",
        "title": "Forms in Action",
        "content": """
        # 🔍 Understanding Forms Through Examples
        
        ## Mathematical Forms
        
        ### The Form of Triangle
        - **In our world:** We draw triangles on paper, build triangular structures
        - **All imperfect:** Slightly crooked lines, not exactly 180°
        - **The Form:** Perfect Triangle that all triangles participate in
        - **How we know:** Through reason, not senses
        
        ## Moral Forms
        
        ### The Form of Justice
        - **In our world:** Laws, courts, fair decisions
        - **All imperfect:** Sometimes unjust laws, biased judges
        - **The Form:** Perfect Justice that all just acts participate in
        - **How we know:** Through philosophical reasoning
        
        ## 💭 Group Discussion (10 minutes):
        **Choose one Form and discuss:**
        - Form of Beauty
        - Form of Courage  
        - Form of Love
        - Form of Truth
        
        **Questions:** What makes something beautiful/courageous/loving/true? How do imperfect examples point to the perfect Form?
        """,
        "timer_minutes": 10,
        "activity_type": "group_discussion"
    },
    {
        "id": "cave_forms_connection",
        "title": "Connecting Cave and Forms",
        "content": """
        # 🔗 How the Cave Illustrates the Forms
        
        ## The Allegory Decoded
        
        | Cave Element | Represents | Form Theory |
        |--------------|------------|-------------|
        | **Shadows** | Sensory appearances | Imperfect copies we mistake for reality |
        | **Fire** | The sun (truth) | The Form of the Good - source of all knowledge |
        | **Real objects** | Mathematical/moral concepts | The eternal Forms |
        | **Outside world** | Realm of Forms | Perfect, unchanging reality |
        | **Escaped prisoner** | Philosopher | Someone who uses reason to see truth |
        | **Return to cave** | Teaching others | Philosopher's duty to educate |
        
        ## 🎯 The Philosopher's Journey:
        
        **Level 1:** Believing shadows are real (ordinary people)
        **Level 2:** Seeing the fire and objects (learning math/science)  
        **Level 3:** Reaching the outside (understanding Forms)
        **Level 4:** Returning to help others (teaching/politics)
        
        ## 🤔 Critical Question:
        If philosophers have seen truth, why don't people listen to them?
        """,
        "presenter_notes": "This is where students often get confused. Take time to ensure they understand the metaphor."
    },
    {
        "id": "problems_with_forms",
        "title": "Challenges to the Theory",
        "content": """
        # 🤔 Problems with Plato's Theory
        
        ## Historical Criticisms
        
        ### Aristotle's "Third Man" Problem
        - If there's a Form of Human and individual humans...
        - What explains the similarity between the Form and the humans?
        - Do we need a Form of that similarity? (Infinite regress)
        
        ### The Participation Problem
        - **How** do imperfect things "participate" in perfect Forms?
        - If Forms are separate from our world, how do they influence it?
        - What's the actual connection?
        
        ## Modern Questions
        
        ### Scientific Challenge
        - Can evolution explain why we recognize patterns without perfect Forms?
        - Do mathematical concepts exist independently or are they human constructs?
        
        ### Practical Concerns
        - Is there a Form of everything? (Hair, mud, disease?)
        - How do we access Forms if not through senses?
        - Why should perfect Forms care about imperfect copies?
        
        ## 💭 Discussion:
        Do these problems destroy Plato's theory, or can it be defended?
        """,
        "presenter_notes": "Don't just present problems - encourage students to defend Plato or develop modifications."
    },
    {
        "id": "contemporary_connections",
        "title": "Plato Today",
        "content": """
        # 🌐 Plato in the 21st Century
        
        ## Modern Platonists
        
        ### Computer Science
        - **Digital vs. Physical:** Is the digital world more "real" than physical?
        - **Programming:** Code represents perfect logical structures
        - **Virtual Reality:** Creating "more perfect" worlds
        
        ### Mathematics and Physics
        - **Mathematical Platonism:** Numbers and equations exist independently
        - **Quantum Mechanics:** Observable reality vs. underlying mathematical structure
        - **Cosmology:** Search for fundamental laws governing appearance
        
        ## Social Media as Cave
        
        ### Modern Shadows
        - **Instagram/TikTok:** Curated versions of reality
        - **Echo chambers:** Reinforcing limited perspectives  
        - **Deepfakes:** Increasingly convincing false images
        - **Algorithmic feeds:** What we see is controlled by unseen forces
        
        ## 🎯 Reflection Questions:
        1. What would Plato think about virtual reality?
        2. Are smartphones like the chains in the cave?
        3. How do we escape our modern "caves"?
        """,
        "presenter_notes": "Students really connect when they see how ancient philosophy applies to their digital lives."
    },
    {
        "id": "assignment_preview",
        "title": "Assignment 2 Preview",
        "content": """
        # 📝 Assignment 2: Revised Cave Reflection
        
        ## Your Mission:
        Revise your Plato's Cave reflection using today's feedback and new understanding of the Theory of Forms.
        
        ### Requirements:
        - **Length:** 300-400 words (same as before)
        - **Due:** Tuesday of Week 3
        - **Focus:** Incorporate understanding of Forms theory
        - **Style:** Clear thesis, evidence, personal connection
        
        ### New Elements to Include:
        1. **Forms Connection:** How does the Cave illustrate the difference between appearance and reality?
        2. **Personal Application:** What "shadows" do you mistake for reality?
        3. **Contemporary Example:** Modern parallel to Plato's allegory
        4. **Critical Thinking:** One strength OR weakness of Plato's theory
        
        ### Grading Criteria:
        - **Improvement from original** (shows engagement with feedback)
        - **Understanding of concepts** (accurate use of philosophical terms)
        - **Clear writing** (thesis, evidence, conclusion)
        - **Personal insight** (meaningful connections to your experience)
        """,
        "presenter_notes": "Emphasize that this is about improvement, not perfection. Philosophy is a skill developed through practice."
    }
]

# Assignment 2 tracking
ASSIGNMENT2_SECTIONS = {
    "draft_review": {
        "title": "Review Your Original Draft",
        "description": "Look at your Assignment 1 submission and identify areas for improvement based on today's discussion.",
        "required": True
    },
    "forms_integration": {
        "title": "Connect Cave to Forms Theory", 
        "description": "Explain how the Cave Allegory illustrates Plato's Theory of Forms using specific examples.",
        "required": True
    },
    "contemporary_parallel": {
        "title": "Modern Cave Example",
        "description": "Identify a contemporary situation where people mistake 'shadows' for reality.",
        "required": True
    },
    "critical_analysis": {
        "title": "Critical Evaluation",
        "description": "Discuss one strength OR weakness of Plato's Theory of Forms.",
        "required": True
    },
    "final_draft": {
        "title": "Final Revised Reflection",
        "description": "Complete 300-400 word revision incorporating all elements above.",
        "required": True
    }
}

# Quiz questions about Plato
QUIZ_DATA = {
    "plato_basics": {
        "title": "Plato's Theory of Forms",
        "questions": [
            {
                "question": "According to Plato, the world we perceive through our senses is:",
                "options": [
                    "The most real and reliable source of knowledge",
                    "An imperfect copy of a more perfect reality",
                    "An illusion that doesn't exist at all",
                    "The only world that exists"
                ],
                "correct": 1,
                "explanation": "Plato believed our sensory world consists of imperfect copies or 'shadows' of perfect Forms. The sensory world is real but less real than the world of Forms."
            },
            {
                "question": "In the Cave Allegory, what do the shadows on the wall represent?",
                "options": [
                    "Evil or false ideas that deceive people",
                    "Sensory experiences that we mistake for ultimate reality", 
                    "Mathematical concepts that are hard to understand",
                    "Political propaganda used to control people"
                ],
                "correct": 1,
                "explanation": "The shadows represent all the sensory experiences and appearances that we typically take to be reality, when they're actually just copies of deeper truths."
            },
            {
                "question": "What is the main point of Plato's Theory of Forms?",
                "options": [
                    "Perfect mathematical and moral concepts exist in a realm beyond our physical world",
                    "All knowledge comes from sensory experience and observation",
                    "There is no objective truth, only individual opinions",
                    "The physical world is all that exists"
                ],
                "correct": 0,
                "explanation": "Plato argued that perfect Forms (like perfect Justice, Beauty, Truth) exist in an eternal realm and serve as the standards for all imperfect copies in our world."
            },
            {
                "question": "Why does the escaped prisoner return to the cave?",
                "options": [
                    "He realizes the outside world was just another illusion",
                    "He wants to rule over the other prisoners",
                    "He feels a duty to help others reach enlightenment",
                    "He is forced to return against his will"
                ],
                "correct": 2,
                "explanation": "Plato believed philosophers have a moral obligation to return and help others achieve understanding, even if they face ridicule or resistance."
            }
        ]
    },
    "cave_allegory": {
        "title": "Understanding the Cave Allegory",
        "questions": [
            {
                "question": "What does the journey from cave to sunlight represent?",
                "options": [
                    "Growing up and becoming an adult",
                    "The process of philosophical education and enlightenment",
                    "Escaping from political oppression",
                    "Learning to use your physical senses better"
                ],
                "correct": 1,
                "explanation": "The journey represents education (paideia) - the process of philosophical learning that moves us from ignorance to knowledge, from opinion to understanding."
            },
            {
                "question": "According to Plato, why do people resist philosophical truth?",
                "options": [
                    "Because they are naturally evil or stupid",
                    "Because truth is painful and they prefer comfortable illusions",
                    "Because philosophers explain things poorly",
                    "Because there is no real truth to discover"
                ],
                "correct": 1,
                "explanation": "Plato suggests that people resist truth because it's challenging and disruptive to their existing beliefs - like how bright light hurts eyes accustomed to darkness."
            }
        ]
    }
}

# Resources for Week 3
RESOURCES = {
    "videos": [
        {
            "title": "Plato's Allegory of the Cave - TED-Ed",
            "url": "https://www.youtube.com/watch?v=1RWOpQXTltA",
            "description": "Beautiful animated explanation of the Cave Allegory",
            "duration": "7 minutes"
        },
        {
            "title": "Plato's Theory of Forms - Crash Course Philosophy",
            "url": "https://www.youtube.com/watch?v=MgotDFs6cdE", 
            "description": "Clear explanation of Forms with modern examples",
            "duration": "10 minutes"
        },
        {
            "title": "The Matrix and Plato's Cave",
            "url": "https://www.youtube.com/watch?v=n7jnorm3gNs",
            "description": "Comparing the famous movie to Plato's allegory",
            "duration": "8 minutes"
        }
    ],
    "readings": [
        {
            "title": "Plato's Republic - Book VII (Cave Allegory)",
            "url": "http://classics.mit.edu/Plato/republic.8.vii.html",
            "description": "Original text of the Cave Allegory - challenging but rewarding"
        },
        {
            "title": "Stanford Encyclopedia: Plato's Theory of Forms",
            "url": "https://plato.stanford.edu/entries/plato-metaphysics/",
            "description": "Scholarly overview of Forms theory and major criticisms"
        }
    ]
}

def display_slide(slide_data: dict) -> None:
    """Display a slide with enhanced formatting"""
    col1, col2 = st.columns([4, 1])
    
    with col1:
        st.markdown(slide_data["content"])
        
        # Add interactive elements for specific slides
        if slide_data.get("timer_minutes"):
            st.markdown("---")
            st.info(f"⏰ Activity Time: {slide_data['timer_minutes']} minutes")
            
            if st.button(f"Start {slide_data['timer_minutes']} minute timer"):
                start_timer(slide_data["timer_minutes"])
                st.rerun()
    
    with col2:
        # Timer display
        if st.session_state.timer_active and st.session_state.timer_end:
            remaining = st.session_state.timer_end - time.time()
            if remaining > 0:
                mins, secs = divmod(int(remaining), 60)
                st.markdown(f"""
                <div style="background: linear-gradient(45deg, #ff6b6b, #ee5a24); 
                           color: white; padding: 15px; border-radius: 10px; text-align: center;">
                    <h3>⏰ Timer</h3>
                    <h2>{mins:02d}:{secs:02d}</h2>
                </div>
                """, unsafe_allow_html=True)
                time.sleep(1)
                st.rerun()
            else:
                st.balloons()
                st.success("⏰ Time's up!")
                st.session_state.timer_active = False

def start_timer(minutes: int) -> None:
    """Start activity timer"""
    st.session_state.timer_active = True
    st.session_state.timer_end = time.time() + (minutes * 60)

def display_assignment2():
    """Display Assignment 2: Revised Cave Reflection"""
    st.markdown("# 📝 Assignment 2: Revised Cave Reflection")
    st.markdown("## Building on Your Previous Work")
    
    # Instructions
    with st.expander("📋 Assignment Instructions", expanded=True):
        st.markdown("""
        ### Your Mission:
        Revise your Assignment 1 Cave reflection incorporating new understanding from today's lesson.
        
        ### Requirements:
        - **Length:** 300-400 words
        - **Due:** Tuesday of Week 3
        - **Grade Value:** 4.6% of course grade
        
        ### Must Include:
        1. **Forms Connection:** How does the Cave illustrate appearance vs. reality?
        2. **Personal Application:** What "shadows" do you mistake for reality?
        3. **Contemporary Example:** Modern parallel to the allegory
        4. **Critical Analysis:** One strength OR weakness of Plato's theory
        
        ### Grading Focus:
        - Shows improvement from original draft
        - Demonstrates understanding of philosophical concepts
        - Clear thesis, evidence, and personal insight
        """)
    
    # Progress tracking
    st.markdown("## 📊 Your Progress")
    
    progress_data = st.session_state.assignment2_progress
    completed_sections = len(progress_data['completed_sections'])
    total_sections = len(ASSIGNMENT2_SECTIONS)
    
    st.progress(completed_sections / total_sections)
    st.markdown(f"Completed: {completed_sections}/{total_sections} sections")
    
    # Section-by-section work
    for section_id, section_info in ASSIGNMENT2_SECTIONS.items():
        
        st.markdown(f"## {section_info['title']}")
        st.markdown(section_info['description'])
        
        if section_id == "draft_review":
            st.markdown("### Reflect on Your Original Assignment 1:")
            draft_review = st.text_area(
                "What feedback did you receive? What would you change?",
                value=progress_data.get('revision_notes', ''),
                height=100,
                key=f"review_{section_id}"
            )
            
            if st.button(f"Save Review Notes", key=f"save_{section_id}"):
                progress_data['revision_notes'] = draft_review
                progress_data['completed_sections'].add(section_id)
                st.success("Notes saved!")
        
        elif section_id == "forms_integration":
            st.markdown("### Connect Cave to Forms Theory:")
            forms_connection = st.text_area(
                "How does the Cave Allegory illustrate Plato's Theory of Forms?",
                placeholder="Explain how shadows represent imperfect copies, the fire represents truth, etc.",
                height=120,
                key=f"forms_{section_id}"
            )
            
            if st.button(f"Save Forms Analysis", key=f"save_{section_id}"):
                if len(forms_connection.split()) >= 50:
                    progress_data['forms_analysis'] = forms_connection
                    progress_data['completed_sections'].add(section_id)
                    st.success("Forms analysis saved!")
                else:
                    st.warning("Please write at least 50 words explaining the connection.")
        
        elif section_id == "contemporary_parallel":
            st.markdown("### Modern Cave Example:")
            contemporary = st.text_area(
                "What's a contemporary situation where people mistake 'shadows' for reality?",
                placeholder="Social media, news bubbles, advertising, political propaganda, etc.",
                height=120,
                key=f"contemporary_{section_id}"
            )
            
            if st.button(f"Save Contemporary Example", key=f"save_{section_id}"):
                if len(contemporary.split()) >= 30:
                    progress_data['contemporary_example'] = contemporary
                    progress_data['completed_sections'].add(section_id)
                    st.success("Contemporary example saved!")
                else:
                    st.warning("Please write at least 30 words explaining your example.")
        
        elif section_id == "critical_analysis":
            st.markdown("### Critical Evaluation:")
            analysis_type = st.radio(
                "Choose your focus:",
                ["Strength of Plato's theory", "Weakness of Plato's theory"],
                key=f"type_{section_id}"
            )
            
            critical_analysis = st.text_area(
                f"Explain one {analysis_type.lower()}:",
                placeholder="Consider the problems we discussed: Third Man argument, participation problem, or modern relevance...",
                height=120,
                key=f"critical_{section_id}"
            )
            
            if st.button(f"Save Critical Analysis", key=f"save_{section_id}"):
                if len(critical_analysis.split()) >= 40:
                    progress_data['critical_analysis'] = critical_analysis
                    progress_data['completed_sections'].add(section_id)
                    st.success("Critical analysis saved!")
                else:
                    st.warning("Please write at least 40 words for your analysis.")
        
        elif section_id == "final_draft":
            if len(progress_data['completed_sections']) >= 4:
                st.markdown("### Final Revised Reflection:")
                st.success("All preparatory sections complete! Now write your final reflection.")
                
                final_draft = st.text_area(
                    "Write your complete 300-400 word revised reflection:",
                    value=progress_data.get('final_reflection', ''),
                    height=300,
                    key=f"final_{section_id}"
                )
                
                # Word count
                word_count = len(final_draft.split()) if final_draft else 0
                
                if word_count < 300:
                    st.warning(f"Word count: {word_count}/300 (minimum) - Need {300-word_count} more words")
                elif word_count > 400:
                    st.warning(f"Word count: {word_count}/400 (maximum) - Remove {word_count-400} words")
                else:
                    st.success(f"Word count: {word_count} - Perfect length!")
                
                if st.button("Submit Final Reflection", key=f"submit_{section_id}"):
                    if 300 <= word_count <= 400:
                        progress_data['final_reflection'] = final_draft
                        progress_data['completed_sections'].add(section_id)
                        st.balloons()
                        st.success("Assignment 2 completed and submitted!")
                        
                        # Export option
                        export_data = {
                            'assignment': 'Assignment 2: Revised Cave Reflection',
                            'completion_date': datetime.now().isoformat(),
                            'word_count': word_count,
                            'final_reflection': final_draft,
                            'revision_process': {
                                'original_review': progress_data.get('revision_notes', ''),
                                'forms_analysis': progress_data.get('forms_analysis', ''),
                                'contemporary_example': progress_data.get('contemporary_example', ''),
                                'critical_analysis': progress_data.get('critical_analysis', '')
                            }
                        }
                        
                        json_str = json.dumps(export_data, indent=2)
                        st.download_button(
                            "Download Assignment 2",
                            json_str,
                            file_name=f"assignment2_cave_revision_{datetime.now().strftime('%Y%m%d')}.json",
                            mime="application/json"
                        )
                    else:
                        st.error("Reflection must be between 300-400 words.")
            else:
                st.info("Complete the sections above before writing your final draft.")
        
        st.markdown("---")

def display_quiz(quiz_id: str) -> None:
    """Display interactive quiz"""
    if quiz_id not in QUIZ_DATA:
        st.error("Quiz not found!")
        return
        
    quiz = QUIZ_DATA[quiz_id]
    st.markdown(f"## 📝 {quiz['title']}")
    
    # Track attempts
    if quiz_id not in st.session_state.quiz_attempts:
        st.session_state.quiz_attempts[quiz_id] = 0
    
    with st.form(f"quiz_{quiz_id}"):
        answers = {}
        for i, q in enumerate(quiz["questions"]):
            st.markdown(f"**Question {i+1}:** {q['question']}")
            answer = st.radio(
                "Choose your answer:",
                options=q["options"],
                key=f"q_{quiz_id}_{i}",
                index=None
            )
            if answer:
                answers[i] = q["options"].index(answer)
        
        submitted = st.form_submit_button("Submit Quiz")
        
        if submitted and len(answers) == len(quiz["questions"]):
            st.session_state.quiz_attempts[quiz_id] += 1
            
            # Grade quiz
            correct_count = 0
            total_questions = len(quiz["questions"])
            
            st.markdown("---")
            st.markdown("### 📊 Results:")
            
            for i, q in enumerate(quiz["questions"]):
                if i in answers:
                    is_correct = answers[i] == q["correct"]
                    if is_correct:
                        correct_count += 1
                        st.success(f"✅ Question {i+1}: Correct!")
                    else:
                        st.error(f"❌ Question {i+1}: Incorrect")
                        st.info(f"**Correct answer:** {q['options'][q['correct']]}")
                    
                    # Show explanation
                    st.markdown(f"**Explanation:** {q['explanation']}")
                    st.markdown("---")
            
            # Overall score
            score_pct = (correct_count / total_questions) * 100
            
            if score_pct >= 80:
                st.balloons()
                st.success(f"Excellent work! Score: {correct_count}/{total_questions} ({score_pct:.0f}%)")
            elif score_pct >= 60:
                st.success(f"Good job! Score: {correct_count}/{total_questions} ({score_pct:.0f}%)")
            else:
                st.warning(f"Keep studying! Score: {correct_count}/{total_questions} ({score_pct:.0f}%)")

def display_resources() -> None:
    """Display resources for Week 3"""
    st.markdown("# 📚 Week 3 Resources: Plato's Theory of Forms")
    
    # Videos section
    st.markdown("## 🎥 Videos")
    col1, col2 = st.columns(2)
    
    for i, video in enumerate(RESOURCES["videos"]):
        with col1 if i % 2 == 0 else col2:
            st.markdown(f"### {video['title']}")
            st.markdown(f"{video['description']}")
            st.markdown(f"**Duration:** {video['duration']}")
            st.markdown(f"[Watch Now]({video['url']})")
            st.markdown("---")
    
    # Readings section
    st.markdown("## 📖 Essential Readings")
    for reading in RESOURCES["readings"]:
        st.markdown(f"- **[{reading['title']}]({reading['url']})** - {reading['description']}")

def sidebar_navigation() -> str:
    """Enhanced sidebar with navigation and controls"""
    st.sidebar.markdown("# 🏛️ PHL 201 Week 3")
    st.sidebar.markdown("**Ancient Philosophy: Plato's Theory of Forms**")
    
    # Mode selection
    mode = st.sidebar.radio(
        "Choose Mode:",
        ["📊 Presentation", "📝 Assignment 2", "🧠 Quizzes", "📚 Resources"]
    )
    
    if mode == "📊 Presentation":
        st.sidebar.markdown("## Slide Navigation")
        
        # Slide selector
        slide_titles = [f"{i+1}. {slide['title']}" for i, slide in enumerate(SLIDES)]
        selected_slide = st.sidebar.selectbox(
            "Jump to slide:",
            options=range(len(SLIDES)),
            format_func=lambda x: slide_titles[x],
            index=st.session_state.current_slide
        )
        
        if selected_slide != st.session_state.current_slide:
            st.session_state.current_slide = selected_slide
        
        # Navigation buttons
        col1, col2 = st.sidebar.columns(2)
        with col1:
            if st.button("⬅️ Previous") and st.session_state.current_slide > 0:
                st.session_state.current_slide -= 1
                st.rerun()
        
        with col2:
            if st.button("Next ➡️") and st.session_state.current_slide < len(SLIDES) - 1:
                st.session_state.current_slide += 1
                st.rerun()
        
        # Presenter notes
        st.sidebar.markdown("---")
        if st.sidebar.checkbox("📋 Show Presenter Notes"):
            current_slide = SLIDES[st.session_state.current_slide]
            st.sidebar.markdown("**Notes:**")
            st.sidebar.info(current_slide.get("presenter_notes", "No notes for this slide."))
            
    return mode.split()[1].lower()  # Return just the key part

def main():
    """Main application function"""
    # Custom CSS for better styling
    st.markdown("""
    <style>
    .main > div {
        padding-top: 2rem;
    }
    .stButton > button {
        width: 100%;
        border-radius: 10px;
        border: none;
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
    }
    .stButton > button:hover {
        background: linear-gradient(45deg, #764ba2, #667eea);
    }
    .stProgress .st-bo {
        background-color: #667eea;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Determine current mode from sidebar
    current_mode = sidebar_navigation()
    
    if current_mode == "presentation":
        # Main presentation mode
        current_slide = SLIDES[st.session_state.current_slide]
        display_slide(current_slide)
        
        # Progress indicator
        progress = (st.session_state.current_slide + 1) / len(SLIDES)
        st.progress(progress)
        st.caption(f"Slide {st.session_state.current_slide + 1} of {len(SLIDES)}")
    
    elif current_mode == "assignment":
        display_assignment2()
    
    elif current_mode == "quizzes":
        st.markdown("# 🧠 Week 3 Knowledge Check")
        
        quiz_choice = st.selectbox(
            "Select a quiz:",
            ["plato_basics", "cave_allegory"],
            format_func=lambda x: QUIZ_DATA[x]["title"]
        )
        
        display_quiz(quiz_choice)
    
    elif current_mode == "resources":
        display_resources()

if __name__ == "__main__":
    main()
