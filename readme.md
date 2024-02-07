# ⏲️ Desktop Activity Tracker

A CLI app to track your time while using your desktop.

## Motivation

If you've ever had to use desktop time tracking apps like the Upwork Desktop Application for your work projects, you might have wished for something similar for your personal projects too.

Using this app, you can easily track how much time you spend on different projects, how focused you are, and how many times you sneak off to the kitchen for a snack! 😄

This tracker can make you feel like you've got someone keeping an eye on you, it helps you steer clear of distractions and stay laser-focused on your personal projects, just like you do with your work stuff!

## Installation

Clone the repo or use the "Download ZIP" and extract manually:

    git clone https://github.com/ptvty/desktop-activity-tracker.git

`cd` to the project's directory and install requirements:

    pip install -r requirements.txt

## Usage

### Start tracking

Start tracking by running the `start` script:

    python start.py

Optionally you can pass your project name to have it appended to the screenshot's file name:

    python start.py AWESOME-PROJECT

You should get something like:

    PS C:\desktop-activity-tracker> python start.py AWESOME-PROJECT
    ✅ Tracking started for "AWESOME-PROJECT" project
    📸 Taking screenshots every 10 minutes - at randomized moments
    📂 Saving in "Screenshots" directory

### Stop tracking

Just hit `Ctrl`+`C` to exit the script when you want to stop tracking.

### Review records

You can list the files in the "Screenshots" directory, you have the date and time, the project's name, the level of activiy (from 0 to 10) and the active window's title:

    2024-02-06 23-30 6 DEFAULT init__.py-DAT-Visual-Studio-Code.png
    2024-02-06 23-40 5 DEFAULT Microsoft-Learn-.-Mozilla-Firefox.png
    2024-02-06 23-40 7 DEFAULT init__.py-DAT-Visual-Studio-Code.png
    2024-02-06 23-50 9 DEFAULT shutter.py-DAT-Visual-Studio-Code.png
    2024-02-07 00-00 7 DEFAULT start.py-DAT-Visual-Studio-Code.png