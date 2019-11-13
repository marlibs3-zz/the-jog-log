## The Jog Log

This simple Django web-app allows you to keep a record of your runs. It also calculates the calories that you burned during said exercise.

###To run the local dev server:
- Clone the repo
- Run `docker build -t jogger-dev-server`
- Run `docker run -p 8000:8000 jogger-dev-server`
- Navigate to http://127.0.0.1:8000/

### To run the tests:
- Clone the repo
- Run `docker build -t jogger-dev-server`
- Run `docker run -p 8000:8000 jogger-dev-server python manage.py test`


### If I had more time I would have...
- Tidied up / commented the code
- Added validation for the form, probably by redoing the form using the Forms API and tested it
- Added error handling and a 404 page
- Used proper CSS instead of hand-cranked bootstrap-y magic
- Added a user profile where they could enter their weight instead of entering it per run
