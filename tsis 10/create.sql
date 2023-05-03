CREATE TABLE users(
	id serial PRIMARY KEY,
	first_name varchar(30) NOT NULL,
	last_name varchar(30) NOT NULL
);
CREATE TABLE passports(
	id serial PRIMARY KEY,
	passport_number int NOT NULL,
	city_of_registration varchar(30) NOT NULL,
	fk_passports_users int REFERENCES users(id)
);