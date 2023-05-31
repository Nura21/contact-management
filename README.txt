# create database
CREATE DATABASE contact_management;

-- contact_management.contacts definition

CREATE TABLE `contacts` (
  `name` varchar(100) NOT NULL,
  `phone_number` varchar(150) NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


# run from
python3 Main.py