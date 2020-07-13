# Here we need to correct the prompt, replace ash for bash
#!/bin/bash

echo​​"Starting gunicorn..."
gunicorn -w 16 -b 127.0.0.1:9000 app:app --daemon
sleep 3
echo​​"Starting web server..."
nginx -g ​"daemon off;"