Welcome to Derrick Zhang 1010232374's A3Q1 Comp3005

To create the database just run the following in the postgres query tool:

CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE
);

And use the following to add entries:
INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');

The rest is fairly explanatory and the video will go through it as well.

https://youtu.be/s4Y3GD-Px2c   Link to video

^^
By the way, the student id is at 19 because of prior testing and the fact that it is SERIAL/auto incrementing