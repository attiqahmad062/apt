select * from apt_group;
-- set sql_safe_updates=0;
-- delete from apt_group;
-- set sql_safe_updates=0;


use etiapt;
CREATE TABLE apt_references (
    reference_id INT PRIMARY KEY,
    reference_link VARCHAR(255)
);

select * from apt_references;

ALTER TABLE apt_references
ADD COLUMN technique_id INT,
ADD CONSTRAINT fk_technique_id
    FOREIGN KEY (technique_id)
    REFERENCES apt_group_techniques(id);
    
  -- Step 1: Turn off Foreign Key Checks
SET FOREIGN_KEY_CHECKS = 0;

-- Step 2: Remove the Primary Key Constraint from the 'id' column
ALTER TABLE apt_group_techniques DROP PRIMARY KEY;

-- Step 3: Add the New Primary Key Constraint to the 'techniques_id' column
ALTER TABLE apt_group_techniques ADD PRIMARY KEY (techniques_id);

-- Step 4: Turn on Foreign Key Checks
SET FOREIGN_KEY_CHECKS = 1;
