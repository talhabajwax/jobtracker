create database job_tracker;
use `job_tracker`;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE companies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    website VARCHAR(255),
    location VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE applications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    company_id INT NOT NULL,
    role_title VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL,
    applied_date DATE,
    job_url VARCHAR(500),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (company_id) REFERENCES companies(id)
);
CREATE TABLE application_statuses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);
DROP TABLE applications;
CREATE TABLE applications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    company_id INT NOT NULL,
    status_id INT NOT NULL,
    role_title VARCHAR(255) NOT NULL,
    applied_date DATE,
    job_url VARCHAR(500),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    isActive TINYINT(1) NOT NULL DEFAULT 1,
    isDeleted TINYINT(1) NOT NULL DEFAULT 0,

    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (company_id) REFERENCES companies(id),
    FOREIGN KEY (status_id) REFERENCES application_statuses(id)
);
INSERT INTO application_statuses (name)
VALUES
('Applied'),
('Screening'),
('Interview'),
('Offer'),
('Rejected'),
('Withdrawn');
INSERT INTO application_statuses (name)
VALUES ('Ghosted');
-- get applications
select a.id,a.role_title,c.name as companyName,a.applied_date,s.name as appStatus from applications a
join application_statuses s on a.status_id=s.id
join companies c on a.company_id=c.id
order by a.id desc;
ALTER TABLE applications
ADD COLUMN isActive TINYINT(1) NOT NULL DEFAULT 1,
ADD COLUMN isDeleted TINYINT(1) NOT NULL DEFAULT 0;
