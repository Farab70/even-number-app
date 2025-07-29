from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def even_numbers():
    n = request.args.get('n', default=10, type=int)
    evens = [str(i) for i in range(2, 2*n+1, 2)]
    return "Even numbers: " + ", ".join(evens)

if __name__ == '__main__':
    app.run()
