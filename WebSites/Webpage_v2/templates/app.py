from flask import Flask,render_template,request
from werkzeug.datastructures import ImmutableMultiDict
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('JobHunting.html')

@app.route('/profile/<username>')
def profile(username):
	return "Welcome %s" % username

@app.route('/submitForm', methods=['POST'])
def handleReq():
	error = None
	arrow = None

	#hasWorked = request.form['hasWorked']
	
	#try:
	name = request.form['name']
	age = request.form['age']
	degree = request.form['degree']
	salary = request.form['salary']
	major = request.form['major']
	yrOfExp = request.form['yrOfExp']
	IDE = request.form.getlist('IDE')
	launguage = request.form.getlist('launguage')
	algorithm = request.form.getlist('algorithms')
	framwork = request.form.getlist('framworks')
	skillSets = request.form.getlist("skillSets")
	print(request.form)
	print(name, age)

	# Get the input list for backend model
	inputlist = []

	# Get age range
	if int(age) in range (0, 25):
		inputlist.append(0)
	elif int(age) in range (25, 40):
		inputlist.append(1)
	elif int(age) in range (40, 55):
		inputlist.append(2) 
	elif int(age) in range (55, 120):
		inputlist.append(3)  
	else:
		pass

	# get the degree, salary, year of experience
	print(degree)
	type(degree)
	inputlist.append(int(degree))
	
	# get the salary
	
	if int(salary) in range (0, 1000):
		inputlist.append(0)
	elif int(salary) in range (1000, 40000):
		inputlist.append(1)
	elif int(salary) in range (40000, 50000):
		inputlist.append(2)
	elif int(salary) in range (50000, 60000):
		inputlist.append(3) 
	elif int(salary) in range (60000, 70000):
		inputlist.append(4) 
	elif int(salary) in range (70000, 80000):
		inputlist.append(5)
	elif int(salary) in range (80000, 90000):
		inputlist.append(6)
	elif int(salary) in range (90000, 125000):
		inputlist.append(7)
	elif int(salary) in range (125000, 150000):
		inputlist.append(8)
	elif int(salary) in range (150000, 200000):
		inputlist.append(9)
	elif int(salary) >= 200000:
		inputlist.append(10)       
	else:
		pass

	#inputlist.append(int(salary))
	inputlist.append(int(yrOfExp))

	# get the counts of multiple choice questions
	inputlist.append(len(IDE))
	inputlist.append(len(launguage))
	inputlist.append(len(algorithm))
	inputlist.append(len(framwork))


	print(inputlist)

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

	return render_template("Result.html", name=name, age=age, book_list = book_list, skillSets = skillSets) 
		#result=modelResult, hasWorked = hasWorked,
		#yrOfExp = yrOfExp, skillSets = skillSets,
	
	# except:
	# 	error = "Please check if there is any missing entry!"
	# 	arrow = "<="
	# 	return render_template('JobHunting.html', error = error, arrow = arrow)
# # Error Handling
#
# @app.errorhandler(werkzeug.exceptions.BadRequest)
# def handle_bad_request(e):
#     return 'bad request!', 400


	

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

#Webpage will atuo refresh as debug = true
if __name__ == "__main__":
    app.run(port=8000, debug=True)
