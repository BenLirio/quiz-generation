import os
import sys
import openai
import prompts
openai.api_key = os.getenv("OPENAI_API_KEY")
clear = lambda: os.system('clear')

def make_quiz(quiz_data):
  print("Generating quiz...")
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "system",
        "content": prompts.quiz_creation_prompt
      },
      {
        "role": "assistant",
        "content": prompts.quiz_creation_first_agent_response
      },
      {
        "role": "user",
        "content": f"Quiz Data: \n{quiz_data}"
      },
    ]
  )
  return completion.choices[0].message.content

def extract_json_array(input_string):
  start_found = False
  start = 0
  end = 0
  for i, c in enumerate(input_string):
    if c == '[' and not start_found:
      start_found = True
      start = i
    elif c == ']':
      end = i
  return eval(input_string[start:end+1])

def quiz_to_json(quiz_string):
  print("Converting quiz to JSON...")
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "system",
        "content": prompts.quiz_to_json_prompt(quiz_string)
      },
    ]
  )
  quiz_json_string = completion.choices[0].message.content
  quiz_json = extract_json_array(quiz_json_string)
  return quiz_json

def parse_answer(answer):
  try:
    return ord(answer.strip().lower()) - ord('a')
  except:
    return None

def take_quiz(quiz):
  for quiz_question in quiz:
    question = quiz_question.get('question')
    answers = quiz_question.get('answers')
    correct = quiz_question.get('correct')
    if question is None or answers is None or correct is None:
      print("Invalid quiz question")
      continue
    clear()
    print(question)
    for i, answer in enumerate(answers):
      print(f"{chr(ord('A') + i)}) {answer}")
    while True:
      answer = parse_answer(input("Answer: "))
      if answer is None:
        print(f"Answer should be a letter between A and {chr(ord('A') + len(answers)-1)}")
        continue
      if answer == correct:
        print("Correct!")
        input("Press enter to continue")
        break
      else:
        print("Incorrect. Try again.")



if __name__ == '__main__':
  if len(sys.argv) < 2:
    print("Please provide a quiz data file as an argument.")
    sys.exit(1)
  quiz_data_file = sys.argv[1]
  quiz_data = open(quiz_data_file).read()
  quiz = make_quiz(quiz_data)
  quiz_json = quiz_to_json(quiz)
  take_quiz(quiz_json)
  clear()
  print("Thanks for taking the quiz!")