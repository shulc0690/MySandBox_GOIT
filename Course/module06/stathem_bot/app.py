import os
from openai import OpenAI

client = OpenAI(api_key=)

API_KEY_PATH = 'stathem_bot/secret_key.bin'

# 

def startup():
    if os.path.exists(API_KEY_PATH):
        with open(API_KEY_PATH, 'rb') as file:
            api_key = file.read().decode('utf-8')
            print(api_key)
    else:
        while True:
            user_input = input("Введіть API_KEY")
            if len(user_input) == 51 and user_input.startswith('sk-'):
                api_key = user_input
                with open(API_KEY_PATH, 'wb') as file:
                    file.write(user_input.encode("utf-8"))
                break
            else:
                print("Enter key blyat")
        

def main():
    user_input = input("Введіть запит: ")



response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)