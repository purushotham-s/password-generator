# password-generator
Web app to generate random passwords

How to run:

`$ pip install -r requirements.txt` # install flask

`$ python3 app.py`

App runs on port 8000, on all interfaces. You can access it on `http://localhost:8000` or `http://<IP_ADDRESS>:8000`


How to build docker image of the app:

`$ cd /<APP_DIR>`

`$ sudo docker build . -t password-generator`

You can then run the docker image my running:

`$ sudo docker run -d --name="password-generator" -p 8000:8000 password-generator`
