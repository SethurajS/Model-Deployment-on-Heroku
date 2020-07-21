# Model-Deployment-on-Heroku

# Deploying a simple regression model API with Heroku.

* Before pushing your app into github, 
    a) Make sure that you have "Procfile", "requirements.txt" files in your directory, you must add these files to your repository.
    b) Make sure that your "requirements.txt" contain "gunicorn".

1. Push your flask app with model on github.
2. Go to https://heroku.com/
3. SignUp / SignIn and then select "New" button on top right.
4. Scroll down and find "Deployment method" section.
5. There you can see three options : "Heroku Git", "Github", "Container Registry".
6. Select the Github option, link your Github Account with heroku.
7. Put your Repository Name in the given space and then press connect.
8. Then it will install all the requirements and finally launch your API.


Deployed API ->  https://model-salary-prediction-api.herokuapp.com/
