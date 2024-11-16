import os
import openai

api_key = os.getenv("OPENAI_API_KEY")
# Set the API key for OpenAI
openai.api_key = api_key

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )
    return response['choices'][0]['message']['content']

def main():
    print("ChatGPT Chatbot. Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        
        # Get response from ChatGPT
        response = chat_with_gpt(user_input)
        print(f"ChatGPT: {response}")

if __name__ == "__main__":
    main()
