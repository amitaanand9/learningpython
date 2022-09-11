import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

data_filepath = '/Users/amitaanand/PythonStuff/data/Diamonds Prices2022.csv'
diamond_data = pd.read_csv(data_filepath)

diamond_data = diamond_data.drop(['Unnamed: 0'],axis=1)

encoder = LabelEncoder()
diamond_data['cut'] = encoder.fit_transform(diamond_data['cut'])
diamond_data['clarity'] = encoder.fit_transform(diamond_data['clarity'])
diamond_data['color'] = encoder.fit_transform(diamond_data['color'])

print(diamond_data.head())

y = diamond_data.price

features = ['carat',  'x', 'y', 'z', 'cut', 'clarity', 'color']
X = diamond_data[features]

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)


forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)

predict = forest_model.predict(val_X)
print(mean_absolute_error(val_y, predict))