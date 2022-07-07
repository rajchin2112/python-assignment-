import numpy as np 
import pandas as pd
import math
patient_id = input('Enter the Patinet id: ')
df=pd.read_csv("COVID DATA FINAL.csv", index_col=0)
# print(df.keys())
pad = df.loc[patient_id]
score=0
print("RT-PCR ====>",pad.rtpcr)
print("CT-Scan ====>",pad.ctscan)
print("SPO2 ====>",pad.spo2)
print("inhale and exhale ====>",pad.rateofinhaleandexhale)
if pad.rtpcr == "POSITIVE":
    score += 1
if pad.ctscan == '0%<10%' or pad.ctscan == '0%<25%':
    score += 3
elif pad.ctscan == '25%<50%':
    score += 2
elif pad.ctscan == '50%<75%':
    score += 1
spo2 = int((pad.spo2).split('%')[0])
if spo2 < 80:
    score += 3
elif spo2  >= 80 and spo2 < 90:
    score += 2
elif spo2  >= 90 and spo2 < 98:
    score += 1
if pad.rateofinhaleandexhale < 22:
    score += 3
elif pad.rateofinhaleandexhale >= 22 and pad.rateofinhaleandexhale < 25:
    score += 2
elif pad.rateofinhaleandexhale >= 25 and pad.rateofinhaleandexhale < 30:
    score += 1
print("Overall Score:", score//4)
score_text='' 
if score//4 == 0:
    # print("The patinet is good condition and safe")
    score_text += "good. follow the safe measure"
elif score//4 == 1:
    # print("the patinet is modrate condition")
    score_text += "having mild symptoms and do self quartine"
elif score//4 == 2:
    # print("the patinet is high condition")
    score_text += "should be admitted in hospital"
elif score//4 == 3:
    # print("the patinet is severe condition")
    score_text += "should be admitted in hospital and monitored in ICU"
print(patient_id, "is tested RT-PCR", pad.rtpcr, "and", score_text)