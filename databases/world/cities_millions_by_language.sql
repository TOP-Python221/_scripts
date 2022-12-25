  select ci.`Name`
    from `city` as ci
    join `country` as co
      on ci.`CountryCode` = co.`Code`
	 and ci.`Population` > 1000000
	join `countrylanguage` as cl
      on co.`Code` = cl.`CountryCode`
	 and cl.`Language` = 'russian'
     and cl.`Percentage` >= 10
order by co.`Name`, ci.`Name`
