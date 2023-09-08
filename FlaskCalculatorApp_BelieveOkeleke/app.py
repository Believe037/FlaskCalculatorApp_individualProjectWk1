from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)



@app.route("/")
def home():
  return render_template("index.html")

@app.route("/result", methods=['POST'])
def result():
    num1 = request.form['num1']
    num2 =request.form['num2']

    num1 = float(num1)
    num2 = float(num2)
    result = 0
    operation = request.form['operation']
    if operation == 'add':
      result = num1 + num2
      content = 'sum'
    elif operation == 'subtract':
      result = num1 - num2
      content = 'difference'
    elif operation == 'multiply':
      result = num1 * num2
      content = 'product'
    elif operation == 'divide':
      content = 'quotient'
      if num2 != 0:
        result = num1 / num2
      else:
        result = "Error: Division by zero"
    return render_template('result.html', result=result, content=content)
   


    
    
 
  

if __name__ == "__main__":
  app.run(debug=True)