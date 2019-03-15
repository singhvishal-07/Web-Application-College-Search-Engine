from flask import *
import pandas as pd
app = Flask(__name__)
data = pd.read_excel('sharanbotnew.xlsx')
mumdata = pd.read_excel('mumbai.xlsx')
navidata= pd.read_excel('navimumbai.xlsx')
otherdata=pd.read_excel('others.xlsx')
#https://sarahleejane.github.io/learning/python/2015/08/09/simple-tables-in-webapps-using-flask-and-pandas-with-python.html
@app.route("/")
def shows():
    return render_template('home.html')
@app.route("/home")
def showhome():
    return render_template('home.html')
@app.route("/login")
def login():
    return render_template('login.html')
@app.route("/about")
def showabout():
    return render_template('about.html')
@app.route('/showmumbai')
def showmum():
    l = mumdata.values.tolist()
    return render_template('showmum.html', l=l)
@app.route('/shownavimumbai')
def shownavi():
    l = navidata.values.tolist()
    return render_template('shownavi.html', l=l)
@app.route('/showothers')
def showothers():
    l = otherdata.values.tolist()
    return render_template('showothers.html', l=l)
@app.route("/<int:id>")
def showcollege(id):
    data1=data[id:id+1]
    cname=data1["COLLEGENAME"][id]
    print(cname)
    loc=data1["LOCATION"][id]
    print(loc)
    ownership=data1["OWNERSHIP"][id]
    print(ownership)
    approved=data1["APPROVED BY"][id]
    print(approved)
    print("abc")
    fees=data1["FEES"][id]
    print(fees)
    exam=data1["EXAM ACCEPTED"][id]
    courses=data1["COURSES"][id]
    about=data1["ABOUT"][id]
    intake=data1["INTAKE"][id]
    cutOff=data1["CUT-OFF"][id]
    placement=data1["PLACEMENT"][id]
    return render_template('clgtest.html',imgg=id,name=cname,location=loc,own=ownership,app=approved,fees=fees,exam=exam,courses=courses,about=about,intake=intake,cutOff=cutOff,placement=placement)
'''@app.route("/")
def show():
    l=[[0,"A"],[1,"B"],[2,"C"]]
    return render_template('testing.html',l=l)'''
'''@app.route("/")
def show():
    return render_template('home.html')'''
'''@app.route("/")
def show():
    l=[[0,"A"],[1,"B"],[2,"C"]]
    print(l)
    return render_template('result.html')'''
#@app.route("/")
#def shows():
#    return render_template('home.html')
@app.route("/show")
def mumshow():
    l=data.values.tolist()
    print(l)
    return render_template('Untitled.html',l=l)
'''@app.route("/mumbai")
def mumshow():
    l=data.values.tolist()
    return render_template('newcard.html',l=1)'''
'''y=[]
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['hell'] == 'Do Something':
            x=request.form.getlist('hello')
            x=[y.append(x)]
            print(x)
            print(y)
        elif request.form['hell'] == 'Do Something Else':
            x=request.form.getlist('hell')
            x=[y.append(x)]
            print(y)
            q=fn(y[0],y[1],y[2],y[3],y[4],y[5])
            print(q)
            print(type(q))
            z=q.to_html()
            #getlist for list
            return render_template('filter.html',a=z)
        return render_template('filter.html')
    return render_template('filter.html')



def fn(A, B, C, D, E, F):
    c = 1
    for x in A:
        if (c == 1):
            z = data[data['LOCATION'].str.contains(x)]
            c = c + 1
        else:
            z1 = data[data['LOCATION'].str.contains(x)]
            z = pd.concat([z, z1])
    c = 1
    for x in B:
        if (c == 1):
            z1 = z[z['OWNERSHIP'].str.contains(x)]
            c = c + 1
        else:
            z2 = z[z['OWNERSHIP'].str.contains(x)]
            z1 = pd.concat([z1, z2])
    c = 1
    for x in C:
        if (c == 1):
            z2 = z1[z1['APPROVED BY'].str.contains(x)]
            c = c + 1
        else:
            z3 = z1[z1['APPROVED BY'].str.contains(x)]
            z2 = pd.concat([z2, z3])
    c = 1
    for x in D:
        if (c == 1):
            z3 = z2[z2['EXAM ACCEPTED'].str.contains(x)]
            c = c + 1
        else:
            z4 = z2[z2['EXAM ACCEPTED'].str.contains(x)]
            z3 = pd.concat([z3, z4])
    c = 1
    for x in E:
        if (c == 1):
            z4 = z3[z3['FEES'].astype(str).str[1] == x]
            c = c + 1
        else:
            z5 = z3[z3['FEES'].astype(str).str[1] == x]
            z4 = pd.concat([z4, z5])
    c = 1
    for x in F:
        if (c == 1):
            z5 = z4[z4['COURSES'].str.contains(x)]
            c = c + 1
        else:
            z6 = z3[z4['COURSES'].str.contains(x)]
            z5 = pd.concat([z5, z6])
    return z5'''
if __name__ == "__main__":
    app.run(debug=True)

