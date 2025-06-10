# Import the 'pyshorteners' library which provides URL shortening services
import pyshorteners 

# Prompt the user to enter a URL and store it in the variable 'url'
url = input("Enter URL :-")  

# Create a Shortener object, use the TinyURL service to shorten the URL,
# and print the shortened version to the screen
print("URL after shortening :-", pyshorteners.Shortener().tinyurl.short(url))
