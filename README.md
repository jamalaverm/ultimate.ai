# Ultimate

# Data Engineer Coding Challenge

Julian Malaver - jamalaverm@hotmail.com

## Solution

Anaconda environment:

- python: 3.9.18
- beautifulsoup4: 4.12.2
- apache-beam: 2.51.0

Docker:

- mongodb: 7.0.2 (latest)

## Characteristics:

I utilized pycharm as my IDE tool, and anaconda as the python environment manager.

I used the provided code for generating stream messages.

Apache beam was the selected stream processing framework.

The data is obtained every 20 seconds from the socket and the number of covid cases are gotten at the same rate.

## How to use it:

- Clone copy code from https://github.com/jamalaverm/ultimate.ai.
- Set the mongodb docker container, map container port 27017 to local port 27017.
- Create a database called **ultimate** and a collection **coronavirus** inside mongodb, or modify the configuration file **configuration.py** to set your own values.
- Prepare Anaconda Environment with the corresponding libraries.
- Execute **generator/twitter_stream_simulator.py** to start generating messages.
- Execute **main.py** to start processing data and inserting documents into mongoDB.
