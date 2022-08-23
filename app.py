from flask import Flask, render_template 

app = Flask(__name__)

JOBS = [
  {
     'id':1,
    'title' : 'Data Analyst',
    'location': 'Accra, Ghana',
    'salary' : '₵100,000'
  },
  {
     'id':2,
    'title' : 'Data Scientist',
    'location': 'Kumasi, Ghana',
    'salary' : '₵150,000'
  },
  {
     'id':3,
    'title' : 'Frontend Enginer',
    'location': 'Cape Coast, Ghana',
    'salary' : '₵120,000'
  },
  {
     'id':4,
    'title' : 'Backend Enginer',
    'location': 'Tema, Ghana',
    'salary' : '₵500,000'
  },
]

@app.route("/")
def hello_world():
    return render_template('home.html', 
                           jobs=JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)