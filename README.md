# Program Maker

Welcome to Program Maker, this is a Python program designed to help you create schedules for lessons and groups. This program reads input from a text file, processes the information, and generates all possible schedules that are not CLASHING based on the provided data.

## 🚀 Features

- Dynamic scheduling for lessons and groups.
- Support for multiple lessons and additional groups.
- Usage of this program can save a lot of time.
- Prevents clash in your time schedule.

## 🌟 Input File Format

The text file should start with the number of lessons (an integer). 
Following that, list the lesson names (strings).
For each lesson, specify how many times it occurs in a week and provide the corresponding schedule.
Repeat this process for all lessons.
If a lesson has multiple groups, indicate 'yes' and specify the schedule for each group; otherwise, mark 'no.' Continue this pattern for all other lessons.

Example Input/Output File:

- [Program.txt](program.txt)
- [Output.txt](output.txt)

## 🎩 Is it complex?

Don't worry; it's designed to simplify your scheduling woes. Let's unravel the magic behind the scenes and analyze what our program actually does with using our [Program.txt](program.txt) input. 🚀

## 🎯 How to Use

1. Run the program:
   ```bash
   python program_maker.py
   ```
   The output will be:
   ```
   Welcome to Program Maker
   Enter your txt file:
   ```
   - Enter your .txt file here. Now lets analyze the format of .txt file from the initial example [Program.txt](program.txt).
     
2. Understanding the input file format:
   ```
   3                      # Number of Lessons
   LESSON1                - Lesson Name
   LESSON2                - Lesson Name
   LESSON3                - lesson Name
   2                      # how many times 1. lesson occurs in a week and provide the corresponding schedule.
   Wednesday 10:30
   Friday 12:30
   1                      # how many times 2. lesson occurs in a week and provide the corresponding schedule.
   Thursday 14:30
   1                      # how many times 3. lesson occurs in a week and provide the corresponding schedule.
   Tuesday 8:30
   yes                    - Does 1. lesson has 2. group? if yes type 'yes' and provide the corresponding schedule.
   Monday 10:30
   Tuesday 12:30
   no                     - Does 1. lesson has 3. group? if no type 'no'
   yes                    - Does 2. lesson has 2. group? if yes type 'yes' and provide the corresponding schedule.
   Wednesday 8:30
   no                     - Does 2. lesson has 3. group? if no type 'no'
   no                     - Does 3. lesson has 2. group? if no type 'no'
   ```
   
3. Output:
   ``` 
   Your all possible programs: 
   Monday       Tuesday      Wednesday    Thursday     Friday      
   ----------------------------------------------------------------
                LESSON3                                            | 8:30-10:20
                             LESSON1                               | 10:30-12:20
                                                       LESSON1     | 12:30-14:20
                                          LESSON2                  | 14:30-16:20
                                                                   | 16:30-17:20
   Lesson LESSON1: Group 1, Lesson LESSON2: Group 1, Lesson LESSON3: Group 1
   
   Monday       Tuesday      Wednesday    Thursday     Friday      
   ----------------------------------------------------------------
                LESSON3                                            | 8:30-10:20
   LESSON1                                                         | 10:30-12:20
                LESSON1                                            | 12:30-14:20
                                          LESSON2                  | 14:30-16:20
                                                                   | 16:30-17:20
   Lesson LESSON1: Group 2, Lesson LESSON2: Group 1, Lesson LESSON3: Group 1
   
   Monday       Tuesday      Wednesday    Thursday     Friday      
   ----------------------------------------------------------------
                LESSON3      LESSON2                               | 8:30-10:20
                             LESSON1                               | 10:30-12:20
                                                       LESSON1     | 12:30-14:20
                                                                   | 14:30-16:20
                                                                   | 16:30-17:20
   Lesson LESSON1: Group 1, Lesson LESSON2: Group 2, Lesson LESSON3: Group 1
   
   Monday       Tuesday      Wednesday    Thursday     Friday      
   ----------------------------------------------------------------
                LESSON3      LESSON2                               | 8:30-10:20
   LESSON1                                                         | 10:30-12:20
                LESSON1                                            | 12:30-14:20
                                                                   | 14:30-16:20
                                                                   | 16:30-17:20
   Lesson LESSON1: Group 2, Lesson LESSON2: Group 2, Lesson LESSON3: Group 1
   
   You have 4 possible program
   ```
   
<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExN3E1Y3RmMDBwNXdibG4zaWhiNG9zdncwMjltaTJvbGRtazYwdjJsZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/KAq5w47R9rmTuvWOWa/giphy.gif" alt="Giphy Animation">
</p>

