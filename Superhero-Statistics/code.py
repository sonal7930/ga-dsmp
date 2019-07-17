# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)
#Code starts here 
data["Gender"].replace("-","Agender",inplace = True)

gender_count = data["Gender"].value_counts()
gender_count.plot.bar()


# --------------
#Code starts here
alignment = data["Alignment"].value_counts()
alignment.plot.pie(title='Character Alignment')


# --------------
#Code starts here
sc_df = data[["Strength","Combat"]]
sc_covariance = round(sc_df["Strength"].cov(sc_df["Combat"]),2)
sc_strength = sc_df["Strength"].std()
sc_combat = sc_df["Combat"].std()
sc_pearson = round(sc_covariance/(sc_strength * sc_combat),2)
print(sc_pearson)


ic_df = data[["Intelligence","Combat"]]
ic_covariance = round(ic_df["Intelligence"].cov(ic_df["Combat"]),2)
ic_intelligence = ic_df["Intelligence"].std()
ic_combat = ic_df["Combat"].std()
ic_pearson = round(ic_covariance/(ic_intelligence * ic_combat),2)
print(ic_pearson)


# --------------
#Code starts here

total_high = data["Total"].quantile(0.99) 

super_best = data[data["Total"] > total_high]

super_best_names = list(super_best["Name"])
print(super_best_names)


# --------------
#Code starts here

fig, (ax_1, ax_2,ax_3) = plt.subplots(1,3, figsize=(20,8))

#Plotting box plot
ax_1.boxplot(super_best['Intelligence'])

#Setting the subplot axis title
ax_1.set(title='Intelligence')


#Plotting box plot
ax_2.boxplot(super_best['Speed'])

#Setting the subplot axis title
ax_2.set(title='Speed')


#Plotting box plot
ax_3.boxplot(super_best['Power'])

#Setting the subplot axis title
ax_3.set(title='Power')

#Code ends here   


