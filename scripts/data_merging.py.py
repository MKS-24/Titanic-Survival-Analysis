import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

                                    # Merging Data 
                                    
d1 = pd.read_csv('D:/Data Analyst/Internship_Data/titanic/train.csv')
d2 = pd.read_csv('D:/Data Analyst/Internship_Data/titanic/test.csv')
d3 = pd.read_csv('D:/Data Analyst/Internship_Data/titanic/gender_submission.csv')
concate_data = pd.merge(d2,d3 , on='PassengerId' , how='outer')
df = pd.concat([d1,concate_data], axis=0)
df.to_csv('titanic.csv', index=False)

