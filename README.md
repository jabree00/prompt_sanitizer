## What specific problem are you addressing?
The original Pasteguard acts as a DLP proxy and browser extension to prevent leakage of sensitive information. However, the tool does not work with any of the popular free models.
 
## Why is the problem important?
The popular free AI models such as Gemini 3.5 Flash hold value for development or low-budget applications. These applications are more likely to have exploitable flaws. Therefore, these applications are also likely to need the support of a tool like Pasteguard. 

## What existing tools or approaches exist?
The current solution that I have explored acts as a proxy intercepting the traffic containing 
the prompt and then forwarding it on to the agent.
 
## What gap does your tool fill?


## Known Limitations 
This solution is limited by the libraries it uses. Thus far, the solution could not successfully redact a username resembling a person's first and last name. 
 
# Credit Notes
The inspiration for this tool's dashboard and replacement tags comes from [PasteGuard](https://github.com/sgasser/pasteguard/tree/main). 

# Resources 
[Querying Gemini 3.5 Flash Model](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5#rest)
[python-dotenv package](https://pypi.org/project/python-dotenv/)
[scapy package](https://pypi.org/project/scapy/)
[genai package](https://pypi.org/project/genai/)
[Scapy Tutorial](https://www.geeksforgeeks.org/python/packet-sniffing-using-scapy/)
[Another Scapy Tutorial](https://cse365.cse.buffalo.edu/PSS-Lab/)
[Python Classes](https://www.w3schools.com/python/python_classes.asp)
[Spacy Tutorial](https://spacy.io/usage/linguistic-features#section-named-entities)


# How to Run on Linux / Mac 
So far, I have found that running the installs for spacy and en_core_web_sm 
as separate commands has been the most successful means of getting the application 
to run. 

1. Install python3 / pip 
2. python3 -m venv .venv 
3. source .venv/bin/activate
4. pip install -r requirements.txt
5. pip install -U pip setuptools wheel 
6. pip install spacy 
7. python -m spacy download en_core_web_sm

## Troubleshooting 
You may also need to run this line:
pip install -U click spacy 

# AI Usage 

## Overview 
For the most part, I used AI to:
1. Determine the feasibility of my proposed approach to creating this tool. 
2. Get a general outline for creating a DLP solution.   
3. Get the standard PII regexes used within the program. 

## Prompts
Prompt #1 (ChatGPT): What is the easiest way to intercept network traffic and forward it on using Python only? Don't give me full details, just a high-level overview.

Prompt #2 (ChatGPT): Would I have a better chance of capturing the outgoing unencrypted traffic heading toward Gemini's 3.5 Flash model if I use curl instead of the API?

Prompt #3 (ChatGPT): So, there isn't a way to capture the unencrypted traffic of a pre-existing application

Prompt #4 (ChatGPT): How then does PasteGuard manage to transform prompts before it reaches the model?

Prompt #5 (ChatGPT): What about the docker version of PasteGuard?

Prompt #6: Why bother with a proxy at that point? Why should I not simply create a library that extends the genai library and has "santize_query" method that queries the model based on a given prompt WITH the sensitive info redacted? Just evaluate the feasibility and any pitfalls of my idea.

Prompt #7 (Gemini): create my own python package

Prompt #8 (ChatGPT):
Give me standard Python regexes for the following: social security numbers phone numbers email addresses bank account numbers routing numbers EIN numbers tax ID numbers credit card numbers debit card numbers

Prompt #9 (ChatGPT):
What about a standard regex for names?

Prompt #10 (Gemini):
import spacy no module named click

Prompt #11 (Gemini):
alternatives to spacy

Prompt #12 (Gemini)
getting started with spacy mac

