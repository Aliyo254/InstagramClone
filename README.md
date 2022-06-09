# The-Gram

## author
[Alinur Ali](https://github.com/aliyo254/)

## description
An application that mimics instagram where a user can post photos ,like and comment on photos and follow friends to see their photos
## how it works
- a user creates an account
- a user edits his/her profile
- a user can post a photo
- a user can follow friends to see their photos
## Installation requirements
To run the application do the following:

- clone this repo by running:
` git clone https://github.com/Aliyo254/InstagramClone.git
- set up a virtual environment
 ` python3.8 -m venv  python3.8 -m venv virtual `
 - activate virtual environment
  ` source virtual/bin/activate `
- to install all requirements
` pip install -r "requirements.txt" `
 - create a file .env and put in the following configurations:
   ```
      - SECRET_KEY=<secret key>
      - DEBUG=False
      - DB_NAME=<database name>
      - DB_USER='<username>
      - DB_PASSWORD=<your password>
      - DB_HOST='127.0.0.1'
      - MODE='dev'
      - ALLOWED_HOSTS=<your site name>
      - DISABLE_COLLECTSTATIC=1
   ```

- run the application locally with
 ` python manage.py runserver `
## Link to live site


## likely bugs
Currently the application has no known bugs but if you come across any issues feel free to contact me from the email address that will be provided below.
## Testing
- to run tests run ` python manage.py test app `
## technologies used
The technologies used to build the application are:

- Python3.8 and django1.11
- Bootstrap3
- css
- heroku live server

## contact details
feel free to email me at alinurali254@gmail.com incase of any feedback or bugs you face

## LICENCE
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
