import spacy
import os
#from date_spacy import find_dates
from spacy.language import Language
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_KEY"))

@Language.component("openai_summarizer")
def summarize_text(doc):
    """Custom component that summarizes the text using OpenAI's GPT model."""
    dates = []
    for ent in doc.ents:
        if ent.label_ == 'DATE':
            dates = dates.append(ent.text)
            
    date_string = " ".join(dates)
    prompt = (
        "Please accurately take the following document to create a legal chronology." 
        #"Please also use the dates here in this string: \n{date_string}\n" 
        "Present output in markdown with a header called chronology."
        "Format dates in UTC."
        "Please follow a format of 'DATE (MM/DD/YYYY): EVENT SUMMARIZATION'."
        "Seperate each event with a new line character."
        "Make sure the dates are in chronological order"
        "Take your time, and make sure to think through it as to minimize error.")
    
    response = client.chat.completions.create(model="ft:gpt-3.5-turbo-0125:personal::APDWVpcR",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": doc.text}
    ],)
    summary = response.choices[0].message.content
    doc._.summary = summary
    return doc
    return summary

nlp = spacy.blank("en")

if not spacy.tokens.Doc.has_extension("summary"):
    spacy.tokens.Doc.set_extension("summary", default=None)

nlp.add_pipe("openai_summarizer", last=True)
nlp.add_pipe('find_dates')

def summarize(text):
    """Summarizes the input text using the OpenAI GPT model."""
    doc = nlp(text)
    return doc._.summary
