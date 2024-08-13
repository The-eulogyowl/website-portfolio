from flask import Flask, render_template, jsonify

app=Flask(__name__)

Projects=[
  {
    'id':1,
    'title':'Project 1',
    'description':'This is a project 1',
    'finish date':'2-9-2024'
  },
  {
    'id':2,
    'title':'Project 2',
    'description':'This is a project 1',
    'finish date':'2-9-2024'
  },
  {
    'id':3,
    'title':'Project 3',
    'description':'This is a project 1',
    'finish date':'2-9-2024'
  },
  {
    'id':4,
    'title':'Project 4',
    'description':'This is a project 1',
  }
]

@app.route("/")
def Hello_world():
  return render_template('home.html',projects=Projects)


@app.route("/api/projects")
def list_projects():
  return jsonify(Projects)
if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)