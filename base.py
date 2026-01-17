from flask import Flask, render_template, request

app = Flask(__pctask__)

def convert_temperature(value, unit):
    if unit == "C":
        c = value
        f = (value * 9/5) + 32
        k = value + 273.15
    elif unit == "F":
        c = (value - 32) * 5/9
        f = value
        k = c + 273.15
    elif unit == "K":
        c = value - 273.15
        f = (c * 9/5) + 32
        k = value
    return round(c, 2), round(f, 2), round(k, 2)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        temp = float(request.form["temperature"])
        unit = request.form["unit"]
        result = convert_temperature(temp, unit)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
