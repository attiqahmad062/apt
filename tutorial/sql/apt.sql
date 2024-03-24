use  etiapt;
select * from apt_group;
select * from apt_group_techniques;
select * from sub_id;
select * from software_used;

select * from etiapt
SET SQL_SAFE_UPDATES = 0;
SET FOREIGN_KEY_CHECKS = 0;
-- -- Delete the table if it exists
DELETE FROM apt_group;
DELETE FROM apt_group_techniques;
SET FOREIGN_KEY_CHECKS = 1;
-- Re-enable safe mode
SET SQL_SAFE_UPDATES = 1;