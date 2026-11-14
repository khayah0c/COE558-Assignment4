
from flask import Flask, request, jsonify, render_template
import math

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["GET", "POST"])
def calculate():

    # Step 1: Parse the HTTP request
    if request.method == "GET":
        data = request.args.to_dict()
    else:
        data = request.get_json(silent=True)

    # Step 2: Validate the request data
    if not isinstance(data, dict):
        return jsonify({
            "error": "Invalid JSON request body"
        }), 400

    try:
        num1 = float(data["num1"])
        num2 = float(data["num2"])
        operation = data["operation"]

        if not isinstance(operation, str):
            raise ValueError("Invalid operation")

        if not math.isfinite(num1) or not math.isfinite(num2):
            raise ValueError("Numbers must be finite")

    except (KeyError, ValueError, TypeError, OverflowError):
        return jsonify({
            "error": "Invalid numbers or operation"
        }), 400

    # Step 3: Perform the arithmetic operation
    if operation == "add":
        result = num1 + num2

    elif operation == "subtract":
        result = num1 - num2

    elif operation == "multiply":
        result = num1 * num2

    elif operation == "divide":
        if num2 == 0:
            return jsonify({
                "error": "Division by zero is not allowed"
            }), 400
        result = num1 / num2

    else:
        return jsonify({
            "error": "Unsupported arithmetic operation"
        }), 400

    if not math.isfinite(result):
        return jsonify({
            "error": "Arithmetic result is out of range"
        }), 400

    # Step 4: Return the JSON response
    return jsonify({
        "num1": num1,
        "num2": num2,
        "operation": operation,
        "result": result
    }), 200


@app.errorhandler(405)
def method_not_allowed(error):
    response = jsonify({
        "error": "HTTP method not allowed"
    })
    response.headers["Allow"] = "GET, POST, HEAD, OPTIONS"
    return response, 405


if __name__ == "__main__":
    app.run(debug=True, port=5000)
