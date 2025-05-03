import openai
from typing import List

api_key=""
client=openai.OpenAI(api_key=api_key)
#Function to Generate memo based on the notes and template

def generate_memo(notes: str, template: str):
    prompt =f"Generate a project memo based on the following notes: {notes}. Use the following template: {template}"
    response=client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert IRS tax consultant and memo writer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=1000
    )

    return response.choices[0].message.content


#Example templates for different industries
TEMPLATES={
    "IT Project": "Title: {title}\nOverview: :{overview}\nTechnical Details:{details}",
    "Construction Project": "Project Title: {title}\nScope:{scope}\nBudget:{budget}",

}