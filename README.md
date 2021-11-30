# Description

This is a simple user data browser I've made for some job interview. 
Got permission to share.

# How to use

`cd` into project's directory, create virtual env (`virtualenv .venv && source .venv/bin/activate`) 
and install all dependencies with `pip -r requirements.txt`. 
Then do `./run.sh`. It should create and populate database with data from 
[remote api](https://jsonplaceholder.typicode.com), then launch test server. 
Open `127.0.0.1:8000` in your browser and you will get a table view containing 
following info about user's posts in database:

- Name of author
- Post title
- Post body
