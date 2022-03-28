# 1. About
This is an app that get three inputs from the front end. Specifically, the user input their first name, last name and zip code. Then, the data is organized in a json file and be sent to back end. In the back end, the first name and second name is converted to pig latin. The zip code is used to get the county and population information through Zip API.

# 2. Features

- Restrict the input to increase the stability and security.

- Unit test is written for the back end using mock.

- Using Zip API to support zip code information lookup.

# 3. How to use

(1) Get the front end code.

 `git clone https://github.com/JoyVivian/zero-frontend.git`

(2) Go to the source code folder.

(3) Run `npm start`

(4) Input and test the app. No need to config the backend. It was deployed on Heroku.


# Test the code

! Important the Zip API only provide 10 requests for users every hour. So do not test the code more than 10 times every hour, or it will return an error.