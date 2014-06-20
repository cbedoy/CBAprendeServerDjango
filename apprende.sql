BEGIN;
CREATE TABLE "manager_course" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(45) NOT NULL,
    "description" text NOT NULL
)
;
CREATE TABLE "manager_theme" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(50) NOT NULL,
    "description" text NOT NULL,
    "course_id" integer NOT NULL REFERENCES "manager_course" ("id")
)
;
CREATE TABLE "manager_question" (
    "id" integer NOT NULL PRIMARY KEY,
    "question" text NOT NULL,
    "answer1" text NOT NULL,
    "answer2" text NOT NULL,
    "answer3" text NOT NULL,
    "answer4" text NOT NULL,
    "correct" integer NOT NULL,
    "feedback" text NOT NULL,
    "theme_id" integer NOT NULL REFERENCES "manager_theme" ("id")
)
;
CREATE TABLE "manager_university" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(45) NOT NULL
)
;
CREATE TABLE "manager_user" (
    "id" integer NOT NULL PRIMARY KEY,
    "username" varchar(45) NOT NULL,
    "password" varchar(45) NOT NULL,
    "first_name" varchar(45) NOT NULL,
    "last_name" varchar(45) NOT NULL,
    "facebook" varchar(100),
    "twitter" varchar(100),
    "age" integer NOT NULL,
    "points" real NOT NULL,
    "plays" integer NOT NULL
)
;
CREATE TABLE "manager_statistics" (
    "id" integer NOT NULL PRIMARY KEY,
    "level" integer NOT NULL,
    "correct" integer NOT NULL,
    "wrongs" integer NOT NULL,
    "points" real NOT NULL,
    "date" date NOT NULL,
    "player_id" integer NOT NULL REFERENCES "manager_user" ("id")
)
;
COMMIT;
