alter table tasks drop foreign key fk_tasks_user;
drop index fk_tasks_user on tasks;

insert into tasks (user_id, title, description, completed) select user_id, title, description, completed from tasks;
insert into tasks (user_id, title, description, completed) select user_id, title, description, completed from tasks;
insert into tasks (user_id, title, description, completed) select user_id, title, description, completed from tasks;
insert into tasks (user_id, title, description, completed) select user_id, title, description, completed from tasks;
insert into tasks (user_id, title, description, completed) select user_id, title, description, completed from tasks;
insert into tasks (user_id, title, description, completed) select user_id, title, description, completed from tasks;
insert into tasks (user_id, title, description, completed) select user_id, title, description, completed from tasks;
insert into tasks (user_id, title, description, completed) select user_id, title, description, completed from tasks;
insert into tasks (user_id, title, description, completed) select user_id, title, description, completed from tasks;
insert into tasks (user_id, title, description, completed) select user_id, title, description, completed from tasks;
insert into tasks (user_id, title, description, completed) select user_id, title, description, completed from tasks;
insert into tasks (user_id, title, description, completed) select user_id, title, description, completed from tasks;
insert into tasks (user_id, title, description, completed) select user_id, title, description, completed from tasks;

insert into tasks (user_id, title) values (5, 'Maya Task 1');

select count(*) from tasks;

explain analyze select * from tasks where user_id = 5;

create index idx_tasks_user_id on tasks (user_id);

explain analyze select * from tasks where user_id = 5;

delete from tasks where id > 13;

alter table tasks
    add constraint fk_tasks_user
    foreign key (user_id) references users (id)
    on delete cascade;
