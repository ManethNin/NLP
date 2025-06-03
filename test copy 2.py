import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyBYDKgOWlQ-v7kUpCgA4AWQ2j7JvsY6Uok")

def generate_similar_domains(user_input):
    # Create the model
    generation_config = {
        "temperature": 0.9,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
    }

    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash-exp",
        generation_config=generation_config,
    )

    prompt = f"""
    Given the domain name(either in sinhala or english) '{user_input}', generate:
    - 3 similar English domain names
    - 2 similar Sinhala (Singlish) domain names
    
    Rules:
    1. Keep the same TLD (e.g., .lk) as the input domain
    2. Make suggestions relevant to the theme/meaning of the input domain. user_input can be both english or sinhala
    3. For English: Use related words, synonyms, or combinations
    4. For Sinhala: Use transliterated Sinhala words related to the theme
    
    Return ONLY the domain names in this exact JSON format:
    {{ "domain1.tld", "domain2.tld", "domain3.tld","domain1.tld", "domain2.tld"}}
    """

    chat = model.start_chat()
    response = chat.send_message(prompt)
    
    try:
        # Clean and extract the JSON response
        response_text = response.text
        if "```json" in response_text:
            response_text = response_text.split("```json")[1].split("```")[0].strip()
        elif "```" in response_text:
            response_text = response_text.split("```")[1].strip()
        return response_text
    except Exception as e:
        return f"Error processing response: {str(e)}"

# Example usage
if __name__ == "__main__":
    test_input = "hhdh.lk"
    suggestions = generate_similar_domains(test_input)
    print(suggestions)



