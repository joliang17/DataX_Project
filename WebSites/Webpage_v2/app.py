from flask import Flask,render_template,request
import pandas as pd

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
	skillSets = request.form.getlist("skillSets")
	print(request.form)
	print(name, age)

	# Read book directory csv and display it if user lack reletive skills
	book_list = list()
	if 'Python' not in skillSets:
		filename = 'Book_Directory_Python.csv'
		data_book_Python = pd.read_csv(filename, header=0)
		book_list += list(data_book_Python.values)
	if 'R' not in skillSets:
		filename = 'Book_Directory_R.csv'
		data_book_R = pd.read_csv(filename, header=0)
		book_list += list(data_book_R.values)

	# check if every variable is valid
	# if (error)


	# major = findMajor(request.form['major'])
	# pass variables to Model

	return render_template("Result.html", name=name, age=age, hasWorked = hasWorked,
	yrOfExp = yrOfExp, skillSets = skillSets, book_list = book_list) #result=modelResult, )

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