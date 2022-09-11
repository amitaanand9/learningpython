import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

train_data_filepath = '/Users/amitaanand/PythonStuff/data/train.csv'
train_data = pd.read_csv(train_data_filepath)
print(train_data.head())

encoder = LabelEncoder()
train_data['ExterQual'] = encoder.fit_transform(train_data['ExterQual'])
train_data['ExterCond'] = encoder.fit_transform(train_data['ExterCond'])





test_data_filepath = '/Users/amitaanand/PythonStuff/data/test.csv'
test_data = pd.read_csv(test_data_filepath)

y = train_data.SalePrice

features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 
'TotRmsAbvGrd', 'Fireplaces', 'OverallQual', 'OverallCond', 'BsmtFinSF1', 'GrLivArea', 
'KitchenAbvGr', 'GarageCars', 'WoodDeckSF', 'ExterQual', 'ExterCond' ]
X = train_data[features]

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)


forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)

iowa_predict = forest_model.predict(val_X)
print(mean_absolute_error(val_y, iowa_predict))



