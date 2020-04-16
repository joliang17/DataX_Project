from flask import Flask,render_template,request

# csv = readCSV('./...csv')
# csvData

def findMajor(input):
	csvData.find(input)
	return Major

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('JobHunting.html')

@app.route('/profile/<username>')
def profile(username):
	return "Welcome %s" % username

@app.route('/submitForm', methods=['POST'])
def handleReq():
	name = request.form['name']
	age = request.form['age']
	hasWorked = request.form['hasWorked']
	yrOfExp = request.form['yrOfExp']
	# skillSets = request.form.getlist("skillSets")
	print(request.form)
	print(name, age)

	## To-do:
	
	# check if every variable is valid
	# if (error) 


	# major = findMajor(request.form['major'])
	# pass variables to Model

	return render_template("Result.html", name=name, age=age, hasWorked = hasWorked, yrOfExp = yrOfExp) #result=modelResult, )

# Get the local data passed to HTML 
@app.route('/post/<int:book_id>')
def show_post(book_id):
	return "the book id is %s" % book_id

@app.route('/Result/<int:age>', methods=['GET','POST'])
def Result(age):
	return render_template("Result.html", age=age)

    # if request.method == 'POST':
    # 	age = request.form['age']
    # 	return render_template('Result.html', age=age)

    # else:	
    # 	return render_template('JobHunting.html')

if __name__ == "__main__":
    app.run(port=8000)
