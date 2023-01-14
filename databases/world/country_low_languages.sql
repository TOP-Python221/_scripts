  select c.`Name`,
         sum(cl.`Percentage`) as 'All languages'
    from `country` as c
    join `countrylanguage` as cl
      on c.`Code` = cl.`CountryCode`
group by c.`Code`
  having sum(cl.`Percentage`) between 1 and 95 
order by sum(cl.`Percentage`)
