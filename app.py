from flask import Flask, render_template, request, redirect, session, url_for
from sqlite3 import *
from flask import request
from tensorflow.keras.models import model_from_json
import cv2
import requests
api_key = 'AIzaSyDhY6ulQ4apf4GjZyOQvg3KC4ug6Fx0b0I'
from PIL import Image
import base64
import io

app = Flask(__name__)
app.secret_key = 'abc'


@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')

@app.route('/skincan', methods=['POST','GET'])
def skincan():
    return render_template('skincan.html')

@app.route('/prev', methods=['POST','GET'])
def prev():
    return render_template('prev.html')

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        con=None
        try:
            con = connect('skin_assessment.db')
            cursor = con.cursor()
            sql = "select * from users where email ='%s' and password = '%s'"
            cursor.execute(sql % (email,password))
            con.commit()
            data = cursor.fetchall()
            if len(data) == 0:
                return render_template('login.html', msg = 1)
            else:
                session['email'] = email
                return redirect(url_for('skinExam'))

        except Exception as e:
            con.rollback()
            msg = "issue" + str(e)
            return render_template('login.html',m=msg)
        
        finally:
            if con is not None:
                con.close()
    else:
        return render_template('login.html')
    
@app.route('/contact', methods=['POST','GET'])
def contact():
    if request.method== 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        msg = request.form['message']
        con= None
        try:
            con = connect('skin_assessment.db')
            cursor = con.cursor()
            sql = "insert into contactus values('%s', '%s' ,'%s' ,'%s')"
            cursor.execute(sql % (name,email,phone,msg))
            con.commit()
            return render_template('contact.html',m = 1)

        except Exception as e:
            con.rollback()
            return render_template('contact.html',m = e)

        finally:
            if con is not None:
                con.close()
    else:
        return render_template('contact.html')

@app.route("/signup", methods=['POST','GET'])
def signup():	
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        age = request.form['age']
        email = request.form['email']
        password = request.form['password']
        try:
            con = connect('skin_assessment.db')
            cursor = con.cursor()
            sql = "select * from users where email ='%s' and password = '%s'"
            cursor.execute(sql % (email,password))
            data = cursor.fetchall()
            if len(data) == 0:
                sql1 = "insert into users(name,email,password,gender,age) values('%s','%s','%s','%s','%s')"
                cursor.execute(sql1 % (name,email,password,gender,age))
                con.commit()
                return redirect(url_for('login'))
            else:
                return render_template('signup.html', msg = 1)
        except Exception as e:
            con.rollback()
            return render_template('signup.html',m = e)
        finally:
            if con is not None:
                con.close()
    else:
        return render_template('signup.html')

@app.route("/skinExam", methods = ['POST','GET'])
def skinExam():
    if 'email' in session:
        return render_template('skinExam.html')
    else:
        return redirect(url_for('login'))

@app.route('/logout', methods=['POST','GET'])
def logout():
    session.pop('email',None)
    return redirect(url_for('index'))

@app.route("/skinExamResult", methods=["GET", "POST"])
def skinExamResult():
    if request.method == 'POST':
        f = request.files['file'] 
        file_name = f.filename
        path='static/files'+f.filename
        f.save(path)

        im = Image.open(path)
        rgb_im = im.convert('RGB')
        data = io.BytesIO()
        rgb_im.save(data, "JPEG")
        encoded_img_data = base64.b64encode(data.getvalue())

        j_file = open('model.json', 'r')
        loaded_json_model = j_file.read()
        j_file.close()
        model = model_from_json(loaded_json_model)
        model.load_weights('final_mobilenet1.h5')
        img = path
        img = cv2.resize(cv2.imread(img), (224,224))
        img = img/255.0
        prediction = model.predict(img.reshape(1,224,224,3))
        v1 = prediction[0][0]*100
        v2 = prediction[0][1]*100
        v3 = prediction[0][2]*100
        v4 = prediction[0][3]*100
        l = [v1,v2,v3,v4]
        l1=['Acne/Rosacea','Melanoma Skin Cancer Nevi and Moles','Psoriasis/Lichen Planus','Vasculitis']
        m = 0
        for i in range(0,len(l)):
            if l[i]>m:
                m = l[i]
                m1 = l1[i]
        print(m,m1)
        if 'email' in session:
            email = session['email']
            con=None
            try:
                con = connect('skin_assessment.db')
                cursor = con.cursor()
                cursor1 = con.cursor()
                sql = "select * from users where email ='%s'"
                sql1 = "update users set disease = '%s' where email ='%s'"
                cursor.execute(sql % (email))
                cursor1.execute(sql1 % (m1,email))
                con.commit()
                data = cursor.fetchall()
                for row in data:
                    name = row[0]
                    email = row[1]
                    gender = row[3]
                    age = row[4]
                print(name,gender,age)
              
            finally:
                if con is not None:
                    con.close()
            
        return render_template('skinExam.html', img_data = encoded_img_data.decode('utf-8'), v1 = v1, v2 = v2, v3 = v3, v4 = v4, msg = 1, name = name, gender = gender, age= age, email = email, file_name = file_name, m = round(m,2),m1=m1)
        
    else: 
        return render_template("skinExam.html")

@app.route('/derm', methods=['POST','GET'])
def derm():
    return render_template('derm.html')

@app.route('/dermat', methods=['POST','GET'])
def dermat():
    if request.method == 'POST':
        c = request.form['city']
        # url variable store url
        url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
        query = "dermatologists in " + c
       
        # get method of requests module
        # return response object
        r = requests.get(url + 'query=' + query +
                        '&key=' + api_key)
  
  
        # json method of response object convert
        #  json format data into python format data
        x = r.json()

        # now x contains list of nested dictionaries
        # we know dictionary contain key value pair
        # store the value of result key in variable y
        y = x['results']
        name = []
        address = []
        # keep looping upto length of y
        for i in range(len(y)):
      
            # Print value corresponding to the
            # 'name' key at the ith index of y
            name.append(y[i]['name'])
            address.append(y[i]['formatted_address'])

            #print(y[i]['name'])
            
            #print(y[i]['formatted_address'])
        print(name)
        print(" ")
        print(address)
        print(" ")
        print(" ")
        if len(name) > 0:
            m = 1
        print(len(name), len(address))
    return render_template("dermat.html", name=name, address=address, m=m)

@app.route('/support', methods=['POST','GET'])
def support():
    return render_template('support.html')


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host="0.0.0.0")