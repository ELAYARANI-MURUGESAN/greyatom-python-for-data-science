# --------------
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
#df=pd.DataFrame()
data=pd.read_csv(path)
loan_status=data['Loan_Status'].value_counts().plot(kind="bar")
plt.show()
data.iloc[25,1] 
data.iloc[53,9] 
property_and_loan=data.groupby(['Property_Area', 'Loan_Status']).size().unstack().plot(kind='bar', stacked=False)
plt.xlabel('Propery_Area')
plt.ylabel('Loan_Status')
plt.xticks(rotation=45)
#
education_and_loan=data.groupby(['Education', 'Loan_Status']).size().unstack().plot(kind="bar")
plt.xlabel='Education_Status'
plt.ylabel='Loan_Status'
plt.xticks(rotation=45)
#
graduate=data[data['Education'] == 'Graduate']
not_graduate=data[data['Education']=='Not Graduate']
graduate['LoanAmount'].plot(kind='density',label='Graduate')
not_graduate['LoanAmount'].plot(kind='density',label='Not Graduate')


#
fig, (ax_1, ax_2,ax_3) = plt.subplots(1,3, figsize=(10,20))
ax_1.scatter(data['ApplicantIncome'],data["LoanAmount"])
ax_1.set(title='Applicant Income')
ax_2.scatter(data['CoapplicantIncome'],data["LoanAmount"])
ax_2.set(title='Coapplicant Income')
data['TotalIncome']= data['ApplicantIncome']+ data['CoapplicantIncome']
ax_3.scatter(data['TotalIncome'],data["LoanAmount"])
ax_3.set(title='Total Income')
print(data['TotalIncome'][1])



