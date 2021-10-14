from Log_Writer.logger import App_Logger
from flask import Flask , request , render_template
from flask_cors import CORS , cross_origin
from Raw_Data_Formatter.data_formatter import formatter
from Data_Validator.data_validator import Validator
from Preprocessing.preprocessor import Preprocessor
from Get_Model_for_Cluster.model_finder import Find_model
import sys

app=Flask(__name__)
CORS(app)

log_writer = App_Logger()

@app.route('/',methods=['GET','POST'])
@cross_origin()
def homePage():
    log_writer.log(log_message="Rendered Home Page")
    return render_template("index.html")

@app.route('/Prediction',methods=['POST'])
@cross_origin()
def index():
    try:
        if request.method=='POST':

            # Gathering the data and converting it to dataframe
            data=formatter().format_data()

            # Validating the input data
            err=Validator().validate(data)
            if err>0:
                sys.exit()

            # Preprocessing the data
            data=Preprocessor().preprocess(data)

            # Finding the cluster to which data point belongs
            # and importing the model trained for that cluster
            data,model=Find_model().get_model(data)

            pred=model.predict(data)[0]

            if pred==0:
                statement="You suffer from Compensated/Subclinical Hyperthyroidism. \n " \
                          "Get an appointment with a doctor immediately "
            if pred==1:
                statement="You do not suffer from any form of Hyperthyroidism \n"
            if pred==2:
                statement="You suffer from Primary Hyperthyroidism. \n" \
                          " Get an appointment with a doctor immediately "
            if pred==3:
                statement="You suffer from Secondary Hyperthyroidism. \n" \
                          " Get an appointment with a doctor immediately "


            return render_template("results.html",prediction=statement)
        else:
            return render_template("index.html")
    except Exception as e:
        log_writer.log(log_message="Error Occured in index page route")
        return print(e)

if __name__=="__main__":
    app.run(debug=True,host="127.0.0.1",port=8001)
