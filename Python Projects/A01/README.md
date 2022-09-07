## Project 01 - Factors & Rock, Paper, Scissors Game

### Loic Konan

### Description

<h2 align = "center">Factors </h2>

> - Write a program that will keep running (i.e. doing what is being asked below), till the user inputs an 'E' (for exit).
> - Ask the user for a number.
> - The program should display all positive factors of the number that is input.
>   - For instance, if the user inputs 100, all factors of 100 are displayed. The factors are: **[1, 2, 4, 5, 10, 20, 25, 50, 100]**
>   - Similarly, if the user inputs 150, all factors of 150 are displayed. The factors are: **[1, 2, 3, 5, 6, 10, 15, 25, 30, 50, 75, 150]**
>
> - Then, if the total number of Factors is
>   - Less than 10: Display "This is too less - Good Bye". And the Program Ends !
>
>   - More than 10: Do the following
>     - Display the highest 3 factors (e.g. for 150 - the highest 3 factors are 50, 75, 150)
>     - Display the average of the above 3 factors (e.g. for 150 - average is 91.667). And the Program Ends !
>

### Files

|   #   | File               | Description                    | Status                  |
| :---: | ------------------ | ------------------------------ | ----------------------- |
|   1   | [main.py](main.py) | Solution for the first problem | :ballot_box_with_check: |

<br>
<br>

<h2 align = "center">Rock, Paper, Scissors Game </h2>

> - Write a program that lets the user play the game of **Rock, Paper, Scissors** against the computer. The program should work as follows:
>
> **1.**
>
> - When the program begins, a random number in the ***range of 1 through 3 is generated***.
> - For this, you need to import the random library **(import random) and use the randint function (random.randint(1, 3))**
>
> **2.**
>
> - If the number is 1, then the computer has chosen rock.
> - If the number is 2, then the computer has chosen paper.
> - If the number is 3, then the computer has chosen scissors. (Don’t display the computer’s choice yet.)
>
> **3.**
>
> - The user enters his or her choice of **“rock,” “paper,” or “scissors”** at the keyboard.
> - You can say something like:
>   - **Enter 1 for rock, 2 for paper, 3 for scissors**
>
> **4.**
>
> - The computer’s choice is displayed. And the User’s choice is displayed.
>
> **5.**
>
> - The winner is selected according to the following rules:
>   - If one player chooses rock and the other player chooses scissors, then rock wins. **(The rock smashes the scissors.)**
>     - If one player chooses scissors and the other player chooses paper, then scissors wins. **(Scissors cuts paper.)**
>     - If one player chooses paper and the other player chooses rock, then paper wins. **(Paper wraps rock.)**
>   - If both players make the same choice, **the game must be played again to determine the winner**.

### Files

|   #   | File                | Description                     | Status                  |
| :---: | ------------------- | ------------------------------- | ----------------------- |
|   1   | [main1.py](main1.py) | Solution for the second problem | :ballot_box_with_check: |
