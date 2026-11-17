DELETE FROM task_tags;
DELETE FROM tasks;
DELETE FROM tags;
DELETE FROM users;

INSERT INTO users (id, name, email) VALUES
    (1, 'Sara Haddad',   'sara.haddad@example.com'),
    (2, 'Omar Khalil',   'omar.khalil@example.com'),
    (3, 'Lina Mansour',  'lina.mansour@example.com'),
    (4, 'Yousef Nasser', 'yousef.nasser@example.com'),
    (5, 'Maya Saleh',    'maya.saleh@example.com'),
    (6, 'Adam Barakat',  'adam.barakat@example.com');

INSERT INTO tags (id, name) VALUES
    (1, 'work'),
    (2, 'personal'),
    (3, 'urgent'),
    (4, 'shopping'),
    (5, 'health'),
    (6, 'learning');

INSERT INTO tasks (id, user_id, title, description, completed) VALUES
    -- Sara
    (1,  1, 'Write quarterly report',    'Summarize Q3 sales numbers for the team meeting', FALSE),
    (2,  1, 'Review pull requests',      'Check the open PRs on the backend repo',          TRUE),
    (3,  1, 'Book dentist appointment',  '',                                                FALSE),
    (4,  1, 'Buy groceries',             'Milk, eggs, bread, coffee',                        TRUE),
    -- Omar
    (5,  2, 'Prepare client demo',       'Demo the new dashboard to the client on Friday',  FALSE),
    (6,  2, 'Fix login bug',             'Users get logged out after 5 minutes',            TRUE),
    (7,  2, 'Finish SQL course',         'Complete the joins and indexes chapters',          FALSE),
    -- Lina
    (8,  3, 'Go for a run',              '5 km in the park',                                 TRUE),
    (9,  3, 'Update project report',     'Add the final test results',                       TRUE),
    (10, 3, 'Plan birthday party',       'Book a venue and send invitations',                FALSE),
    (11, 3, 'Read FastAPI docs',         'Dependencies and background tasks sections',       TRUE),
    -- Yousef
    (12, 4, 'Renew car insurance',       'Expires at the end of the month',                  FALSE),
    (13, 4, 'Order new laptop charger',  '',                                                TRUE);

INSERT INTO task_tags (task_id, tag_id) VALUES
    (1, 1), (1, 3),            -- report: work, urgent
    (2, 1),                    -- PRs: work
    (3, 2), (3, 5),            -- dentist: personal, health
    (4, 2), (4, 4),            -- groceries: personal, shopping
    (5, 1), (5, 3),            -- demo: work, urgent
    (6, 1), (6, 3),            -- bug: work, urgent
    (7, 6),                    -- SQL course: learning
    (8, 2), (8, 5),            -- run: personal, health
    (9, 1),                    -- project report: work
    (10, 2),                   -- party: personal
    (11, 1), (11, 6),          -- FastAPI docs: work, learning
    (12, 2), (12, 3),          -- insurance: personal, urgent
    (13, 4);                   -- charger: shopping