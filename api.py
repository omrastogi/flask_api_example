from flask import Flask, jsonify
app = Flask(__name__)
# on the terminal type: curl http://127.0.0.1:5000/
@app.route('/')
def home():
        data = "hello world"
        print(f"\n\n{data}\n\n")
        return jsonify({'data': data})


@app.route('/home/<int:num>')
def disp(num):
    return jsonify({'data': num ** 2})


# driver function
if __name__ == '__main__':
    app.run(host="0.0.0.0")
