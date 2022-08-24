from flask import Flask, render_template
app = Flask(__name__)



@app.route('/')
def home():
    return render_template("index.html", num=8,num2=8)

@app.route('/<int:num2>')
def add_int(num2):
    return render_template("index.html", num=8,num2=num2)


#I made myself turn this in without watch the solution video. I wasn't able to get the Ninja bonuses on my own
#but I will continue to build on what I learned 


# @app.route('/<int:num3>/<int:num4>')
# def add_xy(num3, num4):
#     return render_template("xy.html",num3=num3, num4=num4)






if __name__=="__main__":
    app.run(debug=True)