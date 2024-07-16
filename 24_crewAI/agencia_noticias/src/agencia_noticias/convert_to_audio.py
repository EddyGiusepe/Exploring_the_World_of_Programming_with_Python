#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""
# import os                                                                                                                                                                                                          
# from dotenv import load_dotenv
# from pathlib import Path
# load_dotenv(Path("agencia_noticias/.env"))

from pathlib import Path
# from openai import OpenAI
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
import openai
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
#openai.api_key  = os.environ['OPENAI_API_KEY']
Eddy_key_openai  = os.environ['OPENAI_API_KEY']

from openai import OpenAI
client = OpenAI(api_key=Eddy_key_openai)


MAX_CHARACTERS = 4096


with open('/home/eddygiusepe/1_Eddy_Giusepe/Exploring_the_World_of_Programming_with_Python/24_crewAI/agencia_noticias/src/agencia_noticias/report_ptbr.md', 'r', encoding='utf-8') as file:
    string = file.read()

# remove hashtags symbols
string = string.replace('#', '')
string = string.replace('*', '')

text = []
remaining_text = string
def splitter(string):
    last_period = string[:MAX_CHARACTERS].rfind('.')
    # find the last period before the limit
    last_period = string[:MAX_CHARACTERS].rfind('.')
    # split the file at the last period
    return string[:last_period+1], string[last_period+1:]

# calculate the size of the file in characters
file_size = len(string)

# if the file is too large, split it into smaller files. But the split should be done at the end of a sentence
while len(remaining_text) > 0:
        
        if len(remaining_text) < MAX_CHARACTERS:
            text.append(remaining_text)
            remaining_text = ''
        else:
                
            extracted, remaining_text = splitter(remaining_text)
            print(len(extracted), len(remaining_text))
            text.append(extracted)
            input("Press Enter to continue...")


print(text)

print('File size: ', file_size)


for i, t in enumerate(text):
    print(f"Text {i}: ", t)
    response = client.audio.speech.create(
        model="tts-1",
        voice="echo",
        input=t
    )
    speech_file_path = Path(__file__).parent / f"speech_{i}.mp3"
    print(f"Saving to {speech_file_path}")
    response.stream_to_file(speech_file_path)