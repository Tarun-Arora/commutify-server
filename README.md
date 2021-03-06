# Commutify

## Introduction

Welcome to the Commutify Project. In this project, we have implemented a real-time chatting website that lets you connect to the community, COMMUTIFY !!

### Setting up the Project

- Make sure `python3.8` and `pip` are installed. Install `pipenv` by running `pip install pipenv`.
- Install python dependencies using the command `pipenv install` Please use only pipenv for managing dependencies (Follow this [link](https://realpython.com/pipenv-guide/) if you are new to pipenv).
- To activate this project's virtualenv, run `pipenv shell`.
- Run `python manage.py migrate` to apply migrations.
- Start the development server using `python manage.py runserver`

	pip install channels-redis
	sudo docker run -p 6379:6379 -d redis:5

## API ENDPOINTS

We are including the description of the API for your reference.

### Auth System

For this API, you will have to use Token-based Authorization. All the requests made to the API (except the Login and Register endpoints) shall need an  **Authorization header**  with a valid token and the prefix  **Token**.

The authorization header shall have the following format:
`Authorization: Token <token>`

-   `POST /auth/login/`
    Takes the username and password as input, validates them and returns the **Token**, if the credentials are valid.  
  
	Request Body (Sample):
	```
	{
	  "username": "string",
	  "password": "string"
	}
	```
	Response Body (Sample):
	```
	{
	  "token":  "string"
	}
	```
	Response Code: `200`

-   `POST /auth/register/`

	Register a user in Django by taking the name, email, username and password as input.
  
	Request Body (Sample):
	```
	{
	    "username": "string",
	    "email": "user@example.com",
	    "password": "string"
        "first_name": "string",
        "last_name": "string", 
        "dob": "YYYY/MM/DD"
	}
	```
	Response Body (Sample):
	```
	{
	    "Success": "You are now registered. Please verify your email."
	}
	```
	Response Code: `200`

3. VERIFY       (BASE_URL + 'verify/<auth_token>/')
    GET

4. FORGOT PASSWORD OTP Email (BASE_URL + 'forgotpwd/<email>/')
    POST
    Req. Body
        {

        }

5. RESET PASSWORD   (BASE_URL + 'resetpwd/')
    POST
    Req. Body
        {
            'email'
            'otp'
            'newpasswd'
        }
