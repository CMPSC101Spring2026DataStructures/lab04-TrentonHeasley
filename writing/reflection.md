# Reflection: Rock, Paper, Scissors Lab

Name: Trenton Heasley
Date: 2/20/26

Please answer the following questions after you have completed the programming lab. Write your answers in complete sentences and provide thoughtful responses.

## Comprehension Questions

1. What is the purpose of breaking a program into functions? How did this help you in completing the lab?

Your Response:

it helps divide the code into pieces that can be called to use multiple times. this allows for a more concise code that is easier to maintain and understand. it also breaks up code by its functionality making it easier to build on.



2. Describe how you validated user input in your version of the Rock, Paper, Scissors game. Why is input validation important?

Your Response:

i set up a dictionary with 1, rock, 2, paper, 3, scissors. i set up a while loop that continues to run until a valid choice is inputed by the user triggering a return. using this dictionary i check the input from the user against the dictionary after i use strip and lower to regulate the input. if valid input then it returns input

3. How did you use comments and docstrings in your code? Give an example of a helpful comment or docstring you wrote.

Your Response:

i used comments in main to clarify what the code is so you dont have to sift through it to understand the structure of the code. one example is "Function to handle user input also ensures the user enters a valid move."

4. Explain how the computer's move is generated in your program. What Python features did you use to accomplish this?

Your Response:

its just return random.choice(choices). it pulls a random choice from the list to use as the computer's input

5. What was the most challenging part of refactoring the spaghetti code into a more structured program? How did you overcome this challenge?

Your Response:

i changed up the user input code a little bit to adjust it to how i taught myself to handle a loop that you need to break only when specific conditions are met. im using a return as the loop breakers when sucsessful rather than a break. 

## Ethical Reflection Questions

1. Why is it important to write code that is easy for others to read and maintain? How does this relate to your responsibilities as a programmer?

Your Response:

being able to work with others and producing work that others can work on is really important. making the code readable and breaking it up into segments makes it more understandable and modular. 

2. Consider the use of open source code (like the spaghetti code provided). What are some ethical considerations when using, modifying, or sharing code written by others?

Your Response:

i think the big thing to consider is crediting the original coder. just like you can "steal" sentances and papers from authors you can steal code if you aren't transparent in your aquiring and intentions with it.

---

(Did you remember to add your name and date at the top of your reflection file?)
