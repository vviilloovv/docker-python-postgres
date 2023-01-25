create table if not exists users(
  id serial primary key
  , name varchar(20)
  , age int
);
create sequence if not exists user_id_seq;

create table if not exists books(
  id serial primary key
  , title varchar(30)
  , author varchar(30)
);
create sequence if not exists book_id_seq;