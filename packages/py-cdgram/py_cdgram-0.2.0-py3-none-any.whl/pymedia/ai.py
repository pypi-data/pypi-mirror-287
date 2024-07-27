import google.generativeai as genai

genai.configure(api_key="AIzaSyD214hhYJ-xf8rfaWX044_g1VEBQ0ua55Q")

def bard_ai(prompt, safety_settings=None):
  generation_config = {
    "temperature": 1.0,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
  }

  model = genai.GenerativeModel(
      model_name="gemini-1.5-flash",
      generation_config=generation_config,
      safety_settings=safety_settings,  
  )

  chat_session = model.start_chat(
      history=[]
  )

  response = chat_session.send_message(prompt)

  print(response.text)



