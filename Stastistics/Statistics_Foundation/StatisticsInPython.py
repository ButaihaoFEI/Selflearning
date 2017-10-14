#Pandas Data frame
import pandas as pd
import numpy as np
from scipy import stats

data = pd.read_csv('brain_size.csv',sep=';',na_values='.')

#Return spaced numbers over a specified interval - np.linspace(start,stop,interval)
t=np.linspace(-6,6,20)
#sin(x) - np.sin(x)
sin_t = np.sin(t)
cos_t = np.cos(t)

#return the pd.df with specified format
pdFormat = pd.DataFrame({'t':t, 'sin':sin_t, 'cos':cos_t})

#Attributs and methodes of dataframe
pdFormat.shape
pdFormat.columns
#read specified columns
pdFormat['cos']
#select specified values; use two level structure of dataframe
pdFormat[pdFormat['cos']>0]
#describe() is a methode
pdFormat.describe()
#value_counts() very useful methode which can view the distribution of the different value (specially text variables)
pdFormat['Gender'].value_counts()


#groupby 
#turn the data frame to a special groupby dataframe which isn't visable
#but it's useful when we should seperate the value of a specified variable,like 'Gender' in this case
groupby_gender = data.groupby('Gender')
for gender, value in groupby_gender['VIQ']:
    print((gender, value.mean()))

groupby_gender.mean()
groupby_gender.boxplot()


#Student's test
#We make a hypothesis that mean is 90,looking for p value to judge whether accept or reject
#p value > signifiance level -> to accept this hypothesis
#otherwise to reject
#one-sample 
stats.ttest_1samp(data['VIQ'],90)
#check packages
import sys
'scipy' in sys.modules
#two-samples
#we want to test whether these samples have the same statistical properties
female_viq = data[data['Gender'] == 'Female']['VIQ']
male_viq = data[data['Gender'] == 'Male']['VIQ']
stats.ttest_ind(female_viq, male_viq)

#Paired Test
#compare the two samples whether have signifiant difference
stats.ttest_rel(data['FSIQ'], data['PIQ'])

