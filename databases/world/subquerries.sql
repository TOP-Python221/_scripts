  select c.`Code` as 'code',
		 ct.`Name` as 'city'
	from country as c
	join city as ct
	  on c.`Code` = ct.`CountryCode`
	 and ct.`Population` >= 1000000;

  select c.`Code` as 'code',
		 cl.`Language` as 'lang'
	from country as c
	join countrylanguage as cl
	  on c.`Code` = cl.`CountryCode`
	 and cl.`Percentage` > 50;


  select subq1.`code`,
		 subq1.`city`,
         subq2.`lang`
    from (select c.`Code` as 'code',
				 ct.`Name` as 'city'
			from country as c
            join city as ct
              on c.`Code` = ct.`CountryCode`
			 and ct.`Population` >= 1000000) as subq1
    join (select c.`Code` as 'code',
				 cl.`Language` as 'lang'
			from country as c
            join countrylanguage as cl
              on c.`Code` = cl.`CountryCode`
			 and cl.`Percentage` > 50) as subq2
	  on subq1.`code` = subq2.`code`
