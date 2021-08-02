from flask import Flask, render_template, redirect,flash, url_for, request
import psycopg2 
import psycopg2.extras

app = Flask(__name__)

app.secret_key = "skillchen-secretkey"
DB_HOST="localhost"
DB_NAME="sampledb"
DB_PORT="5433"
DB_USER="postgres"
DB_PASS="dba"
conn = psycopg2.connect(dbname=DB_NAME,user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)


@app.route("/")
def home():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("select * from students2")
    rows = cursor.fetchall()    
    return render_template('index.html', students=rows)

@app.route("/delete", methods=["GET","POST"])
def delete():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        #test = request.form.getlist('mycheckbox')
        for getid in request.form.getlist('mycheckbox'):
            print(getid)
            cur.execute('DELETE FROM students2 where id={0}'.format(getid))
            conn.commit()
        flash('Student Removed Successfully')
        return redirect("/")
        

if __name__ == '__main__':
    app.run(debug=True)