import os
import openai
import openai_translate

openai.api_key = openai_translate.API_KEY

def translate_text(prompt):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.3,
    max_tokens=100,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )
  return response.choices[0].text.strip()
    
prompt = 'translate this into traditional chinese. /n/n Silicon Valley Bank and Signature Bank Reignite /n ‘Moral Hazard’ Dilemma Bitcoin Was Designed to End'

result = translate_text(prompt)
print(result)