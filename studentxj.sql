-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: studentxj
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Temporary view structure for view `c_g`
--

DROP TABLE IF EXISTS `c_g`;
/*!50001 DROP VIEW IF EXISTS `c_g`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `c_g` AS SELECT 
 1 AS `Cno`,
 1 AS `Gavg`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `course` (
  `Cno` varchar(20) NOT NULL,
  `Cname` varchar(20) NOT NULL,
  `Tno` varchar(20) NOT NULL,
  `ccredit` float DEFAULT NULL,
  PRIMARY KEY (`Cno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course`
--

LOCK TABLES `course` WRITE;
/*!40000 ALTER TABLE `course` DISABLE KEYS */;
INSERT INTO `course` VALUES ('1','计组','1001',5),('2','计网','1002',3),('3','计操','1003',4),('4','算法','1004',3),('5','数据库','1005',5),('6','数据结构','1006',4.5);
/*!40000 ALTER TABLE `course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `s_g`
--

DROP TABLE IF EXISTS `s_g`;
/*!50001 DROP VIEW IF EXISTS `s_g`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `s_g` AS SELECT 
 1 AS `Sno`,
 1 AS `Gavg`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `sc`
--

DROP TABLE IF EXISTS `sc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sc` (
  `Sno` varchar(20) NOT NULL,
  `Cno` varchar(20) NOT NULL,
  `grade` int DEFAULT NULL,
  `ccredit` float DEFAULT NULL,
  PRIMARY KEY (`Sno`,`Cno`),
  UNIQUE KEY `SCno` (`Sno`,`Cno` DESC),
  KEY `Cno` (`Cno`),
  CONSTRAINT `sc_ibfk_1` FOREIGN KEY (`Sno`) REFERENCES `student` (`Sno`),
  CONSTRAINT `sc_ibfk_2` FOREIGN KEY (`Cno`) REFERENCES `course` (`Cno`),
  CONSTRAINT `sc_chk_1` CHECK (((`grade` >= 0) and (`grade` <= 100)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sc`
--

LOCK TABLES `sc` WRITE;
/*!40000 ALTER TABLE `sc` DISABLE KEYS */;
INSERT INTO `sc` VALUES ('10001','1',94,5),('10001','2',90,3),('10001','3',88,4),('10002','1',90,5),('10002','3',88,4),('10003','5',87,5),('10003','6',94,4.5),('1004','1',96,5),('1004','3',88,4),('1004','4',99,3);
/*!40000 ALTER TABLE `sc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `Sno` varchar(20) NOT NULL,
  `Sname` varchar(20) NOT NULL,
  `Ssex` varchar(2) DEFAULT NULL,
  `Sclass` varchar(20) DEFAULT NULL,
  `Smajor` varchar(20) DEFAULT NULL,
  `Sdept` varchar(10) DEFAULT NULL,
  `Sbir` date DEFAULT NULL,
  `Stele` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`Sno`),
  UNIQUE KEY `Stusno` (`Sno`),
  CONSTRAINT `student_chk_1` CHECK ((`Ssex` in (_utf8mb4'男',_utf8mb4'女'))),
  CONSTRAINT `student_chk_2` CHECK (regexp_like(`Stele`,_utf8mb4'^[0-9]+$'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('10001','张三','男','01','计算机科学与技术','计算机学院','2001-01-01','190'),('10002','李四','男','02','自动化','自动化学院','2001-01-01','288'),('10003','王五','男','03','软件工程','软件学院','2001-03-03','190'),('1004','张一','男','04','应用数学','数学学院','2001-02-02','222');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `c_g`
--

/*!50001 DROP VIEW IF EXISTS `c_g`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_unicode_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `c_g` (`Cno`,`Gavg`) AS select `sc`.`Cno` AS `Cno`,avg(`sc`.`grade`) AS `AVG(grade)` from `sc` group by `sc`.`Cno` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `s_g`
--

/*!50001 DROP VIEW IF EXISTS `s_g`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_unicode_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `s_g` (`Sno`,`Gavg`) AS select `sc`.`Sno` AS `Sno`,avg(`sc`.`grade`) AS `AVG(grade)` from `sc` group by `sc`.`Sno` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-02  3:23:06
