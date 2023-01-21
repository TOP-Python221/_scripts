drop schema if exists mus_collection;
create schema mus_collection;

use mus_collection;


create table artists (
	`id` mediumint unsigned auto_increment primary key,
    `name` varchar(100) not null,
    constraint `CH_artists_name` check (`name` <> '')
);

create table genres (
	`id` tinyint unsigned auto_increment primary key,
	`name` varchar(50) not null unique,
    constraint `CH_genres_name` check (`name` <> '')
);

create table countries (
	`id` tinyint unsigned auto_increment primary key,
	`name` varchar(50) not null unique,
    constraint `CH_countries_name` check (`name` <> '')
);

create table labels (
	`id` smallint unsigned auto_increment primary key,
    `name` varchar(100) not null,
    constraint `CH_labels_name` check (`name` <> ''),
    `country_id` tinyint unsigned not null,
    `office_address` varchar (200) not null
);

create table albums (
	`id` int unsigned auto_increment primary key,
    `name` varchar(100) not null,
    constraint `CH_albums_name` check (`name` <> ''),
    `year` year not null,
    `review` text,
    `artist_id` mediumint unsigned not null,
    `label_id` smallint unsigned not null
);

create table genres_albums (
    `genre_id` tinyint unsigned not null,
    `album_id` int unsigned not null
);

create table tracks (
	`id` int unsigned auto_increment primary key,
    `name` varchar(100) not null,
	constraint `CH_tracks_name` check (`name` <> ''),
    `duration` time not null,
	constraint `CH_tracks_duration` check (`duration` > 0),
    `artist_id` mediumint unsigned not null,
    `album_id` int unsigned not null
);
        
create table genres_tracks (
    `genre_id` tinyint unsigned not null,
    `track_id` int unsigned not null
);


alter table labels 
	add constraint `FK_labels_country_id`
		foreign key (`country_id`)
        references countries (`id`);

alter table albums 
	add constraint `FK_albums_artist_id` 
		foreign key (`artist_id`)
		references artists (`id`),
	add constraint `FK_albums_label_id`
		foreign key (`label_id`)
		references labels (`id`);

alter table genres_albums 
	add constraint `FK_genres_albums_genre_id`
		foreign key (`genre_id`)
		references genres (`id`),
	add constraint `FK_genres_albums_album_id`
		foreign key (`album_id`)
		references albums (`id`);

alter table tracks 
	add constraint `FK_tracks_artist_id` 
		foreign key (`artist_id`)
		references artists (`id`),
	add constraint `FK_tracks_album_id` 
		foreign key (`album_id`)
		references albums (`id`);

alter table genres_tracks 
	add constraint `FK_genres_tracks_genre_id`
		foreign key (`genre_id`)
		references genres (`id`),
	add constraint `FK_genres_tracks_track_id`
		foreign key (`track_id`)
		references tracks (`id`);
