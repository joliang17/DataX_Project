from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def index():
   return render_template('JobHunting.html')

# @app.route("/results")
# def results():
#    return render_template('ResultPage.html')



if __name__ == "__main__":
   app.run(host="0.0.0.0", debug=True)
