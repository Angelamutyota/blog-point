# News_API

## Author

ANGELA MUTYOTA

# Description
Blogpoint is a personal blogging website where users can create and share your opinions and other users can read and comment on them. Additionally, the site contains a feature that displays random quotes to inspire your users. 


## User Story

1. A user should see various blog posts on the homepage of the application.
2. A user can create and access their profile
3. A user can comment on other blog posts
4. A user can either update or delete their blogs from their profile 


## Development Installation
To get the code..

1. Cloning the repository:
  ```bash
  git clone https://github.com/Angelamutyota/blog-point.git

2. Move to the folder and install requirements
  ```bash
  cd blog-point
  pip install -r requirements.txt
  ```
3. Exporting Configurations
  ```bash
  export SECRET KEY='{Enter your secret Key}'
  export MAIL_USERNAME='{enter your email}'
  export MAIL_PASSWORD='{enter your email password}'


  ```
4. Running the application
  ```bash
  python3.8 manage.py server
  ```
5. Testing the application
  ```bash
  python3.8 manage.py test
  ```
Open the application on your browser `127.0.0.1:5000`.


## Technology used

* Python3.8
* Flask
* Heroku


## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug


## License
* *MIT License:*
* Copyright (c) 2021 **Angela Mbithe**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.