
from flask import Flask, request, json

recommendations = {
"Biosphere":['Clean water and sanitation', 'Climate action', 'Life below water', 'Life on land'],
"Society":['No Poverty', 'Zero Hunger', 'Good Health and well-being', 'Quality education', 'Gender Equality', 'Affordable and clean energy', 'Sustainable cities and communities', 'Peace, justice and strong institutions'],
"Economy":['Decent work and economic growth', 'Industry, innovation and infrastructure', 'Reduced inequalities', 'Responsible consumption and production']
}


api = Flask(__name__)

@api.route('/recommend', methods=['GET'])
def get_():
    return json.dumps(recommendations)

@api.route('/recommend', methods=['POST'])
def post_():
    rr=[]
    json_data = request.get_json(force=True)
    i=json_data['interest']
    for j in i:
        rr=rr+recommendations[j]
    return json.dumps({'status': 'success', 'recommendations': rr}), 201


if __name__ == '__main__':
    api.run()
