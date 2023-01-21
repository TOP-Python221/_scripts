insert into `artists`
	(`name`)
values
	('Эпидемия'),
	('Наталия Баева'),
	('Андрей Климковский');

insert into `genres`
	(`name`)
values
	('symphonic metal'),
	('power metal'),
	('opera'),
	('romance'),
	('ambient'),
	('space ambient');

insert into `countries`
	(`name`)
values
	('Россия'),
	('USA');

insert into `labels`
	(`name`, `country_id`, `office_address`)
values
	('Moroz Records', 1, '103062, Москва Город, улица Макаренко, 5/16, стр.1'),
	('Уральская Государственная Консерватория имени М.П. Мусоргского', 1, '620014, Свердловская область, город Екатеринбург, пр-кт Ленина, д.26'),
	('Neane Records', 1, ''),
	('Berklee College of Music', 2, '1140 Boylston Street Boston, MA 02215 USA');

insert into `albums`
	(`name`, `year`, `artist_id`, `label_id`)
values
	('Эльфийская Рукопись', 2004, 1, 1),
	('Камерные произведения для колоратурного сопрано', 1985, 2, 2),
	('Млечный путь', 1997, 3, 3),
	('Arias for soprano', 1995, 2, 4);

insert into `genres_albums`
	(`genre_id`, `album_id`)
values
	(1, 1),
	(2, 1),
	(3, 2),
	(4, 4),
	(5, 3),
	(6, 3);

insert into `tracks`
	(`name`, `duration`, `artist_id`, `album_id`)
values
	('Час Испытания', '453', 1, 1),
	('Осколки Прошлого', '421', 1, 1),
	('Полька \"В детской\"', '220', 2, 2),
	('Старт к Луне', '358', 3, 3),
	('Одинокая станция', '513', 3, 3),
	('Narina\'s aria from \"Don Pascuale\"', '450', 2, 4),
	('First aria of Snegurochka from \"Snegurochka\"', '512', 2, 4);

insert into `genres_tracks`
	(`genre_id`, `track_id`)
values
	(1, 1),
	(2, 2),
	(4, 3),
	(6, 4),
	(6, 5),
	(3, 6),
	(3, 7);
