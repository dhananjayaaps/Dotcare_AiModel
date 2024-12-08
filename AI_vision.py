import google.generativeai as genai
from flask import jsonify
from pinecone import Pinecone

from credentials import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

def askAboutMother(question):

    prompt = f"""{question}"""
    # print(prompt)

    # print(prompt)
    generation_config = {
      "temperature": 1,
      "top_p": 0.95,
      "top_k": 40,
      "max_output_tokens": 8192,
      "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
      model_name="gemini-1.5-flash",
      generation_config=generation_config,
    )
    response = model.generate_content(prompt)

    # print(response.text)

    return jsonify(response.text.split('|')), 200