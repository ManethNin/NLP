print("hi")

from openai import OpenAI

client = OpenAI(api_key="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")

#"AIzaSyBYDKgOWlQ-v7kUpCgA4AWQ2j7JvsY6Uok" - gemini
# # Load model directly
# from transformers import AutoTokenizer, AutoModelForCausalLM

# tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-70b-hf")
# model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-70b-hf")

def generate_similar_domains(user_input):
#     domain_parts = user_input.split('.')
#     domain_name = domain_parts[0]
#     extension = domain_parts[1] if len(domain_parts) > 1 else ""

    prompt = f"""Generate 3 unique similar English domain names and 2 unique Sinhala (Singlish) domain names based on the given domain name. Do not include any additional text or explanation. Provide only the suggestions in JSON format, structured as follows:

Example:
Input: fastfoods.lk
Output:
{"quickmeals.lk", "fastmeals.lk", "quickfoods.lk" , "ikmanfoods.lk", "fastkaama.lk"}

user input = {user_input}"""

    # inputs = tokenizer(prompt, return_tensors="pt")
    outputs = client.completions.create(model="gpt-4o",  
    prompt=prompt,
    max_tokens=150,
    temperature=1.0,
    n=1,
    stop=None)

    # Clean the output
    # generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Extract only the domain names
    suggestions = outputs.choices[0].text.strip().split('\n')
    for i, suggestion in enumerate(suggestions):
        print(f"Suggestion {i + 1}: {suggestion}")

    return suggestions

# def print_suggestions(suggestions):
#     for i, domain in enumerate(suggestions, 1):
#         # print(f"{domain}")

# Example usage
suggestions = generate_similar_domains('freshfruits.lk')
# print_suggestions(suggestions)