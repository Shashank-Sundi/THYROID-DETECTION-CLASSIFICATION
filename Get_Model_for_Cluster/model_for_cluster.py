import pickle
from Log_Writer.logger import App_Logger

def model_for_cluster(cluster):
    log_writer = App_Logger()
    try:
        rf_c1 = pickle.load(open("Models/rf_c1.pickle",'rb'))
        xgb_c2 = pickle.load(open("Models/xgb_c2.pickle",'rb'))
        logreg_c3 = pickle.load(open("Models/logreg_c3.pickle",'rb'))
        logreg_c4 = pickle.load(open("Models/logreg_c4.pickle",'rb'))

        if cluster == 0:
            log_writer.log(log_message="cluster : 1 -- Model for data pt.-->Random Forest ")
            return rf_c1
        if cluster == 1:
            log_writer.log(log_message="cluster : 2 -- Model for data pt.-->XGBoost ")
            return xgb_c2
        if cluster == 2:
            log_writer.log(log_message="cluster : 3 -- Model for data pt.-->Logistic Regression ")
            return logreg_c3
        if cluster == 3:
            log_writer.log(log_message="cluster : 4 -- Model for data pt.-->Logistic Regression ")
            return logreg_c4

    except Exception as e:
        log_writer.log(log_message="Error occured while loading model for the particular cluster")
        return print(e)