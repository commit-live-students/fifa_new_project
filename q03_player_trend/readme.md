# Visualization

A rich club has decided to hire you as their manager. You have all the money to build a team from scratch.

Now you have the data. Being a data scientist, you first want to check the general trend of market with respect to players and their worth 

## Write a function `q03_player_trend` that :

- Makes use of the dataframe obtained from 'q02_convert'
- Groups player by their `position` column and plots it
- Plots the wage distribution of top 100 players(according to `Wage (M)`)
- Plots a graph comparing `Overall` and `Value (M)` 


Parameters :

| parameter | dtype          | Argument Type | default value | description                   |
|-----------|----------------|---------------|---------------|-------------------------------|
| variable  |pandas.DataFrame| compulsory    |               | Dataframe to be loaded        |

Returns:

Returns nothing

The plot should look similar to

1. Player v Position:

https://github.com/commit-live-students/fifa_project_new/blob/master/images/PlayerVPosition.png

2. Wage Distribution

https://github.com/commit-live-students/fifa_project_new/blob/master/images/WageDistribution.png

3. Value v Overall
  
https://github.com/commit-live-students/fifa_project_new/blob/master/images/ValueVOverall.png

 
 
 ## After plotting, analyse the graph.
 
 
 