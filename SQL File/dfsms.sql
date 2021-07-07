-- MySQL dump 10.13  Distrib 8.0.23, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: dfsms
-- ------------------------------------------------------
-- Server version	8.0.23-0ubuntu0.20.04.1

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
-- Table structure for table `tbladmin`
--

DROP TABLE IF EXISTS `tbladmin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbladmin` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `AdminName` varchar(45) DEFAULT NULL,
  `UserName` char(45) DEFAULT NULL,
  `MobileNumber` bigint DEFAULT NULL,
  `Email` varchar(120) DEFAULT NULL,
  `Password` varchar(120) DEFAULT NULL,
  `AdminRegdate` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `UpdationDate` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbladmin`
--

LOCK TABLES `tbladmin` WRITE;
/*!40000 ALTER TABLE `tbladmin` DISABLE KEYS */;
INSERT INTO `tbladmin` VALUES (1,'Admin','admin',1234567899,'admin@test.com','f925916e2754e5e03f75dd58a5733251','2019-12-22 18:30:00','2019-12-25 14:56:18');
/*!40000 ALTER TABLE `tbladmin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tblcategory`
--

DROP TABLE IF EXISTS `tblcategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tblcategory` (
  `id` int NOT NULL AUTO_INCREMENT,
  `CategoryName` varchar(200) DEFAULT NULL,
  `CategoryCode` varchar(50) DEFAULT NULL,
  `PostingDate` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblcategory`
--

LOCK TABLES `tblcategory` WRITE;
/*!40000 ALTER TABLE `tblcategory` DISABLE KEYS */;
INSERT INTO `tblcategory` VALUES (13,'Milk','MK01','2021-04-21 17:18:07'),(14,'Butter','BT01','2021-04-21 17:19:57');
/*!40000 ALTER TABLE `tblcategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tblcompany`
--

DROP TABLE IF EXISTS `tblcompany`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tblcompany` (
  `id` int NOT NULL AUTO_INCREMENT,
  `CompanyName` varchar(150) DEFAULT NULL,
  `PostingDate` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblcompany`
--

LOCK TABLES `tblcompany` WRITE;
/*!40000 ALTER TABLE `tblcompany` DISABLE KEYS */;
INSERT INTO `tblcompany` VALUES (12,'Nastle','2021-04-21 17:18:40'),(13,'olpers','2021-04-21 17:20:26'),(14,'milk pack','2021-04-26 16:21:15');
/*!40000 ALTER TABLE `tblcompany` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tblcustomers`
--

DROP TABLE IF EXISTS `tblcustomers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tblcustomers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `orderID` int NOT NULL,
  `Name` varchar(50) NOT NULL,
  `contact` varchar(50) DEFAULT NULL,
  `paymentMode` varchar(50) NOT NULL,
  `postingDate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblcustomers`
--

LOCK TABLES `tblcustomers` WRITE;
/*!40000 ALTER TABLE `tblcustomers` DISABLE KEYS */;
INSERT INTO `tblcustomers` VALUES (3,43230197,'ali',NULL,'cash','2021-05-04 21:09:46'),(4,30774051,'ahmed',NULL,'cash','2021-05-06 21:24:48'),(5,57967116,'khan','23345','cash','2021-05-08 20:06:02'),(6,22468175,'Naveed','03488993455','card','2021-05-08 20:59:20'),(7,72332462,'Naeem','34345345','card','2021-05-08 23:15:57'),(8,79780065,'Kaisar','345345346','cash','2021-06-08 19:19:30');
/*!40000 ALTER TABLE `tblcustomers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tblorders`
--

DROP TABLE IF EXISTS `tblorders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tblorders` (
  `id` int NOT NULL AUTO_INCREMENT,
  `orderID` int NOT NULL,
  `productName` varchar(50) NOT NULL,
  `category` varchar(50) NOT NULL,
  `company` varchar(50) NOT NULL,
  `quantity` int NOT NULL,
  `unitPrice` int NOT NULL,
  `total` int DEFAULT NULL,
  `postingDate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblorders`
--

LOCK TABLES `tblorders` WRITE;
/*!40000 ALTER TABLE `tblorders` DISABLE KEYS */;
INSERT INTO `tblorders` VALUES (1,43230197,'milk','Milk','milk pack',6,45,NULL,'2021-05-04 21:09:46'),(2,43230197,'fullCream','Butter','Nastle',1,200,NULL,'2021-05-04 21:09:46'),(3,43230197,'milk','Milk','milk pack',1,45,NULL,'2021-05-04 21:09:47'),(4,30774051,'fullCream','Butter','olpers',5,100,NULL,'2021-05-06 21:24:48'),(5,30774051,'milk','Milk','milk pack',4,45,NULL,'2021-05-06 21:24:48'),(6,57967116,'fullCream','Butter','olpers',3,100,NULL,'2021-05-08 20:06:03'),(7,22468175,'Balai','cream','milk pack',20,120,NULL,'2021-05-08 20:59:20'),(8,22468175,'milk','Milk','milk pack',50,45,NULL,'2021-05-08 20:59:20'),(9,22468175,'fullCream','Butter','olpers',10,100,NULL,'2021-05-08 20:59:20'),(10,72332462,'fullCream','Butter','olpers',50,100,NULL,'2021-05-08 23:15:57'),(11,79780065,'fullCream','Butter','olpers',50,100,NULL,'2021-06-08 19:19:30');
/*!40000 ALTER TABLE `tblorders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tblproducts`
--

DROP TABLE IF EXISTS `tblproducts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tblproducts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Category` varchar(255) DEFAULT NULL,
  `Company` varchar(255) DEFAULT NULL,
  `Product` varchar(255) DEFAULT NULL,
  `Pricing` int DEFAULT NULL,
  `PostingDate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblproducts`
--

LOCK TABLES `tblproducts` WRITE;
/*!40000 ALTER TABLE `tblproducts` DISABLE KEYS */;
INSERT INTO `tblproducts` VALUES (2,'Butter','olpers','fullCream',100,'2021-04-26 20:32:12'),(3,'Milk','milk pack','milk',45,'2021-04-26 21:23:00'),(4,'cream','milk pack','Balai',120,'2021-05-08 20:57:49'),(5,'Butter','Nastle','liaqat',50,'2021-05-08 22:07:08');
/*!40000 ALTER TABLE `tblproducts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tblproductstemp`
--

DROP TABLE IF EXISTS `tblproductstemp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tblproductstemp` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Category` varchar(255) DEFAULT NULL,
  `Company` varchar(255) DEFAULT NULL,
  `Product` varchar(255) DEFAULT NULL,
  `Pricing` int DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `PostingDate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblproductstemp`
--

LOCK TABLES `tblproductstemp` WRITE;
/*!40000 ALTER TABLE `tblproductstemp` DISABLE KEYS */;
/*!40000 ALTER TABLE `tblproductstemp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'dfsms'
--

--
-- Dumping routines for database 'dfsms'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-01  9:57:56
