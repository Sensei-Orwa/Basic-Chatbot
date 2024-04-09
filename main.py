import openai

openai.api_key = "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"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5",
        messages = [{"role": "user", "content": prompt }]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)

