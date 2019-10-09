from flask import Flask, request, json

recommendations = {
"Biosphere":['Clean water and sanitation', 'Climate action', 'Life below water', 'Life on land'],
"Society":['No Poverty', 'Zero Hunger', 'Good Health and well-being', 'Quality education', 'Gender Equality', 'Affordable and clean energy', 'Sustainable cities and communities', 'Peace, justice and strong institutions'],
"Economy":['Decent work and economic growth', 'Industry, innovation and infrastructure', 'Reduced inequalities', 'Responsible consumption and production']
}

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()
