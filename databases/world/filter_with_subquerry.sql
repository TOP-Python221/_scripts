  select c.`Name` as 'name',
		 min(cl.`Percentage`) as 'min_perc'
	from country as c
	join countrylanguage as cl
	  on c.`Code` = cl.`CountryCode`
	 and cl.`Percentage` > 0
group by c.`Name`;


  select c.`Name`,
		 cl.`Language`,
         cl.`Percentage`
    from country as c
    join countrylanguage as cl
      on c.`Code` = cl.`CountryCode`
	 and cl.`Percentage` > 0
	join (select c.`Name` as 'name',
			     min(cl.`Percentage`) as 'min_perc'
		    from country as c
		    join countrylanguage as cl
			  on c.`Code` = cl.`CountryCode`
		     and cl.`Percentage` > 0
	    group by c.`Name`) as subq
	  on c.`Name` = subq.`Name`
	 and cl.`Percentage` = subq.`min_perc`
order by c.`Name`, cl.`Percentage`;
