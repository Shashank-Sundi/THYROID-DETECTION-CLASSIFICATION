import pickle
from Log_Writer.logger import App_Logger

def null_value_imputer(data):
    log_writer=App_Logger()
    try:
        imputer = pickle.load(open("Models/knn_imputer.pickle", 'rb'))
        data = imputer.transform(data)
        log_writer.log(log_message="Null Value Imputation Completed Successfully")
        return data
    except Exception as e:
        log_writer.log(log_message="ERROR occured in null value imputation")
        return print(e)

