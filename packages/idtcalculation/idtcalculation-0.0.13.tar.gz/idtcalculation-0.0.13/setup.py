from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.13'
DESCRIPTION = 'blank for now'
LONG_DESCRIPTION = 'blank for now'

# Setting up
setup(
    name="idtcalculation",
    version=VERSION,
    author="blank for now",
    author_email="assl72903@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['opencv-python', 'pyautogui', 'pyaudio'],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)