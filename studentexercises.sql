DROP TABLE IF EXISTS AssignedExercise;
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Instructor;
DROP TABLE IF EXISTS Exercise;
DROP TABLE IF EXISTS Cohort;

CREATE TABLE Cohort (
    id	   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name   TEXT NOT NULL UNIQUE
);

CREATE TABLE Exercise (
    id	   					INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name   					TEXT NOT NULL UNIQUE,
	programming_language 	TEXT NOT NULL
);

CREATE TABLE Student (
    id	   			INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    first_name   	TEXT NOT NULL,
    last_name   	TEXT NOT NULL,
    slack_handle 	TEXT NOT NULL UNIQUE,
    cohort_id 		INTEGER NOT NULL,
    FOREIGN KEY(cohort_id) REFERENCES Cohort(id)
);

CREATE TABLE Instructor (
    id	   			INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    first_name   	TEXT NOT NULL,
    last_name  		TEXT NOT NULL,
    slack_handle 	TEXT NOT NULL UNIQUE,
    specialty 		TEXT NOT NULL,
    cohort_id 		INTEGER NOT NULL,
    FOREIGN KEY(cohort_id) REFERENCES Cohort(id)
);

CREATE TABLE AssignedExercise (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	exercise_id INTEGER NOT NULL,
	student_id INTEGER NOT NULL,
	FOREIGN KEY(exercise_id) REFERENCES Exercise(id),
	FOREIGN KEY(student_id) REFERENCES Student(id)
);

INSERT INTO Cohort (name)
VALUES ("Cohort 36");

INSERT INTO Cohort (name)
VALUES ("Cohort 37");

INSERT INTO Cohort (name)
VALUES ("Cohort 38");

INSERT INTO Exercise (name, programming_language)
VALUES ("Advanced Divs", "HTML");

INSERT INTO Exercise (name, programming_language)
VALUES ("Setting the Lists: The Python Dictionary", "Python");

INSERT INTO Exercise (name, programming_language)
VALUES ("Getting a Date()", "Javascript");

INSERT INTO Exercise (name, programming_language)
VALUES ("Props to the Component", "Javascript");

INSERT INTO Exercise (name, programming_language)
VALUES ("Snake Case for Dummies", "Python");

INSERT INTO Instructor 
	SELECT null, "Cyndi", "Mallum", "cmallam0", "Support", c.id 
	FROM Cohort c
	WHERE name = "Cohort 36";
	
INSERT INTO Instructor 
	SELECT null, "Vladimir", "Van Schafflaer", "vvanschafflaer0", "Business Development", c.id 
	FROM Cohort c
	WHERE name = "Cohort 37";
	
INSERT INTO Instructor 
	SELECT null, "Emmerich", "Lathe", "elathe0", "Legal", c.id 
	FROM Cohort c
	WHERE name = "Cohort 38";
	
INSERT INTO Student 
	SELECT null, "Sammie", "Greenley", "sgreenley0", c.id 
	FROM Cohort c
	WHERE name = "Cohort 36";
	
INSERT INTO Student 
	SELECT null, "Renaud", "Carillo", "rcarillo1", c.id 
	FROM Cohort c
	WHERE name = "Cohort 36";
	
INSERT INTO Student 
	SELECT null, "Shaine", "Willbourne", "swillbourne0", c.id 
	FROM Cohort c
	WHERE name = "Cohort 37";

INSERT INTO Student 
	SELECT null, "Alfy", "Donnelly", "adonnelly1", c.id 
	FROM Cohort c
	WHERE name = "Cohort 37";

INSERT INTO Student 
	SELECT null, "Brenda", "Leblanc", "bleblanc0", c.id 
	FROM Cohort c
	WHERE name = "Cohort 38";

INSERT INTO Student 
	SELECT null, "Tonia", "Cheater", "tcheater1", c.id 
	FROM Cohort c
	WHERE name = "Cohort 38";

INSERT INTO Student 
	SELECT null, "Giovanna", "Caldron", "gcaldron2", c.id 
	FROM Cohort c
	WHERE name = "Cohort 36";
	
INSERT INTO AssignedExercise (exercise_id, student_id)
VALUES (1, 3);

INSERT INTO AssignedExercise (exercise_id, student_id)
VALUES (1, 5);

INSERT INTO AssignedExercise (exercise_id, student_id)
VALUES (2, 2);

INSERT INTO AssignedExercise (exercise_id, student_id)
VALUES (2, 4);

INSERT INTO AssignedExercise (exercise_id, student_id)
VALUES (3, 1);

INSERT INTO AssignedExercise (exercise_id, student_id)
VALUES (3, 6);

INSERT INTO AssignedExercise (exercise_id, student_id)
VALUES (4, 7);

INSERT INTO AssignedExercise (exercise_id, student_id)
VALUES (1, 7);

INSERT INTO AssignedExercise (exercise_id, student_id)
VALUES (4, 1);

INSERT INTO AssignedExercise (exercise_id, student_id)
VALUES (5, 2);

INSERT INTO AssignedExercise (exercise_id, student_id)
VALUES (4, 3);

INSERT INTO AssignedExercise (exercise_id, student_id)
VALUES (1, 4);

INSERT INTO AssignedExercise (exercise_id, student_id)
VALUES (3, 5);

INSERT INTO AssignedExercise (exercise_id, student_id)
VALUES (2, 6);


--SELECT * FROM AssignedExercise
--ORDER BY student_id;


SELECT COUNT(), s.slack_handle
FROM Student s
JOIN AssignedExercise ae
ON s.id = ae.student_id 
GROUP BY s.slack_handle;