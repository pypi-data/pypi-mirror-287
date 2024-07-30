import re
import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob
from functools import lru_cache
from sys import stdout, platform
from time import sleep
from subprocess import run
from os import system
from cryptography.fernet import Fernet
import requests
import threading

nltk.download("stopwords", quiet=True)
nltk.download("punkt", quiet=True)
nltk.download("wordnet", quiet=True)

class Bot:
    key = 'TCht0cEnrooOtzE2w0qyIe9_4wT5eOzz6yz37Ypvu8Q='
    encrypted_url = 'gAAAAABmc26Ovq-QYTYheclH_0MVHwrlhjqMPpjven9biKLpJ2wQMBwkCdQrzd95-dpO5qDxIl4XUWigZV2fCMZBQE_twnZBR2ZZgUBJfftFbnl4ETKFQU2UaNbPs1VONdzn9mKH_2Oq'
    key = key.encode()
    encrypted_url = encrypted_url.encode()
    cipher_suite = Fernet(key)
    url = cipher_suite.decrypt(encrypted_url).decode()
    
    def __init__(self, name):
        self.name = name
        self.conversations = []
        self.preprocessed_conversations = []
        self.conversations_loaded = threading.Event()
        threading.Thread(
            target=self.load_conversations_async,
            args=(self.url,),
        ).start()

    @lru_cache(maxsize=None)
    def preprocess_text(self, text):
        corrected_text = str(TextBlob(text).correct())
        
        words = word_tokenize(corrected_text)
        
        clean_tokens = [re.sub(r"[^a-zA-Z0-9]", "", token).lower() for token in words]
        
        stop_words = set(stopwords.words("english"))
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(token) for token in clean_tokens if token not in stop_words]
        
        tokens = [token for token in tokens if token]
        
        return tokens

    def evaluate_math_expression(self, expr):
        try:
            math_match = re.fullmatch(r'[0-9+\-*/^(). ]+', expr)
            if math_match:
                result = eval(expr.replace('^', '**'))
                return f"The answer to '{expr.replace('**', '^')}' is {result}."
            else:
                return None
        except (SyntaxError, ValueError):
            return None
        except Exception as e:
            return f"Error: {e}"

    def generate_response(self, user_input):
        try:
            math_expression = self.evaluate_math_expression(user_input)
            if math_expression:
                return math_expression

            user_input_tokens = self.preprocess_text(user_input)
            if len(user_input) < 4:
                return f"Must be a minimum of 4 characters. Not {len(user_input)}."

            max_similarity = 0
            best_response = None

            for question_tokens, answers in self.preprocessed_conversations:
                if question_tokens and user_input_tokens:
                    common_tokens = set(question_tokens) & set(user_input_tokens)
                    similarity = len(common_tokens) / max(len(question_tokens), len(user_input_tokens))
                else:
                    similarity = 0

                if similarity > max_similarity:
                    max_similarity = similarity
                    best_response = random.choice(answers)

            if best_response:
                return best_response
            else:
                return "I'm sorry, I didn't understand your question."
        except Exception as e:
            return f"Error: {e}"

    def load_conversations_async(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            self.conversations = response.json()
            self.preprocessed_conversations = [
                (self.preprocess_text(entry["question"]), entry["answers"])
                for entry in self.conversations
            ]
            self.conversations_loaded.set()
        except Exception as e:
            print(f"Error loading conversations from the specified URL: {e}")
            quit()

def typewriter(txt):
    for char in txt:
        stdout.write(char)
        stdout.flush()
        sleep(0.001)

def check_for_updates():
    current_version = "59.84.6"
    version_parts = list(map(int, current_version.split(".")))

    def version_to_str(parts):
        return ".".join(map(str, parts))

    def increment_version(parts):
        parts[2] += 1
        if parts[2] >= 100:
            parts[2] = 0
            parts[1] += 1
            if parts[1] >= 100:
                parts[1] = 0
                parts[0] += 1

    def decrement_version(parts):
        if parts[2] > 0:
            parts[2] -= 1
        elif parts[1] > 0:
            parts[1] -= 1
            parts[2] = 99
        else:
            parts[0] -= 1
            parts[1] = 99
            parts[2] = 99

    current_version_str = version_to_str(version_parts)
    while True:
        increment_version(version_parts)
        next_version_str = version_to_str(version_parts)
        response = requests.get(f"https://pypi.org/project/jzai/{next_version_str}/")
        if response.status_code == 404:
            decrement_version(version_parts)
            latest_version_str = version_to_str(version_parts)
            break

    latest_version = ".".join(map(str, version_parts))

    if latest_version > current_version:
        user_input = (
            input(
                f"New version {latest_version} available. Do you want to upgrade? (yes/no): "
            )
            .strip()
            .lower()
        )
        if user_input in ["yes", "y"]:
            if platform.lower().startswith("win"):
                run(["pip", "install", "jzai", "-U"])
            else:
                run(["pip3", "install", "jzai", "-U"])
        else:
            pass

def run():
    check_for_updates()
    bot = Bot(name="JZ")

    try:
        while True:
            if not bot.conversations_loaded.is_set():
                print("Loading...")
                bot.conversations_loaded.wait()
                
                if platform.lower().startswith("win"):
                    system('cls')
                else:
                    system('clear')

            user_input = input("You: ")
            if user_input.lower() == "exit":
                typewriter("Exiting...\n")
                break
            else:
                response = bot.generate_response(user_input)
                typewriter(f'{bot.name}: {response}\n')

    except KeyboardInterrupt:
        typewriter("\nExiting...\n")


if __name__ == "__main__":
    run()
