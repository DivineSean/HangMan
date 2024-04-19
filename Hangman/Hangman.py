import random
import tkinter as tk
import pygame
from concurrent.futures import ThreadPoolExecutor

message_label = None
stats = None

def play_music():
    pygame.mixer.music.load("song.mp3")
    pygame.mixer.music.play(loops=-1)
    

def stop_music():
    pygame.mixer.music.stop()

def draw_hangman(turns):
    stages = [
        """
        \t\t\t\t--------
        \t\t\t\t|      |
        \t\t\t\t|      
        \t\t\t\t|      
        \t\t\t\t|      
        \t\t\t\t|      
        \t\t\t\t|
        \t\t\t\t----------
        """,
        """
        \t\t\t\t--------
        \t\t\t\t|      |
        \t\t\t\t|      O
        \t\t\t\t|     
        \t\t\t\t|     
        \t\t\t\t|     
        \t\t\t\t|
        \t\t\t\t----------
        """,
        """
        \t\t\t\t--------
        \t\t\t\t|      |
        \t\t\t\t|      O
        \t\t\t\t|      |
        \t\t\t\t|      
        \t\t\t\t|     
        \t\t\t\t|
        \t\t\t\t----------
        """,
        """
        \t\t\t\t--------
        \t\t\t\t|      |
        \t\t\t\t|      O
        \t\t\t\t|     /|
        \t\t\t\t|      
        \t\t\t\t|      
        \t\t\t\t|
        \t\t\t\t----------
        """,
        """
        \t\t\t\t--------
        \t\t\t\t|      |
        \t\t\t\t|      O
        \t\t\t\t|     /|\\
        \t\t\t\t|      
        \t\t\t\t|     
        \t\t\t\t|
        \t\t\t\t----------
        """,
        """
        \t\t\t\t--------
        \t\t\t\t|      |
        \t\t\t\t|      O
        \t\t\t\t|     /|\\
        \t\t\t\t|     / 
        \t\t\t\t|     
        \t\t\t\t|
        \t\t\t\t----------
        """,
        """
        \t\t\t\t--------
        \t\t\t\t|      |
        \t\t\t\t|      O
        \t\t\t\t|     /|\\
        \t\t\t\t|     / \\
        \t\t\t\t|     
        \t\t\t\t|
        \t\t\t\t----------
        """
    ]
    if turns > 6:
        return stages[6]
    return stages[turns]

def word_list(num):
    words = [
        "apple", "banana", "cherry", "date", "elderberry", "fig", "grape",
        "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya",
        "quince", "raspberry", "strawberry", "tangerine", "watermelon",
        "python", "programming", "computer", "science", "algorithm", "artificial",
        "intelligence", "machine", "learning", "data", "analysis", "visualization",
        "web", "development", "software", "engineer", "design", "user", "interface",
        "database", "network", "security", "cybersecurity", "cloud", "computing",
        "internet", "browser", "protocol", "encryption", "authentication", "authorization",
        "hacking", "privacy", "virtual", "reality", "augmented", "blockchain",
        "cryptocurrency", "bitcoin", "ethereum", "decentralized", "finance", "smart",
        "contracts", "tokenization", "decentralized", "application", "fintech",
        "financial", "technology", "banking", "payments", "e-commerce", "startup",
        "venture", "capital", "entrepreneur", "innovation", "disruption", "agile",
        "scrum", "kanban", "project", "management", "productivity", "leadership",
        "teamwork", "communication", "presentation", "negotiation", "problem",
        "solving", "critical", "thinking", "creativity", "inspiration", "motivation",
        "success", "achievement", "fulfillment", "happiness", "mindfulness",
        "meditation", "health", "fitness", "nutrition", "exercise", "wellness",
        "yoga", "medication", "therapy", "counseling", "psychology", "psychiatry",
        "mental", "emotional", "stress", "anxiety", "depression", "relationships",
        "friendship", "family", "love", "romance", "marriage", "parenting",
        "childhood", "education", "school", "college", "university", "learning",
        "teaching", "student", "teacher", "curriculum", "syllabus", "lesson",
        "lecture", "course", "textbook", "exam", "grading", "grading", "system",
        "homework", "assignment", "research", "study", "scholarship", "grant",
        "tuition", "fees", "financial", "aid", "scholarship", "work", "study",
        "internship", "placement", "career", "employment", "job", "interview",
        "resume", "cover", "letter", "professional", "networking", "recruitment",
        "hiring", "salary", "benefits", "promotion", "raise", "evaluation",
        "performance", "appraisal", "termination", "layoff", "resignation",
        "retirement", "quitting", "sabbatical", "vacation", "holiday", "leave",
        "absence", "sickness", "injury", "disability", "accident", "emergency",
        "first", "aid", "emergency", "services", "paramedic", "ambulance",
        "hospital", "clinic", "emergency", "room", "ER", "emergency", "department",
        "urgent", "care", "triage", "nurse", "doctor", "physician", "surgeon",
        "medical", "treatment", "diagnosis", "therapy", "surgery", "procedure",
        "operation", "recovery", "healthcare", "medicine", "medication", "prescription",
        "drug", "pharmacy", "side", "effect", "allergy", "immunity", "vaccination",
        "herd", "immunity", "epidemic", "pandemic", "outbreak", "contagious",
        "transmission", "infection", "infectious", "disease", "virus", "bacteria",
        "parasite", "fungus", "immune", "system", "respiratory", "gastrointestinal",
        "cardiovascular", "nervous", "endocrine", "urinary", "reproductive",
        "anatomy", "physiology", "biology", "chemistry", "physics", "mathematics",
        "geometry", "algebra", "trigonometry", "calculus", "statistics", "probability",
        "logic", "reasoning", "deduction", "induction", "fallacy", "argument",
        "premise", "conclusion", "proof", "theorem", "axiom", "postulate",
        "hypothesis", "experiment", "observation", "theory", "law", "principle",
        "method", "technique", "model", "framework", "paradigm", "approach",
        "strategy", "tactic", "plan", "execution", "implementation", "iteration",
        "optimization", "efficiency", "effectiveness", "accuracy", "precision",
        "reliability", "validity", "reproducibility", "verification", "validation",
        "evaluation", "assessment", "measurement", "metric", "indicator",
        "benchmark", "standard", "quality", "control", "assurance", "management",
        "regulation", "compliance", "certification", "accreditation", "audit",
        "inspection", "review", "feedback", "improvement", "change", "adaptation",
        "evolution", "revolution", "discovery", "invention", "innovation",
        "creation", "development", "growth", "progress", "advancement",
        "transformation", "transition", "movement", "shift", "trend", "pattern",
        "cycle", "repetition", "iteration", "generation", "era", "age",
        "century", "millennium", "past", "present", "future", "history",
        "historical", "event", "artifact", "document", "record", "archive",
        "museum", "artifact", "artifact", "preservation", "conservation",
        "restoration", "exhibition", "collection", "curation", "heritage",
        "culture", "tradition", "custom", "ritual", "belief", "value",
        "norm", "ethics", "morality", "justice", "equality", "freedom",
        "democracy", "liberty", "human", "rights", "civil", "rights",
        "social", "justice", "environment", "climate", "change", "global",
        "warming", "pollution", "conservation", "sustainability", "renewable",
        "energy", "alternative", "energy", "efficiency", "green", "technology",
        "sustainable", "development", "urban", "rural", "planning", "infrastructure",
        "transportation", "public", "transit", "road", "rail", "airport",
        "seaport", "highway", "bridge", "tunnel", "parking", "structure",
        "building", "architecture", "construction", "engineering", "design",
        "landscape", "urban", "design", "interior", "design", "lighting",
        "furniture", "fixture", "appliance", "electronic", "device", "gadget",
        "smartphone", "tablet", "computer", "laptop", "desktop", "server",
        "network", "router", "modem", "switch", "firewall", "antivirus",
        "malware", "spyware", "adware", "phishing", "spam", "cybercrime",
        "identity", "theft", "hacker", "cyber", "attack", "defense",
        "cyber", "security", "digital", "privacy", "data", "protection",
        "encryption", "authentication", "authorization", "cloud", "computing",
        "big", "data", "data", "analytics", "machine", "learning", "artificial",
        "intelligence", "internet", "of", "things", "IoT", "smart", "home",
        "smart", "city", "smart", "grid", "wearable", "technology", "virtual",
        "reality", "augmented", "reality", "mixed", "reality", "extended",
        "reality", "immersive", "experience", "gaming", "gamification",
        "entertainment", "music", "film", "television", "streaming",
        "platform", "content", "creation", "production", "distribution",
        "marketing", "advertising", "branding", "promotion", "publicity",
        "communication", "journalism", "media", "print", "media", "broadcast",
        "media", "digital", "media", "social", "media", "network", "platform",
        "service", "provider", "user", "engagement", "interaction",
        "communication", "conversation", "dialogue", "forum", "community",
        "network", "group", "channel", "page", "profile", "feed",
        "notification", "message", "inbox", "chat", "thread", "post",
        "comment", "like", "dislike", "share", "follow", "subscribe",
        "trending", "viral", "content", "algorithm", "recommendation",
        "personalization", "privacy", "security", "data", "protection",
        "terms", "of", "service", "policy", "regulation", "compliance",
        "governance", "ethics", "law", "legal", "system", "court",
        "judge", "lawyer", "attorney", "prosecutor", "defense",
        "plaintiff", "defendant", "witness", "jury", "verdict",
        "appeal", "justice", "civil", "criminal", "case", "trial",
        "lawsuit", "lawsuit", "settlement", "compensation",
        "damages", "punishment", "fine", "sentence", "imprisonment",
        "probation", "parole", "execution", "execution", "method",
        "capital", "punishment", "death", "penalty", "corporal",
        "punishment", "torture", "cruelty", "inhumane", "treatment",
        "human", "rights", "liberty", "freedom", "justice", "equality",
        "fairness", "opportunity", "diversity", "inclusion", "equity",
        "accessibility", "empowerment", "advocacy", "activism", "protest",
        "demonstration", "movement", "revolution", "reform", "change",
        "progress", "evolution", "innovation", "adaptation", "resilience",
        "sustainability", "development", "growth", "prosperity",
        "well-being", "quality", "of", "life", "happiness", "fulfillment",
        "meaning", "purpose", "creativity", "art", "expression",
        "music", "dance", "theater", "literature", "film", "visual",
        "art", "design", "architecture", "fashion", "food", "cuisine",
        "gastronomy", "wine", "beer", "spirit", "cocktail", "beverage",
        "coffee", "tea", "soft", "drink", "water", "juice", "milk",
        "soda", "alcohol", "chocolate", "dessert", "cake", "pastry",
        "bread", "biscuit", "cookie", "candy", "ice", "cream", "snack",
        "appetizer", "entree", "main", "course", "side", "dish", "salad",
        "soup", "stew", "sandwich", "pizza", "pasta", "rice", "noodle",
        "grain", "vegetable", "fruit", "nut", "seed", "legume", "protein",
        "dairy", "egg", "meat", "poultry", "seafood", "fish", "shellfish",
        "crustacean", "mollusk", "invertebrate", "animal", "mammal",
        "reptile", "amphibian", "bird", "fish", "arthropod", "insect",
        "plant", "flower", "tree", "shrub", "grass", "herb", "spice",
        "condiment", "seasoning", "flavor", "ingredient", "preparation",
        "cooking", "baking", "grilling", "roasting", "boiling", "steaming",
        "frying", "sauteing", "stir", "frying", "marinating", "seasoning",
        "recipe", "cookbook", "chef", "restaurant", "cuisine", "dish",
        "menu", "ingredient", "supplier", "wholesale", "retail",
        "market", "supermarket", "grocery", "store", "shop", "boutique",
        "convenience", "store", "online", "shopping", "e-commerce",
        "delivery", "service", "pick", "up", "service", "customer",
        "service", "support", "satisfaction", "loyalty", "recommendation",
        "review", "rating", "feedback", "complaint", "return",
        "refund", "exchange", "warranty", "guarantee", "terms",
        "conditions", "privacy", "policy", "security", "policy",
        "payment", "method", "payment", "gateway", "transaction",
        "processing", "billing", "shipping", "delivery", "logistics",
        "supply", "chain", "inventory", "management", "stock",
        "stock", "keeping", "unit", "SKU", "barcode", "RFID",
        "fulfillment", "warehouse", "storage", "packaging",
        "pallet", "container", "transportation", "freight",
        "logistics", "carrier", "courier", "tracking", "traceability",
        "route", "planning", "route", "optimization", "vehicle",
        "fleet", "driver", "safety", "regulation", "compliance",
        "insurance", "claim", "accident", "prevention",
        "reliability", "maintenance", "repair", "service",
        "mechanic", "diagnostics", "inspection", "certification",
        "registration", "license", "permit", "regulation",
        "compliance", "law", "policy", "regulator", "government",
        "agency", "authority", "enforcement", "legal", "jurisdiction",
        "court", "lawyer", "litigation", "litigant", "plaintiff",
        "defendant", "petitioner", "respondent", "judge", "trial",
        "courtroom", "hearing", "evidence", "argument", "objection",
        "ruling", "verdict", "appeal", "appellate", "court",
        "Supreme", "Court", "justice", "judicial", "system",
        "law", "enforcement", "police", "officer", "sheriff",
        "deputy", "marshal", "patrol", "agent", "investigator",
        "detective", "inspector", "forensic", "crime", "scene",
        "evidence", "witness", "testimony", "statement",
        "interview", "interrogation", "arrest", "booking",
        "charge", "arraignment", "bail", "bond", "jail",
        "prison", "correctional", "facility", "penitentiary",
        "conviction", "sentence", "probation", "parole",
        "release", "community", "service", "rehabilitation",
        "reentry", "recidivism", "reform", "justice", "system",
        "law", "court", "police", "crime", "punishment",
        "penalty", "prison", "justice", "equality", "rights",
        "freedom", "democracy", "citizen", "constitution",
        "government", "legislature", "executive", "judiciary",
        "separation", "powers", "checks", "balances",
        "federalism", "local", "government", "state",
        "government", "county", "government", "city",
        "government", "municipality", "township",
        "village", "community", "neighborhood", "block",
        "district", "ward", "precinct", "borough",
        "census", "population", "demographics", "ethnicity",
        "race", "religion", "language", "culture",
        "diversity", "immigration", "emigration",
        "refugee", "asylum", "citizenship", "passport",
        "visa", "residence", "naturalization",
        "nationality", "identity", "document",
        "documentation", "registration", "record",
        "registry", "database", "identification",
        "verification", "authentication", "authorization",
        "credential", "certificate", "license",
        "permit", "qualification", "certification",
        "training", "education", "degree",
        "diploma", "certification", "qualification",
        "professional", "qualification", "credential",
        "accreditation", "certification",
        "examination", "assessment", "evaluation",
        "verification", "validation", "audit",
        "inspection", "regulation", "compliance",
        "standards", "guidelines", "criteria",
        "requirements", "policy", "procedure",
        "protocol", "practice", "code", "ethics",
        "conduct", "behavior", "principle", "value",
        "morality", "ethics", "integrity",
        "professionalism", "accountability",
        "responsibility", "transparency",
        "honesty", "fairness", "impartiality",
        "respect", "dignity", "equality",
        "justice", "democracy", "freedom",
        "liberty", "rights", "human", "rights",
        "civil", "rights", "legal", "rights",
        "constitutional", "rights", "privacy",
        "data", "protection", "confidentiality",
        "security", "safety", "health", "well-being",
        "prosperity", "success", "happiness",
        "fulfillment", "achievement", "satisfaction",
        "progress", "development", "growth",
        "innovation", "creativity", "change",
        "adaptation", "transformation", "improvement",
        "optimization", "efficiency", "effectiveness",
        "quality", "excellence", "performance",
        "productivity", "sustainability",
        "environmental", "sustainability",
        "economic", "sustainability",
        "social", "sustainability", "equity",
        "inclusion", "diversity", "accessibility",
        "empowerment", "advocacy", "activism",
        "philanthropy", "volunteering", "charity",
        "donation", "fundraising", "community",
        "service", "social", "service", "public",
        "service", "civic", "engagement",
        "participation", "collaboration",
        "partnership", "alliance", "network",
        "coalition", "community", "organization",
        "nonprofit", "organization", "NGO",
        "civil", "society", "association", "club",
        "group", "team", "organization", "company",
        "enterprise", "business", "corporation",
        "firm", "company", "agency", "institution",
        "organization", "structure", "system",
        "process", "program", "project", "initiative",
        "venture", "enterprise", "undertaking",
        "effort", "endeavor", "task", "challenge",
        "opportunity", "risk", "threat", "obstacle",
        "constraint", "limitation", "barrier",
        "problem", "issue", "solution", "strategy",
        "plan", "action", "activity", "task",
        "project", "program", "initiative",
        "effort", "endeavor", "goal", "objective",
        "target", "outcome", "result", "achievement",
        "success", "performance", "productivity",
        "effectiveness", "efficiency", "quality",
        "excellence", "innovation", "creativity",
        "improvement", "development", "progress",
        "growth", "change", "transformation",
        "adaptation", "evolution", "revolution",
        "disruption", "impact", "effect", "influence",
        "contribution", "benefit", "advantage",
        "value", "importance", "significance",
        "relevance", "role", "function", "purpose",
        "meaning", "context", "environment",
        "situation", "condition", "circumstance",
        "factor", "variable", "element"
    ]
    return words[num]

def check_letter(str, letter, word):
    i = 0
    s = ""

    while(i < len(word)):
        if (letter == word[i]):
            s += letter
        else:
            s += str[i]
        i += 1
    return s

def print_display(text, size, canvas, x, y, color):
    return canvas.create_text(x, y, text=text, font=("Arial", size), fill=color)

def input_display(root, canvas, Word, hidden_word, num, disp):
    disp = print_display("The KeyWord : " + hidden_word[0] , 20, canvas, 280, 430, "black")
    print_display("Status : ", 20, canvas, 220, 550, "black")
    stats = print_display(draw_hangman(num[0]), 20, canvas, 100, 530, "blue")
    input_label = print_display("Guess a lettre : " , 20, canvas, 500, 430, "black")
    input_entry = tk.Entry(root, font=("Arial", 20), width=5)
    input_entry.pack()
    input_entry.place(x=580, y=415)

    submit_button = tk.Button(root, text="Submit", font=("Arial", 20), command=lambda: get_user_input(root, canvas, Word, input_entry, hidden_word, num, disp, input_label, submit_button))
    submit_button.pack()
    submit_button.place(x=420, y=455)

    ex_button = tk.Button(root, text="Exit", font=("Arial", 20), command=lambda: exit_application())
    ex_button.pack()
    ex_button.place(x=0, y=0)

    play_button = tk.Button(root, text="Play Music", font=("Arial", 20), command=lambda:play_music())
    play_button.place(x=890, y=0)

    stop_button = tk.Button(root, text="Stop Music", font=("Arial", 20), command=lambda:stop_music())
    stop_button.place(x=890, y=40)
    return submit_button, input_entry, disp, stats

def play_again(canvas, exit_button, input_label, disp, input_entry, play_again_button, message_label):
    canvas.delete(input_label)
    canvas.delete(disp)
    play_again_button.destroy()
    input_entry.destroy()
    exit_button.destroy()
    canvas.delete(message_label)
    canvas.delete(stats)
    hangman_gui()

def exit_application():
    root.destroy()

def get_user_input(root, canvas, Word, input_entry, hidden_word, num, disp, input_label, submit_button):
    global message_label
    global stats
    if message_label is not None:
        canvas.delete(message_label)
    if stats is not None:
        canvas.delete(stats)
    else:
        stats = print_display("Status : ", 20, canvas, 220, 550, "black")
        print_display(draw_hangman(num[0]), 20, canvas, 100, 530, "blue")

    letter = input_entry.get().lower()
    input_entry.delete(0, tk.END)
    if not letter.isalpha() or len(letter) != 1:
        message_label = print_display("Please enter only one letter!", 20, canvas, 475, 500, "red")
        num[0] += 1
    elif letter in Word:
        if letter not in hidden_word[0]:
            hidden_word.append(check_letter(hidden_word[0], letter, Word))
            hidden_word.pop(0)
            submit_button.destroy()
            input_entry.destroy()
            canvas.delete(input_label)
            canvas.delete(disp)
            submit_button, input_entry, disp , stats = input_display(root, canvas, Word, hidden_word, num, disp)
            if (hidden_word[0] == Word):
                submit_button.destroy()
                message_label = print_display("        Congratulations!\nYou have guessed the word!", 20, canvas, 475, 520, "green")
                exit_button = tk.Button(root, text="Exit", font=("Arial", 20), command=lambda : exit_application())
                exit_button.pack()
                exit_button.place(x=500, y=455)
                play_again_button = tk.Button(root, text="Play Again", font=("Arial", 20), command=lambda: play_again(canvas, exit_button, input_label, disp, input_entry, play_again_button, message_label))
                play_again_button.pack()
                play_again_button.place(x=370, y=455)
            else:
                message_label = print_display("Correct", 20, canvas, 475, 500, "green")
        else:
            message_label = print_display("You Already Guessed That Letter!", 20, canvas, 475, 500, "green")
    else:
        num[0] += 1
        message_label = print_display("Incorrect", 20, canvas, 475, 500, "red")
    print_display("Status : ", 20, canvas, 220, 550, "black")
    canvas.delete(stats)
    stats = print_display(draw_hangman(num[0]), 20, canvas, 100, 530, "blue")
    if (num[0] == 6):
        canvas.delete(message_label)
        message_label = print_display("You Lost! The word was " + Word, 20, canvas, 475, 520, "red")
        exit_button = tk.Button(root, text="Exit", font=("Arial", 20), command=lambda : exit_application())
        exit_button.pack()
        exit_button.place(x=500, y=455)
        play_again_button = tk.Button(root, text="Play Again", font=("Arial", 20), command=lambda: play_again(canvas, exit_button, input_label, disp, input_entry, play_again_button, message_label))
        play_again_button.pack()
        play_again_button.place(x=370, y=455)

def hangman_gui():
    try:
        display_text = """🅆🄴🄻🄲🄾🄼🄴 🅃🄾 🄷🄰🄽🄶🄼🄰🄽"""
    except SyntaxError:
        display_text = """WELCOME TO HANGMAN"""
    
    print_display(display_text, 45, canvas, 512, 100, "white")
    Word = word_list(random.randint(0, 1257))
    num = [0]
    hidden_word = ["_" * len(Word)]
    input_display(root, canvas, Word, hidden_word, num, "none")

root = tk.Tk()
root.title("Hangman By DivineSean")
root.iconbitmap("icon.ico")
root.geometry("1024x1024")
pygame.mixer.init()
canvas = tk.Canvas(root, width=1024, height=1024)
canvas.pack()
image_names = tk.PhotoImage(file="S.png")
canvas.create_image(0, 0, anchor="nw", image=image_names)
hangman_gui()
root.mainloop()