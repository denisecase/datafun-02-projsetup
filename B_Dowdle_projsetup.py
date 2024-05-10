''' Project 2: This module provides functions for creating a series of project folders. '''

# 2. Import Dependencies (At the Top, After the Introduction)
import time
import pathlib
import Dowdle_utils

# 3. Define Functions for Folder Creation
## Function 1. For item in Range: Create a function to generate folders for a given range (e.g., years).
def create_folders_for_range(start, end):
    for i in range(start, end):
        pathlib.Path(f"{i}").mkdir(exist_ok=True)

## Function 2. For Item in List: Develop a function to create folders from a list of names.
def create_folders_from_list(folder_list):
    for folder in folder_list:
        pathlib.Path(folder).mkdir(exist_ok=True)        

## Function 3. List Comprehension: Create a function to create prefixed folders by transforming a list of names 
## and combining each with a prefix (e.g., "data-").
def create_prefixed_folders(folder_list, prefix):
    for folder in folder_list:
        pathlib.Path(f"{prefix}-{folder}").mkdir(exist_ok=True)

## Function 4. While Loop: Write a function to create folders periodically (e.g., one folder every 5 seconds).
def create_folders_periodically(duration,period):
    start_time = time.time()
    while(time.time()-start_time < duration): ## continue running while the time elapsed from start is less than the given duration
        current_time = time.time()-start_time
        pathlib.Path(f" {round(current_time)} seconds").mkdir(exist_ok=True)
        time.sleep(period) ## wait specified amount of seconds before beginning next iteration

# 4. Always Join Paths with Pathlib
## Create a path object
project_path = pathlib.Path.cwd()

## Define the new sub folder path
data_path = project_path.joinpath('data')

## Create new if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

# 5. Define Main Function
def main():
    ## print byline from imported module
    print(f"Byline: {Dowdle_utils}")

    ## call function 1 to create a folder for each number in a range
    create_folders_for_range(start=1995,end=2000)

    ## call function 2 to create a folder for each string in a list
    folder_names = ["Pigs", "Cows", "Goats"]
    create_folders_from_list(folder_names)

    ## call function 3 to create folders using comprehension
    create_prefixed_folders(folder_names,prefix="Adopted")

    ## call function 4 to create a folder every 5 seconds for the specified duration
    create_folders_periodically(duration=15,period=5)

# Conditional Script Execution (at the end of the file)
if __name__ == '__main__':
    main()