# Import the regular expression module to handle pattern matching

import re
responses = {
    "hello" : "Hi there ! How can i assist you today!!!",
    "bye" : "Goodbye! Have a great day!.",
    "default": "Sorry! I didn't get you"
}
# Function to find the appr. response based on the user's input
def chatbot_response(user_input):
    user_input  = user_input.lower()

    for keyword in responses:
        if keyword == "default":
            continue
        if re.search(keyword,user_input):
            return responses[keyword]
        
    return responses["default"]




#Main function 

def chatbot():
    print("Chatbot: Hello I'm here to assist you. (Type 'bye to exit)")

    while True:

        user_input = input("You:")

        if user_input.lower() == "bye":
            print(responses["bye"])
            break
        else:
            response = chatbot_response(user_input)
            print(response)

chatbot()
