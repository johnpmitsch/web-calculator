from flask import Flask, request, render_template, url_for


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('calculator.html')

@app.route('/result.html', methods=['GET', 'POST'])
def calculate():
    num_one = request.form['num_one']
    num_two = request.form['num_two']
    operand = request.form['operand']
    try:
        result = eval(num_one + operand + num_two)
    except SyntaxError:
        return render_template('calculator.html')
    return render_template('result.html', Result=result)

if __name__ == "__main__":
    app.run(debug=True)
