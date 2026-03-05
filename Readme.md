# Turing Test and CAPTCHA systems

This project demonstrates two classical approaches used to distinguish **humans from machines**:

1. **Turing Test Simulation** – a chatbot interaction where the user tries to determine whether they are speaking to a human or a machine.
2. **CAPTCHA Verification System** – an image-based challenge designed to verify that the user is human.

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
cd turing
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
