from Log_Writer.logger import App_Logger
from flask import request
import numpy as np

def aggregate_data():
    log_writer=App_Logger()
    try:
        if request.form['Age'] == "":
            age = np.nan
        else:
            age = float(request.form['Age'])

        sex = int(request.form['Sex'])
        on_thyroxine = int(request.form['on_thyroxine'])
        query_on_thyroxine = int(request.form['query_on_thyroxine'])
        on_antithyroid_medication = int(request.form['on_antithyroid_medication'])
        sick = int(request.form['sick'])
        pregnant = int(request.form['pregnant'])
        thyroid_surgery = int(request.form['thyroid_surgery'])
        I131_treatment = int(request.form['I131_treatment'])
        query_hypothyroid = int(request.form['query_hypothyroid'])
        query_hyperthyroid = int(request.form['query_hyperthyroid'])
        lithium = int(request.form['lithium'])
        goitre = int(request.form['goitre'])
        tumor = int(request.form['tumor'])
        hypopituitary = int(request.form['hypopituitary'])
        psych = int(request.form['psych'])

        if request.form['TSH'] == "":
            TSH = np.nan
        else:
            TSH = float(request.form['TSH'])

        if TSH == np.nan:
            TSH_nan = 1
        else:
            TSH_nan = 0

        if request.form['T3'] == "":
            T3 = np.nan
        else:
            T3 = float(request.form['T3'])

        if T3 == np.nan:
            T3_nan = 1
        else:
            T3_nan = 0

        if request.form['TT4'] == "":
            TT4 = np.nan
        else:
            TT4 = float(request.form['TT4'])

        if TT4 == np.nan:
            TT4_nan = 1
        else:
            TT4_nan = 0

        if request.form['T4U'] == "":
            T4U = np.nan
        else:
            T4U = float(request.form['T4U'])

        if request.form['FTI'] == "":
            FTI = np.nan
        else:
            FTI = float(request.form['FTI'])

        if FTI == np.nan:
            FTI_nan = 1
        else:
            FTI_nan = 0

        if request.form['referral_source'] == "":
            referral_source = np.nan
        else:
            referral_source = int(request.form['referral_source'])

        log_writer.log(log_message="Collected inputs from HTML form")

        data = [[age, sex, on_thyroxine, query_on_thyroxine,
                 on_antithyroid_medication, sick, pregnant, thyroid_surgery,
                 I131_treatment, query_hypothyroid, query_hyperthyroid, lithium,
                 goitre, tumor, hypopituitary, psych, TSH, TSH_nan, T3,
                 T3_nan, TT4, TT4_nan, T4U, FTI, FTI_nan, referral_source]]

        log_writer.log(log_message="Aggregated data inputs from HTML form")
        return data

    except Exception as e:
        log_writer.log(log_message="ERROR occured in Data Collection and Aggregation")
        return print(e)
