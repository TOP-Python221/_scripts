  select co.`Name`,
		 ci.`Name` as 'City',
		 co.`HeadOfState`
    from `country` as co
    join `city` as ci
      on co.`Capital` = ci.`ID`
