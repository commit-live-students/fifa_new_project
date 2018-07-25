# Finding Best Squad
You have analysed the market and decided that the market is fair with respect to players and their worth. Your club has asked you to buy best players of their respective playing position. Based on your tactical football mind, you have two gameplay position list,
1. 4-3-3
https://7500toholte.sbnation.com/2015/5/8/8566029/football-tactics-basics-the-4-3-3-formation-explained
2. 3-5-2
https://7500toholte.sbnation.com/2015/7/14/8933799/football-tactics-basics-the-3-5-2-formation-explained


## Write a function `q04_get_best_squad` that:
- Takes in the lists of positions for which the best squad has to be found out.
- Takes the dataframe created from function `q02_clean_data`.
- Iterates over positions and finds out maximum value of the column `Overall` along with its `Position` and name of the player and stores it in a dataframe.
- Compares the avg. `Overall` value of both dataframes and returns the one with the better average along with it's playing position list


Parameters :

| parameter | dtype          | Argument Type | default value | description                   |
|-----------|----------------|---------------|---------------|-------------------------------|
| variable  |pandas.DataFrame | compulsory    |               | Dataframe to be loaded        |
| variable  |List | compulsory    |               | List of football playing positions        |
| variable  |List | compulsory    |               | List of football playing positions        |



Returns:

| returns  | dtype            | description                                |
|----------|------------------|--------------------------------------------|
| variable | pandas.DataFrame | Dataframe of the team having better Overall avg.|
| variable | list | List of the football playing position associated with the returned dataframe|
 