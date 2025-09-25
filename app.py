# Topic quizzes from original program
TOPIC_QUIZZES = {
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

def display_quiz(quiz_id: str) -> None:
    """Display topic-specific quiz"""
    if quiz_id not in TOPIC_QUIZZES:
        st.error("Quiz not found!")
        return
        
    quiz = TOPIC_QUIZZES[quiz_id]
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
    st.markdown("# 📚 Resources: Ancient Philosophy & Human Nature")
    
    # Videos section
    st.markdown("## 🎥 Recommended Videos")
    
    videos = [
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
            "url": "https://www.youtube.com/watch?v=LlzgtG_09Z0",
            "description": "Comparing the famous movie to Plato's allegory",
            "duration": "8 minutes"
        }
    ]
    
    col1, col2 = st.columns(2)
    
    for i, video in enumerate(videos):
        with col1 if i % 2 == 0 else col2:
            st.markdown(f"### {video['title']}")
            st.markdown(f"{video['description']}")
            st.markdown(f"**Duration:** {video['duration']}")
            st.markdown(f"[Watch Now]({video['url']})")
            st.markdown("---")
    
    # Readings section
    st.markdown("## 📖 Essential Readings")
    
    readings = [
        {
            "title": "Plato's Republic - Book VII (Cave Allegory)",
            "url": "http://classics.mit.edu/Plato/republic.8.vii.html",
            "description": "Original text of the Cave Allegory - challenging but rewarding"
        },
        {
            "title": "Stanford Encyclopedia: Plato's Theory of Forms",
            "url": "https://plato.stanford.edu/entries/plato-metaphysics/",
            "description": "Scholarly overview of Forms theory and major criticisms"
        },
        {
            "title": "Internet Encyclopedia: Human Nature",
            "url": "https://iep.utm.edu/human-nature/",
            "description": "Comprehensive overview of philosophical theories of human nature"
        }
    ]
    
    for reading in readings:
        st.markdown(f"- **[{reading['title']}]({reading['url']})** - {reading['description']}")
    
    # Study tips
    st.markdown("## 💡 Study Tips")
    
    with st.expander("How to Study Philosophy Effectively"):
        st.markdown("""
        ### Before Reading:
        - Preview the main questions the text addresses
        - Consider what you already believe about the topic
        
        ### While Reading:
        - Take notes on key arguments and evidence
        - Ask yourself: What is the philosopher trying to prove?
        - Identify premises and conclusions
        
        ### After Reading:
        - Summarize the main argument in your own words
        - Consider objections: What might someone disagree with?
        - Connect ideas to your own experience and other readings
        
        ### Discussion Preparation:
        - Prepare thoughtful questions
        - Consider multiple perspectives on each issue
        - Practice explaining concepts to others
        """)

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
        - **Due:**"""
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
    },
    {
        "id": "plato_tripartite_soul",
        "title": "Plato's Theory of the Soul",
        "content": """
        # ⚖️ Plato's Tripartite Soul
        
        ## Three Parts of Human Nature
        
        ### 1. Reason (Logos) - The Charioteer
        - **Location:** Head/brain
        - **Function:** Logical thinking, planning, understanding Forms
        - **Virtue:** Wisdom (sophia)
        - **Goal:** Knowledge of truth and goodness
        
        ### 2. Spirit/Emotion (Thumos) - The Noble Horse  
        - **Location:** Chest/heart
        - **Function:** Courage, anger, ambition, pride
        - **Virtue:** Courage (andreia)
        - **Goal:** Honor and recognition
        
        ### 3. Appetite (Epithumia) - The Wild Horse
        - **Location:** Abdomen/below
        - **Function:** Physical desires (food, sex, comfort)  
        - **Virtue:** Temperance (sophrosyne)
        - **Goal:** Immediate pleasure and satisfaction
        
        ## The Chariot Metaphor
        
        > "Let me speak briefly about the nature of the soul by using an image. And let the image have three parts: two winged horses and a charioteer... One of the charioteer's horses is of noble breed, the other ignoble."
        
        - **Charioteer (Reason)** must control and direct the horses
        - **Noble horse (Spirit)** can be trained to support reason  
        - **Wild horse (Appetite)** constantly pulls toward base pleasures
        - **Harmony achieved** when reason rules with spirit's help over appetite
        
        ## Justice in the Soul
        **Individual justice occurs when:**
        - Reason rules through wisdom
        - Spirit supports reason through courage  
        - Appetite obeys reason through temperance
        - Each part performs its proper function
        
        ## Conflict and Control
        - **Internal conflicts** arise when appetite or spirit rebel against reason
        - **Philosophical education** trains reason to govern effectively
        - **Self-control** possible through practiced rational discipline
        """,
        "presenter_notes": "Ask students to identify times they've experienced conflicts between these different aspects of themselves."
    },
    {
        "id": "immaterial_soul_thesis",
        "title": "The Immaterial Soul: Plato's Arguments",
        "content": """
        # 👻 The Immaterial Soul Thesis
        
        ## Core Claims
        
        ### What Makes the Soul Immaterial?
        1. **Non-physical substance** - Not made of matter
        2. **Survives bodily death** - Continues existing after material body dies  
        3. **Grasps eternal Forms** - Can understand perfect, unchanging truths
        4. **Source of rationality** - What makes humans capable of reason
        5. **Personal identity** - What makes you "you" over time
        
        ## Plato's Evidence for Immateriality
        
        ### Argument from Grasping Perfect Concepts
        - **Premise 1:** Our minds can grasp perfect mathematical and moral concepts
        - **Premise 2:** Perfect concepts (like perfect circles, justice) don't exist in material world
        - **Premise 3:** Material things can only interact with other material things
        - **Conclusion:** Our minds must be immaterial to grasp immaterial Forms
        
        ### The Recollection Argument
        - **Observation:** We can recognize truths we were never explicitly taught
        - **Example:** Slave boy in Meno can discover geometric theorems through questioning
        - **Explanation:** Soul learned these truths before birth in realm of Forms
        - **Implication:** Soul existed before this life, so it's not dependent on body
        
        ### Argument from Opposites
        - **Pattern:** All things come from their opposites (hot from cold, tall from short)
        - **Application:** Life comes from death, death from life
        - **Cycle:** If process stopped, everything would end up dead
        - **Conclusion:** Souls must return from death to life (immortality/reincarnation)
        
        ## Contemporary Parallels
        - **Consciousness studies:** "Hard problem" of subjective experience
        - **Near-death experiences:** Reports of consciousness during clinical death
        - **Mathematical Platonism:** Do numbers exist independently of physical world?
        - **Personal identity:** What persists through bodily changes over lifetime?
        """,
        "presenter_notes": "Connect to current debates about consciousness, AI, and whether mind reduces to brain."
    },
    {
        "id": "aristotle_critique",
        "title": "Aristotle's Response to Plato",
        "content": """
        # 🎯 Aristotle's Critique of Forms and Soul
        
        ## Problems with the Theory of Forms
        
        ### The "Third Man" Argument
        - **Problem:** If humans resemble Form of Human, what explains this resemblance?
        - **Infinite regress:** Need a Form of Resemblance, then a Form of that resemblance, etc.
        - **Conclusion:** Theory leads to logical contradiction
        
        ### The Participation Problem  
        - **Question:** How exactly do material things "participate in" Forms?
        - **Mystery:** What is the actual connection between two separate realms?
        - **Challenge:** Forms are supposed to explain material world but connection unexplained
        
        ### Unnecessary Multiplication
        - **Ockham's Razor:** Don't multiply entities beyond necessity
        - **Alternative:** Properties exist in objects, not separate realm
        - **Simpler explanation:** Universals exist in particulars, not apart from them
        
        ## Aristotle's Alternative: The Soul as Form
        
        ### Soul as Organization, Not Substance
        - **Plato's view:** Soul is separate immaterial thing temporarily inhabiting body
        - **Aristotle's view:** Soul is the form, structure, or organization of living body
        - **Analogy:** Soul relates to body as shape relates to wax
        
        ### Human Uniqueness Through Rationality
        - **Vegetative soul:** Growth, nutrition (plants, animals, humans have this)
        - **Sensitive soul:** Perception, movement (animals and humans have this)  
        - **Rational soul:** Abstract thought, reasoning (only humans have this)
        
        ### The Rational Part Survives?
        - **Inconsistency:** Aristotle sometimes suggests rational part might survive death
        - **Problem:** If soul is body's organization, how can part survive body's destruction?
        - **Interpretation debate:** Scholars disagree whether Aristotle believed in personal immortality
        
        ## Implications of Disagreement
        
        **If Plato is right:** Humans have immaterial souls, personal immortality possible  
        **If Aristotle is right:** Humans are sophisticated material beings, death likely final  
        
        **Modern relevance:** Debate continues in neuroscience, psychology, and philosophy of mind
        """,
        "presenter_notes": "This disagreement between Plato and Aristotle shaped 2000+ years of Western thought about human nature."
    },
    {
        "id": "judeo_christian_synthesis",
        "title": "Augustine and the Judeo-Christian View",
        "content": """
        # ✝️ Augustine's Synthesis: Plato Meets Christianity
        
        ## Core Judeo-Christian Claims
        
        ### Humans Made in God's Image
        - **Biblical foundation:** "And God said, let us make man in our image, after our likeness"
        - **Rational nature:** Like God, humans can reason and make moral choices
        - **Moral responsibility:** Capacity for good and evil, held accountable
        - **Relationship with divine:** Designed for connection with God
        
        ### Augustine's Adaptation of Plato
        
        #### Forms Exist in Mind of God
        - **Plato's problem:** Where do eternal Forms exist?
        - **Augustine's solution:** Forms are God's eternal ideas/blueprints
        - **Quote:** "Ideals are certain original Forms, or permanent and unchanging archetypes of things that are not themselves formed by anything else."
        
        #### The Will vs. Pure Reason
        - **Plato's emphasis:** Reason should rule over appetite and emotion
        - **Augustine's addition:** Will is crucial - power to choose between good and evil
        - **Christian doctrine:** Human will corrupted by original sin, needs divine grace
        
        ### Three Disordered Desires (Augustine's Psychology)
        1. **Lust (concupiscentia)** - Craving for physical pleasures
        2. **Curiosity** - Restless desire for new experiences  
        3. **Pride** - Desire for others' approval and dominance
        
        ## Impact on Western Civilization
        
        ### Rational Justification for Discrimination
        - **Aristotle's hierarchy:** Some humans naturally suited to be slaves
        - **Misapplication:** Used to justify oppression of Indigenous peoples, Africans
        - **Historical tragedy:** Philosophical ideas used to defend horrific injustices
        
        ### Positive Contributions
        - **Human dignity:** All humans made in God's image, inherently valuable
        - **Universal moral law:** Same ethical standards apply to all people
        - **Individual worth:** Each person has unique relationship with God
        - **Social responsibility:** Duty to care for others, especially vulnerable
        
        ## Modern Questions
        
        ### Compatibility with Science
        - **Evolution:** Can religious view of human nature accommodate evolutionary origins?
        - **Neuroscience:** What happens to soul-based theories as we learn more about brain?
        - **Psychology:** Do we need supernatural explanations for human behavior?
        
        ### Practical Implications  
        - **Medical ethics:** Does soul-theory affect decisions about life support, abortion?
        - **Criminal justice:** How does view of human nature affect punishment vs. rehabilitation?
        - **Social policy:** Should government assume humans are naturally good or selfish?
        """,
        "presenter_notes": "Emphasize how philosophical ideas about human nature have real-world consequences, both positive and negative."
    },
    {
        "id": "modern_challenges",
        "title": "Contemporary Challenges & Applications",
        "content": """
        # 🔬 Modern Philosophy Meets Ancient Questions
        
        ## Neuroscience vs. Immaterial Soul
        
        ### The Hard Problem of Consciousness
        - **David Chalmers' challenge:** How does subjective experience arise from objective brain?
        - **Explanatory gap:** We can map brain states but not explain why there's subjective experience
        - **Zombie argument:** Could there be beings physically identical to us but without consciousness?
        
        ### Near-Death Experiences (NDEs)
        - **Reported phenomena:** Out-of-body experiences, life reviews, encounters with deceased
        - **Materialist explanation:** Brain chemistry during cardiac arrest
        - **Dualist interpretation:** Evidence for soul's independence from body
        - **Research challenge:** How to study scientifically?
        
        ## Evolutionary Psychology & Human Nature
        
        ### Biological Altruism (Desmond Morris)
        - **Gene-centered evolution:** Behaviors that help genetic relatives survive
        - **Apparent contradiction:** Selfless behavior serves selfish genetic interests
        - **Modern expansion:** Technology allows helping non-relatives globally
        - **Question:** Does evolutionary explanation eliminate genuine altruism?
        
        ### Psychological Egoism Debate
        - **Hobbes' claim:** All actions ultimately self-interested
        - **Counter-examples:** Martyrdom, anonymous charitable giving, parental sacrifice
        - **Mercer's introspection:** When we examine our motives, do we find only self-interest?
        - **Philosophical challenge:** Can we ever prove genuine altruism exists?
        
        ## Digital Age Plato's Caves
        
        ### Social Media Shadows
        - **Curated reality:** Instagram/TikTok present edited versions of life
        - **Echo chambers:** Algorithms reinforce existing beliefs
        - **Deepfakes:** Increasingly convincing false images and videos
        - **Information bubbles:** We see only what platforms want us to see
        
        ### Virtual Reality & Reality
        - **Simulation hypothesis:** Could we be living in a computer simulation?
        - **Augmented reality:** Digital overlays change perception of physical world
        - **Gaming worlds:** Some spend more time in virtual than physical environments
        - **Platonic question:** Which reality is more "real"?
        
        ## AI and Human Uniqueness
        
        ### Machine Consciousness
        - **Turing test:** Can machines convince us they're conscious?
        - **Chinese room argument:** Understanding vs. symbol manipulation
        - **Large language models:** Do they truly understand or just process patterns?
        - **Human distinctiveness:** What remains uniquely human?
        
        ### Moral Status of AI
        - **If machines become conscious:** Do they deserve rights?
        - **Platonic Forms:** Could AI access eternal truths better than humans?
        - **Soul-based ethics:** Only beings with souls have moral worth?
        - **Functional approach:** Consciousness, not souls, determines moral status
        
        ## Practical Applications Today
        
        ### Medical Ethics
        - **Persistent vegetative state:** Is person still there without consciousness?
        - **Brain death:** When does personal existence end?
        - **Artificial life support:** Does soul leave body immediately at death?
        
        ### Criminal Justice
        - **Rehabilitation vs. punishment:** Can human nature be changed?
        - **Moral responsibility:** Are we fully responsible if behavior determined by brain chemistry?
        - **Juvenile justice:** When do humans develop full moral agency?
        """,
        "presenter_notes": "Connect ancient philosophical questions to current headlines and technological developments students encounter daily."
    }
]

# Comprehensive 80-question quiz combining existing and new content
COMPREHENSIVE_QUIZ = {
    "title": "Comprehensive Philosophy Assessment: Ancient Philosophy & Human Nature",
    "description": "80-question assessment covering Plato's Forms, human nature theories, and philosophical argumentation",
    "questions": [
        # Plato's Theory of Forms (Questions 1-20)
        {
            "id": 1,
            "question": "According to Plato, the world we perceive through our senses is:",
            "options": [
                "The most real and reliable source of knowledge",
                "An imperfect copy of a more perfect reality", 
                "An illusion that doesn't exist at all",
                "The only world that exists"
            ],
            "correct": 1,
            "explanation": "Plato believed our sensory world consists of imperfect copies or 'shadows' of perfect Forms. The sensory world is real but less real than the world of Forms.",
            "category": "Forms Theory"
        },
        {
            "id": 2, 
            "question": "In Plato's Theory of Forms, what makes the Forms 'more real' than material objects?",
            "options": [
                "Forms are bigger and more powerful than physical things",
                "Forms are eternal, unchanging, and perfect while material things are temporary and flawed",
                "Forms can be seen with our eyes while material things are invisible", 
                "Forms are located in a specific place while material things exist everywhere"
            ],
            "correct": 1,
            "explanation": "Forms are considered more real because they are eternal, unchanging, and perfect, serving as the unchanging standards or patterns that material objects imperfectly copy.",
            "category": "Forms Theory"
        },
        {
            "id": 3,
            "question": "What does the 'participation' relationship mean in Plato's theory?",
            "options": [
                "Forms actively participate in creating the material world",
                "Material objects are imperfect copies that 'participate in' or resemble perfect Forms",
                "Humans participate in Forms through religious ceremonies",
                "Forms and material objects are equal participants in reality"
            ],
            "correct": 1,
            "explanation": "Participation means that material objects are imperfect copies or instances of perfect Forms - they 'participate in' the Form by resembling it imperfectly.",
            "category": "Forms Theory"
        },
        {
            "id": 4,
            "question": "According to Plato, why can we recognize that a drawn triangle is triangular even though it's imperfect?",
            "options": [
                "Because we learned geometry in school",
                "Because our soul has knowledge of the perfect Form of Triangle from before birth",
                "Because all triangles in the physical world are actually perfect",
                "Because recognition is just a learned behavioral response"
            ],
            "correct": 1,
            "explanation": "Plato's theory of recollection suggests our souls knew the perfect Forms before birth, which is why we can recognize imperfect copies and understand mathematical truths.",
            "category": "Forms Theory"
        },
        {
            "id": 5,
            "question": "What is the Form of the Good in Plato's theory?",
            "options": [
                "Just another Form like all the others",
                "The highest Form that makes all other Forms knowable and gives them reality",
                "A form that only exists in human minds",
                "The least important of all Forms"
            ],
            "correct": 1,
            "explanation": "The Form of the Good is the highest Form that, like the sun, illuminates and makes all other Forms knowable. It is the source of truth and reality for all other Forms.",
            "category": "Forms Theory"
        },
        {
            "id": 6,
            "question": "In Plato's Divided Line analogy, which represents the highest level of knowledge?",
            "options": [
                "Images and shadows (eikasia)",
                "Physical objects (pistis)", 
                "Mathematical reasoning (dianoia)",
                "Knowledge of Forms through dialectic (noesis)"
            ],
            "correct": 3,
            "explanation": "Noesis, or knowledge of Forms through philosophical dialectic, represents the highest level of knowledge in Plato's epistemological hierarchy.",
            "category": "Forms Theory"
        },
        {
            "id": 7,
            "question": "Which of these would Plato consider closer to true reality?",
            "options": [
                "A photograph of a beautiful sunset",
                "The actual sunset in the physical world",
                "The mathematical equations describing light and color",
                "The Form of Beauty itself"
            ],
            "correct": 3,
            "explanation": "The Form of Beauty itself would be closest to true reality, as it is the eternal, perfect standard that all beautiful things imperfectly copy or participate in.",
            "category": "Forms Theory"
        },
        {
            "id": 8,
            "question": "What does Plato mean when he says philosophers should rule?",
            "options": [
                "Philosophers are naturally more ambitious than others",
                "Only philosophers have seen true reality and can guide others toward it",
                "Philosophers are better at making money than others",
                "Philosophy is the easiest subject to master"
            ],
            "correct": 1,
            "explanation": "Philosophers should rule because they have achieved knowledge of the Forms, especially the Form of Good, and can therefore guide society based on true knowledge rather than mere opinion.",
            "category": "Forms Theory"
        },

        # Cave Allegory (Questions 9-16)
        {
            "id": 9,
            "question": "In the Cave Allegory, what do the shadows on the wall represent?",
            "options": [
                "Evil or false ideas that deceive people",
                "Sensory experiences that we mistake for ultimate reality",
                "Mathematical concepts that are hard to understand", 
                "Political propaganda used to control people"
            ],
            "correct": 1,
            "explanation": "The shadows represent all the sensory experiences and appearances that we typically take to be reality, when they're actually just copies of deeper truths.",
            "category": "Cave Allegory"
        },
        {
            "id": 10,
            "question": "What does the journey from cave to sunlight represent?",
            "options": [
                "Growing up and becoming an adult",
                "The process of philosophical education and enlightenment",
                "Escaping from political oppression",
                "Learning to use your physical senses better"
            ],
            "correct": 1,
            "explanation": "The journey represents education (paideia) - the process of philosophical learning that moves us from ignorance to knowledge, from opinion to understanding.",
            "category": "Cave Allegory"
        },
        {
            "id": 11,
            "question": "Why does the escaped prisoner return to the cave?",
            "options": [
                "He realizes the outside world was just another illusion",
                "He wants to rule over the other prisoners",
                "He feels a duty to help others reach enlightenment",
                "He is forced to return against his will"
            ],
            "correct": 2,
            "explanation": "Plato believed philosophers have a moral obligation to return and help others achieve understanding, even if they face ridicule or resistance.",
            "category": "Cave Allegory"
        },
        {
            "id": 12,
            "question": "According to Plato, why do people resist philosophical truth?",
            "options": [
                "Because they are naturally evil or stupid",
                "Because truth is painful and they prefer comfortable illusions",
                "Because philosophers explain things poorly",
                "Because there is no real truth to discover"
            ],
            "correct": 1,
            "explanation": "Plato suggests that people resist truth because it's challenging and disruptive to their existing beliefs - like how bright light hurts eyes accustomed to darkness.",
            "category": "Cave Allegory"
        },
        {
            "id": 13,
            "question": "In the Cave Allegory, what does the fire inside the cave represent?",
            "options": [
                "The Form of the Good",
                "Human reason and intelligence",
                "The physical sun that illuminates the material world",
                "The evil that keeps people chained"
            ],
            "correct": 2,
            "explanation": "The fire represents the physical sun and the source of illumination in the material world, as opposed to the actual sun outside which represents the Form of the Good.",
            "category": "Cave Allegory"
        },
        {
            "id": 14,
            "question": "What do the chains in the Cave Allegory symbolize?",
            "options": [
                "Physical imprisonment by tyrants",
                "Economic poverty and lack of resources",
                "Ignorance, prejudice, and false beliefs that prevent seeing truth",
                "The natural limitations of human senses"
            ],
            "correct": 2,
            "explanation": "The chains represent ignorance, prejudice, and false beliefs that prevent people from turning toward truth and achieving philosophical enlightenment.",
            "category": "Cave Allegory"
        },
        {
            "id": 15,
            "question": "In Plato's Cave, why would the prisoners likely kill the returning philosopher?",
            "options": [
                "Because he has become physically dangerous",
                "Because they fear losing their comfortable illusions and reject disturbing truths",
                "Because he demands to be their ruler",
                "Because he has lost his ability to see shadows clearly"
            ],
            "correct": 1,
            "explanation": "The prisoners would reject and potentially harm the philosopher because his message threatens their comfortable worldview and forces them to confront the possibility that their entire reality is illusory.",
            "category": "Cave Allegory"
        },
        {
            "id": 16,
            "question": "Which modern phenomenon best parallels Plato's Cave?",
            "options": [
                "People reading books in libraries",
                "Social media echo chambers that reinforce existing beliefs",
                "Students learning mathematics in school",
                "Scientists conducting experiments in laboratories"
            ],
            "correct": 1,
            "explanation": "Social media echo chambers create environments where people see only information that confirms their existing beliefs, much like prisoners seeing only shadows that confirm their limited worldview.",
            "category": "Cave Allegory"
        },

        # Plato's Psychology/Soul (Questions 17-28)
        {
            "id": 17,
            "question": "According to Plato's tripartite theory, which part of the soul should rule?",
            "options": [
                "Appetite (epithumia) because it drives us to survive",
                "Spirit (thumos) because it gives us courage",
                "Reason (logos) because it can know truth and goodness",
                "All three parts should rule equally"
            ],
            "correct": 2,
            "explanation": "Reason should rule because only reason can grasp the Forms, understand truth, and determine what is truly good for the whole person.",
            "category": "Plato's Psychology"
        },
        {
            "id": 18,
            "question": "In Plato's chariot metaphor, what does the charioteer represent?",
            "options": [
                "The body that carries the soul",
                "Reason that must control and direct the horses of spirit and appetite",
                "The physical world that constrains the soul",
                "Death that ends the soul's journey"
            ],
            "correct": 1,
            "explanation": "The charioteer represents reason, which must skillfully control and direct the two horses (spirit and appetite) to achieve harmony and reach truth.",
            "category": "Plato's Psychology"
        },
        {
            "id": 19,
            "question": "According to Plato, what happens when appetite rules over reason?",
            "options": [
                "The person achieves perfect happiness",
                "The person becomes more creative and spontaneous",
                "The person becomes enslaved to desires and loses the ability to control them",
                "The person develops better physical health"
            ],
            "correct": 2,
            "explanation": "When appetite dominates, people become enslaved by their desires and lose self-control, making it impossible to achieve true happiness or virtue.",
            "category": "Plato's Psychology"
        },
        {
            "id": 20,
            "question": "What virtue corresponds to the spirit (thumos) part of the soul in Plato's theory?",
            "options": [
                "Wisdom (sophia)",
                "Courage (andreia)", 
                "Temperance (sophrosyne)",
                "Justice (dikaiosyne)"
            ],
            "correct": 1,
            "explanation": "Courage corresponds to spirit - when spirit is properly trained to support reason, it manifests as courage in facing challenges and defending what is right.",
            "category": "Plato's Psychology"
        },
        {
            "id": 21,
            "question": "How does Plato argue for the immortality of the soul?",
            "options": [
                "The soul is made of indestructible atoms",
                "The soul can grasp eternal, unchanging Forms, so it must itself be eternal",
                "The soul is too small to be destroyed",
                "Religious texts prove the soul is immortal"
            ],
            "correct": 1,
            "explanation": "Plato argues that since the soul can understand eternal, unchanging Forms, it must share their eternal nature and therefore survive bodily death.",
            "category": "Plato's Psychology"
        },
        {
            "id": 22,
            "question": "What does Plato's 'recollection' theory suggest about learning?",
            "options": [
                "We learn everything through sensory experience",
                "Learning is impossible without good teachers",
                "Learning is actually remembering truths our soul knew before birth",
                "Learning only happens through memorization"
            ],
            "correct": 2,
            "explanation": "The recollection theory suggests that learning involves remembering knowledge our souls acquired before birth through direct contact with the Forms.",
            "category": "Plato's Psychology"
        },
        {
            "id": 23,
            "question": "In Plato's view, what distinguishes humans from animals?",
            "options": [
                "Only humans have appetites and desires",
                "Only humans have emotions and feelings",
                "Only humans have rational souls that can grasp eternal truths",
                "Only humans are made of physical matter"
            ],
            "correct": 2,
            "explanation": "According to Plato, humans are unique because they have rational souls capable of grasping eternal Forms and abstract truths, unlike animals who lack this rational capacity.",
            "category": "Plato's Psychology"
        },
        {
            "id": 24,
            "question": "What does individual justice mean in Plato's psychology?",
            "options": [
                "Obeying all laws and social customs",
                "Each part of the soul performing its proper function under reason's rule",
                "Treating everyone exactly the same way",
                "Following whatever desires are strongest"
            ],
            "correct": 1,
            "explanation": "Individual justice occurs when reason rules, spirit courageously supports reason, and appetite obeys - each part fulfilling its proper role in harmony.",
            "category": "Plato's Psychology"
        },
        {
            "id": 25,
            "question": "According to Plato, why do internal conflicts arise in people?",
            "options": [
                "Because people have too many choices in life",
                "Because spirit and appetite rebel against reason's authority",
                "Because society imposes too many rules",
                "Because people don't get enough sleep"
            ],
            "correct": 1,
            "explanation": "Internal conflicts arise when spirit (emotions/pride) or appetite (physical desires) rebel against reason's rightful authority, creating disharmony in the soul.",
            "category": "Plato's Psychology"
        },
        {
            "id": 26,
            "question": "What role does philosophical education play in Plato's psychology?",
            "options": [
                "It teaches people how to satisfy their appetites more effectively",
                "It strengthens reason's ability to govern spirit and appetite",
                "It eliminates spirit and appetite entirely",
                "It proves that reason is unnecessary for happiness"
            ],
            "correct": 1,
            "explanation": "Philosophical education trains and strengthens reason so it can effectively govern the other parts of the soul and achieve psychological harmony.",
            "category": "Plato's Psychology"
        },
        {
            "id": 27,
            "question": "In the Phaedrus, Plato describes the soul's wings. What do these wings represent?",
            "options": [
                "The soul's ability to fly in the physical world",
                "The soul's power to ascend to the realm of Forms through love of truth and beauty",
                "The soul's capacity for rapid thinking",
                "The soul's connection to birds and nature"
            ],
            "correct": 1,
            "explanation": "The soul's wings represent its power to ascend to the realm of Forms through philosophical love (eros) of truth and beauty, rising above the material world.",
            "category": "Plato's Psychology"
        },
        {
            "id": 28,
            "question": "What happens to the soul after death according to Plato?",
            "options": [
                "It ceases to exist entirely",
                "It remains trapped in the grave with the body",
                "It is judged and may be reincarnated based on how philosophically it lived",
                "It automatically goes to paradise regardless of how it lived"
            ],
            "correct": 2,
            "explanation": "Plato believed souls are judged after death and reincarnated based on their philosophical development - those who lived rationally get better rebirths.",
            "category": "Plato's Psychology"
        },

        # Aristotle's Critique (Questions 29-36)
        {
            "id": 29,
            "question": "What is Aristotle's 'Third Man' argument against Plato's Forms?",
            "options": [
                "There must be three versions of every Form",
                "If humans resemble the Form of Human, we need another Form to explain that resemblance, leading to infinite regress",
                "Only three people can understand each Form",
                "Forms exist in groups of three"
            ],
            "correct": 1,
            "explanation": "The Third Man argument shows that Plato's theory leads to infinite regress - if we need Forms to explain resemblances, we need additional Forms to explain those resemblances, ad infinitum.",
            "category": "Aristotle's Critique"
        },
        {
            "id": 30,
            "question": "How does Aristotle's view of the soul differ from Plato's?",
            "options": [
                "Aristotle denies that humans have souls at all",
                "Aristotle thinks the soul is the form or organization of the body, not a separate substance",
                "Aristotle believes souls exist only in animals, not humans",
                "Aristotle thinks there are four parts to the soul instead of three"
            ],
            "correct": 1,
            "explanation": "Aristotle views the soul as the form, structure, or organization of a living body, not as a separate immaterial substance that can exist independently.",
            "category": "Aristotle's Critique"
        },
        {
            "id": 31,
            "question": "What is the 'participation problem' that Aristotle raises against Plato?",
            "options": [
                "Too many people want to participate in philosophy",
                "Plato never explains how material things actually 'participate in' separate Forms",
                "Forms don't want to participate in the material world",
                "Participation requires physical contact, which is impossible"
            ],
            "correct": 1,
            "explanation": "Aristotle points out that Plato never clearly explains the actual mechanism by which material objects 'participate in' or connect to separate, immaterial Forms.",
            "category": "Aristotle's Critique"
        },
        {
            "id": 32,
            "question": "According to Aristotle, what makes humans unique among animals?",
            "options": [
                "Humans are the only animals with souls",
                "Humans are the only animals that can move",
                "Humans are the only animals with rational capacity for abstract thought",
                "Humans are the only animals that need food"
            ],
            "correct": 2,
            "explanation": "While all living things have souls (vegetative for plants, sensitive for animals), only humans have rational souls capable of abstract thought and reasoning.",
            "category": "Aristotle's Critique"
        },
        {
            "id": 33,
            "question": "What are Aristotle's three types of soul?",
            "options": [
                "Vegetative (growth), sensitive (perception), rational (thought)",
                "Body, mind, and spirit",
                "Past, present, and future souls",
                "Good, neutral, and evil souls"
            ],
            "correct": 0,
            "explanation": "Aristotle distinguished vegetative souls (nutrition/growth), sensitive souls (perception/movement), and rational souls (abstract thought) in a hierarchy of complexity.",
            "category": "Aristotle's Critique"
        },
        {
            "id": 34,
            "question": "Does Aristotle believe in personal immortality?",
            "options": [
                "Yes, definitely - all souls survive death",
                "No, definitely - no part of the soul survives",
                "It's unclear - he sometimes suggests the rational part might survive",
                "Only animal souls survive, not human souls"
            ],
            "correct": 2,
            "explanation": "Aristotle's position is ambiguous - while generally viewing the soul as bodily organization, he sometimes suggests the rational aspect might survive, leading to scholarly debate.",
            "category": "Aristotle's Critique"
        },
        {
            "id": 35,
            "question": "How does Aristotle's approach to universals differ from Plato's Forms?",
            "options": [
                "Aristotle denies that universals exist at all",
                "Aristotle locates universals in particular objects rather than a separate realm",
                "Aristotle thinks universals are more important than Plato did",
                "Aristotle believes in exactly the same Forms as Plato"
            ],
            "correct": 1,
            "explanation": "Rather than existing in a separate realm, Aristotle argues that universals exist in the particular objects themselves - the universal 'humanity' exists in individual humans.",
            "category": "Aristotle's Critique"
        },
        {
            "id": 36,
            "question": "What does Aristotle mean by saying the soul is to the body as shape is to wax?",
            "options": [
                "Souls can be molded like wax",
                "The soul is the form or organization of matter, not a separate substance",
                "Bodies are made of wax-like material", 
                "Souls leave impressions on bodies like stamps on wax"
            ],
            "correct": 1,
            "explanation": "This analogy illustrates that the soul is the form, structure, or organization of bodily matter - inseparable from it, just as shape cannot exist apart from the wax.",
            "category": "Aristotle's Critique"
        },

        # Human Nature Theories (Questions 37-52)
        {
            "id": 37,
            "question": "According to Thomas Hobbes' materialist view, humans are essentially:",
            "options": [
                "Rational souls temporarily inhabiting physical bodies",
                "Complex physical machines driven by self-interest",
                "Divine beings made in God's image",
                "Naturally good creatures corrupted by society"
            ],
            "correct": 1,
            "explanation": "Hobbes argued for psychological egoism - humans are material beings whose behavior can be explained entirely through physical causes and self-interested motivations.",
            "category": "Human Nature"
        },
        {
            "id": 38,
            "question": "What is 'psychological egoism' as defended by philosophers like Hobbes?",
            "options": [
                "The view that people should be selfish",
                "The descriptive claim that all human actions are ultimately motivated by self-interest",
                "The idea that psychology is the most important science",
                "The belief that egos are psychological constructs"
            ],
            "correct": 1,
            "explanation": "Psychological egoism is a descriptive theory claiming that humans always act from self-interested motives, even when actions appear altruistic.",
            "category": "Human Nature"
        },
        {
            "id": 39,
            "question": "How does the Judeo-Christian view of human nature differ from Greek rationalism?",
            "options": [
                "It denies that humans have rational capacities",
                "It adds the concept of humans being made in God's image with moral will",
                "It rejects the idea that humans have souls",
                "It claims humans are naturally perfect"
            ],
            "correct": 1,
            "explanation": "The Judeo-Christian view incorporates Greek rationalism but adds that humans are made in God's image, have free will, and bear moral responsibility for choosing good or evil.",
            "category": "Human Nature"
        },
        {
            "id": 40,
            "question": "According to Augustine, what are the three disordered desires that corrupt human will?",
            "options": [
                "Reason, spirit, and appetite",
                "Lust, curiosity, and pride", 
                "Faith, hope, and charity",
                "Mind, body, and soul"
            ],
            "correct": 1,
            "explanation": "Augustine identified lust (for physical pleasures), curiosity (for new experiences), and pride (for others' approval) as the three disordered desires that lead people away from God.",
            "category": "Human Nature"
        },
        {
            "id": 41,
            "question": "What does Augustine mean by saying Forms exist 'in the mind of God'?",
            "options": [
                "God is confused and thinks about Forms all the time",
                "Forms are God's eternal ideas or blueprints for creation",
                "God created Forms as separate beings",
                "Forms control God's thoughts"
            ],
            "correct": 1,
            "explanation": "Augustine solved the problem of where eternal Forms exist by locating them as eternal ideas in God's mind - the divine blueprints or patterns for creation.",
            "category": "Human Nature"
        },
        {
            "id": 42,
            "question": "According to Mark Mercer's introspective argument, what do we find when we examine our own motivations?",
            "options": [
                "We always act from pure altruism",
                "We expect some form of self-regarding benefit from our actions",
                "We never have any motivations at all",
                "We are completely unconscious of our motivations"
            ],
            "correct": 1,
            "explanation": "Mercer argues that honest introspection reveals we always expect some self-regarding end (pleasure, satisfaction, meaning) from our intentional actions.",
            "category": "Human Nature"
        },
        {
            "id": 43,
            "question": "How might evolutionary biology challenge traditional views of altruism?",
            "options": [
                "Evolution proves altruism never exists in any form",
                "Apparently altruistic behaviors may serve genetic self-interest",
                "Evolution shows humans are naturally evil",
                "Biology has nothing to say about altruism"
            ],
            "correct": 1,
            "explanation": "Evolutionary explanations suggest apparently selfless behaviors may actually serve genetic self-interest by helping relatives who share our genes survive and reproduce.",
            "category": "Human Nature"
        },
        {
            "id": 44,
            "question": "What practical difference does your view of human nature make?",
            "options": [
                "It has no practical consequences whatsoever",
                "It affects how you relate to others, what political systems you support, and how you make moral judgments",
                "It only matters for academic philosophers",
                "It determines what food you like"
            ],
            "correct": 1,
            "explanation": "Views of human nature profoundly influence relationships, political preferences, moral judgments, educational approaches, and expectations about human behavior.",
            "category": "Human Nature"
        },
        {
            "id": 45,
            "question": "According to Jeremy Bentham's utilitarian view, what motivates human behavior?",
            "options": [
                "The desire to follow moral rules",
                "The pursuit of pleasure and avoidance of pain",
                "The quest for knowledge and truth",
                "Religious devotion and spiritual growth"
            ],
            "correct": 1,
            "explanation": "Bentham argued that humans are governed by two sovereign masters - pleasure and pain - and that all actions aim to maximize pleasure and minimize pain.",
            "category": "Human Nature"
        },
        {
            "id": 46,
            "question": "What is the 'Traditional Western View' of human nature?",
            "options": [
                "Humans are essentially rational beings with immaterial souls",
                "Humans are purely physical machines with no special properties",
                "Humans are naturally evil and need strict control",
                "Humans are perfect beings who never make mistakes"
            ],
            "correct": 0,
            "explanation": "The Traditional Western View, influenced by Greek philosophy and Christianity, holds that humans are rational beings with immaterial souls that have a purpose and endure over time.",
            "category": "Human Nature"
        },
        {
            "id": 47,
            "question": "How was Aristotle's hierarchy of natural slavery misused historically?",
            "options": [
                "It was used to justify the enslavement of Indigenous peoples and Africans",
                "It was used to promote universal human equality",
                "It had no historical impact whatsoever",
                "It was only used to organize school curricula"
            ],
            "correct": 0,
            "explanation": "Aristotle's claim that some humans are 'natural slaves' was tragically misappropriated to justify the enslavement and oppression of Indigenous peoples, Africans, and others deemed 'less rational.'",
            "category": "Human Nature"
        },
        {
            "id": 48,
            "question": "What does Freud's view of human nature emphasize?",
            "options": [
                "Humans are naturally good and rational",
                "Humans are driven by unconscious desires for aggression and sexuality",
                "Humans have no nature at all",
                "Humans are purely spiritual beings"
            ],
            "correct": 1,
            "explanation": "Freud emphasized that human behavior is largely driven by unconscious desires, particularly aggressive and sexual impulses that civilized society attempts to control.",
            "category": "Human Nature"
        },

        # Contemporary Applications (Questions 49-64)
        {
            "id": 49,
            "question": "How might Plato's Cave apply to social media?",
            "options": [
                "Social media helps us see reality more clearly",
                "Social media creates echo chambers where we see only information that confirms our beliefs",
                "Social media has nothing to do with philosophy",
                "Social media eliminates all illusions"
            ],
            "correct": 1,
            "explanation": "Social media algorithms often create echo chambers that show us only information confirming our existing beliefs, much like prisoners seeing only shadows that reinforce their limited worldview.",
            "category": "Contemporary"
        },
        {
            "id": 50,
            "question": "What is the 'hard problem of consciousness' in modern philosophy of mind?",
            "options": [
                "Consciousness is too hard for ordinary people to understand",
                "How subjective, first-person experience arises from objective brain processes",
                "Why some people are more conscious than others",
                "How to measure consciousness scientifically"
            ],
            "correct": 1,
            "explanation": "The hard problem asks how subjective, qualitative experience (qualia) emerges from objective, physical brain processes - why there's 'something it's like' to be conscious.",
            "category": "Contemporary"
        },
        {
            "id": 51,
            "question": "How do near-death experiences (NDEs) relate to the debate about immaterial souls?",
            "options": [
                "They definitively prove souls exist",
                "They definitively prove souls don't exist", 
                "They provide potential evidence for soul-body separation but remain scientifically controversial",
                "They have nothing to do with soul theories"
            ],
            "correct": 2,
            "explanation": "NDEs are interpreted differently - dualists see them as evidence for soul-body separation, while materialists explain them through brain chemistry during cardiac arrest.",
            "category": "Contemporary"
        },
        {
            "id": 52,
            "question": "What would Plato likely think about virtual reality technology?",
            "options": [
                "VR is the ultimate reality humans should strive for",
                "VR creates even more layers of illusion, moving us further from truth",
                "VR has no philosophical significance",
                "VR perfectly represents the world of Forms"
            ],
            "correct": 1,
            "explanation": "Plato would likely view VR as creating additional layers of illusion and appearance, moving us even further away from direct knowledge of eternal Forms and truth.",
            "category": "Contemporary"
        },
        {
            "id": 53,
            "question": "How does artificial intelligence challenge traditional views of human uniqueness?",
            "options": [
                "AI proves humans have no special qualities",
                "AI forces us to reconsider what makes humans unique - consciousness, creativity, or moral agency",
                "AI confirms that humans are the only rational beings",
                "AI has no relevance to human nature"
            ],
            "correct": 1,
            "explanation": "As AI systems become more sophisticated, we're forced to reconsider what truly distinguishes humans - is it consciousness, creativity, emotions, or moral responsibility?",
            "category": "Contemporary"
        },
        {
            "id": 54,
            "question": "What is 'mathematical Platonism' in contemporary philosophy?",
            "options": [
                "The view that mathematics is too difficult for most people",
                "The view that mathematical objects exist independently of human minds",
                "The view that Plato was good at mathematics",
                "The view that mathematics should not be taught"
            ],
            "correct": 1,
            "explanation": "Mathematical Platonism holds that numbers, equations, and geometric objects exist independently of human minds, much like Plato's eternal Forms.",
            "category": "Contemporary"
        },
        {
            "id": 55,
            "question": "How might deepfake technology relate to Plato's concerns about appearance vs. reality?",
            "options": [
                "Deepfakes make reality clearer than ever",
                "Deepfakes create increasingly convincing false appearances, making it harder to distinguish truth from illusion",
                "Deepfakes have no philosophical implications",
                "Deepfakes solve the problem of appearance vs. reality"
            ],
            "correct": 1,
            "explanation": "Deepfakes create incredibly convincing false appearances, exemplifying Plato's concern that we can easily mistake illusions for reality in our sensory experience.",
            "category": "Contemporary"
        },
        {
            "id": 56,
            "question": "What does the 'simulation hypothesis' suggest?",
            "options": [
                "Computer simulations are always inaccurate",
                "We might be living inside a computer simulation created by advanced beings",
                "Simulations are the best way to learn",
                "Reality is definitely not a simulation"
            ],
            "correct": 1,
            "explanation": "The simulation hypothesis suggests that what we take to be reality might actually be a computer simulation, raising Platonic questions about the nature of ultimate reality.",
            "category": "Contemporary"
        },
        {
            "id": 57,
            "question": "How do modern neuroscience findings challenge dualist theories of mind?",
            "options": [
                "Neuroscience proves dualism is correct",
                "Brain studies show strong correlations between mental states and brain states, suggesting mind depends on brain",
                "Neuroscience has nothing to say about the mind",
                "Neuroscience proves the soul exists in the brain"
            ],
            "correct": 1,
            "explanation": "Neuroscience shows strong correlations between mental states and brain states, and that brain damage affects personality and consciousness, challenging the idea of an independent immaterial soul.",
            "category": "Contemporary"
        },
        {
            "id": 58,
            "question": "What ethical questions arise if artificial intelligences become conscious?",
            "options": [
                "No ethical questions would arise",
                "We would need to consider their rights, moral status, and how we treat them",
                "We should immediately destroy all AI",
                "Only humans can ever have moral status"
            ],
            "correct": 1,
            "explanation": "If AIs become conscious, we'd face questions about their moral rights, whether it's wrong to harm them, and how to determine their moral status - consciousness or souls as the basis for rights.",
            "category": "Contemporary"
        },
        {
            "id": 59,
            "question": "How does evolutionary psychology explain apparently altruistic behavior?",
            "options": [
                "It proves altruism never exists",
                "It suggests helping relatives helps our genes survive, so 'altruism' serves genetic self-interest",
                "It shows humans are naturally evil",
                "It proves God created altruism"
            ],
            "correct": 1,
            "explanation": "Evolutionary psychology suggests that helping relatives who share our genes serves genetic self-interest, making apparently altruistic behavior actually self-interested at the genetic level.",
            "category": "Contemporary"
        },
        {
            "id": 60,
            "question": "What might Plato think about social media 'influencers'?",
            "options": [
                "They are philosopher-kings who should rule society",
                "They are like the prisoners casting shadows in the cave, creating illusions that distract from truth",
                "They represent the ideal form of communication",
                "They have no relevance to his philosophy"
            ],
            "correct": 1,
            "explanation": "Plato would likely see influencers as similar to the shadow-casters in the cave, creating appealing illusions and appearances that distract people from pursuing genuine knowledge and truth.",
            "category": "Contemporary"
        },

        # Philosophical Argumentation & Critical Thinking (Questions 61-72)
        {
            "id": 61,
            "question": "What makes a philosophical argument valid?",
            "options": [
                "The conclusion is true",
                "The premises are true",
                "If the premises were true, the conclusion would necessarily follow",
                "Everyone agrees with it"
            ],
            "correct": 2,
            "explanation": "A valid argument is one where the conclusion necessarily follows from the premises - if the premises were true, the conclusion would have to be true, regardless of whether the premises are actually true.",
            "category": "Argumentation"
        },
        {
            "id": 62,
            "question": "What makes a philosophical argument sound?",
            "options": [
                "It is both valid and has true premises",
                "It sounds convincing when spoken aloud",
                "It uses sophisticated vocabulary",
                "It cites many famous philosophers"
            ],
            "correct": 0,
            "explanation": "A sound argument is both valid (conclusion follows from premises) and has true premises, which guarantees the conclusion is true.",
            "category": "Argumentation"
        },
        {
            "id": 63,
            "question": "What is a 'categorical argument' in logic?",
            "options": [
                "An argument that's categorically wrong",
                "An argument using categorical statements about class membership (All X are Y, Some X are Y, etc.)",
                "An argument made by Aristotle",
                "An argument that creates categories"
            ],
            "correct": 1,
            "explanation": "Categorical arguments use statements about class membership and relationships between categories, like 'All humans are mortal,' 'Some dogs are friendly,' etc.",
            "category": "Argumentation"
        },
        {
            "id": 64,
            "question": "What is the difference between a priori and a posteriori knowledge?",
            "options": [
                "A priori comes before a posteriori chronologically",
                "A priori knowledge is independent of experience; a posteriori depends on experience",
                "A priori is easier than a posteriori",
                "There is no difference"
            ],
            "correct": 1,
            "explanation": "A priori knowledge (like mathematical truths) can be known independently of sensory experience, while a posteriori knowledge (like empirical facts) requires experience.",
            "category": "Argumentation"
        },

        # Synthesis & Application Questions (Questions 65-80)
        {
            "id": 65,
            "question": "If Plato is correct about Forms, what would this mean for scientific knowledge?",
            "options": [
                "Science would be impossible",
                "Science discovers eternal mathematical relationships that exist independently of the physical world",
                "Science would be purely subjective",
                "Science would have no connection to mathematics"
            ],
            "correct": 1,
            "explanation": "If Forms exist, scientific laws might be discoveries of eternal mathematical relationships in the realm of Forms, giving science objective validity beyond mere descriptions of changing appearances.",
            "category": "Synthesis"
        },
        {
            "id": 66,
            "question": "How might someone defend Plato's Forms against Aristotle's Third Man argument?",
            "options": [
                "Deny that resemblance needs explanation",
                "Argue that the Form of Resemblance is fundamentally different from other Forms",
                "Accept infinite regress as not necessarily problematic",
                "All of the above are possible defensive strategies"
            ],
            "correct": 3,
            "explanation": "Defenders of Plato might use various strategies: denying resemblance needs explanation, arguing the Form of Resemblance is special, or accepting that infinite regress isn't necessarily problematic.",
            "category": "Synthesis"
        },
        {
            "id": 67,
            "question": "If psychological egoism is true, how might this affect criminal justice policy?",
            "options": [
                "It would support rehabilitation over punishment, since people act from self-interest that can be redirected",
                "It would support harsh punishment, since people only respond to threats",
                "It would have no effect on policy",
                "Both A and B are possible implications"
            ],
            "correct": 3,
            "explanation": "Psychological egoism could support either rehabilitation (redirecting self-interest toward legal behavior) or punishment (deterring through fear), depending on what most effectively influences self-interested behavior.",
            "category": "Synthesis"
        },
        {
            "id": 68,
            "question": "What would be the strongest evidence against Plato's theory of recollection?",
            "options": [
                "People sometimes forget things they learned",
                "Cultural differences in mathematical and moral concepts across societies",
                "The fact that learning requires teaching",
                "Brain damage affecting memory and reasoning"
            ],
            "correct": 1,
            "explanation": "If souls have innate knowledge of eternal truths, we wouldn't expect significant cultural variation in mathematical or moral concepts, yet such variation exists across human societies.",
            "category": "Synthesis"
        },
        {
            "id": 69,
            "question": "How might a materialist explain moral intuitions without appealing to a Form of Justice?",
            "options": [
                "Moral intuitions are illusions with no real basis",
                "Evolution shaped moral intuitions because cooperation helped group survival",
                "Moral intuitions come from social conditioning alone",
                "All of the above are materialist strategies"
            ],
            "correct": 3,
            "explanation": "Materialists can explain moral intuitions through evolutionary adaptation, social conditioning, cultural learning, or as useful illusions, without requiring eternal Forms.",
            "category": "Synthesis"
        },
        {
            "id": 70,
            "question": "If consciousness could be uploaded to a computer, what would this mean for theories of personal identity?",
            "options": [
                "It would prove the soul is immaterial",
                "It would suggest personal identity is based on information patterns rather than physical substance",
                "It would be impossible by definition",
                "It would prove consciousness doesn't exist"
            ],
            "correct": 1,
            "explanation": "Successful consciousness uploading would suggest that personal identity consists in information patterns or functional organization rather than specific material substances like souls or brains.",
            "category": "Synthesis"
        },
        {
            "id": 71,
            "question": "How might Plato's political philosophy relate to modern debates about expertise vs. democracy?",
            "options": [
                "Plato would support direct democracy where everyone votes on everything",
                "Plato would favor rule by experts (technocracy) over popular opinion",
                "Plato would think political systems don't matter",
                "Plato would support random selection of leaders"
            ],
            "correct": 1,
            "explanation": "Plato argued that philosopher-kings who know the Form of Justice should rule, suggesting he'd favor technocracy where experts make decisions based on knowledge rather than popular opinion.",
            "category": "Synthesis"
        },
        {
            "id": 72,
            "question": "What is the relationship between Plato's epistemology (theory of knowledge) and his metaphysics (theory of reality)?",
            "options": [
                "They are completely unrelated",
                "Knowledge of eternal Forms is possible because the soul is immortal and shares their eternal nature",
                "Metaphysics is less important than epistemology",
                "They contradict each other"
            ],
            "correct": 1,
            "explanation": "Plato's theories are integrated - we can have knowledge of eternal, unchanging Forms because our souls are themselves eternal and immaterial, capable of grasping what is like them.",
            "category": "Synthesis"
        },
        {
            "id": 73,
            "question": "How does Augustine's emphasis on will differ from Plato's emphasis on reason?",
            "options": [
                "Augustine rejects reason entirely",
                "Augustine adds that knowing the good isn't enough - we need grace to will the good",
                "Augustine thinks will is less important than reason",
                "There is no difference between them"
            ],
            "correct": 1,
            "explanation": "While Plato thought knowledge of the Good would lead to virtue, Augustine recognized that humans can know what's right but still choose evil, requiring divine grace to empower the will.",
            "category": "Synthesis"
        },
        {
            "id": 74,
            "question": "If we discovered that all human behavior could be perfectly predicted by brain scans, what would this mean for free will?",
            "options": [
                "It would prove free will exists",
                "It would challenge the reality of free will and moral responsibility",
                "It would have no implications for free will",
                "It would only affect criminal behavior"
            ],
            "correct": 1,
            "explanation": "Perfect predictability from brain states would suggest our choices are determined by prior physical causes, challenging traditional notions of free will and moral responsibility.",
            "category": "Synthesis"
        },
        {
            "id": 75,
            "question": "What would Aristotle likely think about modern cognitive science research on reasoning?",
            "options": [
                "It would completely contradict his philosophy",
                "It would support his view that rational thinking is a natural capacity that can be developed",
                "It would prove that reason doesn't exist",
                "It would have no relevance to his philosophy"
            ],
            "correct": 1,
            "explanation": "Research showing that reasoning is a natural human capacity that improves with practice and education would likely support Aristotle's view of rationality as a developed natural function.",
            "category": "Synthesis"
        },
        {
            "id": 76,
            "question": "How might the discovery of alien intelligence affect traditional Western views of human nature?",
            "options": [
                "It would have no effect on theories of human nature",
                "It would challenge the uniqueness of human rationality and might expand concepts of personhood",
                "It would prove that humans have souls",
                "It would disprove all philosophy"
            ],
            "correct": 1,
            "explanation": "Rational alien life would challenge human uniqueness and force us to reconsider what makes beings valuable - consciousness, rationality, or specifically human souls.",
            "category": "Synthesis"
        },
        {
            "id": 77,
            "question": "What is the strongest objection to Mercer's psychological egoism argument?",
            "options": [
                "People sometimes act impulsively without thinking",
                "Anonymous charitable giving where the giver receives no recognition or satisfaction",
                "Some people claim they don't expect any self-regarding benefit",
                "Evolutionary biology explains altruism"
            ],
            "correct": 1,
            "explanation": "Anonymous giving with no personal recognition, satisfaction, or even knowledge of impact would be difficult to explain as self-regarding, challenging Mercer's introspective argument.",
            "category": "Synthesis"
        },
        {
            "id": 78,
            "question": "How do reincarnation beliefs in Plato's philosophy relate to modern debates about personal identity?",
            "options": [
                "They are completely unrelated topics",
                "Both concern what persists through radical changes to make you 'you' over time",
                "Reincarnation proves personal identity doesn't exist",
                "Modern philosophy has solved these issues"
            ],
            "correct": 1,
            "explanation": "Both reincarnation and personal identity debates address what essential aspect persists through dramatic changes - whether across lifetimes or throughout one lifetime.",
            "category": "Synthesis"
        },
        {
            "id": 79,
            "question": "If artificial intelligence achieved consciousness but lacked emotions, what would this reveal about human nature?",
            "options": [
                "It would prove emotions are essential to consciousness",
                "It would suggest rationality and emotion might be separable aspects of mind",
                "It would be impossible by definition",
                "It would prove AI can never be conscious"
            ],
            "correct": 1,
            "explanation": "Conscious but emotionless AI would suggest that Plato might have been right that reason can exist independently of appetite and emotion, challenging integrated views of mind.",
            "category": "Synthesis"
        },
        {
            "id": 80,
            "question": "What is the most fundamental question that all theories of human nature attempt to answer?",
            "options": [
                "How many people exist in the world?",
                "What distinguishes humans from other beings and what gives human life meaning and moral significance?",
                "What foods humans should eat?",
                "When did humans first appear on Earth?"
            ],
            "correct": 1,
            "explanation": "All theories of human nature ultimately address what makes humans special or distinctive and what gives human existence meaning, purpose, and moral worth.",
            "category": "Synthesis"
        }
    ]
}

def display_comprehensive_quiz():
    """Display the comprehensive 80-question quiz"""
    st.markdown("# 📝 Comprehensive Philosophy Assessment")
    st.markdown("## 80 Questions on Ancient Philosophy & Human Nature")
    
    with st.expander("📋 Quiz Information", expanded=True):
        st.markdown("""
        ### Coverage:
        - **Plato's Theory of Forms** (Questions 1-8)
        - **Cave Allegory** (Questions 9-16) 
        - **Plato's Psychology** (Questions 17-28)
        - **Aristotle's Critique** (Questions 29-36)
        - **Human Nature Theories** (Questions 37-48)
        - **Contemporary Applications** (Questions 49-60)
        - **Philosophical Argumentation** (Questions 61-64)
        - **Synthesis & Critical Analysis** (Questions 65-80)
        
        ### Instructions:
        - Answer all 80 questions
        - Take your time - this is designed for deep thinking
        - Each question includes detailed explanations
        - Results will show category-by-category performance
        """)
    
    # Quiz taking interface
    if st.button("Begin Comprehensive Assessment"):
        st.session_state.quiz_started = True
        st.session_state.current_question = 0
        st.session_state.answers = {}
    
    if st.session_state.get('quiz_started', False):
        display_quiz_interface()

def display_quiz_interface():
    """Display interactive quiz interface for comprehensive assessment"""
    current_q = st.session_state.get('current_question', 0)
    total_questions = len(COMPREHENSIVE_QUIZ['questions'])
    
    if current_q < total_questions:
        question = COMPREHENSIVE_QUIZ['questions'][current_q]
        
        # Progress bar
        progress = (current_q + 1) / total_questions
        st.progress(progress)
        st.caption(f"Question {current_q + 1} of {total_questions}")
        
        # Question display
        st.markdown(f"### Question {current_q + 1}")
        st.markdown(f"**Category:** {question['category']}")
        st.markdown(f"**{question['question']}**")
        
        # Answer options
        answer = st.radio(
            "Select your answer:",
            options=question['options'],
            key=f"question_{question['id']}",
            index=None
        )
        
        # Navigation buttons
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if current_q > 0 and st.button("⬅️ Previous"):
                st.session_state.current_question = current_q - 1
                st.rerun()
        
        with col2:
            if answer is not None and st.button("Next ➡️"):
                st.session_state.answers[question['id']] = {
                    'selected': question['options'].index(answer),
                    'correct': question['correct'],
                    'category': question['category']
                }
                st.session_state.current_question = current_q + 1
                st.rerun()
        
        with col3:
            if current_q == total_questions - 1 and answer is not None:
                if st.button("🏁 Finish Quiz"):
                    st.session_state.answers[question['id']] = {
                        'selected': question['options'].index(answer),
                        'correct': question['correct'], 
                        'category': question['category']
                    }
                    st.session_state.quiz_completed = True
                    st.rerun()
    
    elif st.session_state.get('quiz_completed', False):
        display_quiz_results()

def display_quiz_results():
    """Display comprehensive quiz results with detailed analysis"""
    answers = st.session_state.get('answers', {})
    questions = COMPREHENSIVE_QUIZ['questions']
    
    # Calculate overall score
    total_correct = sum(1 for ans in answers.values() if ans['selected'] == ans['correct'])
    total_questions = len(answers)
    overall_percentage = (total_correct / total_questions) * 100
    
    # Category breakdown
    category_stats = {}
    for ans_data in answers.values():
        cat = ans_data['category']
        if cat not in category_stats:
            category_stats[cat] = {'correct': 0, 'total': 0}
        category_stats[cat]['total'] += 1
        if ans_data['selected'] == ans_data['correct']:
            category_stats[cat]['correct'] += 1
    
    st.markdown("# 📊 Quiz Results")
    
    # Overall performance
    if overall_percentage >= 90:
        st.balloons()
        st.success(f"🌟 Outstanding! Score: {total_correct}/{total_questions} ({overall_percentage:.1f}%)")
        st.markdown("You demonstrate exceptional mastery of ancient philosophy and human nature theories!")
    elif overall_percentage >= 80:
        st.success(f"🎯 Excellent! Score: {total_correct}/{total_questions} ({overall_percentage:.1f}%)")
    elif overall_percentage >= 70:
        st.success(f"👍 Good work! Score: {total_correct}/{total_questions} ({overall_percentage:.1f}%)")
    elif overall_percentage >= 60:
        st.warning(f"📚 Fair progress. Score: {total_correct}/{total_questions} ({overall_percentage:.1f}%)")
        st.markdown("Consider reviewing the material and retaking sections where needed.")
    else:
        st.error(f"📖 More study needed. Score: {total_correct}/{total_questions} ({overall_percentage:.1f}%)")
        st.markdown("Focus on the fundamentals and work through the readings carefully.")
    
    # Category breakdown
    st.markdown("## 📈 Performance by Category")
    
    for category, stats in category_stats.items():
        percentage = (stats['correct'] / stats['total']) * 100
        st.markdown(f"**{category}:** {stats['correct']}/{stats['total']} ({percentage:.1f}%)")
        st.progress(percentage / 100)
    
    # Detailed answers with explanations
    if st.checkbox("📝 Show Detailed Answer Review"):
        st.markdown("## 🔍 Answer Review")
        
        for i, question in enumerate(questions):
            if question['id'] in answers:
                ans_data = answers[question['id']]
                is_correct = ans_data['selected'] == ans_data['correct']
                
                with st.expander(f"Q{i+1}: {question['question']} {'✅' if is_correct else '❌'}"):
                    st.markdown(f"**Your answer:** {question['options'][ans_data['selected']]}")
                    if not is_correct:
                        st.markdown(f"**Correct answer:** {question['options'][ans_data['correct']]}")
                    st.markdown(f"**Explanation:** {question['explanation']}")
    
    # Export results
    if st.button("📄 Download Results"):
        results_data = {
            'timestamp': datetime.now().isoformat(),
            'overall_score': f"{total_correct}/{total_questions} ({overall_percentage:.1f}%)",
            'category_breakdown': {cat: f"{stats['correct']}/{stats['total']} ({(stats['correct']/stats['total'])*100:.1f}%)" 
                                 for cat, stats in category_stats.items()},
            'detailed_answers': [
                {
                    'question': q['question'],
                    'selected': q['options'][answers[q['id']]['selected']] if q['id'] in answers else 'Not answered',
                    'correct': q['options'][q['correct']],
                    'is_correct': answers[q['id']]['selected'] == q['correct'] if q['id'] in answers else False,
                    'explanation': q['explanation']
                }
                for q in questions
            ]
        }
        
        json_str = json.dumps(results_data, indent=2)
        st.download_button(
            "Download Results",
            json_str,
            file_name=f"philosophy_quiz_results_{datetime.now().strftime('%Y%m%d_%H%M')}.json",
            mime="application/json"
        )

def enhanced_sidebar_navigation():
    """Enhanced sidebar with comprehensive navigation"""
    st.sidebar.markdown("# 🏛️ PHL 201 Enhanced")
    st.sidebar.markdown("**Ancient Philosophy & Human Nature**")
    
    # Mode selection with enhanced options
    mode = st.sidebar.radio(
        "Choose Mode:",
        ["📊 Presentation", "🧠 Comprehensive Quiz", "🎯 Topic Quizzes", "📚 Resources", "💭 Discussion Forums"]
    )
    
    if mode == "📊 Presentation":
        st.sidebar.markdown("## Slide Navigation")
        
        # Enhanced slide selector with categories
        slide_categories = {
            "Introduction": [0],
            "Plato's Forms": [1, 2],
            "Human Nature": [3, 4, 5],
            "Aristotle & Critique": [6],
            "Religious Synthesis": [7],
            "Modern Applications": [8]
        }
        
        selected_category = st.sidebar.selectbox("Jump to topic:", list(slide_categories.keys()))
        if selected_category:
            available_slides = slide_categories[selected_category]
            slide_titles = [f"{i+1}. {SLIDES[i]['title']}" for i in available_slides]
            selected_idx = st.sidebar.selectbox(
                "Select slide:",
                range(len(available_slides)),
                format_func=lambda x: slide_titles[x]
            )
            selected_slide = available_slides[selected_idx]
            
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
    
    elif mode == "🧠 Comprehensive Quiz":
        st.sidebar.markdown("## Quiz Progress")
        if st.session_state.get('quiz_started', False):
            current_q = st.session_state.get('current_question', 0)
            total_q = len(COMPREHENSIVE_QUIZ['questions'])
            progress = current_q / total_q
            st.sidebar.progress(progress)
            st.sidebar.markdown(f"Question {current_q + 1} of {total_q}")
        
        if st.sidebar.button("🔄 Reset Quiz"):
            for key in ['quiz_started', 'current_question', 'answers', 'quiz_completed']:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()
    
    return mode.split()[1].lower()

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
    
    # Simple text area for assignment submission
    st.markdown("## Write Your Revised Reflection")
    
    reflection_text = st.text_area(
        "Enter your revised reflection (300-400 words):",
        height=300,
        placeholder="Begin with a clear thesis about what Plato's Cave teaches us about reality and knowledge. Then connect it to the Theory of Forms, provide a modern example, and offer critical analysis..."
    )
    
    if reflection_text:
        word_count = len(reflection_text.split())
        if word_count < 300:
            st.warning(f"Word count: {word_count}/300 (minimum) - Need {300-word_count} more words")
        elif word_count > 400:
            st.warning(f"Word count: {word_count}/400 (maximum) - Remove {word_count-400} words")
        else:
            st.success(f"Word count: {word_count} - Perfect length!")
            
            if st.button("Submit Assignment"):
                st.balloons()
                st.success("Assignment submitted successfully!")

# Topic quizzes from original program
TOPIC_QUIZZES = {
    "plato_basics": {
        "title": "Plato's Theory of Forms",
        "questions": [
            {
                "question": "According to Plato, the
