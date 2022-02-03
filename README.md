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
cd ..
source env/bin/activate
pip install -r requirements.txt
deactivate
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

**Note**: You might have some browser warnings about insecure link when you click on the "Visit APD" button. I'm not sure if
this will be a problem if both the servers are hosted on https, or if this is some cors issue. But I'm unable to test this,
since ngrok is allowing only 1 connection per machine on the free version. Looks like this might require a server setup
with nginx reverse proxy, 2 subdomains and let's encrypt certificates to properly test. Either way, we cannot have that
error on production, since that will require the user to blindly trust serverFoo and ignore the browser warning.
