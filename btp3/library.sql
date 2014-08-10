-- MySQL dump 10.13  Distrib 5.5.34, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: library
-- ------------------------------------------------------
-- Server version	5.5.34-0ubuntu0.13.04.1

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
-- Table structure for table `Book_Copy`
--

DROP TABLE IF EXISTS `Book_Copy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Book_Copy` (
  `Book_ID` varchar(13) NOT NULL,
  `ISBN` varchar(13) DEFAULT NULL,
  `isReference` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`Book_ID`),
  KEY `ISBN` (`ISBN`),
  CONSTRAINT `Book_Copy_ibfk_1` FOREIGN KEY (`ISBN`) REFERENCES `Book_Type` (`ISBN`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Book_Copy`
--

LOCK TABLES `Book_Copy` WRITE;
/*!40000 ALTER TABLE `Book_Copy` DISABLE KEYS */;
INSERT INTO `Book_Copy` VALUES ('1','1234',0),('10','12333',1),('2','1234',0),('3','1234',1),('4','1235',0),('5','1235',0),('6','1235',1),('7','1236',1),('8','1237',0),('9','12333',0);
/*!40000 ALTER TABLE `Book_Copy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Book_Type`
--

DROP TABLE IF EXISTS `Book_Type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Book_Type` (
  `ISBN` varchar(13) NOT NULL,
  `BookAuthor` varchar(255) DEFAULT NULL,
  `BookName` varchar(255) DEFAULT NULL,
  `BookEdition` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`ISBN`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Book_Type`
--

LOCK TABLES `Book_Type` WRITE;
/*!40000 ALTER TABLE `Book_Type` DISABLE KEYS */;
INSERT INTO `Book_Type` VALUES ('12333','Navathe','Fundamentals of Database Systems','5'),('1234','J.K.Rowling','Harry Potter','1'),('1235','J.K.Rowling','Harry Potter','2'),('1236','J.K.Rowling','Harry Potter','3'),('1237','J.K.Rowling','Harry Potter','4');
/*!40000 ALTER TABLE `Book_Type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customer`
--

DROP TABLE IF EXISTS `Customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Customer` (
  `Customer_ID` varchar(13) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `roll_no` varchar(13) DEFAULT NULL,
  PRIMARY KEY (`Customer_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer`
--

LOCK TABLES `Customer` WRITE;
/*!40000 ALTER TABLE `Customer` DISABLE KEYS */;
INSERT INTO `Customer` VALUES ('1','Lakshit','l@s.iiit.ac.in','201101107'),('2','Aayush','a@s.iiit.ac.in','201101224'),('3','XYZ','XYZ@iiit.ac.in','');
/*!40000 ALTER TABLE `Customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Issue`
--

DROP TABLE IF EXISTS `Issue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Issue` (
  `Issue_ID` varchar(13) NOT NULL,
  `Book_ID` varchar(13) DEFAULT NULL,
  `Issue_date` date DEFAULT NULL,
  `Customer_ID` varchar(13) DEFAULT NULL,
  `expiry_date` date DEFAULT NULL,
  `Staff_ID` varchar(13) DEFAULT NULL,
  PRIMARY KEY (`Issue_ID`),
  KEY `Book_ID` (`Book_ID`),
  KEY `Customer_ID` (`Customer_ID`),
  KEY `Staff_ID` (`Staff_ID`),
  CONSTRAINT `Issue_ibfk_1` FOREIGN KEY (`Book_ID`) REFERENCES `Book_Copy` (`Book_ID`),
  CONSTRAINT `Issue_ibfk_2` FOREIGN KEY (`Customer_ID`) REFERENCES `Customer` (`Customer_ID`),
  CONSTRAINT `Issue_ibfk_3` FOREIGN KEY (`Staff_ID`) REFERENCES `Staff` (`Staff_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Issue`
--

LOCK TABLES `Issue` WRITE;
/*!40000 ALTER TABLE `Issue` DISABLE KEYS */;
INSERT INTO `Issue` VALUES ('1','1','0000-00-00','1','0000-00-00','1'),('2','2','0000-00-00','1','0000-00-00','1');
/*!40000 ALTER TABLE `Issue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Returns`
--

DROP TABLE IF EXISTS `Returns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Returns` (
  `Book_ID` varchar(13) DEFAULT NULL,
  `Issue_ID` varchar(13) DEFAULT NULL,
  `Returns_Date` date DEFAULT NULL,
  `Staff_ID` varchar(13) DEFAULT NULL,
  KEY `Staff_ID` (`Staff_ID`),
  KEY `Book_ID` (`Book_ID`),
  KEY `Issue_ID` (`Issue_ID`),
  CONSTRAINT `Returns_ibfk_1` FOREIGN KEY (`Staff_ID`) REFERENCES `Staff` (`Staff_ID`),
  CONSTRAINT `Returns_ibfk_2` FOREIGN KEY (`Book_ID`) REFERENCES `Book_Copy` (`Book_ID`),
  CONSTRAINT `Returns_ibfk_3` FOREIGN KEY (`Issue_ID`) REFERENCES `Issue` (`Issue_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Returns`
--

LOCK TABLES `Returns` WRITE;
/*!40000 ALTER TABLE `Returns` DISABLE KEYS */;
INSERT INTO `Returns` VALUES ('1','1','0000-00-00','2');
/*!40000 ALTER TABLE `Returns` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Staff`
--

DROP TABLE IF EXISTS `Staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Staff` (
  `Staff_ID` varchar(13) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `phone_number` varchar(14) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Staff_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Staff`
--

LOCK TABLES `Staff` WRITE;
/*!40000 ALTER TABLE `Staff` DISABLE KEYS */;
INSERT INTO `Staff` VALUES ('1','Ln1','9999955555','Ln1@iiit.ac.in'),('2','Ln2','9999955553','Ln2@iiit.ac.in');
/*!40000 ALTER TABLE `Staff` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-04-04 22:32:28
