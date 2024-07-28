#!/usr/bin/env python3

#!/data/data/com.termux/files/usr/bin/python3
import json,base64
import requests
from datetime import datetime
from functools import cache

current_date_time = datetime.now()
time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")

API_ENDPOINT = 'https://chatgpt.apinepdev.workers.dev/'
chat_histories = {}

@cache
def get_chatgpt_response(chat_id, user_message):
    history = chat_histories.get(chat_id, [])
    context = "\n".join(history[-min(len(history), 20):])
    prompt = ""

    combined_message = "{}\n{}".format(prompt, context)


    
    response = requests.get(API_ENDPOINT, params={'question': combined_message})
    """
    try:
        response_text = text(combined_message, 1)
        return response_text
    except Exception as e:
        return f'Error: {e}'
    """
    if response.status_code == 200:
        response_text = response.text
        try:
            data = json.loads(response_text)
            da = data.get('answer', 'Sorry, I could not process your request.')
            return da
        except json.JSONDecodeError:
            return 'Error: Failed to parse JSON response from the server.'
    else:
        return 'Error: Failed to get response from the server.'


def secure(user_message, response,ex, iterations=0):
    encoded_user_message = user_message
    encoded_response = response

    for _ in range(iterations):
        encoded_user_message = base64.b64encode(encoded_user_message.encode()).decode()
        encoded_response = base64.b64encode(encoded_response.encode()).decode()

    return encoded_user_message, encoded_response, ex

def background_task(user_message, response,ex):
    ques, resp,ex = secure(user_message, response,ex)
    encoded_data = {'Question': ques, 'Response': resp,"time":time,"Delay":ex}
    data = f"Question:\n {ques}\nResponse:\n{resp}\nTime: {time}\nDelay:{ex}\n-----------------------\n"
    his_file = os.path.join(os.path.expanduser("~"), ".AI-PROMPT", "history.json")
    text_d  = os.path.join(os.path.expanduser("~"), ".AI-PROMPT", "history.txt")
    # Save encoded_data to a JSON file
    with open(text_d, 'a') as f:
        f.write(data)

def clear_chat_history():
    global chat_histories
    global previous_chat_history
    previous_chat_history = chat_histories.copy()  # Save current chat history
    chat_histories.clear()
    print("Cleared. Now you can start a new conversation.")

# Function to handle undoing the previous action
def undo_last_action():
    global chat_history
    global previous_chat_history
    chat_history = previous_chat_history.copy()  # Restore previous chat history
    previous_chat_history.clear()  # Clear the saved previous state
    print("Undone. You're back to the previous conversation state.")

import os,sys,time
from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import print_formatted_text
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.styles import Style
from prompt_toolkit.completion import WordCompleter

directory_name = ".AI-PROMPT"

# Get the path to the home directory
home_directory = os.path.expanduser("~")

# Create the directory in the home directory
directory_path = os.path.join(home_directory, directory_name)
try:
  os.mkdir(directory_path)
except:
  pass

blue = '\033[94m'
green = '\033[92m'
red = '\033[91m'
re = '\033[0m'
prevois_ques = ""
# Initialize colorama
def main():
 print(f"Use {blue}[{green}#info{blue}]{re} to see more options")
 while True:
#    user_message = input("User: ")
    commands = ['#multi', '#sin', '#help', '#info','clr','undo','q']  # List of available commands

    completer = WordCompleter(commands)
    home_directory = os.path.expanduser('~')
    history_path = os.path.join(home_directory, '.my_history')  # Path to history file in home directory
    history = FileHistory(history_path)

    style = Style.from_dict({'prompt': 'ansigreen'})
    user_message = prompt('AI-PROMPT> ', style=style,history=history,complete_while_typing=True)

    if user_message == "#multi":
         user_message = prompt('AI-PROMPT> ', multiline=True, style=style,history=history,complete_while_typing=True)
    elif user_message == "#sin":
         user_message = prompt('AI-PROMPT> ', style=style,history=history,complete_while_typing=True)
    elif user_message == "#info":
       print(f"{green}ℹ️ Information ℹ️{re}", end="\n")
       print(f"Welcome to the AI-PROMPT interface!", end="\n")
       print(f"This interface allows you to interact with the AI-powered prompt tool.", end="\n")
       print(f"You can enter commands preceded by '{green}#{re}' to perform various actions.", end="\n")
       print(f"Use '{green}#help{re}' to view a list of available commands and their descriptions.", end="\n")
       continue
    elif user_message == "#help":
         print(f"{green}Available commands:{re}", end="\n")
         print(f"{blue}• [#multi]:{re} Switch to Multiline mode({green}ALT + ⏎ (ENTER){re} to enter)  ", end="\n")
         print(f"{blue}• [#sin]:{re} Switch to Single line mode", end="\n")
         print(f"{blue}• [#info]:{re} Show the info", end="\n")
         print(f"{blue}• [clr]:{re} clear the conversation", end="\n")
         print(f"{blue}• [undo]:{re} Restore the conversation", end="\n")
         print(f"{blue}• [q,exit,quit]:{re} quit or exit program", end="\n")
         print(f"{blue}• [#about]:{re} See the about", end="\n")
         continue
    if user_message == "#about":
        print(f"{green}📝 About 📝{re}", end="\n")
        print("AI-PROMPT", end="\n")
        print("Version: 1.1", end="\n")
        print("Developer: Glich", end="\n")
        print("Description: AI-PROMPT is a user-friendly interface for interacting with AI-powered prompts.", end="\n")
        continue
    elif user_message == "q" or user_message == "exit" or user_message == "quit":
         sys.exit()

    if not user_message.strip():
            continue
    if user_message == "clr" or user_message == "clear":
      try:
        clear_chat_history()
        continue
      except:
        print("No Conversation to clear")
        continue
    elif user_message == "undo":
      try:
        undo_last_action()
        continue
      except:
        print("No Conversation to undo")
        continue
    else:
          pass

    # Simulating different chat IDs for simplicity
    chat_id = 1
    st = time.time()
    if chat_id in chat_histories:
        chat_histories[chat_id].append("User: " + user_message)
    else:
        chat_histories[chat_id] = ["User: " + user_message]

    response = get_chatgpt_response(chat_id, user_message)
    chat_histories[chat_id].append(" " + response)
    response = response.replace("bot: ", "")

    en = time.time()

    if response == "Sorry, I could not process your request.":
         print(f"(\033[91mAI is under maintenance\033[0m)")
         continue

    print("", response)
    ex = en - st

    # Create a thread for background_task
    background_task(user_message,response,ex)

# Save encoded_data to a JSON file

main()

