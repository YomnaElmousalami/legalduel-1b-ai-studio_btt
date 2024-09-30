import spacy
import os
from spacy.language import Language
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_KEY"))

@Language.component("openai_summarizer")
def summarize_text(doc):
    """Custom component that summarizes the text using OpenAI's GPT model."""
    prompt = ("You are a helpful assistant that transforms text into a legal chronology."
        "Extract dates from events and summarize the event. Follow a format of 'DATE (MM/DD/YYYY): EVENT SUMMARIZATION'."
        "Bold dates and seperate each event with a new line")
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": doc.text}
    ],
    max_tokens=100)
    summary = response.choices[0].message.content
    doc._.summary = summary
    return doc

nlp = spacy.blank("en")

# Register the custom extension attribute 'summary' for SpaCy Doc
if not spacy.tokens.Doc.has_extension("summary"):
    spacy.tokens.Doc.set_extension("summary", default=None)

# Add the custom component to the pipeline
nlp.add_pipe("openai_summarizer", last=True)

def summarize(text):
    """Summarizes the input text using the OpenAI GPT model."""
    doc = nlp(text)
    return doc._.summary