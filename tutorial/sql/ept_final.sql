CREATE DATABASE  IF NOT EXISTS `etiapt` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `etiapt`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: etiapt
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alias`
--

DROP TABLE IF EXISTS `alias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alias` (
  `id` int NOT NULL AUTO_INCREMENT,
  `value` varchar(255) DEFAULT NULL,
  `attack_campaign_id` int DEFAULT NULL,
  `group_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKtnuaykscmm5cjhf5t6vxsfmg7` (`attack_campaign_id`),
  KEY `FKjtjvgfs9mnglspq972qre46oy` (`group_id`),
  CONSTRAINT `FKjtjvgfs9mnglspq972qre46oy` FOREIGN KEY (`group_id`) REFERENCES `apt_group` (`id`),
  CONSTRAINT `FKtnuaykscmm5cjhf5t6vxsfmg7` FOREIGN KEY (`attack_campaign_id`) REFERENCES `attack_campaign` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=299 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alias`
--

LOCK TABLES `alias` WRITE;
/*!40000 ALTER TABLE `alias` DISABLE KEYS */;
/*!40000 ALTER TABLE `alias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `apt_group`
--

DROP TABLE IF EXISTS `apt_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `apt_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_name` varchar(255) DEFAULT NULL,
  `mitre_name` varchar(255) DEFAULT NULL,
  `summary` longtext,
  `created_date` datetime DEFAULT NULL,
  `modified_date` datetime DEFAULT NULL,
  `associated_groups` varchar(255) DEFAULT NULL,
  `group_url` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UK_8sucq9ruesbnx11by8smbxsly` (`group_name`)
) ENGINE=InnoDB AUTO_INCREMENT=21046 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `apt_group`
--

LOCK TABLES `apt_group` WRITE;
/*!40000 ALTER TABLE `apt_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `apt_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `apt_group_attack_campaigns`
--

DROP TABLE IF EXISTS `apt_group_attack_campaigns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `apt_group_attack_campaigns` (
  `groups_id` int NOT NULL,
  `attack_campaigns_id` int NOT NULL,
  KEY `FKnvbkxc8yg6vwisalu42j08e7m` (`attack_campaigns_id`),
  KEY `FKm81hqu7jjfp756bqp1clndts6` (`groups_id`),
  CONSTRAINT `FKm81hqu7jjfp756bqp1clndts6` FOREIGN KEY (`groups_id`) REFERENCES `apt_group` (`id`),
  CONSTRAINT `FKnvbkxc8yg6vwisalu42j08e7m` FOREIGN KEY (`attack_campaigns_id`) REFERENCES `attack_campaign` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `apt_group_attack_campaigns`
--

LOCK TABLES `apt_group_attack_campaigns` WRITE;
/*!40000 ALTER TABLE `apt_group_attack_campaigns` DISABLE KEYS */;
/*!40000 ALTER TABLE `apt_group_attack_campaigns` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `apt_group_countries`
--

DROP TABLE IF EXISTS `apt_group_countries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `apt_group_countries` (
  `groups_id` int NOT NULL,
  `countries_id` int NOT NULL,
  KEY `FKpqd7pr5mdn1ulnkjmjti6iwn` (`countries_id`),
  KEY `FKikar0q5bmml12qg66gpvxyk25` (`groups_id`),
  CONSTRAINT `FKikar0q5bmml12qg66gpvxyk25` FOREIGN KEY (`groups_id`) REFERENCES `apt_group` (`id`),
  CONSTRAINT `FKpqd7pr5mdn1ulnkjmjti6iwn` FOREIGN KEY (`countries_id`) REFERENCES `country_lkp` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `apt_group_countries`
--

LOCK TABLES `apt_group_countries` WRITE;
/*!40000 ALTER TABLE `apt_group_countries` DISABLE KEYS */;
/*!40000 ALTER TABLE `apt_group_countries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `apt_group_sectors`
--

DROP TABLE IF EXISTS `apt_group_sectors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `apt_group_sectors` (
  `groups_id` int NOT NULL,
  `sectors_id` int NOT NULL,
  KEY `FKnnjhspt19c4apb7sv5ruo8tpb` (`sectors_id`),
  KEY `FK4i3wrseuqqvi7299v6r51fpne` (`groups_id`),
  CONSTRAINT `FK4i3wrseuqqvi7299v6r51fpne` FOREIGN KEY (`groups_id`) REFERENCES `apt_group` (`id`),
  CONSTRAINT `FKnnjhspt19c4apb7sv5ruo8tpb` FOREIGN KEY (`sectors_id`) REFERENCES `sector_lkp` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `apt_group_sectors`
--

LOCK TABLES `apt_group_sectors` WRITE;
/*!40000 ALTER TABLE `apt_group_sectors` DISABLE KEYS */;
/*!40000 ALTER TABLE `apt_group_sectors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `apt_group_techniques`
--

DROP TABLE IF EXISTS `apt_group_techniques`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `apt_group_techniques` (
  `groups_id` varchar(255) DEFAULT NULL,
  `techniques_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `description` longtext,
  `domain_name` varchar(255) DEFAULT NULL,
  `reference` varchar(255) DEFAULT NULL,
  `sub_id` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`techniques_id`),
  KEY `FKmojo8d3wqerr5iv219205mh8d` (`techniques_id`),
  KEY `FKqiufy5mk9w015gk82sfcd2ea4` (`groups_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `apt_group_techniques`
--

LOCK TABLES `apt_group_techniques` WRITE;
/*!40000 ALTER TABLE `apt_group_techniques` DISABLE KEYS */;
/*!40000 ALTER TABLE `apt_group_techniques` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `apt_references`
--

DROP TABLE IF EXISTS `apt_references`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `apt_references` (
  `reference_id` int NOT NULL,
  `reference_link` varchar(255) DEFAULT NULL,
  `apt_group_techniques_techniques_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`reference_id`,`apt_group_techniques_techniques_id`),
  KEY `fk_apt_references_apt_group_techniques1_idx` (`apt_group_techniques_techniques_id`),
  CONSTRAINT `fk_apt_references_apt_group_techniques1` FOREIGN KEY (`apt_group_techniques_techniques_id`) REFERENCES `apt_group_techniques` (`techniques_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `apt_references`
--

LOCK TABLES `apt_references` WRITE;
/*!40000 ALTER TABLE `apt_references` DISABLE KEYS */;
/*!40000 ALTER TABLE `apt_references` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `attack_campaign`
--

DROP TABLE IF EXISTS `attack_campaign`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attack_campaign` (
  `id` int NOT NULL AUTO_INCREMENT,
  `associated_indicators` int DEFAULT NULL,
  `case_name` varchar(255) DEFAULT NULL,
  `method_tool_used` longtext,
  `sources` longtext,
  `special_characteristics` longtext,
  `summary` longtext,
  `created_date` datetime DEFAULT NULL,
  `modified_date` datetime DEFAULT NULL,
  `source_id` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UK_qx11o2rnfqllloj3lu11oxnh5` (`case_name`)
) ENGINE=InnoDB AUTO_INCREMENT=2060 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attack_campaign`
--

LOCK TABLES `attack_campaign` WRITE;
/*!40000 ALTER TABLE `attack_campaign` DISABLE KEYS */;
/*!40000 ALTER TABLE `attack_campaign` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `attack_campaign_countries`
--

DROP TABLE IF EXISTS `attack_campaign_countries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attack_campaign_countries` (
  `attack_campaigns_id` int NOT NULL,
  `countries_id` int NOT NULL,
  KEY `FK6k5ea5wrsktlto0l7ftoaaxnr` (`countries_id`),
  KEY `FK4g7b7w488k1doyrw5r3ci4yex` (`attack_campaigns_id`),
  CONSTRAINT `FK4g7b7w488k1doyrw5r3ci4yex` FOREIGN KEY (`attack_campaigns_id`) REFERENCES `attack_campaign` (`id`),
  CONSTRAINT `FK6k5ea5wrsktlto0l7ftoaaxnr` FOREIGN KEY (`countries_id`) REFERENCES `country_lkp` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attack_campaign_countries`
--

LOCK TABLES `attack_campaign_countries` WRITE;
/*!40000 ALTER TABLE `attack_campaign_countries` DISABLE KEYS */;
/*!40000 ALTER TABLE `attack_campaign_countries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `attack_campaign_sectors`
--

DROP TABLE IF EXISTS `attack_campaign_sectors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attack_campaign_sectors` (
  `attack_campaigns_id` int NOT NULL,
  `sectors_id` int NOT NULL,
  KEY `FK45ag3bmho9er14cul69fi3eli` (`sectors_id`),
  KEY `FKbm0hydxo34ujft02u9rb29i76` (`attack_campaigns_id`),
  CONSTRAINT `FK45ag3bmho9er14cul69fi3eli` FOREIGN KEY (`sectors_id`) REFERENCES `sector_lkp` (`id`),
  CONSTRAINT `FKbm0hydxo34ujft02u9rb29i76` FOREIGN KEY (`attack_campaigns_id`) REFERENCES `attack_campaign` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attack_campaign_sectors`
--

LOCK TABLES `attack_campaign_sectors` WRITE;
/*!40000 ALTER TABLE `attack_campaign_sectors` DISABLE KEYS */;
/*!40000 ALTER TABLE `attack_campaign_sectors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `country_lkp`
--

DROP TABLE IF EXISTS `country_lkp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `country_lkp` (
  `id` int NOT NULL,
  `cca2` varchar(255) DEFAULT NULL,
  `cca3` varchar(255) DEFAULT NULL,
  `country_name` varchar(255) DEFAULT NULL,
  `region` varchar(255) DEFAULT NULL,
  `sub_region` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UK_m7svrihrrk0q18knx0vs464xa` (`cca2`),
  UNIQUE KEY `UK_i9qsnc3dfckjrcxxvq6jbj1rb` (`cca3`),
  UNIQUE KEY `UK_jt192ag5t7g7ll8vccqgqc0sy` (`country_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `country_lkp`
--

LOCK TABLES `country_lkp` WRITE;
/*!40000 ALTER TABLE `country_lkp` DISABLE KEYS */;
/*!40000 ALTER TABLE `country_lkp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ioc`
--

DROP TABLE IF EXISTS `ioc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ioc` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` datetime DEFAULT NULL,
  `file_description` varchar(255) DEFAULT NULL,
  `file_type` varchar(255) DEFAULT NULL,
  `malware_signature_type` varchar(255) DEFAULT NULL,
  `md5` varchar(255) DEFAULT NULL,
  `sha1` varchar(255) DEFAULT NULL,
  `sha_256` varchar(255) DEFAULT NULL,
  `target_machine` varchar(255) DEFAULT NULL,
  `value` longtext,
  `attack_campaign_id` int DEFAULT NULL,
  `ioc_type_lkp_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKise0y07mwmdyyau8spsq6urgq` (`attack_campaign_id`),
  KEY `FKafa0stnwjcrku3kgusd6ulnv2` (`ioc_type_lkp_id`),
  CONSTRAINT `FKafa0stnwjcrku3kgusd6ulnv2` FOREIGN KEY (`ioc_type_lkp_id`) REFERENCES `ioc_type_lkp` (`id`),
  CONSTRAINT `FKise0y07mwmdyyau8spsq6urgq` FOREIGN KEY (`attack_campaign_id`) REFERENCES `attack_campaign` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=113519 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ioc`
--

LOCK TABLES `ioc` WRITE;
/*!40000 ALTER TABLE `ioc` DISABLE KEYS */;
/*!40000 ALTER TABLE `ioc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ioc_type_lkp`
--

DROP TABLE IF EXISTS `ioc_type_lkp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ioc_type_lkp` (
  `id` int NOT NULL,
  `value` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UK_lwxd57v5769ll74693pwv0ska` (`value`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ioc_type_lkp`
--

LOCK TABLES `ioc_type_lkp` WRITE;
/*!40000 ALTER TABLE `ioc_type_lkp` DISABLE KEYS */;
/*!40000 ALTER TABLE `ioc_type_lkp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `procedure_example`
--

DROP TABLE IF EXISTS `procedure_example`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `procedure_example` (
  `id` varchar(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `reference` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `procedure_example`
--

LOCK TABLES `procedure_example` WRITE;
/*!40000 ALTER TABLE `procedure_example` DISABLE KEYS */;
/*!40000 ALTER TABLE `procedure_example` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `region_preference`
--

DROP TABLE IF EXISTS `region_preference`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `region_preference` (
  `id` int NOT NULL AUTO_INCREMENT,
  `enabled` tinyint(1) DEFAULT '1',
  `value` varchar(255) DEFAULT NULL,
  `user_preference_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK9m6rg67s0ha9veg3chkcw2pjh` (`user_preference_id`),
  CONSTRAINT `FK9m6rg67s0ha9veg3chkcw2pjh` FOREIGN KEY (`user_preference_id`) REFERENCES `user_preference` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=115 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `region_preference`
--

LOCK TABLES `region_preference` WRITE;
/*!40000 ALTER TABLE `region_preference` DISABLE KEYS */;
/*!40000 ALTER TABLE `region_preference` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sector_lkp`
--

DROP TABLE IF EXISTS `sector_lkp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sector_lkp` (
  `id` int NOT NULL,
  `value` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UK_hluwp9p17ucwev4krhf1315nm` (`value`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sector_lkp`
--

LOCK TABLES `sector_lkp` WRITE;
/*!40000 ALTER TABLE `sector_lkp` DISABLE KEYS */;
/*!40000 ALTER TABLE `sector_lkp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sector_preference`
--

DROP TABLE IF EXISTS `sector_preference`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sector_preference` (
  `id` int NOT NULL AUTO_INCREMENT,
  `enabled` tinyint(1) DEFAULT '1',
  `sector_id` int DEFAULT NULL,
  `value` varchar(255) DEFAULT NULL,
  `user_preference_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FKswjj7ocr6gy3h5fk2by0l1ve7` (`user_preference_id`),
  CONSTRAINT `FKswjj7ocr6gy3h5fk2by0l1ve7` FOREIGN KEY (`user_preference_id`) REFERENCES `user_preference` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=628 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sector_preference`
--

LOCK TABLES `sector_preference` WRITE;
/*!40000 ALTER TABLE `sector_preference` DISABLE KEYS */;
/*!40000 ALTER TABLE `sector_preference` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `software_used`
--

DROP TABLE IF EXISTS `software_used`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `software_used` (
  `Id` varchar(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `reference` varchar(255) DEFAULT NULL,
  `techniques` longtext,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `software_used`
--

LOCK TABLES `software_used` WRITE;
/*!40000 ALTER TABLE `software_used` DISABLE KEYS */;
/*!40000 ALTER TABLE `software_used` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sub_techniques`
--

DROP TABLE IF EXISTS `sub_techniques`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sub_techniques` (
  `id` varchar(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sub_techniques`
--

LOCK TABLES `sub_techniques` WRITE;
/*!40000 ALTER TABLE `sub_techniques` DISABLE KEYS */;
/*!40000 ALTER TABLE `sub_techniques` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `technique`
--

DROP TABLE IF EXISTS `technique`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `technique` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `technique_id` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UK_rqt5ranm0aokv4e06269fg608` (`technique_id`)
) ENGINE=InnoDB AUTO_INCREMENT=531 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `technique`
--

LOCK TABLES `technique` WRITE;
/*!40000 ALTER TABLE `technique` DISABLE KEYS */;
/*!40000 ALTER TABLE `technique` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `technique_technique_types`
--

DROP TABLE IF EXISTS `technique_technique_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `technique_technique_types` (
  `techniques_id` int NOT NULL,
  `technique_types_id` int NOT NULL,
  KEY `FKjunua6uxh8k1diptul8bbn14v` (`technique_types_id`),
  KEY `FK1px4fmi3eww607a1xy32q57rs` (`techniques_id`),
  CONSTRAINT `FK1px4fmi3eww607a1xy32q57rs` FOREIGN KEY (`techniques_id`) REFERENCES `technique` (`id`),
  CONSTRAINT `FKjunua6uxh8k1diptul8bbn14v` FOREIGN KEY (`technique_types_id`) REFERENCES `technique_type_lkp` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `technique_technique_types`
--

LOCK TABLES `technique_technique_types` WRITE;
/*!40000 ALTER TABLE `technique_technique_types` DISABLE KEYS */;
/*!40000 ALTER TABLE `technique_technique_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `technique_type_lkp`
--

DROP TABLE IF EXISTS `technique_type_lkp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `technique_type_lkp` (
  `id` int NOT NULL,
  `value` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UK_9utlrpy2raryqbcqisfpox1xn` (`value`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `technique_type_lkp`
--

LOCK TABLES `technique_type_lkp` WRITE;
/*!40000 ALTER TABLE `technique_type_lkp` DISABLE KEYS */;
/*!40000 ALTER TABLE `technique_type_lkp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_preference`
--

DROP TABLE IF EXISTS `user_preference`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_preference` (
  `id` int NOT NULL AUTO_INCREMENT,
  `campaign_region_notif` tinyint(1) NOT NULL DEFAULT '0',
  `campaign_sector_notif` tinyint(1) NOT NULL DEFAULT '0',
  `created` datetime DEFAULT NULL,
  `value` varchar(255) DEFAULT NULL,
  `group_region_notif` tinyint(1) NOT NULL DEFAULT '0',
  `group_sector_notif` tinyint(1) NOT NULL DEFAULT '0',
  `last_modified` datetime DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `attack_region_frequency` int NOT NULL DEFAULT '0',
  `attack_region_last_processed` datetime DEFAULT NULL,
  `attack_sector_frequency` int NOT NULL DEFAULT '0',
  `attack_sector_last_processed` datetime DEFAULT NULL,
  `group_region_frequency` int NOT NULL DEFAULT '0',
  `group_region_last_processed` datetime DEFAULT NULL,
  `group_sector_frequency` int NOT NULL DEFAULT '0',
  `group_sector_last_processed` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UK_mxcnwvuyw0aqwyt2940cwhidc` (`value`),
  UNIQUE KEY `UK_s5oeayykfc7bpkpdwyrffwcqx` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_preference`
--

LOCK TABLES `user_preference` WRITE;
/*!40000 ALTER TABLE `user_preference` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_preference` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-05 14:37:17
