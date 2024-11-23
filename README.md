# Chronology Creation, LegalDuel
## Fall 2024, AI Studio Project, legalduel-1b-ai-studio
<ins> Table of Contents </ins>
- [Business Focus](#business-focus)
- [Data Preparation and Validation](#data-preparation-and-validation)
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
The first step in this process was converting the documents from .docx to plain text format. Afterwards, we experimented with date and event extraction using libraries such as SpaCy, Stanford Core NLP, and Duckling. However, after going through this process we realized that integrating ChatGPT with Spacy would be eaiser since it already has cleaning and preprocessing built into its own model

### Example of Spacy Date Extraction Code:
<br>
<img src="images/Spacy Date Entity Identification Code.png" alt="Alt Text" width="500">

# Usage
For this project, we developed an AI driven web application to create legal chronologies from a set of given text documents provided by the LegalDuel platform. However, you can upload a pdf file from your personal device or type in the text you want to convert it into a chronology. After you insert the desired text, the web application will generate physical text description of your chronology and you can also download a visual timeline of the chronology. 

