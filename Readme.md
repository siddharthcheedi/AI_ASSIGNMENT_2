# Turing Test and CAPTCHA Architecture

## 1. Turing Test Simulation (`turing_test.py`)

### Architecture
The Turing Test is implemented as a **Rule-Based Conversational Agent** (similar to early NLP systems like ELIZA). 

#### Components:
- **Input Processing**: Reads user input and converts it to lower case for uniform pattern matching.
- **Pattern Matching Engine (Regex)**: Uses Python's `re` module to test input against an ordered set of regular expressions (e.g., matching greetings, questions about identity, weather, etc.).
- **Response Generation**: Maps matched patterns to a list of possible predefined responses. It uses random selection among valid responses to create structural variance and simulate conversational naturalness.
- **Simulated Typing Delay**: Introduces an artificial delay (`time.sleep`) proportional to the length of the response to simulate human typing speed.
- **Evaluation Loop**: The judge interacts iteratively until they exit the program, after which they are forced to make a binary decision (HUMAN or MACHINE).

#### Diagram (Conceptual)
`User Input -> [ Sanitization ] -> [ Regex Rule Matcher ] -> [ Response Selector ] -> [ Typing Delay ] -> Output Message`

## 2. CAPTCHA Verification System (`captcha_system.py`)

### Architecture
The system consists of an **Image-Based Challenge Generator**, leveraging the Python `captcha` library and `Pillow` to create visually distorted text images that deter automated bots.

#### Components:
- **Image CAPTCHA Generator**: 
  - Dynamically creates an image containing a random sequence of alphanumeric characters.
  - Applies a series of visual distortions including background noise (dots and curves), font warping, and varied color palettes.
  - The challenge text is visually rendered, defeating simple text scraping.
- **Display Engine**: 
  - Saves the generated CAPTCHA to disk as `current_captcha.png`.
  - Interfaces with the operating system's default image viewer (via `PIL.Image.show()`) to present the challenge to the human user.
- **Verification Engine**: 
  - Compares the human-typed user input against the original string used to generate the image.
  - Permits a maximum of 3 attempts before locking out the process, presenting a new unique image upon every failure.

#### Diagram (Conceptual)
`System Initiates -> [ Random String Generator ] -> [ Image Rendering with Distortion ] -> Image Displayed -> User Input -> [ Validator Engine ] -> Success/Failure Retry Logic`
