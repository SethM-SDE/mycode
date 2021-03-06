#!/usr/bin/env python3

from flask import Flask
from flask import session
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request

app = Flask(__name__)
app.secret_key = 'baconpancakes'
groups = [{"hostname": "hostA", "ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
          {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
          {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]

# if user hits root
@app.route('/')
def index():
    # if 'uesrname' has value in session
    if 'username' in session:
        username = session['username']
        return redirect(url_for(adder))

    # if 'username' does not have value
    return 'You are not logged in <br><a href = "/login"> click here to log in</b></a>'

@app.route('/add_ip', methods=['POST','GET'])
def adder():
    if 'username' in session:
        if request.method == 'POST':
            hostname = request.form.get('hostname')
            ip = request.form.get('ip')
            fqdn = request.form.get('fqdn')
            groups.append({'hostname': hostname, 'ip': ip, 'fqdn' : fqdn})
            print(groups)
            return redirect(url_for('adder'))
        else:
            print('Groups again')
            print(groups)
            return render_template('jinjatemp.html', groups=groups)

# if user hits /login with a GET or POST
@app.route('/login', methods = ['GET', 'POST'])
def login():
    # if you send a POST vai login button
    if request.method == 'POST':
        session['username'] = request.form.get('username')

        if session['username'] == 'Chewie':
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))

    # return HTML data if GET sent
    return"""
    <form action = "" method = "post">
      <p><input type = text name = username></p>
      <p><input type = submit value = Login></p>
   </form>
  """

@app.route('/logout')
def logout():
    # remove the username from the session if there
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2224)
