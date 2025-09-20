# Vector DataBase

## Overview

This is a side project for running a vector database

The backend uses Python and Fast API, while the frontend uses ReactTS built on Vito, so the project requires the aformentioned technologies to run

for the sake of time, the database runs in-memory, and uses brute force search methods, and is only suitable for small-medium sized projects

The project was run and developed in WSL2 on the Ubuntu distro

## Running the Project

#### Install Dependencies
make install-deps

this should install the dependencies for both the frontend and backend

#### Run Backend
make run-backend

the default port should be http://localhost:8000

the backend should start with blog.json values, but more can be inserted

#### Run Frontend (seperate terminal from)
make run-frontend

the default port should be http://localhost:5173

#### Interacting with the frontend

In order to insert a new entry, simply type the desired text in the top textbox then hit the insert button. It should return "Insert successful!" on success

In order to search for the top k most similar entries, type in the text you want to compare in the leftmost text box, the number of top comparisons in the middle, and then set the comparison type on the right most box. Afterwards, hit the search button