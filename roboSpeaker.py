# import os

# # main program is starting from here
# if __name__== '__main__':
#     print("Welcome to RoboSpeaker 1.1 Created by Arundhati")
#     x=input("Enter what do you want me to speak: ")
#     command=f"engine.say {x}"
#     os.system(command)

import pyttsx3

# main program is starting from here
if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.0 Created by Arundhati")
    print("For the termination of program please enter end (in any case)")
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    while True:
        x = input("Enter what do you want me to speak: ")
        # Speak the provided text
        engine.say(x)

        # Wait for the speech to finish
        engine.runAndWait()

        if x.lower()=="end":
            engine.say("Program execution completed.")
            engine.runAndWait()
            break


    
