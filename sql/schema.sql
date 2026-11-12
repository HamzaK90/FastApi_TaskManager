DROP TABLE IF EXISTS task_tags;
DROP TABLE IF EXISTS tasks;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
	id			INT				NOT NULL AUTO_INCREMENT,
	name		VARCHAR(100)	NOT NULL,
	email		VARCHAR(255)	NOT NULL,
	created_at	DATETIME    	NOT NULL DEFAULT CURRENT_TIMESTAMP,
	
	PRIMARY KEY (id),
    UNIQUE KEY uq_users_email (email)
) ENGINE=InnoDB;

CREATE TABLE tags (
    id    INT         NOT NULL AUTO_INCREMENT,
    name  VARCHAR(50) NOT NULL,

    PRIMARY KEY (id),
    UNIQUE KEY uq_tags_name (name)
) ENGINE=InnoDB;

CREATE TABLE tasks (
	id     		INT         	NOT NULL AUTO_INCREMENT,
	user_id		INT 			NOT NULL,
	title		VARCHAR(100)	NOT NULL,
	description	VARCHAR(500)	NOT NULL DEFAULT '',
	completed	BOOLEAN 		NOT NULL DEFAULT FALSE,
	created_at	DATETIME		NOT NULL DEFAULT CURRENT_TIMESTAMP,
	
	PRIMARY KEY (id),
	CONSTRAINT fk_tasks_user
		FOREIGN KEY (user_id) REFERENCES users (id)
		ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE task_tags (
	task_id		INT		NOT NULL,
	tag_id		INT		NOT NULL,
	
	PRIMARY KEY (task_id,tag_id),
	CONSTRAINT fk_task_tags_task
        FOREIGN KEY (task_id) REFERENCES tasks (id)
        ON DELETE CASCADE,
    CONSTRAINT fk_task_tags_tag
        FOREIGN KEY (tag_id) REFERENCES tags (id)
        ON DELETE CASCADE
) ENGINE=InnoDB;