from flask import Flask, render_template
from flask.templating import render_template_string

app=Flask(__name__)

posts=[{
    "date":"14/02/2021",
    "author":"iMampi",
    "post":"C'est la St-Valentin"
    },
    {"date":"18/02/2021",
    "author":"iMampi",
    "post":"j'ai cru mourrir"
    }
]


@app.route("/")
@app.route("/home/")
def home():
    return render_template('home.html')

@app.route("/about/")
def about():
    return render_template("about.html")

if __name__=='__main__':
    app.run(debug=True)