from flask import Flask, render_template
import os
print("RUNNING FROM:", os.getcwd())

app = Flask(__name__)

# Sample Data
data = {
    "regions": [
        {"name": "North Zone", "threat": 70},
        {"name": "South Zone", "threat": 45}
    ],
    "areas": [
        {"name": "Urban Area", "threat": 60},
        {"name": "Rural Area", "threat": 30}
    ],
    "predictions": [
        {"name": "Next 24h", "threat": 65},
        {"name": "Next 7 Days", "threat": 50}
    ]
}

@app.route("/")
def home():
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)