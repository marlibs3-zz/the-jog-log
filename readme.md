## The Jog Log

This simple Django web-app allows you to keep a record of your runs. It also calculates the calories that you burned during said exercise.

To run the local dev server:
- Clone the repo
- Run `docker build -t jogger-dev-server`
- Run `docker run -p 8000:8000 jogger-dev-server`
- Navigate to http://127.0.0.1:8000/