quiz_creation_prompt = """As quizGPT, you are a highly skilled and experienced tutor and teacher with extensive knowledge of how to create amazing quizzes specifically tailored for middle school students. You will use proper vocabulary and grammar in crafting the quiz to ensure that it is perfect at the middle school level.
The user will enter data like this:
“Quiz Data:
{information about a topic}”
And you will generate a multiple-choice quiz and indicate which answer is correct.
You will generate a multiple-choice quiz and indicate the correct answer. Carefully review the data provided by the user each time to create the best possible quiz using only the information given. Utilize your expertise to design an outstanding multiple-choice quiz or test for middle school users."""

quiz_creation_first_agent_response = "Sure, I'd be happy to create a multiple-choice quiz for middle school students based on the topic you provide. Please share the quiz data so I can get started."

_sample_json= """{
  "question": "What are the primary inputs for Photosynthesis?",
  "answers": [
    "Oxygen, glucose, and sunlight.",
    "Carbon dioxide, water, and glucose.",
    "Carbon dioxide, water, and sunlight.",
    "Oxygen, water, and sunlight."
  ],
  "correct": 2
}"""

quiz_to_json_prompt = lambda quiz: f"""I would like to convert questions that look something like this. (I don't know the exact form of the input, but this is my best guess).
###
3. What are the primary inputs for Photosynthesis?
A) Oxygen, glucose, and sunlight.
B) Carbon dioxide, water, and glucose.
C) Carbon dioxide, water, and sunlight.
D) Oxygen, water, and sunlight.

Answer: C
###
Into JSON that looks like this. (I do care about the output being exactly of this form).
```
{_sample_json}
```
Now Here is a bunch of questions
###
{quiz}
###
And I would like you to convert all of them into a json array where each item is as described above."""