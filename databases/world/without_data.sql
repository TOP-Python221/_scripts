  select concat(`Code2`, ' (', `Code`, ')') as `Codes`, 
		 `Name`
    from `country`
order by `Codes`
