-- Creates a second table in database.
CREATE TABLE IF NOT EXISTS `second_table` (
    `id` INT,
    `name` VARCHAR(256),
    `score` INT,
);

INSERT INTO `second_table` (`id`, `name`, `score`) VALUES
(1, "John", 10);