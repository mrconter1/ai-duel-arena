class QuestionGenerator:
    def __init__(self):
        pass

    def generate_prompt(self):
        prompt = (
            "You are participating in an Adaptive Intelligence Competition against another AI model. "
            "The competition follows this structure:\n\n"
            "1. Initial State: The competition starts with no pre-existing questions.\n"
            "2. Problem Generation:\n"
            "   - You (LLM A) generate a new problem, considering previously generated questions and your opponent's performance.\n"
            "   - You must attempt to solve your own newly created problem multiple times to ensure consistency.\n"
            "   - If you cannot solve it consistently, you must generate a new problem until you create one you can solve consistently.\n"
            "3. Problem Solving:\n"
            "   - Your opponent (LLM B) will access previous questions, its answers, and the correct answers.\n"
            "   - LLM B will attempt to solve the new problem you've created.\n"
            "   - The result (correct or incorrect) is recorded and made available to both LLMs.\n"
            "4. Iteration:\n"
            "   - This process repeats, with you and your opponent alternating roles in generating and solving problems.\n"
            "   - This continues until a predetermined number of problems have been generated and solved.\n"
            "5. Role Reversal:\n"
            "   - The entire process is then repeated with your opponent generating problems and you solving them.\n\n"
            "Your current task is to generate a challenging question. The question can be from any domain of knowledge "
            "or type of intelligence (e.g., emotional intelligence, social intelligence, empathy, programming, logical reasoning, "
            "history, or any other field). There are no restrictions on the domain.\n\n"
            "Please generate a question that adheres to the following guidelines:\n"
            "1. The question should be clear and concise.\n"
            "2. It should have a specific, consistent answer that you can provide.\n"
            "3. The question should be challenging but not impossible.\n"
            "4. Consider the strategic aspect: the goal is to create a question you can answer consistently but your opponent might struggle with.\n"
            "\n"
            "After the question, provide the correct answer. Format your response as follows:\n"
            "Question: [Your generated question here]\n"
            "Answer: [The correct answer to your question]\n"
            "\n"
            "Remember, the aim is to showcase your intelligence and adaptability in both creating and solving problems, "
            "while also considering the overall competition structure and strategy."
        )
        return prompt

def main():
    generator = QuestionGenerator()
    prompt = generator.generate_prompt()
    print("Generated prompt:")
    print(prompt)

if __name__ == "__main__":
    main()