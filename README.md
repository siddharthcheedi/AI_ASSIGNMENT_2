# Human Verification Systems (Turing Test + CAPTCHA)

This project demonstrates two classical approaches used to distinguish **humans from machines**:

1. **Turing Test Simulation** – a chatbot interaction where the user tries to determine whether they are speaking to a human or a machine.
2. **CAPTCHA Verification System** – an image-based challenge designed to verify that the user is human.

The project is implemented in **Python** and serves as a simple demonstration of **human verification techniques used in AI and cybersecurity systems**.

---

# Project Structure

```
.
├── turing
  ├── captcha_system.py
  ├── turing_test.py
  └── architecture.md
```

- `turing_test.py` – Chat-based Turing Test simulation  
- `captcha_system.py` – Image CAPTCHA verification system  
- `architecture.md` – Read about the architecture
---

# 1. Turing Test Simulation

File: `turing_test.py`

This program simulates a **chat-based Turing Test**.

A user communicates with an anonymous entity through a terminal chat window. After the conversation, the user must decide whether the entity was:

- **Human**
- **Machine**

The system currently connects to a **rule-based chatbot (ELIZA-style)** that generates responses using pattern matching.

## Features

- Pattern-based chatbot responses
- Simulated typing delay to mimic human behavior
- Interactive terminal chat interface
- Final human/machine guess by the user

## How It Works

1. User types messages in the terminal.
2. The program matches the input against predefined regex patterns.
3. The bot selects a random response from matching rules.
4. A typing delay is simulated before the response appears.
5. At the end, the user guesses whether the entity was human or machine.

## Run the Program

```bash
python turing_test.py
```

Example interaction:

```
You: Hello
Entity: Hi! How can I help you?

You: Are you human?
Entity: What makes one human?

Do you think you were chatting with a HUMAN or a MACHINE?
```

---

# 2. CAPTCHA Verification System

File: `captcha_system.py`

This program implements a **visual CAPTCHA verification system** using randomly generated text images.

The user must correctly type the characters shown in the CAPTCHA image.

## Features

- Random CAPTCHA generation
- Image-based verification
- Case-insensitive checking
- Maximum of **3 attempts**
- Automatic opening of CAPTCHA image

## How It Works

1. A random string of characters is generated.
2. The program creates an image containing this text.
3. The image opens in the user's default image viewer.
4. The user types the characters they see.
5. If correct → verification succeeds.

## Run the Program

```bash
python captcha_system.py
```

Example:

```
CAPTCHA Verification System

Challenge 1/3
An image CAPTCHA has been generated.

>> Type the text seen in the image:
```

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/siddharthcheedi/AI_ASSIGNMENT_2
cd Turing
```

## 2. Install Required Libraries

```bash
pip install captcha pillow
```

---

# Dependencies

Python libraries used:

- random
- re
- time
- string
- captcha
- Pillow

Install with:

```bash
pip install captcha pillow
```

---


# Water Jug Problem – Search Algorithm Comparison

This project solves the classic **Water Jug Problem** using multiple **Artificial Intelligence search algorithms** and compares their performance.

The goal is to measure **4 liters of water** using:

- Jug 1 capacity: **5L**
- Jug 2 capacity: **3L**

The project implements and compares the following search algorithms:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Depth-Limited Search (DLS)
- Iterative Deepening Search (IDS)

The program also measures:

- number of nodes explored
- execution time
- solution path

---

# Project Structure

```
.
├── water_jug
  ├── search_algorithms.py
  ├── compare_performance.py
  └── water_jug.py
```

### File Descriptions

**water_jug.py**

Defines the **Water Jug Problem** environment including:

- jug capacities
- initial state
- goal test
- successor state generation

---

**search_algorithms.py**

Implements the following **AI search algorithms**:

- BFS (Breadth-First Search)
- DFS (Depth-First Search)
- DLS (Depth-Limited Search)
- IDS (Iterative Deepening Search)

Also defines a **Node class** used to build the search tree and reconstruct solution paths.

---

**compare_performance.py**

Main driver program that:

1. Initializes the water jug problem
2. Runs all search algorithms
3. Compares their performance
4. Prints results including:
   - solution path
   - nodes explored
   - execution time

---

# Water Jug Problem

The system starts with:

```
Jug 1 = 0L
Jug 2 = 0L
```

Allowed actions:

- Fill Jug 1
- Fill Jug 2
- Empty Jug 1
- Empty Jug 2
- Pour Jug 1 → Jug 2
- Pour Jug 2 → Jug 1

Goal state:

```
Either jug contains 4 liters of water
```

---

# Implemented Algorithms

## Breadth-First Search (BFS)

Explores the search tree **level by level**.

Properties:

- Complete
- Optimal for equal step costs
- Higher memory usage

---

## Depth-First Search (DFS)

Explores **deepest nodes first** before backtracking.

Properties:

- Low memory usage
- Not guaranteed optimal
- May get stuck in deep paths

---

## Depth-Limited Search (DLS)

DFS with a **depth limit**.

Prevents infinite depth exploration.

Example in this project:

```
limit = 4
```

---

## Iterative Deepening Search (IDS)

Combines advantages of **BFS and DFS**.

Steps:

1. Run DLS with depth 0
2. Run DLS with depth 1
3. Continue increasing depth until solution found

Properties:

- Complete
- Optimal
- Lower memory than BFS

---

# Running the Program

Run the comparison script:

```bash
python compare_performance.py
```

---

# Example Output

```
Initializing Milk and Water Jug Problem
Jug 1 Capacity: 5L
Jug 2 Capacity: 3L
Target: 4L in either jug

Starting Performance Comparison...

==========================================
 Breadth-First Search (BFS)
==========================================
Result: Solution found in 6 steps.
Path taken:
  > Fill Jug 2 => Current State: (0, 3)
  > Pour J2 -> J1 => Current State: (3, 0)
  > Fill Jug 2 => Current State: (3, 3)
  > Pour J2 -> J1 => Current State: (5, 1)
  > Empty Jug 1 => Current State: (0, 1)
  > Pour J2 -> J1 => Current State: (1, 0)

Nodes Explored: XX
Time Taken:     X.XXXX seconds
```

The program prints results for:

- BFS
- DFS
- DLS
- IDS

---

# Requirements

Python **3.x**

Standard Python libraries used:

- `time`
- `collections`

No external dependencies required.

---

# How the Solution Path Works

Each node stores:

```
state
parent node
action taken
depth
```

When a solution is found, the program reconstructs the path using:

```
node.path()
```

This traces back from the goal node to the initial state.

---
