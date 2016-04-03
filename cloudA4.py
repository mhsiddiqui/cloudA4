from flask import Flask, render_template, redirect
from forms import MyForm
from flask import request
import cmath
import socket

app = Flask(__name__)
app.debug = True
app.secret_key = 's3cr3t'


@app.route('/')
def index():
    form = MyForm()
    return render_template('index.html',
                           title='Home',
                           form=form)

@app.route('/get_equation_solution', methods=['POST', 'GET'])
def get_equation_solution():

    a = float(request.values.get('a'))
    b = float(request.values.get('b') if request.values.get('b') != '' else 0)
    c = float(request.values.get('c') if request.values.get('c') != '' else 0)
    # calculate the discriminant
    d = (b**2) - (4*a*c)

    # find two solutions
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    return render_template('result.html',
                           a=a,
                           b=b,
                           c=c,
                           sol1=sol1,
                           sol2=sol2,
                           ip=get_ip_address())

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("gmail.com", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

if __name__ == '__main__':
    app.run(debug=True)
