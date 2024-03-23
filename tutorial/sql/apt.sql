use etiapt;
CREATE TABLE software_used (
    id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255),
    reference VARCHAR(255),
    techniques VARCHAR(255)
);
CREATE TABLE sub_id (
    id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255)
);

-- Procedure Examples 
CREATE TABLE procedure_example (
    id VARCHAR(255)  PRIMARY KEY,
    name VARCHAR(255),
    description Varchar(255),
    reference varchar(255)
); 
	