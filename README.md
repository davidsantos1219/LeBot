LeBot
Automated Chatbot that talks to other individuals through different personalities.

Features
Automatically logs into a given site given a user's login cookies stored in a JSON file
Detects chats where the other match sent the last message
Reads the previous message as context into a ChatGPT prompt given a system prompt saved in "input.txt" and generates a reply
Saves responses into a file labeled "output.txt" instead of submitting the message
Requirements
Python 3.7+
Google Chrome & Chromedriver
Python Libraries: openai, selenium
Site Login Cookies named "site_cookies.json"
Text file "input.txt" with personality settings (sample provided)
Your Own OpenAI API Key
