# Chronology Creation, LegalDuel
## Fall 2024, AI Studio Project, legalduel-1b-ai-studio
<ins> Table of Contents </ins>
- [Business Focus](#business-focus)
- [Data Preparation and Validation](#data-preparation-and-validation)
- [Approach](#approach)
- [Usage](#usage)

# Business Focus
The goal of the project was to develop AI-driven solutions for common legal tasks, including content generation. For this project, we developed an AI driven web application to create legal chronologies from a set of given text documents provided by the LegalDuel platform. Chronologies are documents that outline a timeline of events, regarding a legal case. They are typically compiled by an attorney sifting through vast amounts of interviews, emails, and other documents to build a timeline. The purpose of creating this AI web application was to make it eaiser for lawyers to spend less time tediously creating chronologies, so instead they can focus on other pressing issues. Additionally, this project is useful for customers at law firms because with more time, competition, and innovation from our AI tool, law firms can help clients more efficiently for less money. Lastly, our project will our allow for more competition and innovatative solutions since new and unique solutions arise from increased competition, since AI tools are being constantly added into the legal sector. 

### Example of a legal Chronology:
<br>
<img src="images/example_of_a_legal_chronology.png" alt="Alt Text" width="1400">

# Data Preparation and Validation
## Dataset Overview
We were given given 30 samples of mock interviews, emails, and other documents. They are not real case scenarios. All of the data was on .docx format and there was a total of 701 KB of data.

### A Sample Data set:
<br>
<img src="images/sample data set.png" alt="Alt Text" width="1400">

## Exploratory Data Analysis
We read the sample documents provided to us, made the chronologies by hand, and compared our results against popular online AI tools (Chat GPT, Claude). The AI tools performed fairly well against our handmade chronologies since our chronologies and the AI ones generated errors at a similar rate.

### Example Chronology generated from ChatGPT:
<br>
<img src="images/chatgpt_chronology.png" alt="Alt Text" width="1000">

## Data Cleaning and Preprocessing
The first step in this process was converting the documents from .docx to plain text format. Afterwards, we experimented with date and event extraction using libraries such as SpaCy, Stanford Core NLP, and Duckling. However, after going through this process we realized that integrating ChatGPT with Spacy would be eaiser since SpaCy already has cleaning and preprocessing built into its own model, and ChatGPT allowed for chat completetions response generation. 

### Example of Spacy Entity Identification Code:
<br>
<img src="images/Spacy Date Entity Identification Code.png" alt="Alt Text" width="500">

### Example of Spacy Date Extraction Code:
<br>
<img src="images/Spacy Date Extraction.png" alt="Alt Text" width="500">

### Example of Spacy and ChatGPT code and response:
<br>
<img src="images/Spacy and Chatgpt.png" alt="Alt Text" width="1400">

# Approach
We decided to train our model with the OpenAI Dashboard. We created 10 training examples in training1.jsonl using the OpenAI Chat Completions API endpoint input prompt. The purpose of a chat completeions input prompt is to generate an output of a chronology, in text, based on specific parameters. Here is an example of a chat completions input prompt we used:

{"messages": 
<br>
[{"role": "system", "content": "Please take the following document and create a chronology. Follow a format of 'DATE (Month Day, Year): EVENT SUMMARIZATION'. Seperate each event with a new line character. Make sure the dates are in chronological order. Take your time, and make sure to think through it as to minimize error."},
<br>
{"role": "user", "content":"John: I believe that I saw his car out last Tuesday, sorry it was on Wednesday actually. "},
<br>
{"role": "assistant", "content":"October 30, 2024: John saw the car."}]}

As seen above, the "messages" section is where you can customize the model to behave. Within each message there is a set of roles and content associated with each role. In our above examples, we specified each role with either "system, "user," or "assistant." The "system" role allows you to specify the behavior of the model that you are using. 

## Selected Models
- gpt-3.5-turbo-0125: We selected this model because it had a low cost in training.
- gpt-4o-2024-08-06: We selected this model because of its increased accuracy of generating the best responses, despite the cost of training being high. 
  
We utilized two approaches to generate the chronologies: Prompt engineering and model finetuning. 

## Prompt Engineering
To generate the best responses

## Model Finetuning

# Usage
For this project, we developed an AI driven web application to create legal chronologies from a set of given text documents provided by the LegalDuel platform. However, you can upload a pdf file from your personal device or type in the text you want to convert it into a chronology. After you insert the desired text, the web application will generate physical text description of your chronology and you can also download a visual timeline of the chronology. 

