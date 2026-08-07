# Prompt Sanitizer
This tool is a Python module designed to provide a quick way to safely query a free
AI model. Ideally, this tool would become available pip. 

## What specific problem are you addressing?
Tools such as Pasteguard acts as a DLP proxy and browser extension to prevent leakage of sensitive information into AI models. However, Pasteguard specifically does not work with any of the popular, freely available models. This tool is, therefore, not useful for anyone depending on free models. 
 
## Why is the problem important?
Google offers at least one free model (Gemini 3.5 Flash), which holds values for development or low-budget applications. These applications are more likely to have exploitable flaws. Therefore, these applications are also likely to need the support of a tool like Pasteguard. 

## What existing tools or approaches exist?
Pasteguard acts as a proxy intercepting the traffic containing 
the prompt and then forwarding it on to the agent. Pasteguard is also experimenting with 
the tool being used as a browser extension. 
 
## What gap does your tool fill?
This tool provides a non-proxy means of redacting sensitive information from 
prompts. It does not rely on access to a paid AI model to work. 

## Known Limitations 
This solution is limited by the libraries it uses. Thus far, the solution could not successfully redact a username resembling a person's first and last name. 

This solution relies on the developer remembering to use the tool. A stronger version 
of this tool could detect data leaks without the developer needing to 
remember to do anything as many data leaks occur because of forgetfulness. We want to limit 
opportunities for forgetfulness to cause problems. 
 
# Credit Notes
The inspiration for this tool's replacement tags comes from [PasteGuard](https://github.com/sgasser/pasteguard/tree/main). 

# Resources 
- [Querying Gemini 3.5 Flash Model](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5#rest)
- [python-dotenv package](https://pypi.org/project/python-dotenv/)
- [scapy package](https://pypi.org/project/scapy/)
- [genai package](https://pypi.org/project/genai/)
- [Scapy Tutorial](https://www.geeksforgeeks.org/python/packet-sniffing-using-scapy/)
- [Another Scapy Tutorial](https://cse365.cse.buffalo.edu/PSS-Lab/)
- [Python Classes](https://www.w3schools.com/python/python_classes.asp)
- [Spacy Tutorial](https://spacy.io/usage/linguistic-features#section-named-entities)
- [Bash Script Example](https://www.w3schools.com/bash/bash_script.php)


# Running the Program on Linux 
So far, I have found that running the installs for spacy and en_core_web_sm 
as separate commands has been the most successful means of getting the application 
to run. 

- Create a .env in the main folder with a variable called GENAI_KEY. You will need to obtain a free API key for Gemini's 3.5 Flash model. You can get your key here: [Get Gemini API key](https://aistudio.google.com/api-keys)

- Run the following in the terminal
1. chmod +x installer_linux.sh
2. ./installer_linux.sh


# Running the Program on Mac 
So far, I have found that running the installs for spacy and en_core_web_sm 
as separate commands has been the most successful means of getting the application 
to run. 

- Create a .env in the main folder with a variable called GENAI_KEY. You will need to obtain a free API key for Gemini's 3.5 Flash model. You can get your key here: [Get Gemini API key](https://aistudio.google.com/api-keys)

- Run the following in the terminal
1. chmod +x installer_mac.sh
2. ./installer_mac.sh


# AI Usage 

## Overview 
For the most part, I used AI to:
1. Determine the feasibility of my proposed approach to creating this tool. 
2. Get a general outline for creating a DLP solution.   
3. Get the standard PII regexes used within the program. 

## Prompts
- (ChatGPT): What is the easiest way to intercept network traffic and forward it on using Python only? Don't give me full details, just a high-level overview.
- (ChatGPT): Would I have a better chance of capturing the outgoing unencrypted traffic heading toward Gemini's 3.5 Flash model if I use curl instead of the API?
- (ChatGPT): So, there isn't a way to capture the unencrypted traffic of a pre-existing application
- (ChatGPT): How then does PasteGuard manage to transform prompts before it reaches the model?
- (ChatGPT): What about the docker version of PasteGuard?
- Why bother with a proxy at that point? Why should I not simply create a library that extends the genai library and has "santize_query" method that queries the model based on a given prompt WITH the sensitive info redacted? Just evaluate the feasibility and any pitfalls of my idea.
- (Gemini): create my own python package
- (ChatGPT): Give me standard Python regexes for the following: social security numbers phone numbers email addresses bank account numbers routing numbers EIN numbers tax ID numbers credit card numbers debit card numbers
- (ChatGPT): What about a standard regex for names?
- (Gemini): import spacy no module named click
- (Gemini): alternatives to spacy
- (Gemini): getting started with spacy mac
- (Gemini): linux bash script
- (Gemini): linux install python and pip 
- (Gemini): hombrew install python3 and pip
- (Gemini): powershell install python and pip 
- Can spacy idenityf specific addresses



