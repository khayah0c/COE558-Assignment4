
# COE558 Assignment 4 - Web Calculator

## Project Description
A web-based calculator developed using Python Flask, HTML, CSS, and JavaScript.

The application provides a REST API and a graphical user interface for performing basic arithmetic operations.

## Features
- Addition
- Subtraction
- Multiplication
- Division
- Input validation
- Division by zero error handling
- GET and POST API support

## Technologies
- Python 3
- Flask 3.1.3
- HTML, CSS, JavaScript
- Postman
- Git and GitHub

## Installation
Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application
```bash
py app.py
```

Open the application at:

http://127.0.0.1:5000/

## REST API
Endpoint: `/calculate`

Supported methods:
- GET
- POST

Example POST request:

```json
{
  "num1": 10,
  "num2": 5,
  "operation": "add"
}
```

Expected result: 15

## API Testing
The REST API was tested using Postman, including successful arithmetic operations and error-handling scenarios.
## Live Application

https://coe558-calculator.onrender.com