import re
import spacy 
from google import genai

class PromptSanitizer: 
    def __init__(self, GENAI_KEY):
        self.client = genai.Client(api_key=GENAI_KEY)


    def regex_scrub_prompt(self,prompt):

        targets = {
            "PHONE" : r"\b(?:\+?1[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?)\d{3}[-.\s]?\d{4}\b",
            "SSN" : r"\b\d{3}-?\d{2}-?\d{4}\b",
            "EIN" : r"\b\d{2}-\d{7}\b",
            "CARD NUMBER": r"\b(?:\d[ -]*?){13,19}\b",
            "EMAIL" : r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
        }

        for key, regex in targets.items():
            prompt = re.sub(regex, "["+ key + " INSERTED]", prompt)

        return prompt

    def nlp_scrub_prompt(self,prompt):
        processor = spacy.load("en_core_web_sm")
        analysis = processor(prompt)

        for entity in analysis.ents:
            if (entity.label_ == "PERSON"):
                start = entity.start_char
                end = entity.end_char
                prompt = prompt[0:start] + "[NAME INSERTED]" + prompt[(end + 1):]

        return prompt

            
    def safely_query(self,prompt):
        safe_prompt = self.regex_scrub_prompt(prompt)
        safe_prompt = self.nlp_scrub_prompt(safe_prompt)
        response = None

        response = self.client.interactions.create(
                model="gemini-3.5-flash", 
                input=safe_prompt
        )

        return (safe_prompt,response)

