## Project 04 - Remove Followers that don't Follow back.

### Loic Konan

### Description

- Program that will **delete anyone** that is **not following** you back on **instagram**
- **Authenticate and authorize** the user's Instagram account using the **Instagram API**.
- **Retrieve the list** of users who are following the user and the list of users the user is following.
- **Compare the followers list** with the **following list** to identify users who are **not following** the user back.
- For each user in the **following list**, check if they are present in the **followers list**.
- If not, add them to a **separate list** of users who are not following the user back.
- Use the Instagram **API to unfollow** each user in the list of users who are **not following the user back**.

### Requirements

- **Python 3.8** or higher.

### Installation

- pip install instaloader
  
### Usage

- Run the program with `python main.py`

### Files

|   #   | File               | Description | Status                  |
| :---: | ------------------ | ----------- | ----------------------- |
|   1   | [main.py](main.py) | Solution    | :ballot_box_with_check: |

