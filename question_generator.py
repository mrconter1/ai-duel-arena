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

def main():
    generator = QuestionGenerationTemplate()
    prompt = generator.generate_prompt()
    print("Generated prompt:")
    print(prompt)

if __name__ == "__main__":
    main()