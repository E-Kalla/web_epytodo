SET time_zone = "+00:00";
CREATE DATABASE IF NOT EXISTS epytodo;
USE epytodo;

CREATE TABLE IF NOT EXISTS user
(
    user_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    username VARCHAR(20) NOT NULL,
    password VARCHAR(20) NOT NULL,
    PRIMARY KEY (user_id)
)
ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS task
(

    task_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    begin datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    end datetime NULL,
    status enum("not started","in progress","done") NOT NULL DEFAULT 'not started',
    PRIMARY KEY (task_id)
)
ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS user_has_task
(
    id INT NOT NULL AUTO_INCREMENT,
    fk_user_id INT UNSIGNED NOT NULL,
    fk_task_id INT UNSIGNED NOT NULL,
    PRIMARY KEY (id)
)
ENGINE=INNODB
