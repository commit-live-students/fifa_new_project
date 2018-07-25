## DataFrame creation
You can't do any analysis without data. In this task you will convert the available data to a dataframe taking only the required columns 


Write a function `q01_read_data` that
        
       a) Returns a pandas DataFrame when given a path to a CSV file
       b) Takes only a subset of dataframe having the following columns - 'Name', 'Age',  
          'Nationality', 'Overall', 'Potential', 'Club', 'Value', 'Preferred Positions', 'Wage.


Parameters :

| parameter | dtype  | Argument Type | default value | description                   |
|-----------|--------|---------------|---------------|-------------------------------|
| path      | string | compulsory    |               | path of the csv file location |


Returns:

| returns  | dtype            | description                                |
|----------|------------------|--------------------------------------------|
| variable | pandas.DataFrame | Dataframe with above operations inculcated |
