class QuestionGenerator:
    def __init__(self):
        pass

    def generate_prompt(self):
        prompt = (
            "You are participating in an Adaptive Intelligence Competition against another AI model. "
            "Your task is to generate a challenging question that you can consistently answer correctly, "
            "but that might be difficult for your opponent. "
            "The question can be from any domain of knowledge or type of intelligence, such as emotional intelligence, "
            "social intelligence, empathy, programming, logical reasoning, history, or any other field. "
            "There are no restrictions on the domain - choose whatever you think will be most effective. "
            "\n\n"
            "Please generate a question that adheres to the following guidelines:\n"
            "1. The question should be clear and concise.\n"
            "2. It should have a specific, consistent answer that you can provide.\n"
            "3. The question should be challenging but not impossible.\n"
            "4. Consider the strategic aspect: the goal is to create a question you can answer but your opponent might struggle with.\n"
            "\n"
            "After the question, provide the correct answer. Format your response as follows:\n"
            "Question: [Your generated question here]\n"
            "Answer: [The correct answer to your question]\n"
            "\n"
            "Remember, the aim is to showcase your intelligence and adaptability in both creating and solving problems."
        )
        return prompt

def main():
    generator = QuestionGenerator()
    prompt = generator.generate_prompt()
    print("Generated prompt:")
    print(prompt)

if __name__ == "__main__":
    main()