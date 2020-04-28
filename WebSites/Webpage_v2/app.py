from flask import Flask,render_template,request
from werkzeug.datastructures import ImmutableMultiDict
import pandas as pd
import numpy as np
# from sklearn.externals import joblib
import os 
from joblib import load

app = Flask(__name__)

def Jobs_Predict(inputlist):
	temp = []
	temp.append(inputlist)
	inputlist = temp

	# Predict job titles

	# inputlist = np.array(inputlist)
	# inputlist = [[1,2,2,3,1,2,2,3]]

	k1_unchanged = svc_jobs.predict_proba(inputlist)[0]
	k1 = svc_jobs.predict_proba(inputlist)[0]

	ynew_result1 = svc_jobs.predict(inputlist)
	k1.sort() 
	# print(k1_unchanged)
	# print(k1)
	# print(ynew_result1)
	# Second=k1[-2]
	# Third=k1[-3]
	# Fourth=k1[-4]

	if ynew_result1 == 0:
		Highest = np.where(k1_unchanged == k1[-2])[0]
		Sec_high =  (np.where(k1_unchanged == k1[-3])[0])
		Third_high = (np.where(k1_unchanged == k1[-4])[0])
		ans1 = [Highest[0], Sec_high[0], Third_high[0]]
		print(ans1)
		
	else:
		Highest = np.where(k1_unchanged == k1[-1])[0] 
		Sec_high =  (np.where(k1_unchanged == k1[-2])[0])
		Third_high = (np.where(k1_unchanged == k1[-3])[0])
		Four_high = (np.where(k1_unchanged == k1[-4])[0])
		ans1 = [Highest[0], Sec_high[0], Third_high[0], Four_high[0]]
		if 0 in ans1: ans1.remove(0)
		print(ans1[0:3])

	job_dict = {0: "Student", 
				1: "Data Scientist",
				2: "Software Engineer",
				3: "Data Analyst",
				4: "Data Engineer",
				5: "Statistician",
				6: "DBA/Database Engineer",
				7: "Research Scientist",
				8: "Product/Project Manager",
				9: "Business Analyst"}

	jobsResult = [job_dict.get(i) for i in ans1]
	print(jobsResult)
	return ans1, jobsResult

def Salary_Predict(ans1):
	salary_input = ans1
	ans2 = []
	for x in salary_input:
		salary_model_input = [[0,0,x,0,0,0,0,0]] 
		k_unchanged=svc_salary.predict_proba(salary_model_input)[0]
		k=svc_salary.predict_proba(salary_model_input)[0]
		ynew_result = svc_salary.predict(salary_model_input)
		#print(k_unchanged)
		k.sort() 
		#print(k)

		if ynew_result == 0:
			Highest = np.where(k_unchanged == k[-2])[0]
			print(Highest)
			ans2.append(Highest[0])
		else:
			Highest = np.where(k_unchanged == k[-1])[0] 
			print(Highest)
			ans2.append(Highest[0])
	
	salary_dict = {0: "0-49,999",  
					1: "50,000-59,999",  
					2: "60,000-69,999",  
					3: "70,000-79,999",  
					4: "80,000-89,999",  
					5: "90,000-99,999",  
					6: "100,000-124,999",  
					7: "125,000-149,999",  
					8: "150,000-199,999",  
					9: "200,000+"}

	SalaryResult = [salary_dict.get(i) for i in ans2]
	print(SalaryResult)
	return ans2, SalaryResult

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

	skillSets += ['SQL', 'Java', 'Julia', 'Scala', 'MATLAB', 'C', 'C++']

	# Read book directory csv and display it if user lack reletive skills	
	book_list = list()
	Skill_List = ['R', 'Python', 'HTML', 'CSS', 'SQL', 'Java', 'Julia', 'Scala', 'MATLAB', 'C', 'C++']

	Missing_Skill = [item for item in Skill_List if item not in skillSets]

	for skill in Missing_Skill:
		filename = r'Data/BookInformation_' + skill + '.csv'
		data_book = pd.read_csv(os.path.join(dir_path, filename), header=0)
		del data_book['Unnamed: 0']
		data_book['Skill'] = skill
		data_book = data_book[['Skill', 'BookName', 'Href']]
		book_list += list(data_book.values)[:3]
    		

	# if 'Python' not in skillSets:
		# filename = r'Data\Book_Directory_Python.csv'
		# data_book_Python = pd.read_csv(os.path.join(dir_path, filename), header=0)
		# book_list += list(data_book_Python.values)
	# if 'R' not in skillSets:
		# filename = r'Data\Book_Directory_R.csv'
		# data_book_R = pd.read_csv(os.path.join(dir_path, filename), header=0)
		# book_list += list(data_book_R.values)

	# check if every variable is valid
	# if (error)


	# pass variables to Model
	ans1, jobsResult = Jobs_Predict(inputlist)
	# Pridict salary
	ans2, SalaryResult = Salary_Predict(ans1)

	filename = r'Data/JobInformation.csv'
	data_job = pd.read_csv(os.path.join(dir_path, filename), header=0)
	del data_job['Unnamed: 0']
	
	AllResult = []
	for i, job in enumerate(jobsResult):
		PreSalary = SalaryResult[i]

		jobInfo = data_job[data_job['Job_Title'] == job][['Job_Title', 'Salary', 'Skills', 'Href']]

		# AvgSalary = jobInfo['Salary'].values[0][1:]
		jobSkills = ', '.join(list(jobInfo['Skills'].values))

		AllResult.append([job, PreSalary, jobSkills])

	return render_template("Result.html", name=name, age=age, book_list = book_list, skillSets = skillSets, jobsResult = AllResult) 

	#result=modelResult, hasWorked = hasWorked, 
	# #yrOfExp = yrOfExp, skillSets = skillSets,
	
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
	dir_path = os.path.dirname(os.path.realpath(__file__))
	try:
		svc_jobs = load(os.path.join(dir_path, r"Model/svc_jobs.pkl"))
		svc_salary = load(os.path.join(dir_path, r"Model/svc_salary.pkl"))
	except Exception as e:
		print(str(e))
		print('No Model Loaded!')
	else:
		app.run(port=8000, debug=True)
		# app.run(port=8000)
