import os
import openai

name = input("What is your name? ")

print(f"Hi {name}!. I'm a super intelligent AI. I can answer any question you ask me. Ask me a question. Type 'exit' to exit.")

while True:
    # Set the API key
    openai.api_key = "YOUR_API_KEY"


    # Ask the user for a prompt
    prompt = input(f"{name}: ")

    if prompt == "exit":
         break

    # Use the ChatGPT API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=4000,
        temperature=0,
    )

    # Print the response
    response = response.choices[0].text
    print("AI: " + response.replace("\n\n", ""))
    os.system("pause")
    os.system("cls")  # Clear the screen (cls or clear)