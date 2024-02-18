-- MariaDB dump 10.19  Distrib 10.11.2-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: nomina
-- ------------------------------------------------------
-- Server version	10.11.2-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Areas`
--

DROP TABLE IF EXISTS `Areas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Areas` (
  `idArea` int(11) NOT NULL AUTO_INCREMENT,
  `NombreArea` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idArea`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Areas`
--

LOCK TABLES `Areas` WRITE;
/*!40000 ALTER TABLE `Areas` DISABLE KEYS */;
INSERT INTO `Areas` VALUES
(1,'Administracion'),
(2,'Ventas');
/*!40000 ALTER TABLE `Areas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Cargos`
--

DROP TABLE IF EXISTS `Cargos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Cargos` (
  `idCargo` int(11) NOT NULL AUTO_INCREMENT,
  `NombreCargo` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idCargo`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cargos`
--

LOCK TABLES `Cargos` WRITE;
/*!40000 ALTER TABLE `Cargos` DISABLE KEYS */;
INSERT INTO `Cargos` VALUES
(1,'Jefe'),
(2,'Aprendiz');
/*!40000 ALTER TABLE `Cargos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Descuentos`
--

DROP TABLE IF EXISTS `Descuentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Descuentos` (
  `idDescuento` int(11) NOT NULL AUTO_INCREMENT,
  `NombreDescuento` varchar(45) DEFAULT NULL,
  `CodigoDescuento` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idDescuento`),
  UNIQUE KEY `CodigoDescuento_UNIQUE` (`CodigoDescuento`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Descuentos`
--

LOCK TABLES `Descuentos` WRITE;
/*!40000 ALTER TABLE `Descuentos` DISABLE KEYS */;
INSERT INTO `Descuentos` VALUES
(1,'Pension','R1'),
(2,'Salud','R2');
/*!40000 ALTER TABLE `Descuentos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Devengados`
--

DROP TABLE IF EXISTS `Devengados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Devengados` (
  `idDevengado` int(11) NOT NULL AUTO_INCREMENT,
  `NombreDevengado` varchar(45) DEFAULT NULL,
  `CodigoDevengado` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idDevengado`),
  UNIQUE KEY `CodigoDevengado_UNIQUE` (`CodigoDevengado`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Devengados`
--

LOCK TABLES `Devengados` WRITE;
/*!40000 ALTER TABLE `Devengados` DISABLE KEYS */;
INSERT INTO `Devengados` VALUES
(1,'Salario','D1'),
(2,'Horas Extra','D2'),
(3,'Auxilio de Transporte','D3');
/*!40000 ALTER TABLE `Devengados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Empleados`
--

DROP TABLE IF EXISTS `Empleados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Empleados` (
  `idEmpleado` int(11) NOT NULL AUTO_INCREMENT,
  `NombreEmpleado` varchar(45) DEFAULT NULL,
  `DocumentoEmpleado` varchar(45) DEFAULT NULL,
  `CuentaEmpleado` varchar(45) DEFAULT NULL,
  `IngresoEmpleado` date DEFAULT NULL,
  `RetiroEmpleado` date DEFAULT NULL,
  `Areas_idAreas` int(11) NOT NULL,
  `Cargos_idCargos` int(11) NOT NULL,
  PRIMARY KEY (`idEmpleado`,`Areas_idAreas`,`Cargos_idCargos`),
  UNIQUE KEY `DocumentoEmpleado_UNIQUE` (`DocumentoEmpleado`),
  KEY `fk_Empleados_Areas1_idx` (`Areas_idAreas`),
  KEY `fk_Empleados_Cargos1_idx` (`Cargos_idCargos`),
  CONSTRAINT `fk_Empleados_Areas1` FOREIGN KEY (`Areas_idAreas`) REFERENCES `Areas` (`idArea`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Empleados_Cargos1` FOREIGN KEY (`Cargos_idCargos`) REFERENCES `Cargos` (`idCargo`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Empleados`
--

LOCK TABLES `Empleados` WRITE;
/*!40000 ALTER TABLE `Empleados` DISABLE KEYS */;
INSERT INTO `Empleados` VALUES
(1,'Jose Perez','1234','214365','2023-04-01',NULL,2,1),
(2,'María Gonzales','1235','325476','2023-04-02',NULL,1,2),
(3,'Maria Rosales','33333','56565656565','2023-04-20',NULL,1,2);
/*!40000 ALTER TABLE `Empleados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Empleados_has_Descuentos`
--

DROP TABLE IF EXISTS `Empleados_has_Descuentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Empleados_has_Descuentos` (
  `Empleados_idEmpleado` int(11) NOT NULL,
  `Descuentos_idDescuento` int(11) NOT NULL,
  `Valor` float DEFAULT NULL,
  `Observacion` text DEFAULT NULL,
  `aplica` bit(1) DEFAULT NULL,
  PRIMARY KEY (`Empleados_idEmpleado`,`Descuentos_idDescuento`),
  KEY `fk_Empleados_has_Descuentos_Descuentos1_idx` (`Descuentos_idDescuento`),
  KEY `fk_Empleados_has_Descuentos_Empleados1_idx` (`Empleados_idEmpleado`),
  CONSTRAINT `fk_Empleados_has_Descuentos_Descuentos1` FOREIGN KEY (`Descuentos_idDescuento`) REFERENCES `Descuentos` (`idDescuento`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Empleados_has_Descuentos_Empleados1` FOREIGN KEY (`Empleados_idEmpleado`) REFERENCES `Empleados` (`idEmpleado`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Empleados_has_Descuentos`
--

LOCK TABLES `Empleados_has_Descuentos` WRITE;
/*!40000 ALTER TABLE `Empleados_has_Descuentos` DISABLE KEYS */;
INSERT INTO `Empleados_has_Descuentos` VALUES
(1,1,90000,'cotiza por el minimo',''),
(1,2,80000,'cotiza por el minimo',''),
(2,1,100000,'cotiza por mas del minimo',''),
(2,2,100000,'cotiza por mas del minimo','');
/*!40000 ALTER TABLE `Empleados_has_Descuentos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Empleados_has_Devengados`
--

DROP TABLE IF EXISTS `Empleados_has_Devengados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Empleados_has_Devengados` (
  `Empleados_idEmpleado` int(11) NOT NULL,
  `Devengados_idDevengado` int(11) NOT NULL,
  `Valor` float DEFAULT NULL,
  `Observacion` text DEFAULT NULL,
  `aplica` bit(1) DEFAULT NULL,
  PRIMARY KEY (`Empleados_idEmpleado`,`Devengados_idDevengado`),
  KEY `fk_Empleados_has_Devengados_Devengados1_idx` (`Devengados_idDevengado`),
  KEY `fk_Empleados_has_Devengados_Empleados1_idx` (`Empleados_idEmpleado`),
  CONSTRAINT `fk_Empleados_has_Devengados_Devengados1` FOREIGN KEY (`Devengados_idDevengado`) REFERENCES `Devengados` (`idDevengado`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Empleados_has_Devengados_Empleados1` FOREIGN KEY (`Empleados_idEmpleado`) REFERENCES `Empleados` (`idEmpleado`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Empleados_has_Devengados`
--

LOCK TABLES `Empleados_has_Devengados` WRITE;
/*!40000 ALTER TABLE `Empleados_has_Devengados` DISABLE KEYS */;
INSERT INTO `Empleados_has_Devengados` VALUES
(1,1,1100000,'un salario minimo',''),
(1,2,300000,'realizo varias horas extra',''),
(1,3,140000,'va en bus todos los dias',''),
(2,1,1000000,'un salario minimo',''),
(2,2,300000,'realizo varias horas extra','');
/*!40000 ALTER TABLE `Empleados_has_Devengados` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-21 12:34:26
