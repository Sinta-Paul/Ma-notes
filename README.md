# Ma-notes
# About The Project

Ma,Notes is a web app that creates notes for any website.The app was built using python,HTML and CSS. The website given by user is scraped and given as prompt to OpenAI api.The notes of the mentioned site is automatically downloaded.

## App Preview
<img width="946" alt="Screenshot 2023-05-21 211120" src="https://github.com/Sinta-Paul/Ma-notes/assets/83969235/fd3f0efa-b92d-4e2d-8782-f595c4ac99ad">
<img width="959" alt="Screenshot 2023-05-21 211549" src="https://github.com/Sinta-Paul/Ma-notes/assets/83969235/ca69af60-3a81-48dd-857b-e369f1f0dfa9">

## Built With

* Django framework
* Html
* Css
* OpenAI Api

<!-- GETTING STARTED -->
# Getting Started
## Dependencies

* Django==4.1.3
* virtualenv==20.17.1
* virtualenvwrapper-win==1.2.7
## Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Sinta-Paul/Ma-notes
   ```
2.Create a virtual environment to install dependencies in and activate it:

  ```sh
  $ virtualenv2 --no-site-packages env
  $ source env/bin/activate
  ```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000`.

<!-- USAGE EXAMPLES -->
# Usage
"Ma,Notes" is a solution to effectively reduce time spent on reading large articles or research papers. The app provides a concise note on any given website. This helps in getting a general understanding of the topic.

<!-- ROADMAP -->
# Roadmap

- Copy website URL 
- Enter URL and generate notes

<!--FUTURE -->
# Future Scope
*  To be able to use this website as a chrome extension
*  To be able to work well for websites with larger contents.

<!-- CONTACT -->
# Project Link: 
[https://github.com/Sinta-Paul/Ma-notes]
