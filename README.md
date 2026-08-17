# Coding Assessment - Python

This repository contains solutions for two programming problems.

1. First Non-Repeating Character
2. Find the Missing Number

Both solutions are written in Python.

--------------------------------------------------
1. FIRST NON-REPEATING CHARACTER
--------------------------------------------------

Problem:

Given a string, find the first character that appears exactly once.

If every character appears more than once, print -1.

The comparison is case-sensitive.

Example 1:

Input:
swiss

Output:
w

Example 2:

Input:
aabbcc

Output:
-1

Example 3:

Input:
programming

Output:
p

Approach:

First, count the number of times each character appears in the
string using a dictionary.

Then check the string from left to right. The first character
whose count is 1 is the answer.

If no such character is found, print -1.

Complexity:

Time Complexity: O(n)
Space Complexity: O(n)


--------------------------------------------------
2. FIND THE MISSING NUMBER
--------------------------------------------------

Problem:

You are given N distinct numbers from 1 to N+1. Exactly one
number is missing from the sequence.

Find the missing number.

Example 1:

Input:
1 2 4 5 6

Output:
3

Example 2:

Input:
1 2 3 5

Output:
4

Example 3:

Input:
2 3 1 5

Output:
4

Approach:

The complete sequence contains numbers from 1 to N+1.

First, calculate the sum of all numbers from 1 to N+1.

Then subtract every number present in the given array.

The remaining value is the missing number.

Complexity:

Time Complexity: O(n)
Extra Space Complexity: O(1)


--------------------------------------------------
HOW TO RUN
--------------------------------------------------

Requirements:

Python 3.x

No external libraries are required.


Run the First Non-Repeating Character program:

python first_non_repeating.py

Example input:

swiss

Output:

w


Run the Find Missing Number program:

python find_missing_number.py

Example input:

1 2 4 5 6

Output:

3


--------------------------------------------------
PROJECT STRUCTURE
--------------------------------------------------

coding-assessment/
|
|-- first_non_repeating.py
|-- find_missing_number.py
|-- README.md
|-- .gitignore


--------------------------------------------------
GIT REPOSITORY
--------------------------------------------------

Initialize Git:

git init

Add the files:

git add .

Commit the files:

git commit -m "Add solutions for coding assessment"

Create a GitHub repository and connect it:

git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main

Replace YOUR_GITHUB_REPOSITORY_URL with your GitHub repository URL.


--------------------------------------------------
SUBMISSION
--------------------------------------------------

The repository should contain:

first_non_repeating.py
find_missing_number.py
README.md
.gitignore

No unnecessary files, build artifacts, IDE folders, or dependency
folders should be uploaded.
