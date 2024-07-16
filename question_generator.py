
class QuestionGenerator:
    def __init__(self):
        pass

    def generate_prompt(self):
        prompt = (
            "You are participating in an AI Intelligence Duel against another AI. Your task is to generate a challenging question "
            "from any domain of knowledge or type of intelligence. This could include emotional intelligence, social intelligence, "
            "empathy, programming, logical reasoning, history, or any other field - there are no restrictions on the domain.\n\n"
            "The main goal is to create a question that is difficult enough to make the other AI fail, but 'easy' enough that you can solve it consistently. "
            "Here's what you need to know about how the rounds will be played:\n\n"
            "1. Question Generation:\n"
            "   - You will generate a new problem.\n"
            "   - You have access to all previously generated questions, the opponent's answers, and the correct answers.\n"
            "   - You must be able to solve your own question consistently. This means solving it correctly three times in a row, "
            "     each time seeing the question with no context or memory of the question writing process or the competition.\n"
            "2. Opponent's Turn:\n"
            "   - Your opponent will attempt to solve the problem you've created.\n"
            "   - They succeed if they solve the question correctly three times in a row.\n"
            "   - Their result (success or failure) will be recorded.\n"
            "3. Iteration:\n"
            "   - This process repeats, with you and your opponent taking turns generating and solving problems.\n"
            "   - The duel will continue for exactly 100 rounds. Each round consists of one AI generating a question and the other attempting to solve it.\n"
            "   - After 50 rounds, the roles will switch: if you were generating questions, you'll start solving, and vice versa.\n\n"
            "Please generate a question and provide its answer. Use the following template:\n\n"
            "Question: [Your question here]\n"
            "Answer: [The specific, correct answer to your question]\n\n"
            "Ensure that your question is clear and concise, and that the answer is specific and correct. "
            "Remember, you should be able to solve this question consistently, but your goal should still be to make the other AI fail. "
        )
        return prompt

def main():
    generator = QuestionGenerator()
    prompt = generator.generate_prompt()
    print("Generated prompt:")
    print(prompt)

if __name__ == "__main__":
    main()