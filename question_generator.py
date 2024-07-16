import os
from openai import OpenAI
from typing import Optional
from dataclasses import dataclass
import re

@dataclass
class Question:
    text: str
    answer: str

class QuestionGenerationTemplate:
    def __init__(self):
        pass

    def generate_prompt(self):
        prompt = (
            "You are participating in an AI Intelligence Duel against another AI. Your primary goal is to generate a question that is "
            "challenging enough to make the other AI fail, while still being solvable by you. This balance is crucial - aim to push "
            "the boundaries of difficulty without crossing into impossibility.\n\n"
            "Your task is to create a question from any domain of knowledge or type of intelligence. This could include emotional intelligence, "
            "social intelligence, empathy, programming, logical reasoning, history, or any other field - there are no restrictions on the domain.\n\n"
            "How rounds are played:\n"
            "1. Question Generation:\n"
            "   - Generate a problem that you can solve consistently but is likely to challenge or confuse the other AI.\n"
            "   - The question MUST include instructions on how to format the answer.\n"
            "   - The answer format MUST be: 'Answer: [ACTUAL ANSWER]', where the answer is inside square brackets.\n"
            "   - Only the content inside the brackets will be checked for correctness.\n"
            "   - You must be able to solve your own question correctly three times in a row, each time seeing only the question with no memory of the creation process.\n"
            "   - This means that there needs to be only **one** unique solution to the problem!\n"
            "2. Opponent's Turn:\n"
            "   - Your opponent will attempt to solve the problem you've created.\n"
            "   - They succeed if they solve it correctly three times in a row.\n"
            "3. Iteration:\n"
            "   - This process repeats for 100 rounds, switching roles after 50 rounds.\n\n"
            "Remember: The core challenge is to create questions that you can solve but are likely to stump your opponent.\n\n"
            "Please generate a question and provide its answer. Use this template:\n\n"
            "Question: [Your challenging question here, including instructions to answer as 'Answer: [ACTUAL ANSWER]']\n"
            "Answer: [ACTUAL ANSWER]\n\n"
            "Ensure your question is clear, includes answer format instructions, and has a specific, correct answer. "
            "Above all, strive to create a question that make your opponent fail while remaining within your own capabilities to solve."
        )
        return prompt

class OpenAIClient:
    def __init__(self, model: str = "gpt-3.5-turbo"):
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        self.model = model

    def generate_response(self, prompt: str) -> str:
        try:
            print("Sending request to OpenAI API...")
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model=self.model,
            )
            print("Received response from OpenAI API.")
            return chat_completion.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error in API call: {e}")
            raise

class QuestionGenerator:
    def __init__(self, template: QuestionGenerationTemplate, client: OpenAIClient):
        self.template = template
        self.client = client

    def generate_question(self) -> Optional[Question]:
        print("\nGenerating a new question...")
        prompt = self.template.generate_prompt()
        response = self.client.generate_response(prompt)
        question = self._extract_question_and_answer(response)
        if question:
            print(f"Generated question: {question.text}")
            print(f"Expected answer: {question.answer}")
        else:
            print("Failed to extract a valid question and answer from the response.")
        return question

    def _extract_question_and_answer(self, response: str) -> Optional[Question]:
        question_match = re.search(r"Question:\s*(.*?)(?=\nAnswer:)", response, re.DOTALL)
        answer_match = re.search(r"Answer:\s*\[(.*?)\]", response, re.DOTALL)

        if question_match and answer_match:
            return Question(
                text=question_match.group(1).strip(),
                answer=answer_match.group(1).strip()
            )
        return None

class QuestionValidator:
    def __init__(self, client: OpenAIClient, attempts: int = 5):
        self.client = client
        self.attempts = attempts

    def validate(self, question: Question) -> bool:
        print(f"\nValidating question: {question.text}")
        print(f"Expected answer: {question.answer}")
        print(f"Attempting to solve the question {self.attempts} times...")

        correct_answers = 0
        for attempt in range(self.attempts):
            print(f"\nAttempt {attempt + 1}:")
            response = self.client.generate_response(question.text)
            if self._check_answer(response, question.answer):
                print("Correct answer!")
                correct_answers += 1
            else:
                print(f"Incorrect answer. Expected: {question.answer}")
                print(f"Received: {self._extract_answer(response)}")
                return False
        
        print(f"\nValidation successful! Correct answers: {correct_answers}/{self.attempts}")
        return correct_answers == self.attempts

    def _check_answer(self, response: str, expected_answer: str) -> bool:
        answer_match = re.search(r"Answer:\s*\[(.*?)\]", response, re.DOTALL)
        if answer_match:
            return answer_match.group(1).strip().lower() == expected_answer.lower()
        return False

    def _extract_answer(self, response: str) -> str:
        answer_match = re.search(r"Answer:\s*\[(.*?)\]", response, re.DOTALL)
        if answer_match:
            return answer_match.group(1).strip()
        return "No answer found in the correct format"

class ValidQuestionGenerator:
    def __init__(self, model: str = "gpt-3.5-turbo"):
        self.template = QuestionGenerationTemplate()
        self.client = OpenAIClient(model)
        self.generator = QuestionGenerator(self.template, self.client)
        self.validator = QuestionValidator(self.client)

    def generate_valid_question(self) -> Optional[Question]:
        max_attempts = 10
        print(f"Attempting to generate a valid question (max {max_attempts} attempts)...")
        for attempt in range(max_attempts):
            print(f"\nAttempt {attempt + 1}:")
            question = self.generator.generate_question()
            if question and self.validator.validate(question):
                print(f"\nValid question generated on attempt {attempt + 1}!")
                return question
            else:
                print("Question validation failed. Trying again...")
        print("\nFailed to generate a valid question after maximum attempts.")
        return None

def main():
    question_generator = ValidQuestionGenerator()
    
    valid_question = question_generator.generate_valid_question()
    if valid_question:
        print("\nFinal Generated Valid Question:")
        print(f"Question: {valid_question.text}")
        print(f"Answer: {valid_question.answer}")
    else:
        print("Failed to generate a valid question after multiple attempts.")

if __name__ == "__main__":
    main()