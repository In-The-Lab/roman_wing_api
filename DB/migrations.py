tables = {}

tables["users"] = (
	"CREATE TABLE `users` ("
	"`id` INT NOT NULL AUTO_INCREMENT, "
	"`first_name` VARCHAR(16) NOT NULL, "
	"`last_name` VARCHAR(16) NOT NULL, "
	"`email` VARCHAR(64) NOT NULL, "
	"`is_admin` BOOLEAN NOT NULL, "
	"`date_created` TIMESTAMP NOT NULL, "
	"PRIMARY KEY (id))"
)

tables["posts"] = (
	"CREATE TABLE `posts` ("
	"`id` int NOT NULL AUTO_INCREMENT, "
	"`creator_id` int NOT NULL, "
	"`body` TEXT NOT NULL, "
	"FOREIGN KEY (`creator_id`) REFERENCES `users` (`id`), "
	"PRIMARY KEY (`id`))"
)