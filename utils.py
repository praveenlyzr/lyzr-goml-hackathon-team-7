import os

def temp_directory():
    if not os.path.exists('tempDir'):
        os.makedirs('tempDir')