# crossSiteForm

## Description
Simple experiment in Python Flask to check if secure form submission is possible from one server to another.

## Dependencies
* Python 3.9 or later
* ngrok 2.2 or later, with an authtoken configured
  * Documentation: [Link](https://ngrok.com/docs#getting-started-authtoken)

## Project setup
```shell
# clone the project to your local machine
# cd into the project directory
chmod +x serverFoo/run.sh
chmod +x serverBar/run.sh
mkdir env
cd env
python3 -m venv .
```

## Running the project
You will need 2 simultaneous terminals to run the project.

Terminal 1 commands:
```shell
# cd into the project directory
source env/bin/activate
cd serverBar/
./run.sh
# This will start the Flask app and ngrok
# Copy the <ngrok generated https link>
```

Terminal 2 commands:
```shell
# cd into the project directory
source env/bin/activate
cd serverFoo/
./run.sh <ngrok generated https link>
```

Visit [0.0.0.0:5001]() and check terminal 2 for the **generated secret**.

Click on the "Visit APD" button on the browser

You will be redirected to the ngrok link where you will see the message:
```text
The secret is: ** generated secret **
```
If the **generated secret** in terminal 2 matches with what shows up on the ngrok https link, then that means that the
secret was successfully passed from the server in terminal 2 to the server in terminal 1.
