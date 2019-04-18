import os

def run_comm(image):
    command = "python image_text.py --image " + str(image)
    os.system(command)