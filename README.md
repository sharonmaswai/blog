# The Country Blog

## Created By: Sharon Maswai

##  Description

This is a blog where you get to view already posted blogs, comment on them and post your own blog.
## Setup

### Prerequiites

- Python 3.6
- Ubuntu software

### Clone the Repo

Run the following command on the terminal: git clone https://github.com/sharonmaswai/blog.git 

### Install Postgres

### Create a Virtual Environment

Run the following commands in the same terminal:

sudo apt-get install python3.6-venv
python3.6 -m venv virtual
source virtual/bin/activate
Install dependancies
Install dependancies that will create an environment for the app to run pip3 install -r requirements




## BDD

| Behaviour | Input  | Output |
| -- |-- |--|
|Signing up| Click sign up| Display registration form|
|Signing in|Click sign in |Login form is displayed|
|Create blog|click create-blog then sign in|Create blog form is displayed|
|Display blogs|click blogs on the navbar|Created blogs are siplayed|
|Delete blog|click delete blog|Blog is deleted|
|Delete comment |click delete comment|comments are deleted|


## Bugs

At the time of deployment there were no known bugs.

## Technologies used

HTML

CSS

Python3.6

Flask

Bootstrap 4


## Running app

In the terminal:

$ ./start.sh

## Support

In case of any challnges contact me at chepsharonmaswai@gmail.com

## License


MIT License

Copyright (c) [2019] [SharonMaswai]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.