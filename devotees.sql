CREATE DATABASE attendance_system;
USE attendance_system;

CREATE TABLE devotees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    serial_number VARCHAR(50) UNIQUE,
    name VARCHAR(100),
    address TEXT,
    position VARCHAR(20),
    contact VARCHAR(15)
);

CREATE TABLE attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    serial_number VARCHAR(50),
    date DATE,
    status VARCHAR(10),
    FOREIGN KEY (serial_number) REFERENCES devotees(serial_number)
);
