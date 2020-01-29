CREATE DATABASE testovacka;
GRANT ALL PRIVILEGES ON DATABASE testovacka TO postgres;
\c testovacka
CREATE TABLE users (
  id serial PRIMARY KEY NOT NULL,
  username VARCHAR(80) NOT NULL,
  password VARCHAR(200) NOT NULL
);
CREATE TABLE session_manager (
  id serial PRIMARY KEY NOT NULL,
  session VARCHAR(260) NOT NULL
);