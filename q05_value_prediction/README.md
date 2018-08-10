# Player Transfer

With your invincible team, you have won the club cup. It's time for the summer market transfer. The club owner has asked you   to buy a future prospect named 'Alex Rodriguez'.

You are confused as to what value you should buy the player for. Thankfully your data science skills will help

# Write a function `q05_value_prediction` that:
- Takes the dataset created from `q02_clean_data`
- Splits the data into train and test(70/30)
- Fits the linear regression model with independent variables as `Overall`, `Potential` ,`Wage (M)` and dependent variable as `Value (M)` and predicts the dependent variable with help of independent variable on train set
- Predicts the `Value (M)` of test set and calculates MAE, RMSE and R^2 Score
- Returns MAE, RMSE, R^2 score

Parameters :

| parameter | dtype          | Argument Type | default value | description                   |
|-----------|----------------|---------------|---------------|-------------------------------|
| variable  |pandas.DataFrame | compulsory    |               | Dataframe to be loaded        |



Returns:

| returns  | dtype            | description                                |
|----------|------------------|--------------------------------------------|
| variable | Float | MAE Score|
| variable | Float | RMSE Score|
| variable | Float | R^2 Score|
 
