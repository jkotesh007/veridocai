import openai
import os
#Set your OpenAI key securely (Environment Variable Recommended)
api_key="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"
client=openai.OpenAI(api_key=api_key)

    #os.getenv("OPENAI_API_KEY"))
def generate_memo_from_notes(notes_text):
    try:
        #Template prompt
        template_prompt=f"""
You are a professional IRS tax memo writer.
Using the following project notes:
\"\"\"{notes_text}\"\"\"

Generate a formal IRS_compliant project memo
Ensure the memo includes:
-Project Background
-Qualified Research Activities
-Technology Uncertainty
-Process of Experimentation
-Business Component
-Conclusion
Use Formal and Technical Language. Write the memo in structured paragraphs.

"""
        response=client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role":"system","content":"You are an expert IRS tax consultant and memo writer."},
                {"role":"system","content":template_prompt}
            ],
            temperature=0.3,
            max_tokens=4000
        )
        memo_text=response.choices[0].message.content
        return memo_text
    except Exception as e:
        print(f"Error generating memo:{e}")
        return None
