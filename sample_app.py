'''
A simple program that makes a request of 
Google Gemini.
'''

import os
from dotenv import load_dotenv
from prompt_sanitizer import * 

load_dotenv()

def main():
    context =  '''
    PROMPT SANITIZER is a Python module used to safely query free AI models.
    The following app provides an inside look on how PROMPT SANITIZER works
    by providing some sample raw prompts and the resulting scrubbed prompt.

    For demo purposes and avoiding free tier limits, this demo DOES NOT 
    query the free model. However, creating a PromptSanitizer object and calling the 
    safely_query() method with the prompt as input will allow you to see 
    that this module queries Gemini's 3.5 Flash model with the sanitized prompt. 

    To see the above feature at work, you will need to get a free API key for one of 
    Gemini's 3.5 Flash model. Please see the README for further instructions. 
    '''
    print(context)
    prompts = []

    prompts.append("My friend\'s phone number 123-456-7890 seems to have stopped working. Her name is Sarah Jacks, and (fun fact) she is actually related to the queen of England. Can you help me figure out what might be going wrong?")
    prompts.append("Is there a relationship between social security numbers - i.e. 111-11-1111 and 222-22-2222?")
    prompts.append("Traceback (most recent call last): File '/Users/michaeladams/prompt_scrubber/client.py, line 8, in <module>")
    prompts.append("My mac address is AB:01:02:03:04:FF and my passport number is C12345678 is there any relationship between the two values?")
    prompts.append("My IP address says 192.168.10.30. Is that public or private?")


    '''
    Query Gemini 3.5 Flash model using each prompt 
    Add a time delay.
    '''

    count = 1
    for prompt in prompts:
        sanitizer = PromptSanitizer()
        response = sanitizer.scrub_prompt(prompt)
        print("-" * 50)
        print(f"PROMPT #{count}:\n{prompt}\n\n")
        print(f"SCRUBBED PROMPT:\n{response}")
        count += 1

    print("-" * 50)
    print("       END OF SAMPLE PROMPTS")
    print("-" * 50)
    confirm = input("\n\nWould you like to try querying the model? Type 'y' to confirm.\n")
    if (confirm == 'y'):
        confirm = input("\n\nHave you updated the .env file with an api key called GENAI_KEY? Type 'y' to confirm.\n")
        if (confirm == 'y'):
            sanitizer = PromptSanitizer()
            prompt = input("\n\nProvide a sample prompt:\n")
            print(f"RAW PROMPT: {prompt}")
            print("-" * 50)
            result = sanitizer.safely_query(prompt)
            print(f"MODIFIED PROMPT: {result[0]}")
            print("-" * 50)
            print(f"GEMINI 3.5 FLASH MODEL RESPONSE: {result[1]}")
            print("-" * 50)
            
        else:
            input("Please update the .env then try again.\n\n")

    print("Sample app execution is terminating...\n\n")


main()