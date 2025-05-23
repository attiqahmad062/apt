-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema etiapt
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema etiapt
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `etiapt` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `etiapt` ;

-- -----------------------------------------------------
-- Table `etiapt`.`apt_group`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `etiapt`.`apt_group` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `group_name` VARCHAR(255) NULL DEFAULT NULL,
  `mitre_name` VARCHAR(255) NULL DEFAULT NULL,
  `summary` LONGTEXT NULL DEFAULT NULL,
  `created_date` DATETIME NULL DEFAULT NULL,
  `modified_date` DATETIME NULL DEFAULT NULL,
  `associated_groups` VARCHAR(255) NULL DEFAULT NULL,
  `group_url` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `UK_8sucq9ruesbnx11by8smbxsly` (`group_name` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 25177
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `etiapt`.`attack_campaign`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `etiapt`.`attack_campaign` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `associated_indicators` INT NULL DEFAULT NULL,
  `case_name` VARCHAR(255) NULL DEFAULT NULL,
  `method_tool_used` LONGTEXT NULL DEFAULT NULL,
  `sources` LONGTEXT NULL DEFAULT NULL,
  `special_characteristics` LONGTEXT NULL DEFAULT NULL,
  `summary` LONGTEXT NULL DEFAULT NULL,
  `created_date` DATETIME NULL DEFAULT NULL,
  `modified_date` DATETIME NULL DEFAULT NULL,
  `source_id` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `UK_qx11o2rnfqllloj3lu11oxnh5` (`case_name` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 2060
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `etiapt`.`alias`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `etiapt`.`alias` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `value` VARCHAR(255) NULL DEFAULT NULL,
  `attack_campaign_id` INT NULL DEFAULT NULL,
  `group_id` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `FKtnuaykscmm5cjhf5t6vxsfmg7` (`attack_campaign_id` ASC) VISIBLE,
  INDEX `FKjtjvgfs9mnglspq972qre46oy` (`group_id` ASC) VISIBLE,
  CONSTRAINT `FKjtjvgfs9mnglspq972qre46oy`
    FOREIGN KEY (`group_id`)
    REFERENCES `etiapt`.`apt_group` (`id`),
  CONSTRAINT `FKtnuaykscmm5cjhf5t6vxsfmg7`
    FOREIGN KEY (`attack_campaign_id`)
    REFERENCES `etiapt`.`attack_campaign` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 299
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `etiapt`.`apt_group_attack_campaigns`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `etiapt`.`apt_group_attack_campaigns` (
  `groups_id` INT NOT NULL,
  `attack_campaigns_id` INT NOT NULL,
  INDEX `FKnvbkxc8yg6vwisalu42j08e7m` (`attack_campaigns_id` ASC) VISIBLE,
  INDEX `FKm81hqu7jjfp756bqp1clndts6` (`groups_id` ASC) VISIBLE,
  CONSTRAINT `FKm81hqu7jjfp756bqp1clndts6`
    FOREIGN KEY (`groups_id`)
    REFERENCES `etiapt`.`apt_group` (`id`),
  CONSTRAINT `FKnvbkxc8yg6vwisalu42j08e7m`
    FOREIGN KEY (`attack_campaigns_id`)
    REFERENCES `etiapt`.`attack_campaign` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `etiapt`.`country_lkp`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `etiapt`.`country_lkp` (
  `id` INT NOT NULL,
  `cca2` VARCHAR(255) NULL DEFAULT NULL,
  `cca3` VARCHAR(255) NULL DEFAULT NULL,
  `country_name` VARCHAR(255) NULL DEFAULT NULL,
  `region` VARCHAR(255) NULL DEFAULT NULL,
  `sub_region` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `UK_m7svrihrrk0q18knx0vs464xa` (`cca2` ASC) VISIBLE,
  UNIQUE INDEX `UK_i9qsnc3dfckjrcxxvq6jbj1rb` (`cca3` ASC) VISIBLE,
  UNIQUE INDEX `UK_jt192ag5t7g7ll8vccqgqc0sy` (`country_name` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `etiapt`.`apt_group_countries`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `etiapt`.`apt_group_countries` (
  `groups_id` INT NOT NULL,
  `countries_id` INT NOT NULL,
  INDEX `FKpqd7pr5mdn1ulnkjmjti6iwn` (`countries_id` ASC) VISIBLE,
  INDEX `FKikar0q5bmml12qg66gpvxyk25` (`groups_id` ASC) VISIBLE,
  CONSTRAINT `FKikar0q5bmml12qg66gpvxyk25`
    FOREIGN KEY (`groups_id`)
    REFERENCES `etiapt`.`apt_group` (`id`),
  CONSTRAINT `FKpqd7pr5mdn1ulnkjmjti6iwn`
    FOREIGN KEY (`countries_id`)
    REFERENCES `etiapt`.`country_lkp` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `etiapt`.`sector_lkp`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `etiapt`.`sector_lkp` (
  `id` INT NOT NULL,
  `value` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `UK_hluwp9p17ucwev4krhf1315nm` (`value` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `etiapt`.`apt_group_sectors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `etiapt`.`apt_group_sectors` (
  `groups_id` INT NOT NULL,
  `sectors_id` INT NOT NULL,
  INDEX `FKnnjhspt19c4apb7sv5ruo8tpb` (`sectors_id` ASC) VISIBLE,
  INDEX `FK4i3wrseuqqvi7299v6r51fpne` (`groups_id` ASC) VISIBLE,
  CONSTRAINT `FK4i3wrseuqqvi7299v6r51fpne`
    FOREIGN KEY (`groups_id`)
    REFERENCES `etiapt`.`apt_group` (`id`),
  CONSTRAINT `FKnnjhspt19c4apb7sv5ruo8tpb`
    FOREIGN KEY (`sectors_id`)
    REFERENCES `etiapt`.`sector_lkp` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `etiapt`.`apt_group_techniques`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `etiapt`.`apt_group_techniques` (
  `groups_id` VARCHAR(255) NULL DEFAULT NULL,
  `techniques_id` VARCHAR(255) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_bin' NOT NULL,
  `description` LONGTEXT NULL DEFAULT NULL,
  `domain_name` VARCHAR(255) NULL DEFAULT NULL,
  `reference` VARCHAR(255) NULL DEFAULT NULL,
  `sub_id` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`techniques_id`),
  INDEX `FKmojo8d3wqerr5iv219205mh8d` (`techniques_id` ASC) VISIBLE,
  INDEX `FKqiufy5mk9w015gk82sfcd2ea4` (`groups_id` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `etiapt`.`software_used`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `etiapt`.`software_used` (
  `software_Id` VARCHAR(255) NOT NULL,
  `name` VARCHAR(255) NULL DEFAULT NULL,
  `reference` VARCHAR(255) NULL DEFAULT NULL,
  `techniques` LONGTEXT NULL DEFAULT NULL,
  PRIMARY KEY (`software_Id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `etiapt`.`apt_technique_references`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `etiapt`.`apt_technique_references` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `reference_link` VARCHAR(45) NULL DEFAULT NULL,
  `apt_group_techniques_techniques_id` VARCHAR(255) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_bin' NOT NULL,
  `software_used_software_Id` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_apt_technique_references_apt_group_techniques1_idx` (`apt_group_techniques_techniques_id` ASC) VISIBLE,
  INDEX `fk_apt_technique_references_software_used1_idx` (`software_used_software_Id` ASC) VISIBLE,
  CONSTRAINT `fk_apt_technique_references_apt_group_techniques1`
    FOREIGN KEY (`apt_group_techniques_techniques_id`)
    REFERENCES `etiapt`.`apt_group_techniques` (`techniques_id`),
  CONSTRAINT `fk_apt_technique_references_software_used1`
    FOREIGN KEY (`software_used_software_Id`)
    REFERENCES `etiapt`.`software_used` (`software_Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 8945
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `etiapt`.`attack_campaign_countries`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `etiapt`.`attack_campaign_countries` (
  `attack_campaigns_id` INT NOT NULL,
  `countries_id` INT NOT NULL,
  INDEX `FK6k5ea5wrsktlto0l7ftoaaxnr` (`countries_id` ASC) VISIBLE,
  INDEX `FK4g7b7w488k1doyrw5r3ci4yex` (`attack_campaigns_id` ASC) VISIBLE,
  CONSTRAINT `FK4g7b7w488k1doyrw5r3ci4yex`
    FOREIGN KEY (`attack_campaigns_id`)
    REFERENCES `etiapt`.`attack_campaign` (`id`),
  CONSTRAINT `FK6k5ea5wrsktlto0l7ftoaaxnr`
    FOREIGN KEY (`countries_id`)
    REFERENCES `etiapt`.`country_lkp` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `etiapt`.`attack_campaign_sectors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `etiapt`.`attack_campaign_sectors` (
  `attack_campaigns_id` INT NOT NULL,
  `sectors_id` INT NOT NULL,
  INDEX `FK45ag3bmho9er14cul69fi3eli` (`sectors_id` ASC) VISIBLE,
  INDEX `FKbm0hydxo34ujft02u9rb29i76` (`attack_campaigns_id` ASC) VISIBLE,
  CONSTRAINT `FK45ag3bmho9er14cul69fi3eli`
    FOREIGN KEY (`sectors_id`)
    REFERENCES `etiapt`.`sector_lkp` (`id`),
  CONSTRAINT `FKbm0hydxo34ujft02u9rb29i76`
    FOREIGN KEY (`attack_campaigns_id`)
    REFERENCES `etiapt`.`attack_campaign` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `etiapt`.`ioc_type_lkp`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `etiapt`.`ioc_type_lkp` (
  `id` INT NOT NULL,
  `value` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `UK_lwxd57v5769ll74693pwv0ska` (`value` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `etiapt`.`ioc`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `etiapt`.`ioc` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `date` DATETIME NULL DEFAULT NULL,
  `file_description` VARCHAR(255) NULL DEFAULT NULL,
  `file_type` VARCHAR(255) NULL DEFAULT NULL,
  `malware_signature_type` VARCHAR(255) NULL DEFAULT NULL,
  `md5` VARCHAR(255) NULL DEFAULT NULL,
  `sha1` VARCHAR(255) NULL DEFAULT NULL,
  `sha_256` VARCHAR(255) NULL DEFAULT NULL,
  `target_machine` VARCHAR(255) NULL DEFAULT NULL,
  `value` LONGTEXT NULL DEFAULT NULL,
  `attack_campaign_id` INT NULL DEFAULT NULL,
  `ioc_type_lkp_id` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `FKise0y07mwmdyyau8spsq6urgq` (`attack_campaign_id` ASC) VISIBLE,
  INDEX `FKafa0stnwjcrku3kgusd6ulnv2` (`ioc_type_lkp_id` ASC) VISIBLE,
  CONSTRAINT `FKafa0stnwjcrku3kgusd6ulnv2`
    FOREIGN KEY (`ioc_type_lkp_id`)
    REFERENCES `etiapt`.`ioc_type_lkp` (`id`),
  CONSTRAINT `FKise0y07mwmdyyau8spsq6urgq`
    FOREIGN KEY (`attack_campaign_id`)
    REFERENCES `etiapt`.`attack_campaign` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 113519
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `etiapt`.`procedure_example`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `etiapt`.`procedure_example` (
  `procedure_eample_id` VARCHAR(255) NOT NULL,
  `name` VARCHAR(255) NULL DEFAULT NULL,
  `description` VARCHAR(255) NULL DEFAULT NULL,
  `reference` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`procedure_eample_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `etiapt`.`user_preference`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `etiapt`.`user_preference` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `campaign_region_notif` TINYINT(1) NOT NULL DEFAULT '0',
  `campaign_sector_notif` TINYINT(1) NOT NULL DEFAULT '0',
  `created` DATETIME NULL DEFAULT NULL,
  `value` VARCHAR(255) NULL DEFAULT NULL,
  `group_region_notif` TINYINT(1) NOT NULL DEFAULT '0',
  `group_sector_notif` TINYINT(1) NOT NULL DEFAULT '0',
  `last_modified` DATETIME NULL DEFAULT NULL,
  `user_id` INT NULL DEFAULT NULL,
  `attack_region_frequency` INT NOT NULL DEFAULT '0',
  `attack_region_last_processed` DATETIME NULL DEFAULT NULL,
  `attack_sector_frequency` INT NOT NULL DEFAULT '0',
  `attack_sector_last_processed` DATETIME NULL DEFAULT NULL,
  `group_region_frequency` INT NOT NULL DEFAULT '0',
  `group_region_last_processed` DATETIME NULL DEFAULT NULL,
  `group_sector_frequency` INT NOT NULL DEFAULT '0',
  `group_sector_last_processed` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `UK_mxcnwvuyw0aqwyt2940cwhidc` (`value` ASC) VISIBLE,
  UNIQUE INDEX `UK_s5oeayykfc7bpkpdwyrffwcqx` (`user_id` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 7
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `etiapt`.`region_preference`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `etiapt`.`region_preference` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `enabled` TINYINT(1) NULL DEFAULT '1',
  `value` VARCHAR(255) NULL DEFAULT NULL,
  `user_preference_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `FK9m6rg67s0ha9veg3chkcw2pjh` (`user_preference_id` ASC) VISIBLE,
  CONSTRAINT `FK9m6rg67s0ha9veg3chkcw2pjh`
    FOREIGN KEY (`user_preference_id`)
    REFERENCES `etiapt`.`user_preference` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 115
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `etiapt`.`sector_preference`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `etiapt`.`sector_preference` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `enabled` TINYINT(1) NULL DEFAULT '1',
  `sector_id` INT NULL DEFAULT NULL,
  `value` VARCHAR(255) NULL DEFAULT NULL,
  `user_preference_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `FKswjj7ocr6gy3h5fk2by0l1ve7` (`user_preference_id` ASC) VISIBLE,
  CONSTRAINT `FKswjj7ocr6gy3h5fk2by0l1ve7`
    FOREIGN KEY (`user_preference_id`)
    REFERENCES `etiapt`.`user_preference` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 628
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `etiapt`.`sub_techniques`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `etiapt`.`sub_techniques` (
  `id` VARCHAR(255) NOT NULL,
  `name` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `etiapt`.`technique`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `etiapt`.`technique` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL DEFAULT NULL,
  `technique_id` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `UK_rqt5ranm0aokv4e06269fg608` (`technique_id` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 531
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `etiapt`.`technique_type_lkp`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `etiapt`.`technique_type_lkp` (
  `id` INT NOT NULL,
  `value` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `UK_9utlrpy2raryqbcqisfpox1xn` (`value` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `etiapt`.`technique_technique_types`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `etiapt`.`technique_technique_types` (
  `techniques_id` INT NOT NULL,
  `technique_types_id` INT NOT NULL,
  INDEX `FKjunua6uxh8k1diptul8bbn14v` (`technique_types_id` ASC) VISIBLE,
  INDEX `FK1px4fmi3eww607a1xy32q57rs` (`techniques_id` ASC) VISIBLE,
  CONSTRAINT `FK1px4fmi3eww607a1xy32q57rs`
    FOREIGN KEY (`techniques_id`)
    REFERENCES `etiapt`.`technique` (`id`),
  CONSTRAINT `FKjunua6uxh8k1diptul8bbn14v`
    FOREIGN KEY (`technique_types_id`)
    REFERENCES `etiapt`.`technique_type_lkp` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
