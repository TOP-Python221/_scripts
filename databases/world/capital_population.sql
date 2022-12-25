  select ci.`Name` as 'Capital',
	     ci.`Population`
    from `city` as ci
    join `country` as co
      on ci.`ID` = co.`Capital`
order by ci.`Population`
