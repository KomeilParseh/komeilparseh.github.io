Title:Mozlink!
Date:2021-5-4-21:00
Modified:2021-5-4-21:00
Category:programing
Tags:tecnology,programin,python,mozlink
Slug:Mozlink
Authors:komeilParseh
description:A program to build shortLinks

# mozlink

![logo](https://raw.githubusercontent.com/KomeilParseh/mozlink/main/app/static/logo.png)

A program to build **shortLinks**

[mozlink-komeilparseh.fandogh.cloud](https://mozlink-komeilparseh.fandogh.cloud/) Temporary (perhaps permanent!) service link.

Note: Sometimes links may **not work** due to site updates.

## How to run

1. Install python3, pip3, virtualenv in your system.
2. Clone the project

`git clone https://github.com/KomeilParseh/mozlink.git && cd mozlink`

3. in the app folder, rename the `config.py.sample` to `config.py` and do proper changes.
4. Create a virtualenv named venv using

`virtualenv -p python3 venv`

5. Connect to virtualenv using

`source venv/bin/activate`

6. From the project folder, install packages using

`pip install -r requirements.txt`

7. Now environment is ready. Run it by

`python app/main.py`
