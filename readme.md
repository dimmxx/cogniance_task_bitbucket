Cogniace task for QA intern position
------------------------------------


TASK 3. SQL SKILLS
------------------
The SQL project consists of 2 files: 
1. sql_script (SQL scripts, MS SQL Server is used)
2. readme.md (this file)


TASK 4. AUTOMATION TESTS
------------------------
Endpoints that are tested: 

1. /np/workouts-partner/v1.0/exercisers/{exerciserUuid}/workouts
2. /np/workouts-partner/v1.0/workouts/{workoutId}

To run the tests:
1. open bash
2. change dir to folder with py files
3. run the command: $ python3 -m unittest TestWorkoutApi.py

The test project contains 4 files: 
1. WorkoutApi.py (the file contains methods which implement the current API)
2. TestWorkoutApi.py (the file contains API test methods)
3. Explain.txt 
4. readme.md (this file)

*all the automated tests are described in Task 2 (https://docs.google.com/spreadsheets/d/1yWqw2L-0FPWitJUqmJcULFC3qwqaAN3uyz7qIbEUIMQ/edit?usp=sharing)


TASK 5. Datamining
------------------
To run the datamining script: - open bash - change dir where the files are located - run the command $ ./dm_script (the file datamining.log must be located in the same dir)

The datamining project contains 4 files:
1. dm_script (bash script)
2. datamining.log (log file)
3. result.txt (output file)
4. readme.md (this file)
