import termcolor

from logic import *  # Use absolute import assuming `logic.py` is in the same directory

# Define symbols for characters, rooms, and weapons
mustard = Symbol("ColMustard")
plum = Symbol("ProfPlum")
scarlet = Symbol("MsScarlet")
characters = [mustard, plum, scarlet]

ballroom = Symbol("ballroom")
kitchen = Symbol("kitchen")
library = Symbol("library")
rooms = [ballroom, kitchen, library]

knife = Symbol("knife")
revolver = Symbol("revolver")
wrench = Symbol("wrench")
weapons = [knife, revolver, wrench]

symbols = characters + rooms + weapons

# Function to check knowledge and print results
def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            termcolor.cprint(f"{symbol}: YES", "green")
        elif not model_check(knowledge, Not(symbol)):
            print(f"{symbol}: MAYBE")

# Construct the knowledge base
knowledge = And(
    Or(mustard, plum, scarlet),  # There must be one person
    Or(ballroom, kitchen, library),  # There must be one room
    Or(knife, revolver, wrench)  # There must be one weapon
)

# Add initial known facts to the knowledge base
knowledge.add(And(
    Not(mustard), Not(kitchen), Not(revolver)
))

# Add constraints for an unknown card
knowledge.add(Or(
    Not(scarlet), Not(library), Not(wrench)
))

# Add more known facts
knowledge.add(Not(plum))
knowledge.add(Not(ballroom))

# Check and print the knowledge
check_knowledge(knowledge)
