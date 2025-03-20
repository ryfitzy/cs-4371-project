import ollama

messages = [
    {"role": "user", "content": "Hello llama3! How are you doing today?"},
    {"role": "user", "content": "What is the latest world news that you are aware of?"}
]

f = open("ollama_log.txt", "a")

for msg in messages:
    response = ollama.chat(model="mistral", messages=[msg])
    f.write(f"User: {msg["content"]}\n")
    f.write(f"Ollama: {response["message"]["content"]}\n")
    f.write("-" * 40 + "\n")

f.close()
