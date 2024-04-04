# import numpy as np
# import pandas as pd
# from sklearn.decomposition import FactorAnalysis


# data = pd.DataFrame({
#     'молоко': np.random.rand(5),
#     'овощи': np.random.rand(5),
#     'мясо': np.random.rand(5),
#     'крупы': np.random.rand(5),
#     'фрукты': np.random.rand(5)
# })


# fa = FactorAnalysis(n_components=2)
# fa.
# fa.fit(data)



# print(fa.components_)

import pandas as pd
from statsmodels.multivariate.factor import Factor
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


df = pd.read_csv('diabetes_012_health_indicators_BRFSS2015.csv')

# вывели список переменных с помощью метода columns, которые в нем содержатся.
# print(df.columns)

# взглянем на размер датафрейма
# print(df.shape)


# Выберем необходимые колонки. Фактически, мы исключили одну единственную: независимую переменную Diabetes_012.
df_sample = df.drop("Diabetes_012", axis=1, inplace=True)
# df_sample = df_sample[['HighBP', 'HighChol', 'CholCheck', 'BMI', 'Smoker',
#        'Stroke', 'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies',
#        'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost', 'GenHlth',
#        'MentHlth', 'PhysHlth', 'DiffWalk', 'Sex', 'Age', 'Education',
#        'Income']]

# Вместо того чтобы использовать полный набор данных, можно сделать относительно маленькую выборку. 
df_sample = df.sample(1000)
# print(df_sample)

# Это те колонки, с которыми мы будем работать. Посмотрим на них повнимательнее.
# print(df_sample.describe())


# разных переменных разные шкалы это может снизить точность результатов
# факторного анализа Поэтому нам нужно привести переменные к стандартизированным значениям.
# Так как формула преобразования довольно простая, то мы можем просто вычислить её для каждой переменной.

# for col in df_sample.columns:
#     df[col] = (df[col] - df[col].mean()) / df[col].std()


df1 = pd.DataFrame(df_sample) 

scaler = StandardScaler()

df1 = scaler.fit_transform(df)

fa = Factor(df1, n_factor=3, method='pa')
res = fa.fit()
# res.get_loadings_frame(threshold=0.3)


res.plot_scree()
plt.show()
