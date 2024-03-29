from flask import Flask, request,redirect

recommendations = {
"Biosphere":['Clean water and sanitation', 'Climate action', 'Life below water', 'Life on land'],
"Society":['No Poverty', 'Zero Hunger', 'Good Health and well-being', 'Quality education', 'Gender Equality', 'Affordable and clean energy', 'Sustainable cities and communities', 'Peace, justice and strong institutions'],
"Economy":['Decent work and economic growth', 'Industry, innovation and infrastructure', 'Reduced inequalities', 'Responsible consumption and production']
}
l=[]
with open("textfile.txt",'r') as f:
    l=[]
    for i in f.readlines():
        l.append(i.rstrip())

app = Flask(__name__)

@app.route('/recommend', methods=['GET', 'POST'])
def post_():
    hh = []
    na = request.values.getlist('checkbox')
    rr=[]
    for j in na:
        for i in l:
            if j in i:
                c=i.split(':')
                rr=rr+c[1]
        #rr=rr+recommendations[j]
    u = "_".join(rr)
    url = "https://smashsdgs.me/recommend.php?actions=" + u
    return redirect(url, code=302)

if __name__ == '__main__':
    app.run()
