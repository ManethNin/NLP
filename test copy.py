
#"AIzaSyBYDKgOWlQ-v7kUpCgA4AWQ2j7JvsY6Uok" - gemini

import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyBYDKgOWlQ-v7kUpCgA4AWQ2j7JvsY6Uok")

def generate_similar_domains(user_input):
    # Create the model
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=generation_config,
    )

    chat_session = model.start_chat(
    history=[
        {
        "role": "user",
        "parts": [
            "Generate 3 unique similar English domain names and 2 unique Sinhala (Singlish) domain names based on the given domain name. Do not include any additional text or explanation. Provide only the suggestions in JSON format, structured as follows:\n\nExample:\nuser_input: fastfoods.lk\nOutput:\n{\"quickmeals.lk\", \"fastmeals.lk\", \"quickfoods.lk\" , \"ikmanfoods.lk\", \"fastkaama.lk\"}\n\nuser input = {user_input}",
        ],
        },
        {
        "role": "model",
        "parts": [
            "```json\n{\n  \"travelguide.lk\",\n  \"traveltips.lk\",\n  \"tourguide.lk\",\n  \"yaathraguru.lk\",\n  \"sancharakaarana.lk\"\n}\n```\n",
        ],
        },
    ]
    )

    response_part = chat_session.history[-1].parts[0]  # Access the last response
    response_text = response_part.text

    # Clean up the response text to extract the JSON content
    if "```json" in response_text:
        response_text = response_text.split("```json")[1].strip("`").strip()

    print(response_text)
    return response_text

# Example usage
suggestions = generate_similar_domains('freshfruits.lk')
# print_suggestions(suggestions)