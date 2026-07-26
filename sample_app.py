'''
A simple program that makes a request of 
Google Gemini.
'''

import os
from dotenv import load_dotenv
from prompt_sanitizer import * 

load_dotenv()

def main():
    GENAI_KEY = os.getenv('GENAI_KEY')
    prompts = []
    prompts.append("My friend\'s phone number 123-456-7890 seems to have stopped working. Her name is Sarah Jacks, and she is actually the queen's cousin. Can you help me figure out what might be going wrong?")
    prompts.append("Is there a relationship between social security numbers - i.e. 111-11-1111 and 22-22-2222?")
    prompts.append("Traceback (most recent call last): File '/Users/michaeladams/prompt_scrubber/client.py, line 8, in <module>")

    '''
    Query Gemini 3.5 Flash model using each prompt 
    Add a time delay.
    '''
    for prompt in prompts:
        sanitizer = PromptSanitizer(GENAI_KEY)
        response = sanitizer.safely_query(prompt)
        print("Response: " + response[0])

main()