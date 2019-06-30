from flask import Flask,render_template
app = Flask(__name__)


@app.route('/')
def learntemplate():
    lis = ['neeraj','vinay','nikhil','ankit ','harsh']
    return render_template('t1.html',list1 = lis)



if __name__ == "__main__":
    app.run(debug=True)
