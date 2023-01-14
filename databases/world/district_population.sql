  select `country`.`Code`,
		 `city`.`District`,
         sum(`city`.`Population`) as 'District population'
    from `city`
    join `country`
      on `city`.`CountryCode` = `country`.`Code`
group by `country`.`Code`, `city`.`District`
order by `country`.`Code`, `city`.`District`
