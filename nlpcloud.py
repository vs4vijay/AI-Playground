import nlpcloud
client = nlpcloud.Client("gpt-j", "your_token", gpu=True)
generation = client.generation("""Here is a tutorial about how to make a cake.

1. Take some flour.
2. Take some sugar.""",
    max_length=500)
print(generation["generated_text"])
