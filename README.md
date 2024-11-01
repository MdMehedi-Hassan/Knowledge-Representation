# Knowledge-Representation

## Clue-Style Logical Reasoning Game in Python

This project demonstrates a *Clue*-style logical deduction game using propositional logic. It employs concepts from AI Knowledge Representation and Logical Reasoning to model and solve the game. The program utilizes a custom `logic.py` module to represent symbols and sentences and performs logical inferences to determine the possible outcomes of the game.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [How It Works](#how-it-works)
- [Code Structure](#code-structure)
- [Examples](#examples)
- [Future Work](#future-work)
- [License](#license)

---

## Overview
This project models a simple *Clue*-style game, where the AI needs to deduce:
- Which character committed the crime
- Where the crime happened
- What weapon was used

The game rules and facts are represented using propositional logic, allowing the AI to make inferences and solve the puzzle. The project can be extended to solve various logic-based puzzles beyond this example.

---

## Installation
1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install required packages**:
   ```bash
   pip install termcolor
   ```

3. **Run the game**:
   ```bash
   python main.py
   ```

---

## How It Works
1. **Knowledge Representation**: The game uses propositional logic to define characters, rooms, and weapons as symbols. Logical sentences represent game rules and facts.
2. **Logical Reasoning**: The `model_check` function evaluates whether the knowledge base entails specific queries. It uses a brute-force approach to check all possible models for logical entailment.
3. **Constraints and Inference**: The program ensures that all game rules are satisfied and makes inferences to solve the puzzle.

### Key Concepts
- **Symbols**: Represent game elements (e.g., Colonel Mustard, Kitchen, Knife).
- **Sentences**: Logical expressions formed using symbols and logical operators (`And`, `Or`, `Not`, etc.).
- **Model Checking**: A method to verify if the knowledge base implies the query, used to make logical inferences.

---

## Code Structure
- `main.py`: The main script that sets up the game and performs logical reasoning.
- `logic.py`: Contains classes for representing logical symbols and sentences, including operations like `And`, `Or`, `Not`, `Implication`, and `Biconditional`.
- `README.md`: Documentation for the project.

---

## Examples
Here are some examples of how the game logic is set up:
1. **Defining Symbols**:
   ```python
   mustard = Symbol("ColMustard")
   kitchen = Symbol("kitchen")
   knife = Symbol("knife")
   ```

2. **Constructing the Knowledge Base**:
   ```python
   knowledge = And(
       Or(mustard, plum, scarlet),  # At least one character is involved
       Or(ballroom, kitchen, library),  # At least one room is involved
       Or(knife, revolver, wrench)  # At least one weapon is involved
   )
   ```

3. **Adding Constraints**:
   ```python
   knowledge.add(Not(mustard))
   knowledge.add(Not(kitchen))
   knowledge.add(Not(revolver))
   ```

4. **Checking Knowledge**:
   ```python
   check_knowledge(knowledge)
   ```

---

## Future Work
- Expand the game to include more characters, rooms, and weapons.
- Implement optimization techniques for the model checking process.
- Create a graphical user interface (GUI) for an improved user experience.
- Integrate more complex logical puzzles and scenarios.
