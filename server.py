from flask import Flask, render_template
app = Flask(__name__)


# --------------- Level 1----------------------------------
@app.route('/play')
def  play(x=3):
    return render_template('index3.html', phrase ="I will print out these 3 boxes for you based on your provided count",x=int(x)) 


# --------------- Level 2----------------------------------
@app.route('/play/<x>')
def  count(x):
    return render_template('index3.html', phrase ="I will print out these boxes for you based on your provided count", x=int(x)) 


# --------------- Level 3----------------------------------
@app.route('/play/<x>/<color>')
def  color(x, color):
    return render_template('index3.html', phrase ="I will print out these boxes for you based on your provided count AND color", x=int(x), color=str(color)) 
    








## Do not touch - always needed
if __name__ =="__main__":
	app.run(debug=True)