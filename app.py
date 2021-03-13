from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    io = []
    for i in range(50):
        i='ddddhello'
        io.append(i)
        print(i)

    return i

if __name__ == '__main__':
    app.run()
