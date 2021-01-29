from flask import Flask, render_template, request
import random
import string

result = ''
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/req', methods=['POST'])
def req(result=result):
    if request.method == 'POST':
        pass_length = request.form['pass_length']
        if request.form.get('symb'):
            include_symb = request.form['symb']
            result = generate_password(pass_length, include_symb)
        else:
            result = generate_password(pass_length)
        return render_template('index.html', result=result)

def generate_password(pass_length, include_symb=True):
    password = []
    pass_length = int(pass_length)
    if include_symb:
        password.append(random.choice('!@#$%^&*(){}[]'))
        pass_length -= 1
    for x in range(pass_length - 4):
        password.append(random.choice(string.ascii_lowercase))
    for x in range(2):
        password.append(random.choice(string.ascii_uppercase))
    for x in range(2):
        password.append(random.choice(string.digits))
    random.shuffle(password)
    #print(''.join(password))
    return ''.join(password)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8000 , debug = True)
