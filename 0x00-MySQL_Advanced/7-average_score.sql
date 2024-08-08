--  SQL script that creates a stored procedure ComputeAverageScoreForUser.
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE `average` FLOAT;

    SELECT AVG(`score`) INTO `average`
    FROM `corrections`
    WHERE `corrections`.`user_id` = `user_id`;

    UPDATE `users`
    SET `average_score` = `average`
    WHERE `users`.`id` = `user_id`;

END//

DELIMITER ;
