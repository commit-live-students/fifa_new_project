# Data Preprocessing

After loading the required data into structured format, next step is to cleanse the data for better analysis. 

## Write a function `q02_clean_data` that:

- Removes the symbol K, â‚¬, M from the column named as `Value` and `Wage`.
- Renames columns to `Value (M)` and `Wage (M)`(and subseqently transforms the unit of wages from K to M ).
- Changes their data-type to float64.
- Splits the column `Preferred Positions`, takes the first position and stores it in a new column called `Position`

Parameters :

| parameter | dtype          | Argument Type | default value | description                   |
|-----------|----------------|---------------|---------------|-------------------------------|
| variable  |pandas.DataFrame| compulsory    |               | Dataframe to be loaded        |

Returns:

| returns  | dtype            | description                                |
|----------|------------------|--------------------------------------------|
| variable | pandas.DataFrame | Dataframe with above operations inculcated |
 