import google.generativeai as genai

def get_insights_from_genai(metrics_data):
    api_key = GENAI_API_KEY
    genai.configure(api_key=api_key)

    generation_config = {
      "temperature": 1,
      "top_p": 0.95,
      "top_k": 64,
      "max_output_tokens": 8192,
      "response_mime_type": "text/plain",
    }
    safety_settings = [
      {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
      },
      {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
      },
      {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
      },
      {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
      },
    ]

    model = genai.GenerativeModel(
      model_name="gemini-1.5-flash",
      safety_settings=safety_settings,
      generation_config=generation_config,
    )

    chat_session = model.start_chat(
      history=[
      ]
    )
    
    message = f"In 200 words, provide insights (in bullet points for each topic)  for the following metrics \
        data also include the ip address of the node:\n{json.dumps(metrics_data, indent=2)}"
    response = chat_session.send_message(message)

    return response.text