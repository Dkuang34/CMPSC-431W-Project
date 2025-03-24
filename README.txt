Overall, this project thus far is a simple login screen for all the users in our database. Essentially, when your run it, you are presented with a user login screen. This screen prompts the user to enter their login, consisting of a username (email) and password. Upon entering their information, if it is incorrect, red text will show up to tell them the username or password is incorrect. However, if their information is correct, they are directed to the NittanyBusiness homepage, which is not finished as of right now.

There are 4 files within this project, each of which I will give a short description of:

users_setup.py: This python script was used for us to populate the database for our test use. The function of this code is to go through the Users csv file and input each username and password combo into our database. So, let me quickly go through the logic. We define a simple function called sha256hash which sha256 hashes a password. This completes the hashing requirement to increase the security and privacy of our users' passwords. Then, the u_setup() function filters through the Users csv file and inputs each username/password into the database. First, it establishes a connection with the database, then creates the USERS table. Once the setup part is complete, it goes into the Users csv and reads through it. Each new row is a new username/password combo, and thus for each row, it inputs the username and hashed password into the database as a new USER entry.

app.py: This file completes the overarching logic of the project. First, there is the login() function which verifies a login attempt. It will get the username and password entered by the user, and calls a helper function is_valid_login() to check if that username/password combination was in our database. The is_valid_login() function will hash the user-entered password since the hashed passwords are the ones we store in our database, and then try to SELECT from our USERS table where the username and password is equal to what the user entered. If it was successful in finding an entry in the database, then the user is logged in and sent to our homepage, otherwise, the user sees a message saying, "Login attempt failed. Invalid email or password".

login.html: This file is designing the page for the user login screen. We set the fonts, colors, and proportions of everything on the page from the text to the login boxes. All the headers and labels are titled in here as well. Overall, it is the outline for how the login page is presented.

home.html: Very similar to the login.html file, this file does the exact same thing for the homepage. Since the homepage is mostly empty for now, it just puts words to a few titles and headers, and that is it. Simple, just like the last file, it is the outline for how the homepage looks for users who are directed there after a successful login attempt.

INSTRUCTIONS:
1. Make sure you have the required languages and software tools downloaded (Python, Flask, HTML, SQLite, JavaScript, PyCharm Professional)
2. Download the files given in the zip file and place them into a project folder
3. Open the project folder into PyCharm Professional
4. First, run the users_setup.py file to populate the database with all the users provided for us in the Users csv
5. Then, Open the app.py file and run the Flask app by pressing the Run button in the upper-right side of your screen
6. In the terminal, it will give you a link to "http://127.0.0.1:5000/", click on that
7. Clicking on that link will have brought you to the user login page, with 2 boxes, one for you to enter your username, and one for your password
8. To start, lets enter a username and passwords provided in the Users csv, since we know it is correct and will be in our database. Just for the sake of these instructions, lets enter o5mrsfw0@nittybiz.com as the username and TbIF16hoUqGl as the password.
9. Then, click the Login button
10. Since that was a valid username/password combination, you are directed to the homepage of NittanyBusiness
11. However, if you had entered an incorrect username/password combination, then a simple red text would show up informing you of as much, saying, "Login attempt failed. Invalid email or password"

CONGRATS! You have successfully learned how to use our user login feature for the program!
