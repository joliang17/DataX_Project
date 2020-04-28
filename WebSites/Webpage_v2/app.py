from flask import Flask,render_template,request
from werkzeug.datastructures import ImmutableMultiDict
import pandas as pd
import numpy as np
from sklearn.externals import joblib

app = Flask(__name__)

def dataPre(FormResult):
    name = FormResult['name']
    age = int(FormResult['age'])
    degree = FormResult['degree']
    jobField = FormResult['jobField']
    major = FormResult['major']
    hasWorked = FormResult['hasWorked']
    yrOfExp = FormResult['yrOfExp']
    skillSets = FormResult.getlist("skillSets")

    # major = findMajor(request.form['major'])
    # pass variables to Model
    Temp = []
    # ['Q1', 'Q4', 'Q10', 'Q23', 'Q16_count', 'Q18_count', 'Q24_count', 'Q28_count']
    # Age: interval 
    # TODO: What if age < 18?
    if age <= 24:
        Temp.append(0)
    elif age <= 39:
        Temp.append(1)
    elif age <= 54:
        Temp.append(2)
    else: 
        Temp.append(3)

    # Education level
    if degree == "Associate":
        Temp.append(1)
    elif degree == "Bachelor":
        Temp.append(2)
    elif degree == "Master":
        Temp.append(3)
    elif degree == "Doctoral":
        Temp.append(4)
    else: 
        Temp.append(5)

    # compensation
    # ML years
    # IDEs count
    # languages count
    # ML algorithms count
    # ML frameworks count


    Xnew = []
    Xnew.append(Temp)

    return Xnew

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
    # check if every variable is valid
    # if (error)
    try:
        # imudict = request.form
        # dict0 = imudict.to_dict(flat=False)

        # name = dict0['name'][0]
        # age = dict0['age'][0]
        # hasWorked = dict0['hasWorked'][0]
        # yrOfExp = dict0['yrOfExp'][0]
        # skillSets = dict0['skillSets'] 

        name = request.form['name']
        age = request.form['age']
        degree = request.form['degree']
        jobField = request.form['jobField']
        major = request.form['major']
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

    except:
        print(error)
        error = "Please check if there is any missing entry!"
        arrow = "<="
        return render_template('JobHunting.html', error = error, arrow = arrow)
        
    else:
        Xnew = dataPre(request.form)
        Xnew = [[3,4,3,5,1,2,4,3]]

        k_unchanged=svc_model.predict_proba(Xnew)[0]
        k=svc_model.predict_proba(Xnew)[0]
        ynew_result = svc_model.predict(Xnew)
        k.sort() 
        # Second=k[-2]
        # Third=k[-3]
        # Fourth=k[-4]
        if ynew_result==0:
            Highest = np.where(k_unchanged ==k[-2])[0]
            Sec_high =  (np.where(k_unchanged ==k[-3])[0])
            Third_high = (np.where(k_unchanged ==k[-4])[0])
            ans = [Highest[0], Sec_high[0], Third_high[0]]
            print(ans)
            
        else:
            Highest = np.where(k_unchanged ==k[-1])[0] 
            Sec_high =  (np.where(k_unchanged ==k[-2])[0])
            Third_high = (np.where(k_unchanged ==k[-3])[0])
            Four_high = (np.where(k_unchanged ==k[-4])[0])
            ans = [Highest[0], Sec_high[0], Third_high[0], Four_high[0]]
            ans.remove(0)
            print(ans[0:3])
        
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
        
        jobs = [job_dict.get(i) for i in ans]
        print(jobs)
        return render_template("Result.html", name=name, age=age, hasWorked = hasWorked,
        yrOfExp = yrOfExp, skillSets = skillSets, book_list = book_list, jobsResult = jobs) 
        #result=modelResult, )

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
    import os 
    dir_path = os.path.dirname(os.path.realpath(__file__))
    try:
        svc_model = joblib.load(os.path.join(dir_path, "svc_model.pkl"))
    except:
        print('No Model Loaded!')
    else:
        app.run(port=8000, debug=True)
        # app.run(port=8000)
