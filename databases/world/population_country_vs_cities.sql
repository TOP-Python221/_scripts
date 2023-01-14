  select `country`.`Name` as 'Country',
		 `country`.`Population` as 'Country population',
         sum(`city`.`Population`) as 'Cities population'
    from `city`
    join `country`
      on `city`.`CountryCode` = `country`.`Code`
group by `country`.`Name`
