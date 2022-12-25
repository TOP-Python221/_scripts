  select c.`Name`
    from `country` as c
    join `countrylanguage` as cl
      on cl.`CountryCode` = c.`Code`
	 and cl.`Language` = 'russian'
order by cl.`Percentage` desc
