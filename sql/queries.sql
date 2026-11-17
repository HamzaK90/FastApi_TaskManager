-- SELECT id, title, description, completed FROM tasks WHERE id = 14;

-- SELECT id, title, description, completed FROM tasks ORDER BY id;

-- INSERT INTO tasks (user_id, title, description) VALUES (1, 'New Task', 'This is a new task'); 
--  SELECT id, title, description, completed FROM tasks WHERE id = LAST_INSERT_ID();

-- UPDATE tasks SET completed = true WHERE id = 14;
-- SELECT id, title, description, completed FROM tasks WHERE id = 14;

-- DELETE FROM tasks WHERE id = 14;

-- SELECT 
-- 	tasks.id, 
-- 	users.name AS user_name, 
-- 	tasks.title, 
-- 	tasks.description, 
-- 	tasks.completed, 
-- FROM tasks 
-- JOIN users ON tasks.user_id = users.id;

-- Select 
--     users.id,
--     users.name AS user_name,
--     users.email AS user_email
-- from users
-- left join tasks on tasks.user_id = users.id
-- where tasks.id is null;

-- Select 
--     users.id,
--     users.name AS user_name,
--     users.email AS user_email,
--     count(tasks.completed=1) AS task_completed_count,
--     count(tasks.completed=0) AS task_not_completed_count
-- from users
-- left join tasks on tasks.user_id = users.id
-- group by users.id, users.name, users.email;

-- select
--    tasks.id,
--    tasks.title,
--    tasks.description,
--    tags.name AS tag_name
-- from tasks
-- join task_tags on task_tags.task_id = tasks.id
-- join tags on task_tags.tag_id = tags.id
-- where tags.name = 'work'
-- order by tasks.id;

begin;
insert into users (name, email) values ('Ali', 'ali@example.com');
insert into tasks (user_id, title, description) values (LAST_INSERT_ID(), 'Ali Task 1', 'This is Ali task 1');
commit;

select users.name, tasks.title
from users
join tasks on tasks.user_id = users.id
where users.email = 'ali@example.com';

begin;
insert into users (name, email) values ('Rami', 'rami@example.com');
insert into tasks (user_id, title, description) values (LAST_INSERT_ID(), 'Rami Task 1', 'This is Rami task 1');
rollback;

select users.name, tasks.title
from users
left join tasks on tasks.user_id = users.id
where users.email = 'rami@example.com';
