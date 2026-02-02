# AI Coding Agent Experiment Documentation

## Task
Document the experiment of creating and testing rules for GitHub Copilot to guide its behavior according to desired coding practices.

---
## 1. What I Did
- Created a **rules file (`copilot-instructions.md`)** to guide Copilot’s behavior.
- Defined rules in four categories:
  - **General Behavior**: act as a patient senior developer, ask questions if unclear, prefer correctness over speed.
  - **Coding Style**: write simple, readable code, follow project structure, do not invent APIs or libraries.
  - **Communication**: be concise, explain reasoning when necessary.
  - **Safety**: admit uncertainty, avoid unnecessary changes.
- Added explicit **placeholders and comments** in Python functions to test specific rules.



## 2. What Worked
- Copilot **followed syntax and style rules** reliably (avoided pandas/numpy, wrote readable code).
- Placeholders and explicit comments effectively made Copilot **defer action when unclear**, aligning with rules like *“do not assume requirements.”*
- Small, focused functions helped Copilot **avoid unnecessary refactoring**.
- Testing rules one by one helped **identify patterns of obedience and drift**.



## 3. What Didn’t Work
- Copilot sometimes **defaulted to assumptions** if rules were not explicitly reinforced in comments.
  - Example: assuming CSV headers even when dataset format was unclear.
- Behavioral rules (like asking questions instead of guessing) required **stronger explicit instructions**.
- Rules influence behavior probabilistically, not every suggestion followed the rules perfectly.
- Needed iterative testing and reinforcement to reduce incorrect suggestions.


## 4. Insights Gained
- Rules **effectively guide Copilot’s behavior** when combined with explicit comments and placeholders.
- Explicit comments act as **“in-context training”**, helping Copilot defer rather than assume.
- Behavioral alignment requires both:
  1. A **global rules file** (`copilot-instructions.md`)  
  2. **Local, function-level prompts/comments**
- Proper rules reduce cognitive overhead for the developer by **minimizing corrections, refactors, and guesswork**.
- Copilot behaves like a junior developer:
  - **Strong guidance + structured instructions** = faster, safer collaboration.
  - **Weak guidance** = increased hallucinations and assumptions.



### Conclusion
By creating rules and testing them systematically, I was able to **align Copilot’s behavior with my intent, thought patterns and expectations**.  
The combination of **global rules and local prompts** provides a practical framework for using AI coding assistants effectively in real projects.
