# Chronology Creation, LegalDuel
## Fall 2024, AI Studio Project, legalduel-1b-ai-studio
<ins> Table of Contents </ins>
- [Business Focus](#business-focus)
- [Data Preparation and Validation](#data-preparation-and-validation)
- [Approach](#approach)
- [Key Findings and Insights](#key-findings-and-insights)
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
The first step in this process was converting the documents from .docx to plain text format. Afterwards, we experimented with date and event extraction using libraries such as SpaCy, Stanford Core NLP, and Duckling. However, after going through this process we realized that integrating a ChatGPT model with Spacy would be eaiser since SpaCy already has cleaning and natural language preprocessing built in, and ChatGPT models allows for a chat completetions response generation. 

### Example of Spacy Entity Identification Code:
<br>
<img src="images/Spacy Date Entity Identification Code.png" alt="Alt Text" width="500">

### Example of Spacy Date Extraction Code:
<br>
<img src="images/Spacy Date Extraction.png" alt="Alt Text" width="500">

### Example of Spacy and ChatGPT code and response in text:
<br>
<img src="images/Spacy and Chatgpt.png" alt="Alt Text" width="1400">

# Approach
## Selected Models
We selected two candidate models to explore which one produced the best chronologies. 
- gpt-3.5-turbo-0125: We selected this model because it had a low cost in training.
- gpt-4o-2024-08-06: We selected this model because of its increased accuracy of generating the best responses, despite the cost of training being high.
  
## Prompt Engineering
To generate the best chronology with our two selected models, we decided to use prompt engineering, which is a set of instructions used to generate the best output for our model. To generate the best prompt we decideded to use specific keywords to define our ideal output. For example we stated how we wanted our model to follow the format of 'DATE (MM/DD/YYY): EVENT SUMMARIZATION' as well as 'UTC' format. This gave it a frame of reference on how we wanted our output to be produced instead of saying create a chronology. After specifying our prompt, we decided to use the OpenAI Chat Completions API endpoint to generate the chronologies. The purpose of a chat completions endpoint is to simulate the interaction of a user and the chatbot creating text generated output, based on the user input. 

**Example of prompt engineering and Chat Completions endpoint:**
<br>
<br>
<img src="images/prompt engineering and chat completions.png" alt="Alt Text" width="1000">
<br>

As seen in the image, the prompt was created using prompt engineering. Meanwhile the chat completions api starts from the line that states "response" and ends with "summary=...." The chat completions api contains a messages section which specifies the role and the content associated with each role. The first role that is specified is "system" which allows you to specify the behavior of the model that you are using. The second role that is specified is the "user" role which acts as a user who is typing an input into the chatbot. In the code above, the content of the role "system" is given the prompt we created with prompt engineering and the content of the role user is give the document text that the user enters when using the web application. Afterwards, the line "summary = response.choices[0].message.content" is the output of the model, otherwise known as the chronology. 

## Model Trianing
We decided to train our model with the OpenAI Dashboard. We created 10 training examples in training1.jsonl using the OpenAI Chat Completions API endpoint input prompt. The purpose of a chat completeions input prompt is to generate an output of a chronology, in text, based on specific parameters. Here is an example of a chat completions input prompt:

{"messages": 
<br>
[{"role": "system", "content": "Please take the following document and create a chronology. Follow a format of 'DATE (Month Day, Year): EVENT SUMMARIZATION'. Seperate each event with a new line character. Make sure the dates are in chronological order. Take your time, and make sure to think through it as to minimize error."},
<br>
{"role": "user", "content":"John: I believe that I saw his car out last Tuesday, sorry it was on Wednesday actually. "},
<br>
{"role": "assistant", "content":"October 30, 2024: John saw the car."}]}

**Explanation of Chat Completions Input:**
As seen above, the "messages" section is where you can customize your desired model. Within each message there is a set of roles and content associated with each role. In our above examples, we specified each role with either "system, "user," or "assistant." The "system" role allows you to specify the behavior of the model that you are using. The role of "user" acts as a user who is typing an input into the chatbot. And, the role of "assistant" is the desired response that the model should produce. The "content" is the query or response associated with each role. In the above example, the "system" role is acting as an assistant that generates a chronology with specific instructions, although the word "assistant" is not specified. Meanwhile, the "user" role contains an input response (content) that a user puts into the chatbot. And finally, the content associated with the "assistant" role contains a sample output response that it should provide. 

**Model Hyperparameters to train with:**
We decided to train the models based on the hyperparameters of the number of epochs, batch size, and LR multiplier. 

## Key Findings and Insights

## Key Findings
gpt-3.5-turbo-0125: We utilized the default training hyperparameter values: 3 epochs, 1 batch size, and an LR multiplier of 2. The purpose of doing this was to see how the default values would measure, compared to adjusted hyperparameter values. Although the training cost was low, it did produce a significantly high training loss of 0.8. This suggests that the model is most likely underfitting. 

gpt-4o-2024-08-06: Because the default hyperparameter values did not produce the best results, we decided to try different hyperparameters for this model: 10 epochs, 1 batch size, and an LR multiplier of 2. As a result, the training loss was significantly lower: 0.0027. Although a low training loss is usually good, this training loss is significantly low. This suggests that the model is most likely severly overfitting. 

**gpt-3.5-turbo-0125 training hyperparameters and results:**
<br>
<br>
<img src="images/gpt-3.5 hyperparameters.png" alt="Alt Text" width="500">
<img src="images/gpt-3.5 training loss.png" alt="Alt Text" width="1000">

**gpt-4o-2024-08-06:**
<br>
<br>
<img src="images/gpt 4 hyperparameters.png" alt="Alt Text" width="500">
  
# Usage

