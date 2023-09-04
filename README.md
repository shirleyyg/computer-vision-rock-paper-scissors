# Computer Vision RPS

## Table of Content
    1. Introduction
    2. Computer Vision System

### Introduction
This project implements Rock-Paper-Scissors which is a game in which each player simultaneously shows one of three hand signals representing rock, paper, or scissors. Rock beats scissors. Scissors beats paper. Paper beats rock.

The player who shows the first option that beats the other player's option wins.

This is an implementation of an interactive Rock-Paper-Scissors game, in which the user can play with the computer using the camera.

Firstly we create a Github Repo for the application. Then used git clone to create local repo.

### Computer Vision System
In order to create a computer vision system also called Image project model, I used Teachable-Machine. This model will detect whether a user is showing Rock, Paper or Scissors to the camera.
I created 4 different classes for the model: Rock, Paper, Scissors, Nothing. Each class is trained with images of showing the hand signs for each option to the camera. The "Nothing" class represents empty image. I added more than 1 image as the more we train the model, the more accurate the model will be.

Once the images have been added for all the classes, I clicked train model. After training the model, we want to download it to use it with Python application. I downloaded the model from "Tensorflow" tab which contains the structure and the parameters of the deep learning model. Then I added the model files in the Python repo folder. Then added to staging, committed the changes and pushed to Github repo.

### Setting up the environment
We need to install some dependencies in order to use the model. To do this I have created a virtual environment using conda, and installed all the required libraries for the model to work. In the environment, firstly I installed package manager called pip. Then used pip to install the package libraries: opencv-python, tensorflow, and ipykernel. 