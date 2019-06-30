from flask import Flask,render_template
app = Flask(__name__)


@app.route('/<name>/<sender>')
def learntemplate(name,sender):
    dic = {'name1':name,'sender1':sender}
    return render_template('t1.html',dic = dic)



if __name__ == "__main__":
    app.run(debug=True)
