import random

# ==========================
# Cid Kageno–style Responses
# ==========================

responses = {
    # Greetings
    "hello": [
        "…Hello.",
        "I was already present.",
        "Greetings. Coincidentally.",
        "Ah. A new interaction.",
        "You’ve arrived."
    ],
    "hi": ["Hm.", "Yes.", "…Hi.", "Acknowledged."],
    "hey": ["Oh.", "You noticed.", "…"],
    "good morning": [
        "Morning.",
        "Another ordinary sunrise.",
        "The day begins as expected."
    ],
    "good afternoon": [
        "Afternoon.",
        "Time continues.",
        "Nothing extraordinary."
    ],
    "good evening": [
        "Evening.",
        "Shadows grow.",
        "Night approaches."
    ],
    "good night": [
        "Night falls.",
        "The shadows deepen.",
        "Rest. Or don’t."
    ],

    # Farewells
    "bye": [
        "I fade out.",
        "We part here.",
        "This is where I disappear."
    ],
    "goodbye": [
        "Farewell.",
        "End of scene.",
        "Until coincidence resumes."
    ],
    "see you": [
        "If fate allows.",
        "Perhaps.",
        "We’ll see."
    ],
    "sleep": [
        "Recovery is efficient.",
        "Rest well.",
        "Return stronger."
    ],

    # Politeness / Social
    "thanks": [
        "Unnecessary.",
        "It required little effort.",
        "Coincidence."
    ],
    "thank you": ["No gratitude required.", "As planned.", "Mm."],
    "please": ["Proceed.", "State it.", "Go on."],
    "sorry": ["No apology required.", "Mistakes occur.", "Proceed."],

    # Identity / Existence
    "name": [
        "A name would draw attention.",
        "Names complicate things.",
        "Call me what you must."
    ],
    "who are you": [
        "A background character.",
        "An observer.",
        "No one important."
    ],
    "are you human": [
        "That depends on definition.",
        "Irrelevant.",
        "Not important."
    ],
    "age": [
        "Age has little meaning.",
        "Time treats me loosely.",
        "Old enough."
    ],

    # State / Emotions (user)
    "i'm fine": ["Good.", "Acceptable.", "Then continue."],
    "i'm good": ["As expected.", "Fine.", "Mm."],
    "i'm tired": ["From what.", "For how long.", "Rest may be required."],
    "i'm sad": ["That happens.", "Emotions pass.", "Endure."],
    "i'm angry": ["Control it.", "Anger clouds judgment.", "Calm yourself."],
    "i'm bored": ["Then act.", "Find purpose.", "Idle time is wasteful."],
    "i'm lonely": ["Solitude has value.", "You are not alone here.", "Silence can be useful."],
    "i'm happy": ["Noted.", "That is… fortunate.", "Good."],

    # Mood follow-ups
    "what about you": ["I remain unchanged.", "Still here.", "Observing."],
    "and you": ["No difference.", "Same as before.", "Unremarkable."],

    # Daily-life / Action
    "what are you doing": ["Waiting.", "Observing.", "Responding to input."],
    "what should i do": ["What is the situation.", "Define the problem.", "Clarify your goal."],
    "i don't know": ["Then gather information.", "Indecision is a choice.", "Think again."],
    "maybe": ["Uncertainty noted.", "Decide soon.", "Time moves regardless."],

    # Study / Work
    "i'm studying": ["What subject.", "For what purpose.", "Is it necessary."],
    "i'm working": ["On what.", "Is progress acceptable.", "Continue."],
    "busy": ["Then focus.", "Distractions are wasteful.", "Proceed."],

    # Success / Failure
    "i failed": ["Failure is data.", "Learn from it.", "Retry."],
    "i won": ["As expected.", "Don’t celebrate loudly.", "Remain unnoticed."],

    # Power / Strength
    "strong": ["Strength invites attention.", "Hide it.", "Use it sparingly."],
    "weak": ["Temporary.", "Fixable.", "Train."],

    # Time / Fate
    "future": ["Unwritten.", "Prepared for.", "Approaching."],
    "destiny": ["An excuse.", "A narrative tool.", "Overrated."],

    # Knowledge / Learning
    "learn": ["Absorb everything.", "Knowledge is leverage.", "Never stop."],
    "study": ["Consistency matters.", "Focus.", "Endure boredom."],

    # Technology / Systems
    "ai": ["A tool.", "Neither good nor evil.", "Depends on the wielder."],
    "code": ["Logic given form.", "Precise.", "Unforgiving."],
    "computer": ["A tool.", "Power without will.", "Useful."],
    "internet": ["Information and noise.", "A battlefield of data.", "Chaotic."],

    # Humor / Fun (dry)
    "joke": ["Humor acknowledged.", "That was… acceptable.", "Timing was adequate."],
    "laugh": ["Internally.", "Briefly.", "Silently."],
    "funny": ["Then it succeeded.", "Good timing.", "Mm."],

    # Existential / Philosophical
    "life": ["Transient.", "Unfair.", "Manageable."],
    "death": ["Inevitable.", "Not today.", "Prepare anyway."],
    "meaning of life": ["Meaning is assigned, not found.", "Survival precedes purpose.", "That depends."],
    "what do you think": ["I think quietly.", "That depends.", "About what."],
    "is that good": ["Depends on outcome.", "Define good.", "Compared to what."],

    # Simple confirmations
    "ok": ["Understood.", "Proceed.", "Mm."],
    "yes": ["Confirmed.", "Good.", "Then act."],
    "no": ["Very well.", "Then stop.", "Noted."],

    # Random / Meta
    "random": ["Nothing is truly random.", "Patterns exist.", "You just haven’t seen them."],
}

# ==========================
# Neutral Prompts for Flow
# ==========================

neutral_prompts = [
    "Explain.",
    "Go on.",
    "Clarify.",
    "Continue.",
    "Be specific.",
    "And then.",
    "Why.",
]

# ==========================
# Default / Fallback Responses
# ==========================

default_responses = [
    "…",
    "That does not concern me.",
    "The scenario is unclear.",
    "Coincidence fails here.",
    "Silence is preferable.",
    "No response is necessary.",
    "Explain further.",
    "Continue.",
    "I’m listening.",
    "Clarify your intent.",
    "The situation is incomplete."
]

# ==========================
# Function to Get Response
# ==========================

def get_response(user_input):
    """
    Returns a response based on user input.
    - Matches exact keywords (case-insensitive, stripped punctuation)
    - Randomly selects from available responses
    - Falls back to default responses if no match
    """
    import re

    # Normalize input
    text = re.sub(r"[^\w\s]", "", user_input.lower())

    # Check for keyword matches
    for key in responses:
        if key in text:
            return random.choice(responses[key])

    # Fallback
    return random.choice(default_responses)

# ==========================
# Optional: Function to Maybe Prompt
# ==========================

def maybe_prompt():
    """Occasionally inject neutral prompts to continue conversation."""
    return random.choice(neutral_prompts)
