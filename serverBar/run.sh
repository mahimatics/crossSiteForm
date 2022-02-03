#!/bin/bash
trap "kill 0" EXIT
SERVER_BAR_PORT=5002
flask run --port $SERVER_BAR_PORT &
ngrok http $SERVER_BAR_PORT
wait
