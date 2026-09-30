from flask import Flask, render_template

app = Flask(__name__)

skills = [
    ("HTML", "Web sayfası yapımı"),
    ("CSS", "Tasarım ve düzen"),
    ("Python", "Temel Python"),
    ("Jinja", "Flask ile template"),
]

projects = [
    ("İlk Web Sitem", "HTML ve CSS kullanarak yaptığım ilk site."),
    ("Not Defteri", "Basit bir not alma projesi."),
    ("Portfolio", "Kendimi tanıtmak için hazırladığım portfolio."),
]

@app.route("/")
def home():
    return render_template("index.html", skills=skills, projects=projects)

if __name__ == "__main__":
    app.run(debug=True)
