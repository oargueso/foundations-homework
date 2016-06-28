The main issue I have encountered in the database is the fact some of the accidents (mainly, the ones having taken place in North America) had an empty cell in the Region column, which flaws the analysis.

I have tried to overcome this limitation by creating a sub-dataframe for North America only, where I replaced the empty values by 'NA'. However, two accidents that occurred in Western Europe had also no value in the Region column. I therefore excluded this two cases manually. 
