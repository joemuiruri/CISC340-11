drop table if exists userpassword;
    create table userpassword (
    id integer primary key autoincrement,
    password text not null
);