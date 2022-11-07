from flask import Flask,request,render_template,ibm_db

app= Flask(__name__)
database=ibm_db.connect("DATABASE=bludb;HOSTNAME=b1bc1829-6f45-4cd4-bef4-10cf081900bf.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32304;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt; UID=bdn89663;PWD=y9pVOZ7qDlOOo9sm",'','')


@app.route('/')
def hello_world():
    return render_template("login.html")

@app.route('/form_login',methods=['POST','GET'])
def login():
    email1=request.form['email']
    pwd=request.form['password']

    if email1 not in database:
        return render_template('login.html')
    elif database[email1]!=pwd:
       return render_template('login.html',info='invalid password')
    else:
        return render_template('login.html',email=email1)

    if __name__ =='__main__':
        app.run()