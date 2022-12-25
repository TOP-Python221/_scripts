  select `city`.`Name` as `City`,
         `country`.`Name` as `Country`
    from `city`
    join `country`
      on `city`.`CountryCode` = `country`.`Code`
	 and `country`.`Continent` = 'South America'
