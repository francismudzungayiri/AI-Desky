from openai import OpenAI
import os
import json 


class Challenge:
    
    def __init__(self):
        self.KEY = os.getenv('OPENAI_API_KEY')
        self.client = OpenAI(api_key=self.KEY)

    def extract_info_with_llm(self,prompt):
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[
                {"role": "system", "content": "You are an assistant that extracts structured information from text."},
                {"role": "user", "content": f"Extract the person's name face a challenges, office number, and challenge faced from this prompt and return a json like response:\n\n{prompt}"}
            ]
        )
        #return response.choices[0].message.content
        #return json.loads(response.choices[0].message.content)
        try:
            return json.loads(response.choices[0].message.content)
        except Exception as e:
            print("Error parsing JSON:", e)
            return {"raw_output": response.choices[0].message.content}
    
        
        
    # Example usage
    ##prompt_text = "HELLO MAY I GET ASSISTANCE ON MY PRINTER SEEMS IT HAS A PAPER JAM, ITS LILLIAN FROM E435 "
    #result = extract_info_with_llm(prompt_text)
    #print(result)
