#!/bin/bash
trap "kill 0" EXIT
SERVER_FOO_PORT=5001
SERVER_FOO_URL=$1 flask run --port $SERVER_FOO_PORT &
ngrok http $SERVER_FOO_PORT
wait
