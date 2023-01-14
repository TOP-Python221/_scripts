  select `Name`,
		 `SurfaceArea`
    from `country`;
    
  select `Name`,
		 max(`SurfaceArea`) as 'SurfaceArea'
    from `country`;

  select `Name`,
		 `SurfaceArea`
	from `country`
  having `SurfaceArea` = (select max(`SurfaceArea`) from `country`);
