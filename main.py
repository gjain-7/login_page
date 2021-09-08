from flask import Flask, render_template, request, redirect
import MySQLdb
app = Flask(__name__)
db=MySQLdb.connect(host="localhost",user="<username>",passwd="<pass>",db="cs257")
cursor = db.cursor()

@app.route("/",methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        uid = request.form['userid']
        mobno = request.form['mobile_no']
        passwd = request.form['password']

        query= "SELECT EXISTS(SELECT * FROM users WHERE UserId='{}');".format(uid)
        cursor.execute(query)
        isExist = cursor.fetchone()[0] 
        if isExist:
            return render_template('signup.html',message="Username already in use.")

        query= "insert into users(UserId,mobile_no,password) values('{}','{}','{}');".format(uid,mobno,passwd)
        cursor.execute(query)
        db.commit()
        return redirect("/login")        

    return render_template('signup.html')

@app.route("/login",methods=['POST','GET'])
def signin():
    if request.method == 'POST':
        uid = request.form['userid']
        passwd = request.form['password']
        query= "SELECT EXISTS(SELECT * FROM users WHERE UserId='{}' and password='{}');".format(uid,passwd)
        cursor.execute(query)
        isExist = cursor.fetchone()[0] 
        if isExist:
            cursor.execute("Select * from courses;")           
            data=list() 
            for i in cursor:
                data.append(i)
            # data=tuple(data)
            headings=tuple(i[0] for i in cursor.description)

            return render_template('table.html',headings=headings,data=data)

        else:   
            return render_template('login.html', message = "Invalid username or password")

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)