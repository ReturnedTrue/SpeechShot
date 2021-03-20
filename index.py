from PIL.ImageGrab import grab
from tkinter.filedialog import asksaveasfilename
import speech_recognition as speech

typesallowed = [("PNG Image", "*.png"), ("JPEG Image", "*.jpeg"), ("GIF Image", "*.gif")]
words = [
    "screenshot", 
    "take picture", 
    "take screenshot", 
    "picture", 
    "print screen"
]

while True:
    recogniser = speech.Recognizer()

    with speech.Microphone() as src:
        print("Please input:")
        audio = recogniser.listen(src)

    try:
        said = recogniser.recognize_google(audio)
        if (said in words):
            print("Screenshotting...")

            content = grab()
            filename = asksaveasfilename(filetypes = typesallowed, defaultextension=typesallowed, initialdir="Downloads", title="Save screenshot")

            if (filename):
                try:
                    content.save(filename)
                    print("Saved as: {0}".format(filename))
                except ValueError:
                    print("Unable to save with that file extension.")

            else:
                print("Chosen not to save file.")

        elif (said == "exit"):
            print("Exiting...")
            break

        else:
            print("You said '{0}' which I don't understand".format(said))

    except speech.UnknownValueError:
        print("Couldn't understand what you said.")
    except speech.RequestError as e:
        print("Couldn't request results from Google Speech Recognition service; {0}".format(e))
