# Introducing Polynomial function to linear regression

There are numerous ways to improve a model. One being implementation of Polynomial Function.

http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html


## Write a function `q08_polynomial` that:
- Takes the dataset created from `q02_clean_data`
- Splits the data into train and test(70/30)
- Fit transforms the data using function `PolynomialFeatures` with degree as 3.
- Fits the linear regression model with independent variables as `Overall`, `Potential` ,`Wage (M)` and dependent variable as `Value (M)` and predicts the dependent variable with help of independent variable on train set
- Predicts the `Value (M)` of test set and calculates MAE, RMSE and R^2 Score
- Returns MAE, RMSE, R^2 score, Linear model


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


#Question to ponder upon
Has the model improved? 
Why?



#Bonus Question:
Using the current model try to predict the value of the new prospect 'Alex Rodriguez'. Details given in the notebook