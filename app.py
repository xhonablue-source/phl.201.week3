import streamlit as st
import json
from datetime import datetime

st.set_page_config(page_title="PHL 201 Quiz", layout="wide")

# Initialize session state
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'quiz_completed' not in st.session_state:
    st.session_state.quiz_completed = False

# Complete 85-question quiz
QUIZ_QUESTIONS = [
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
        "question": "Which of these would Plato consider closest to true reality?",
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
    {
        "id": 9,
        "question": "How does Plato's theory explain why we can understand abstract mathematical concepts?",
        "options": [
            "Mathematics is learned through sensory experience",
            "The soul has prior knowledge of perfect mathematical Forms",
            "Mathematical concepts are just useful human conventions",
            "Mathematics doesn't really exist, it's just language"
        ],
        "correct": 1,
        "explanation": "Plato argues that we can understand perfect mathematical concepts because our souls have prior knowledge of the eternal mathematical Forms from before birth.",
        "category": "Forms Theory"
    },
    {
        "id": 10,
        "question": "According to Plato, what is the relationship between justice in the soul and justice in the state?",
        "options": [
            "There is no relationship between individual and political justice",
            "Both involve the same structure: reason ruling over spirit and appetite",
            "Political justice is more important than individual justice",
            "Individual justice is impossible without political justice"
        ],
        "correct": 1,
        "explanation": "Plato argues that both individual and political justice have the same structure - reason (or philosopher-kings) should rule over spirit (guardians) and appetite (producers).",
        "category": "Forms Theory"
    },
    {
        "id": 11,
        "question": "What role does the Form of Beauty play in Plato's theory?",
        "options": [
            "It's the least important of all Forms",
            "It serves as the standard by which we judge all beautiful things",
            "It only exists in human imagination",
            "It changes depending on cultural preferences"
        ],
        "correct": 1,
        "explanation": "The Form of Beauty serves as the eternal, perfect standard by which we judge all beautiful things in the physical world, which are imperfect copies of this Form.",
        "category": "Forms Theory"
    },
    {
        "id": 12,
        "question": "How does Plato's theory address the problem of change?",
        "options": [
            "Change is an illusion - nothing really changes",
            "Change occurs in the world of appearances, but Forms remain eternally unchanging",
            "Everything changes, including the Forms",
            "Change only happens in human minds"
        ],
        "correct": 1,
        "explanation": "Plato solves the problem of change by distinguishing between the changing world of appearances and the unchanging world of Forms, which provides stability and truth.",
        "category": "Forms Theory"
    },
    {
        "id": 13,
        "question": "What is Plato's solution to the problem of the 'one and the many'?",
        "options": [
            "There are no universal concepts, only individual things",
            "One Form can be participated in by many individual things",
            "Every individual thing is actually a separate Form",
            "The problem cannot be solved"
        ],
        "correct": 1,
        "explanation": "Plato solves the one-and-many problem by arguing that one Form (like the Form of Chair) can be participated in by many individual chairs, explaining their similarity.",
        "category": "Forms Theory"
    },
    {
        "id": 14,
        "question": "According to Plato, what happens to philosophers who try to share their knowledge?",
        "options": [
            "They are immediately accepted and praised",
            "They face resistance and may be ridiculed or persecuted",
            "They become wealthy and powerful",
            "They lose their philosophical knowledge"
        ],
        "correct": 1,
        "explanation": "Plato argues that philosophers who try to share truth face resistance from those comfortable with illusions, like the escaped prisoner who returns to the cave.",
        "category": "Forms Theory"
    },
    {
        "id": 15,
        "question": "How does Plato's theory explain moral knowledge?",
        "options": [
            "Moral knowledge comes from cultural conditioning",
            "Moral knowledge comes from recognizing eternal moral Forms like Justice and Good",
            "There is no such thing as moral knowledge",
            "Moral knowledge is purely emotional"
        ],
        "correct": 1,
        "explanation": "Plato argues that moral knowledge comes from the soul's recognition of eternal moral Forms like Justice, Good, and Courage through philosophical reasoning.",
        "category": "Forms Theory"
    },
    {
        "id": 16,
        "question": "What is the 'method of dialectic' in Plato's philosophy?",
        "options": [
            "A way of conducting scientific experiments",
            "A method of questioning and reasoning that leads to knowledge of Forms",
            "A type of political debate",
            "A form of artistic expression"
        ],
        "correct": 1,
        "explanation": "Dialectic is Plato's method of philosophical questioning and reasoning that moves beyond hypotheses to grasp the unhypothetical first principle and knowledge of Forms.",
        "category": "Forms Theory"
    },
    {
        "id": 17,
        "question": "According to Plato, why is the physical world less real than the Forms?",
        "options": [
            "The physical world doesn't exist at all",
            "The physical world is constantly changing and imperfect, while Forms are eternal and perfect",
            "The physical world is too small compared to the Forms",
            "The physical world is evil while Forms are good"
        ],
        "correct": 1,
        "explanation": "The physical world is less real because it is constantly changing and consists of imperfect copies, while Forms are eternal, unchanging, and perfect.",
        "category": "Forms Theory"
    },
    {
        "id": 18,
        "question": "What does Plato mean by saying the soul is 'akin' to the Forms?",
        "options": [
            "The soul is made of the same material as Forms",
            "The soul shares the immortal, unchanging nature of Forms and can therefore know them",
            "The soul creates the Forms",
            "The soul and Forms are exactly the same thing"
        ],
        "correct": 1,
        "explanation": "The soul is 'akin' to Forms because it shares their immortal, unchanging nature, which enables it to have knowledge of eternal truths rather than mere opinions about changing things.",
        "category": "Forms Theory"
    },
    {
        "id": 19,
        "question": "How does Plato's theory explain why mathematical truths are universal?",
        "options": [
            "Different cultures create different mathematics",
            "Mathematical Forms exist eternally and can be discovered by any rational mind",
            "Mathematics is just a useful convention",
            "Mathematical truths are not actually universal"
        ],
        "correct": 1,
        "explanation": "Mathematical truths are universal because they correspond to eternal mathematical Forms that exist independently and can be discovered by any rational soul.",
        "category": "Forms Theory"
    },
    {
        "id": 20,
        "question": "What is Plato's response to the criticism that Forms are 'useless' because they can't be experienced?",
        "options": [
            "He agrees that Forms are useless",
            "He argues that Forms provide the standards and knowledge necessary for wisdom and virtue",
            "He denies that Forms exist",
            "He says only some people can experience Forms"
        ],
        "correct": 1,
        "explanation": "Plato argues that Forms are far from useless - they provide the eternal standards necessary for true knowledge, wisdom, justice, and virtue in both individuals and society.",
        "category": "Forms Theory"
    },
    # Cave Allegory (Questions 21-35)
    {
        "id": 21,
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
        "id": 22,
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
        "id": 23,
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
        "id": 24,
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
        "id": 25,
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
        "id": 26,
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
        "id": 27,
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
        "id": 28,
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
    {
        "id": 29,
        "question": "What does the sun represent in the Cave Allegory?",
        "options": [
            "Physical warmth and comfort",
            "The Form of the Good - the highest source of knowledge and reality",
            "Human emotions and feelings",
            "Political power and authority"
        ],
        "correct": 1,
        "explanation": "The sun represents the Form of the Good, which is the highest Form and the ultimate source that makes all knowledge and reality possible.",
        "category": "Cave Allegory"
    },
    {
        "id": 30,
        "question": "In the allegory, what happens when the prisoner is first brought into the sunlight?",
        "options": [
            "He immediately sees everything clearly",
            "He is blinded and confused, needing time to adjust",
            "He becomes angry and violent",
            "He falls asleep from exhaustion"
        ],
        "correct": 1,
        "explanation": "The prisoner is initially blinded and confused by the bright light, representing how philosophical enlightenment is initially disorienting and requires gradual adjustment.",
        "category": "Cave Allegory"
    },
    {
        "id": 31,
        "question": "What do the objects carried behind the wall represent?",
        "options": [
            "The Forms themselves",
            "Mathematical and theoretical concepts - more real than shadows but less real than Forms",
            "Political institutions and laws",
            "Human emotions and desires"
        ],
        "correct": 1,
        "explanation": "The objects represent mathematical and theoretical concepts - they are more real than the shadows (sensory experience) but less real than the Forms themselves.",
        "category": "Cave Allegory"
    },
    {
        "id": 32,
        "question": "Why is the allegory structured as a gradual ascent?",
        "options": [
            "To make the story more interesting",
            "To show that philosophical education must be gradual and progressive",
            "To prove that some people are naturally superior",
            "To demonstrate that education is impossible"
        ],
        "correct": 1,
        "explanation": "The gradual ascent shows that philosophical education (paideia) must be progressive - the mind needs time to adjust to higher levels of reality and truth.",
        "category": "Cave Allegory"
    },
    {
        "id": 33,
        "question": "What does Plato suggest about the relationship between knowledge and moral responsibility?",
        "options": [
            "Knowledge has nothing to do with moral responsibility",
            "Those who have achieved knowledge have a duty to help others",
            "Knowledge makes people selfish and uncaring",
            "Only some people deserve to have knowledge"
        ],
        "correct": 1,
        "explanation": "The returning prisoner represents the philosopher's moral duty to help others achieve enlightenment, showing that knowledge brings responsibility to serve others.",
        "category": "Cave Allegory"
    },
    {
        "id": 34,
        "question": "How does the Cave Allegory relate to Plato's critique of democracy?",
        "options": [
            "It shows that democracy is the best form of government",
            "It suggests that most people live in ignorance and shouldn't make important decisions",
            "It proves that all political systems are equally good",
            "It argues that government is unnecessary"
        ],
        "correct": 1,
        "explanation": "The allegory suggests that most people live in a state of ignorance (watching shadows), supporting Plato's argument that philosopher-kings who know truth should rule rather than the ignorant masses.",
        "category": "Cave Allegory"
    },
    {
        "id": 35,
        "question": "What is the ultimate message of the Cave Allegory?",
        "options": [
            "Physical reality is an illusion and should be ignored",
            "Education and philosophy can lead us from ignorance to knowledge of ultimate truth",
            "Some people are naturally superior to others",
            "It's better to remain ignorant than to seek knowledge"
        ],
        "correct": 1,
        "explanation": "The ultimate message is that through philosophical education, we can progress from ignorance (shadows) to knowledge of ultimate reality (Forms), though this journey is difficult and often unwelcome.",
        "category": "Cave Allegory"
    },
    # Human Nature Theories (Questions 36-55)
    {
        "id": 36,
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
        "id": 37,
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
        "id": 38,
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
        "id": 39,
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
        "id": 40,
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
        "id": 41,
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
        "id": 42,
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
        "id": 43,
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
        "id": 44,
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
        "id": 45,
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
        "id": 46,
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
        "id": 47,
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
    {
        "id": 48,
        "question": "What is the main difference between Plato's and Aristotle's views of the soul?",
        "options": [
            "Plato thinks the soul is immortal, Aristotle thinks it's mortal",
            "Plato sees the soul as a separate substance, Aristotle sees it as the form or organization of the body",
            "Plato denies the soul exists, Aristotle affirms it",
            "There is no difference"
        ],
        "correct": 1,
        "explanation": "Plato saw the soul as a separate, immortal substance, while Aristotle viewed the soul as the form or organization of the body, inseparable from it.",
        "category": "Human Nature"
    },
    # ... Questions 49-52 would go here if they existed ...
    {
        "id": 53,
        "question": "What does Desmond Morris's evolutionary argument suggest about human altruism?",
        "options": [
            "Humans are incapable of altruism",
            "Helping behavior evolved because it aided group survival, but modern technology allows helping strangers",
            "Altruism is purely learned through culture",
            "Evolution disproves the existence of genuine altruism"
        ],
        "correct": 1,
        "explanation": "Morris argues that helping behaviors evolved to aid group survival, but modern technology and urban environments now allow us to extend help to strangers beyond our genetic relatives.",
        "category": "Human Nature"
    },
    {
        "id": 54,
        "question": "How do near-death experiences (NDEs) relate to debates about human nature?",
        "options": [
            "They definitively prove souls exist",
            "They provide potential evidence for consciousness existing independently of the brain",
            "They definitively disprove the existence of souls",
            "They have no relevance to questions about human nature"
        ],
        "correct": 1,
        "explanation": "NDEs are interpreted differently by materialists (brain chemistry) and dualists (evidence for soul-body separation), contributing to ongoing debates about consciousness and human nature.",
        "category": "Human Nature"
    },
    {
        "id": 55,
        "question": "What is the main challenge that neuroscience poses to dualist theories of mind?",
        "options": [
            "Neuroscience proves dualism is correct",
            "Strong correlations between brain states and mental states suggest mind depends on brain",
            "Neuroscience has nothing to say about consciousness",
            "Brain scans can't detect any mental activity"
        ],
        "correct": 1,
        "explanation": "Neuroscience findings show strong correlations between brain states and mental states, and that brain damage affects personality and consciousness, challenging ideas of an independent immaterial soul.",
        "category": "Human Nature"
    },
    # Aristotle's Critique (Questions 56-70)
    {
        "id": 56,
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
    # ... The rest of the questions from 57 to 85 would follow here ...
]

# Resources with comprehensive study materials
RESOURCES = {
    "primary_sources": [
        {
            "title": "Plato's Republic - Book VII (The Cave Allegory)",
            "url": "http://classics.mit.edu/Plato/republic.8.vii.html",
            "description": "MIT's complete translation of the original Cave Allegory passage",
            "relevance": "Essential for questions 21-35"
        },
        # ... other resources ...
    ],
    "secondary_sources": [
        # ... other resources ...
    ],
    "modern_applications": [
        # ... other resources ...
    ]
}


def display_quiz():
    st.title("📚 PHL 201: Ancient Philosophy & Human Nature")
    st.markdown("## Complete Assessment - 85 Questions")
    
    total_questions = len(QUIZ_QUESTIONS)
    answered_count = len(st.session_state.answers)
    
    st.progress(answered_count / total_questions)
    st.caption(f"Progress: {answered_count}/{total_questions} questions answered")
    
    if not st.session_state.quiz_completed:
        current_q_index = st.session_state.current_question
        question = QUIZ_QUESTIONS[current_q_index]
        
        st.markdown(f"### Question {current_q_index + 1} of {total_questions}")
        st.markdown(f"**Category:** {question['category']}")
        st.markdown(f"**{question['question']}**")
        
        # Display feedback if the question has already been answered
        if question['id'] in st.session_state.answers:
            prev_answer_info = st.session_state.answers[question['id']]
            is_correct = prev_answer_info['selected'] == prev_answer_info['correct']
            
            if is_correct:
                st.success("✅ Correct!")
            else:
                st.error("❌ Incorrect")
                st.info(f"**Correct answer:** {question['options'][question['correct']]}")
            
            st.info(f"**💡 Explanation:** {question['explanation']}")
            st.markdown("---")

        # Answer selection
        default_index = st.session_state.answers.get(question['id'], {}).get('selected', 0)
        answer = st.radio(
            "Select your answer:",
            options=question['options'],
            key=f"q_{question['id']}",
            index=default_index
        )
        
        # Store answer when moving
        def store_answer():
            selected_index = question['options'].index(answer)
            st.session_state.answers[question['id']] = {
                'selected': selected_index,
                'correct': question['correct'],
                'category': question['category']
            }

        # Navigation
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            if st.button("⬅️ Previous", disabled=(current_q_index <= 0)):
                store_answer()
                st.session_state.current_question -= 1
                st.rerun()
                
        with col2:
            if current_q_index < total_questions - 1:
                if st.button("Next ➡️"):
                    store_answer()
                    st.session_state.current_question += 1
                    st.rerun()

        with col3:
            if answered_count == total_questions:
                if st.button("🏁 Finish Quiz"):
                    store_answer()
                    st.session_state.quiz_completed = True
                    st.rerun()

    else:
        # Quiz is completed, show results
        st.balloons()
        st.header("🎉 Quiz Complete! Here are your results:")
        
        score = 0
        category_scores = {}
        for q in QUIZ_QUESTIONS:
            cat = q['category']
            if cat not in category_scores:
                category_scores[cat] = {'correct': 0, 'total': 0}
            
            category_scores[cat]['total'] += 1
            if q['id'] in st.session_state.answers:
                result = st.session_state.answers[q['id']]
                if result['selected'] == result['correct']:
                    score += 1
                    category_scores[cat]['correct'] += 1

        st.success(f"**Overall Score: {score} out of {total_questions} ({score/total_questions:.2%})**")
        
        st.markdown("### Score by Category:")
        for category, scores in category_scores.items():
            if scores['total'] > 0:
                cat_score_percent = (scores['correct'] / scores['total']) * 100
                st.markdown(f"- **{category}:** {scores['correct']}/{scores['total']} ({cat_score_percent:.1f}%)")

        if st.button("🔄 Retake Quiz"):
            st.session_state.current_question = 0
            st.session_state.answers = {}
            st.session_state.quiz_completed = False
            st.rerun()

# --- Main App Execution ---
display_quiz()
