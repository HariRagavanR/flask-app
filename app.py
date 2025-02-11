from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    name = {"name" : "Hello, This is Hari!"}
    print(name)
    op = input("Enter the name: ")
    print(op.upper())
home()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
