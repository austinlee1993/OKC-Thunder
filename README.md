
# OKC Technical Assessment Deliverable

### 1. Backend Engineering

* Architect and implement a normalized PostgreSQL database to store the data provided in `backend/raw_data/play_by_play.csv`. All information in the original data should be accessible via the database, such that a query could reproduce the attached dataset in its full form. In addition to the data that exists in the .csv, you will need to create and store a `gameid` attribute. Each distinct combination of gametimestamp, homenbateamid, and awaynbateamid should share a unique gameid.

* Write a brief description of your database architecture (<250 words). Feel free to provide a visual representation as an aide. Submit relevant responses in the `written_responses` folder provided.

* In the programming language of your choice, write a process to load the dataset into your PostgreSQL database. Ensure that this process can run repeatedly without duplicating or obscuring references in the database. Include the source code of your process in the `backend/scripts` folder. 

* After loading the data, export the state of your database using `pg_dump -U okcapplicant okc > dbexport.pgsql`. Include `dbexport.psql` in the `backend/scripts` folder.

* The skeleton of an API View `PlayerShotStats` can be found in `backend/app/views/stats.py`. Implement this API to aggregate data relative to shots taken in the dataset. The API should take `playerID`, `teamID`, `gameID`, and `gameDate` as optional query parameters to filter the data, and return JSON that contains: 

    * The IDs of all players who took shots 
    * The percentage of all shots taken from 3PT range in the dataset 
    * The FG% on all 3PT attempts 
    * The FG% on all 2PT attempts 
    * The eFG across all results 

    Feel free to import additional modules/libraries in order to do this, but ensure that the `backend/requirements.txt` is updated accordingly.

    Viewing http://localhost:4200/player-shot-stats allows you to see the output of your API, given the optional parameters provided in the user inputs.

### 2. Frontend Engineering

* The `player-stats` component, which is viewable at http://localhost:4200/player-stats, makes a call to an API endpoint at `/api/v1/playerStats` that returns game level box score statistics for 16 players. For this exercise, you can assume that: 

   * All 16 players are on the same team 
   * No players on the team are excluded from the dataset 

* Within the `player-stats` component found in `frontend/src/app/player-stats/`, create an interface that allows a user to see game and season level statistics for players and teams. The interface must display the following statistics at a minimum: 

   * Free Throw Attempts per game 
   * 3PT FG% 
   * eFG%
   * Assists Per Game 
   * Total Blocks 

* Feel free to import additional modules of your choice, and design the interface however you wish. Just make sure that the `package.json` and `package-lock.json` are updated accordingly.

<br></br>


# Application Setup
Please follow the instructions below, from top to bottom sequentially, to ensure that you are set up to run the app. The app is run on an Angular frontend, Django backend, and a PostgreSQL database.

## Set up database
1. Download and install PostgreSQL from https://www.postgresql.org/download/
2. Ensure PostgreSQL is running, and in a terminal run
    ```
    createuser okcapplicant --createdb;
    createdb okc;
    ```
3. connect to the okc database to grant permissions `psql okc`
    ```
    create schema app;
    alter user okcapplicant with password 'thunder';
    grant all on schema app to okcapplicant;
    ```


## Backend
### 1. Install pyenv

Read about pyenv here https://github.com/pyenv/pyenv as well as info on how to install it.

### 2. Installing Prerequisites
```
cd root/of/project
pyenv install 3.6.6
pyenv virtualenv 3.6.6 okc
pyenv local okc
pip install -r backend/requirements.txt
```

### 3. Creating Initial Database Tables and Loading Data From data.json

Create tables with
```
cd /path/to/project/backend
python manage.py migrate
```

Then, load data with
```
python manage.py loaddata data.json --exclude auth.permission --exclude contenttypes
```

### 4. Starting the Backend
Start the backend by running the following commands
```
cd /path/to/project/backend
python manage.py runserver
```
The backend should run on http://127.0.0.1:8000/ (http://localhost:8000/)


## Frontend

### 1. Installing Prerequisites
Install Node.js (14.17.x), then run the following commands
```
cd /path/to/project/frontend
# Install dependencies
npm install
```

### 2. Starting the Frontend
Start the frontend by running the following commands
```
cd /path/to/project/frontend
npm start
```
The frontend should run on http://127.0.0.1:4200/ (http://localhost:4200/). Visit this address to see the app in your browser.


<br></br>
# Questions?

Email bpalipatana@okcthunder.com and tvandehouten@okcthunder.com.
