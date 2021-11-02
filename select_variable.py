import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import statsmodels.api as sm
data = pd.read_csv('NewData.csv')
y = data['LifetimeValue']
x_columns = ['Age','Gender_dummy','EnrollmentDuration','DaysWithoutFrequency','AverageFrequency','UseByTime','AthleticsActivities','WaterActivities','FitnessActivities','DanceActivities','TeamActivities','RacketActivities','CombatActivities','NatureActivities','SpecialActivities','OtherActivities','NumberOfActivities','NumberOfFrequencies','AttendedClasses','AllowedWeeklyVisitsBySLA','AllowedNumberOfVisitsBySLA','RealNumberOfVisits','Ratio','NumberOfRenewals','HasReferences','NumberOfReferences','Dropout']
data[x_columns]
def get_stats():
    x = data[x_columns]
    results = sm.OLS(y, x).fit()
    print(results.summary())
get_stats()

# find that NumberOfRenewals has the highest p-value<0.05, so drop it
x_columns.remove('CombatActivities')
x_columns.remove('NatureActivities')
x_columns.remove('OtherActivities')
x_columns.remove('NumberOfRenewals')
get_stats()