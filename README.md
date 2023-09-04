# Computer Vision RPS

## Table of Content
    1. Introduction
    2. Computer Vision System

### Introduction
This project implements Rock-Paper-Scissors which is a game in which each player simultaneously shows one of three hand signals representing rock, paper, or scissors. Rock beats scissors. Scissors beats paper. Paper beats rock.

The player who shows the first option that beats the other player's option wins.

This is an implementation of an interactive Rock-Paper-Scissors game, in which the user can play with the computer using the camera.

### Computer Vision System
In order to create a computer vision system also called Image project model, I used Teachable-Machine. This model will detect whether a user is showing Rock, Paper or Scissors to the camera.
I created 4 different classes for the model: Rock, Paper, Scissors, Nothing. Each class is trained with images of showing the hand signs for each option to the camera. The "Nothing" class represents empty image. I added more than 1 image as the more we train the model, the more accurate the model will be.