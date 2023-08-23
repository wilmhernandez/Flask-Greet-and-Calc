from flask import Flask, request
from operations import *

app = Flask(__name__)


@app.route("/add")
def perform_add():
    """Add a and b"""
    
    a = request.args.get("a")
    b = request.args.get("b")
    answer = add(a,b)
    return answer


@app.route("/sub")
def perform_sub():
    """Subtract a and b"""
    
    a = request.args.get("a")
    b = request.args.get("b")
    answer = sub(a,b)
    return answer


    
@app.route("/mult")
def perform_sub():
    """"Multipy a and b"""
    
    a = request.args.get("a")
    b = request.args.get("b")
    answer = mult(a,b)
    return answer    



@app.route("/div")
def perform_sub():
    """Divide a and b"""
    
    a = request.args.get("a")
    b = request.args.get("b")
    answer = div(a,b)
    return answer    

OPERATIONS = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route("/math/<operator>")
def do_operation(operator):
    """Do operation with a and b"""
    
    a = request.args.get("a")
    b = request.args.get("b")
    answer = OPERATIONS[operator](a, b)
    
    return answer