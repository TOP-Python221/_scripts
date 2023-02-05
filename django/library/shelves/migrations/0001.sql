BEGIN;
--
-- Create model Author
--
CREATE TABLE "shelves_author" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(20) NOT NULL, "last_name" varchar(30) NOT NULL);
--
-- Create model Book
--
CREATE TABLE "shelves_book" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(50) NOT NULL, "author_id" bigint NOT NULL REFERENCES "shelves_author" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Publisher
--
CREATE TABLE "shelves_publisher" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL);
CREATE TABLE "shelves_publisher_authors" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "publisher_id" bigint NOT NULL REFERENCES "shelves_publisher" ("id") DEFERRABLE INITIALLY DEFERRED, "author_id" bigint NOT NULL REFERENCES "shelves_author" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "shelves_publisher_books" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "publisher_id" bigint NOT NULL REFERENCES "shelves_publisher" ("id") DEFERRABLE INITIALLY DEFERRED, "book_id" bigint NOT NULL REFERENCES "shelves_book" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "shelves_book_author_id_0effa651" ON "shelves_book" ("author_id");
CREATE UNIQUE INDEX "shelves_publisher_authors_publisher_id_author_id_0dd3e916_uniq" ON "shelves_publisher_authors" ("publisher_id", "author_id");
CREATE INDEX "shelves_publisher_authors_publisher_id_eee9b1b1" ON "shelves_publisher_authors" ("publisher_id");
CREATE INDEX "shelves_publisher_authors_author_id_499900ac" ON "shelves_publisher_authors" ("author_id");
CREATE UNIQUE INDEX "shelves_publisher_books_publisher_id_book_id_ce575a61_uniq" ON "shelves_publisher_books" ("publisher_id", "book_id");
CREATE INDEX "shelves_publisher_books_publisher_id_d929a1cb" ON "shelves_publisher_books" ("publisher_id");
CREATE INDEX "shelves_publisher_books_book_id_60d50916" ON "shelves_publisher_books" ("book_id");
COMMIT;
