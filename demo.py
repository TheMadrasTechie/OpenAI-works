import openai
openai.api_key = "YOUR_API_KEY"

model_engine = "text-davinci-003"
prompt = "நண்பா நண்பி எல்லாரும் வணக்கம் எப்படி இருக்கீங்க"
completion = openai. Completion.create(engine=model_engine,prompt=prompt,max_tokens=1024, n=1,stop=None,temperature=0.5,)
response = completion.choices[0].text
print (response)
