use db;

insert into users (uuid, username) values (UUID(), "tatsuki");
insert into books (uuid, title, user_id) values (
  UUID(),
  "施策デザインのための機械学習入門", 
  (select uuid from users where username="tatsuki")
);
