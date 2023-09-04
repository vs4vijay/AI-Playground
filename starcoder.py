from transformers import AutoModelForCausalLM, AutoTokenizer

checkpoint = "bigcode/starcoder"
# checkpoint = "bigcode/santacoder"
device = "cpu" # for GPU usage or "cpu" for CPU usage

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
# to save memory consider using fp16 or bf16 by specifying torch.dtype=torch.float16 for example
model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)

inputs = tokenizer.encode("def print_hello_world():", return_tensors="pt").to(device)
outputs = model.generate(inputs)
print(tokenizer.decode(outputs[0]))

# from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
# checkpoint = "bigcode/starcoder"

# model = AutoModelForCausalLM.from_pretrained(checkpoint)
# tokenizer = AutoTokenizer.from_pretrained(checkpoint)

# pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, device=0)
# print( pipe("def hello():") )


############

