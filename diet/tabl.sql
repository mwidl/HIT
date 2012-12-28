-- MySQL dump 10.13  Distrib 5.5.28, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: HIT
-- ------------------------------------------------------
-- Server version	5.5.28-0ubuntu0.12.04.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `inputs_condition_inst`
--

DROP TABLE IF EXISTS `inputs_condition_inst`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `inputs_condition_inst` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Condition_id` int(11) NOT NULL,
  `Date_id` int(11) NOT NULL,
  `Time` time NOT NULL,
  `Time_End` time DEFAULT NULL,
  `Poss_HIT_Symptome` tinyint(1) DEFAULT NULL,
  `Strength` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `inputs_condition_inst_19296236` (`Condition_id`),
  KEY `inputs_condition_inst_74e2015c` (`Date_id`),
  CONSTRAINT `Condition_id_refs_id_9dd4768b` FOREIGN KEY (`Condition_id`) REFERENCES `inputs_condition` (`id`),
  CONSTRAINT `Date_id_refs_id_72f080cf` FOREIGN KEY (`Date_id`) REFERENCES `inputs_diary` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inputs_condition_inst`
--

LOCK TABLES `inputs_condition_inst` WRITE;
/*!40000 ALTER TABLE `inputs_condition_inst` DISABLE KEYS */;
INSERT INTO `inputs_condition_inst` VALUES (1,1,1,'00:00:00','00:00:00',1,4),(2,1,1,'00:00:00','00:00:00',1,1),(3,1,1,'00:00:00','00:00:00',1,1);
/*!40000 ALTER TABLE `inputs_condition_inst` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inputs_condition_inst_Locations`
--

DROP TABLE IF EXISTS `inputs_condition_inst_Locations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `inputs_condition_inst_Locations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `condition_inst_id` int(11) NOT NULL,
  `bodypart_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `condition_inst_id` (`condition_inst_id`,`bodypart_id`),
  KEY `inputs_condition_inst_Locations_d3e6916c` (`condition_inst_id`),
  KEY `inputs_condition_inst_Locations_928846b3` (`bodypart_id`),
  CONSTRAINT `condition_inst_id_refs_id_bd432c8e` FOREIGN KEY (`condition_inst_id`) REFERENCES `inputs_condition_inst` (`id`),
  CONSTRAINT `bodypart_id_refs_id_ecdd8447` FOREIGN KEY (`bodypart_id`) REFERENCES `inputs_bodypart` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inputs_condition_inst_Locations`
--

LOCK TABLES `inputs_condition_inst_Locations` WRITE;
/*!40000 ALTER TABLE `inputs_condition_inst_Locations` DISABLE KEYS */;
INSERT INTO `inputs_condition_inst_Locations` VALUES (1,3,3);
/*!40000 ALTER TABLE `inputs_condition_inst_Locations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2012-12-27 16:16:01
