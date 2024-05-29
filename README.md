# learning_flask_2
Learning exception handling, request handling, db setup/query, and html templates in flask w/ online tutorial

Initialized a database containing a table with two INT fields, celsius and fahrenheit. These two act as a compositie primary key for the table.

At the /create/ route a user will find a text box and submit button. The user can enter an integer that will represent a temperature in celsius. After the submit button is pressed, the backend will convert the value to fahrenheit and then attempt to add a new entry to the database. If the entry already exists, the sql insert command is ignored. The user is then redirected to the / route where a list of all current entries in the database are listed out.
 
