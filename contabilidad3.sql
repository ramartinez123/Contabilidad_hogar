-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 09-12-2023 a las 15:39:23
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.1.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `contabilidad3`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `accountingitems`
--

CREATE TABLE `accountingitems` (
  `idAccountingItem` int(4) NOT NULL,
  `accountingItem` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `accountingitems`
--

INSERT INTO `accountingitems` (`idAccountingItem`, `accountingItem`) VALUES
(1, 'Bancos $'),
(2, 'Disponibilidades $'),
(3, 'Puntos $'),
(4, 'Inversiones $'),
(5, 'Acreencias $'),
(6, 'Dif Cotiz $'),
(21, 'Bancos u$s'),
(22, 'Disponibilidades u$s'),
(23, 'Aerolineas u$s'),
(24, 'Inversiones u$s'),
(25, 'Acreencias u$s'),
(41, 'Muebles $'),
(51, 'Muebles u$s'),
(52, 'Inmuebles u$s'),
(101, 'Capital'),
(201, 'Prestamos a pagar'),
(202, 'Prestamos'),
(203, 'Deudas a pagar'),
(204, 'Deudas'),
(301, 'Hogar'),
(302, 'Salud'),
(303, 'Financiero'),
(304, 'Calidad de vida'),
(305, 'Comida'),
(306, 'Educacion'),
(307, 'Internet'),
(308, 'Viajes'),
(309, 'Varios'),
(401, 'Ventas'),
(402, 'InversionesGanadas'),
(403, 'DifCotizacion'),
(404, 'Sueldos');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `accountingmethods`
--

CREATE TABLE `accountingmethods` (
  `idAccountingMethod` int(4) NOT NULL,
  `accountingMethod` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `accountingmethods`
--

INSERT INTO `accountingmethods` (`idAccountingMethod`, `accountingMethod`) VALUES
(1, 'Devengado'),
(2, 'Percibido');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `accountingtransactions`
--

CREATE TABLE `accountingtransactions` (
  `idAccountingTransaction` int(7) NOT NULL,
  `FkidVAccount` int(4) NOT NULL,
  `FkidSubAccount` int(4) DEFAULT NULL,
  `FkidVIncreasedBY` int(4) NOT NULL,
  `accruedDate` date NOT NULL,
  `amount` int(11) NOT NULL,
  `FKidCountry` int(4) NOT NULL DEFAULT 1,
  `FkidCity` int(4) NOT NULL DEFAULT 1,
  `comment` varchar(25) DEFAULT NULL,
  `FkidDues` int(4) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `accountingtransactions`
--

INSERT INTO `accountingtransactions` (`idAccountingTransaction`, `FkidVAccount`, `FkidSubAccount`, `FkidVIncreasedBY`, `accruedDate`, `amount`, `FKidCountry`, `FkidCity`, `comment`, `FkidDues`) VALUES
(1124, 2, 0, 1, '2023-09-10', 300000, 1, 1, 'Mi primer sueldo', 0),
(1125, 424, 0, 2, '2023-09-10', 300000, 1, 1, 'Mi primer sueldo', 0),
(1126, 1, 0, 1, '2023-09-10', 50000, 1, 1, 'Extraccion', 0),
(1127, 2, 0, 2, '2023-09-10', 50000, 1, 1, 'Extraccion', 0),
(1128, 301, 0, 1, '2023-09-10', 20000, 1, 1, '', 0),
(1129, 1, 0, 2, '2023-09-10', 20000, 1, 1, '', 0),
(1130, 341, 0, 1, '2023-09-10', 10000, 1, 1, '', 0),
(1131, 213, 0, 2, '2023-09-10', 10000, 1, 1, '', 0),
(1160, 2, 0, 1, '2023-10-10', 300000, 1, 1, 'Mi segundo sueldo', 0),
(1161, 424, 0, 2, '2023-10-10', 300000, 1, 1, 'Mi segundo sueldo', 0),
(1162, 331, 0, 1, '2023-10-10', 1000, 1, 1, '', 0),
(1163, 210, 0, 2, '2023-10-10', 1000, 1, 1, '', 0),
(1164, 341, 0, 1, '2023-10-10', 5000, 1, 1, '', 0),
(1165, 213, 0, 2, '2023-10-10', 5000, 1, 1, '', 0),
(1166, 5, 0, 1, '2023-10-10', 300, 1, 1, '', 0),
(1167, 426, 0, 2, '2023-10-10', 300, 1, 1, '', 0),
(1168, 304, 0, 1, '2023-10-10', 3000, 1, 1, 'fgfg', 0),
(1169, 201, 0, 2, '2023-10-10', 3000, 1, 1, 'fgfg', 0),
(1170, 1, 0, 1, '0000-00-00', 80, 1, 1, '', 0),
(1171, 1, 0, 1, '0000-00-00', 80, 1, 1, '', 0),
(1172, 1, 0, 1, '0000-00-00', 80, 1, 1, '', 0),
(1173, 1, 0, 1, '0000-00-00', 80, 1, 1, '7', 0),
(1175, 1, 0, 1, '0000-00-00', 80, 1, 1, '7', 0),
(1176, 1, 0, 1, '0000-00-00', 80, 1, 1, '7', 0),
(1177, 1, 0, 1, '2023-02-01', 80, 1, 1, '7', 0),
(1178, 1, 0, 1, '2023-02-01', 80, 1, 1, 'es el testing', 0),
(1179, 1, 0, 1, '2023-02-01', 80, 1, 1, 'es el testing', 0),
(1180, 1, 0, 1, '2023-02-01', 80, 1, 1, 'es el testing', 1),
(1181, 1, 0, 1, '2023-02-01', 80, 1, 1, 'es el testing', 1),
(1182, 1, 0, 1, '2023-02-01', 80, 1, 1, 'es el testing', 1),
(1183, 1, 0, 1, '2023-02-01', 80, 1, 1, 'es el testing', 1),
(1184, 1, 0, 1, '2023-02-01', 80, 1, 1, 'es el testing', 1),
(1185, 1, 0, 1, '2023-02-01', 80, 1, 1, 'es el testing', 1),
(1186, 1, 0, 1, '2023-02-01', 80, 1, 1, 'es el testing', 1),
(1187, 1, 0, 1, '2023-02-01', 80, 1, 1, 'es el testing', 1),
(1188, 1, 0, 1, '2023-02-01', 80, 1, 1, 'es el testing', 1),
(1189, 1, 0, 1, '2023-02-01', 80, 1, 1, 'es el testing', 1),
(1190, 1, 0, 1, '2023-02-01', 80, 1, 1, 'es el testing', 1),
(1191, 1, 0, 1, '2023-02-01', 80, 1, 1, 'es el testing', 1),
(1192, 1, 0, 1, '2023-02-01', 80, 1, 1, 'es el testing', 1),
(1193, 1, 0, 1, '2023-02-01', 80, 1, 1, 'es el testing', 1),
(1194, 1, 0, 1, '2023-02-01', 80, 1, 1, 'es el testing', 1),
(1195, 1, 0, 1, '2023-02-01', 80, 1, 1, 'es el testing', 1),
(1196, 1, 0, 1, '2023-02-01', 80, 1, 1, 'es el testing', 1),
(1197, 1, 0, 1, '2023-02-01', 80, 1, 1, 'es el testing', 1),
(1198, 1, 0, 1, '2023-02-01', 80, 1, 1, 'es el testing', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `accounts`
--

CREATE TABLE `accounts` (
  `idAccount` int(4) NOT NULL,
  `account` varchar(25) NOT NULL,
  `FkidAccountType` int(4) NOT NULL,
  `FkidAccountingItem` int(4) NOT NULL,
  `FkidIncreasedBy` int(4) NOT NULL,
  `FkidAccountingMethod` int(4) NOT NULL,
  `FkidCurrency` int(4) NOT NULL,
  `Detalle` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `accounts`
--

INSERT INTO `accounts` (`idAccount`, `account`, `FkidAccountType`, `FkidAccountingItem`, `FkidIncreasedBy`, `FkidAccountingMethod`, `FkidCurrency`, `Detalle`) VALUES
(0, 'Sin Cuenta', 1, 1, 1, 1, 1, ''),
(1, 'Caja', 1, 2, 1, 1, 1, ''),
(2, 'PBancoGalicia', 1, 1, 1, 1, 1, 'Cuenta en Pesos de B'),
(3, 'PBancoSantander', 1, 1, 1, 1, 1, ''),
(4, 'PBancoFrances', 1, 1, 1, 1, 1, ''),
(5, 'DBancoGalicia', 1, 21, 1, 1, 3, ''),
(6, 'DBancoSantander', 1, 21, 1, 1, 3, ''),
(7, 'DBancoFrances', 1, 21, 1, 1, 3, ''),
(8, 'D', 1, 22, 1, 1, 4, ''),
(9, 'E', 1, 22, 1, 1, 6, ''),
(10, 'L', 1, 22, 1, 1, 7, ''),
(11, 'R', 1, 22, 1, 1, 8, ''),
(12, 'C', 1, 22, 1, 1, 9, ''),
(13, 'Sube', 1, 2, 1, 1, 1, ''),
(14, 'Caja Transitoria', 1, 2, 1, 1, 1, ''),
(15, 'TBanco Galicia', 1, 1, 1, 1, 1, ''),
(16, 'TBanco Santander', 1, 1, 1, 1, 1, ''),
(17, 'TBanco Frances', 1, 1, 1, 1, 1, ''),
(21, 'PlazoFijo', 1, 4, 1, 1, 1, ''),
(22, 'Acciones', 1, 4, 1, 1, 1, ''),
(23, 'FondosComunes', 1, 4, 1, 1, 1, ''),
(31, 'Acreencias', 1, 5, 1, 1, 1, ''),
(32, 'SaldosFavorTarjetas', 1, 5, 1, 1, 1, ''),
(33, 'DSaldosFavorTarjetas', 1, 25, 1, 1, 3, ''),
(41, 'Computadoras', 1, 41, 1, 1, 1, ''),
(42, 'Libros', 1, 41, 1, 1, 1, ''),
(43, 'Inmuebles', 1, 52, 1, 1, 3, ''),
(51, 'Aerolineas', 1, 23, 1, 1, 3, ''),
(52, 'Puntos Bancarios', 1, 3, 1, 1, 1, ''),
(61, 'Dif Moneda Ext', 1, 6, 1, 1, 1, ''),
(71, 'Libros a cobrar', 1, 5, 1, 1, 1, ''),
(101, 'Capital', 3, 101, 2, 1, 1, ''),
(201, 'VisaGalicia', 2, 201, 2, 1, 1, ''),
(202, 'DVisaGalicia', 2, 204, 2, 1, 5, ''),
(203, 'VisaSantander', 2, 204, 2, 1, 1, ''),
(204, 'VisaFrances', 2, 204, 2, 1, 1, ''),
(205, 'DVisaFrances', 2, 204, 2, 1, 5, ''),
(206, 'AmexSantander', 2, 204, 2, 1, 1, ''),
(207, 'DAmexSantande', 2, 204, 2, 1, 5, ''),
(208, 'ExpensasPagar', 2, 203, 2, 1, 1, ''),
(209, 'ExpensasAtrasadas', 2, 204, 2, 1, 1, ''),
(210, 'Visa Sant a pagar', 2, 203, 2, 1, 1, ''),
(211, 'Visa Fr a pagar', 2, 203, 2, 1, 1, ''),
(212, 'Amex Santander', 2, 203, 2, 1, 1, ''),
(213, 'Visa Galicia ', 2, 203, 2, 1, 1, ''),
(214, 'TVisaGalicia a pagar', 2, 203, 2, 1, 1, NULL),
(215, 'TVisaSantander a pagar', 2, 203, 2, 1, 1, NULL),
(216, 'TVisaFrances a pagar', 2, 203, 2, 1, 1, NULL),
(217, 'TAmexSantander a pagar', 2, 203, 1, 1, 1, NULL),
(221, 'PrGalicia 1', 2, 202, 2, 1, 1, ''),
(222, 'PrFrances 1', 2, 202, 2, 1, 1, ''),
(223, 'PrGalicia 2', 2, 202, 2, 1, 1, ''),
(224, 'Pr Galicia a Pagar 1', 2, 201, 2, 1, 1, ''),
(225, 'Pr  Galicia a Pagar 2', 2, 201, 2, 1, 1, ''),
(226, 'Pr Frances a Pagar 1', 2, 201, 2, 1, 1, ''),
(227, 'PrFrances 2', 2, 202, 2, 1, 1, ''),
(228, 'Pr Frances a pagar 2', 2, 201, 2, 1, 1, ''),
(249, 'Expensas a pagar', 2, 204, 2, 1, 1, NULL),
(301, 'Expensas', 4, 301, 1, 1, 1, ''),
(302, 'Telefonia', 4, 301, 1, 1, 1, ''),
(303, 'Reparaciones', 4, 301, 1, 1, 1, ''),
(304, 'Luz', 4, 301, 1, 1, 1, ''),
(305, 'Gas', 4, 301, 1, 1, 1, ''),
(306, 'ProveedorInt', 4, 301, 1, 1, 1, ''),
(307, 'Impuestos', 4, 301, 1, 1, 1, ''),
(311, 'MedicinaPrepaga', 4, 302, 1, 1, 1, ''),
(321, 'InteresPrestamo G1', 4, 303, 1, 1, 1, ''),
(322, 'MantBanco', 4, 303, 1, 1, 1, ''),
(323, 'Seguro', 4, 303, 1, 1, 1, ''),
(324, 'C', 4, 303, 1, 1, 1, ''),
(325, 'InteresPrestamo G2', 4, 303, 1, 1, 1, ''),
(326, 'InteresPrestamo G1', 4, 303, 1, 1, 1, ''),
(327, 'InteresPrestamo F1', 4, 303, 1, 1, 1, ''),
(328, 'InteresPrestamo F2', 4, 303, 1, 1, 1, ''),
(331, 'Perfumeria', 4, 304, 1, 1, 1, ''),
(332, 'Indumentaria', 4, 304, 1, 1, 1, ''),
(333, 'Viaticos', 4, 304, 1, 1, 1, ''),
(334, 'Electronica', 4, 304, 1, 1, 1, ''),
(335, 'C', 4, 304, 1, 1, 1, ''),
(336, 'OtrosCalidad', 4, 304, 1, 1, 1, ''),
(337, 'Salidas', 4, 304, 1, 1, 1, ''),
(338, 'TelefoniaCelular', 4, 304, 1, 1, 1, ''),
(341, 'Comida', 4, 305, 1, 1, 1, ''),
(342, 'Restaurant', 4, 305, 1, 1, 1, ''),
(351, 'Suscripciones', 4, 306, 1, 1, 1, ''),
(352, 'Cursos', 4, 306, 1, 1, 1, ''),
(353, 'Libreria', 4, 306, 1, 1, 1, ''),
(361, 'T', 4, 307, 1, 1, 5, ''),
(362, 'Netflix', 4, 307, 1, 1, 1, ''),
(371, 'Aereos', 4, 308, 1, 1, 1, ''),
(372, 'DAereos', 4, 308, 1, 1, 5, ''),
(373, 'Buses', 4, 308, 1, 1, 1, ''),
(374, 'DBuses', 4, 308, 1, 1, 5, ''),
(375, 'Estadia', 4, 308, 1, 1, 1, ''),
(376, 'DEstadia', 4, 308, 1, 1, 5, ''),
(377, 'Varios', 4, 308, 1, 1, 1, ''),
(401, 'VentaLibros', 5, 401, 2, 1, 1, ''),
(411, 'PlazoFijoG', 5, 402, 2, 1, 1, ''),
(412, 'FondosInvG', 5, 402, 2, 1, 1, ''),
(413, 'AccionesG', 5, 402, 2, 1, 1, ''),
(414, 'CedearG', 5, 402, 2, 1, 1, ''),
(421, 'D', 5, 403, 2, 1, 1, ''),
(422, 'E', 5, 403, 2, 1, 1, ''),
(423, 'L', 5, 403, 2, 1, 1, ''),
(424, 'Sueldos $', 5, 404, 2, 1, 1, ''),
(425, 'Servicios $', 5, 404, 2, 1, 1, ''),
(426, 'Sueldos u$s', 5, 404, 2, 1, 1, ''),
(427, 'Servicios u$s', 5, 404, 2, 1, 1, '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `accounttypes`
--

CREATE TABLE `accounttypes` (
  `idAccountType` int(4) NOT NULL,
  `accountType` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `accounttypes`
--

INSERT INTO `accounttypes` (`idAccountType`, `accountType`) VALUES
(1, 'Activo'),
(2, 'Pasivo'),
(3, 'Patrimonio Neto'),
(4, 'Perdidas'),
(5, 'Ganancias');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cities`
--

CREATE TABLE `cities` (
  `idCity` int(4) NOT NULL,
  `city` varchar(25) NOT NULL,
  `FkidCountry` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `cities`
--

INSERT INTO `cities` (`idCity`, `city`, `FkidCountry`) VALUES
(1, 'BsAs', 1),
(2, 'Cord', 1),
(3, 'Resi', 1),
(4, 'Posa', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `countries`
--

CREATE TABLE `countries` (
  `idCountry` int(4) NOT NULL,
  `country` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `countries`
--

INSERT INTO `countries` (`idCountry`, `country`) VALUES
(1, 'Argentina'),
(2, 'Chile'),
(3, 'Brasil'),
(4, 'Uruguay');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `currencies`
--

CREATE TABLE `currencies` (
  `idCurrency` int(4) NOT NULL,
  `currency` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `currencies`
--

INSERT INTO `currencies` (`idCurrency`, `currency`) VALUES
(1, 'Peso'),
(2, 'Dolar'),
(3, 'DolarMep'),
(4, 'DolarBlue'),
(5, 'DolarImp'),
(6, 'Euro'),
(7, 'Libra'),
(8, 'Real'),
(9, 'Chileno'),
(10, 'Uruguayo'),
(11, 'CoronaSueca'),
(12, 'Polaco'),
(13, 'DolarCanadiense');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datacard`
--

CREATE TABLE `datacard` (
  `idDate` int(11) NOT NULL,
  `FkidCard` int(11) NOT NULL,
  `expirationData` date NOT NULL,
  `purchaseLimit` int(11) NOT NULL,
  `dueDate` date NOT NULL,
  `paymentDate` date NOT NULL,
  `feeDate` int(11) NOT NULL DEFAULT 0,
  `minimumFeeDate` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `datacard`
--

INSERT INTO `datacard` (`idDate`, `FkidCard`, `expirationData`, `purchaseLimit`, `dueDate`, `paymentDate`, `feeDate`, `minimumFeeDate`) VALUES
(1, 213, '2025-05-31', 700000, '2023-10-26', '2023-11-07', 0, 0),
(2, 210, '2029-05-31', 1136640, '2023-10-19', '2023-11-01', 0, 39090),
(3, 211, '2029-10-31', 640000, '2023-10-26', '2023-11-07', 0, 0),
(4, 212, '2027-02-28', 384000, '2023-11-09', '2023-11-17', 0, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dues`
--

CREATE TABLE `dues` (
  `idDues` int(4) NOT NULL,
  `dues` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `dues`
--

INSERT INTO `dues` (`idDues`, `dues`) VALUES
(0, '0'),
(1, '1'),
(2, '2'),
(3, '3'),
(4, '4'),
(5, '5'),
(6, '6'),
(7, '7'),
(8, '8'),
(9, '9'),
(10, '10'),
(11, '11'),
(12, '12'),
(13, '13'),
(14, '14'),
(15, '15'),
(16, '16'),
(17, '17'),
(18, '18');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `exchange`
--

CREATE TABLE `exchange` (
  `idExchange` int(4) NOT NULL,
  `dateCoti` date NOT NULL,
  `FKidCurrency` int(4) NOT NULL,
  `ImporteCot` int(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `exchange`
--

INSERT INTO `exchange` (`idExchange`, `dateCoti`, `FKidCurrency`, `ImporteCot`) VALUES
(76, '2023-09-27', 4, 778),
(77, '2023-09-27', 6, 796),
(78, '2023-09-27', 7, 940),
(79, '2023-09-27', 8, 152),
(93, '2023-10-24', 4, 1000),
(94, '2023-10-24', 6, 1100),
(95, '2023-10-24', 7, 1200),
(96, '2023-10-24', 8, 200),
(103, '2023-11-30', 4, 1000),
(104, '2023-11-30', 6, 1100),
(105, '2023-11-30', 7, 1200),
(106, '2023-11-30', 8, 200),
(107, '2023-12-24', 4, 1000),
(108, '2023-12-24', 6, 1100),
(109, '2023-12-24', 7, 1200),
(110, '2023-12-24', 8, 200);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `increasedby`
--

CREATE TABLE `increasedby` (
  `idIncreasedBy` int(4) NOT NULL,
  `increasedBy` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `increasedby`
--

INSERT INTO `increasedby` (`idIncreasedBy`, `increasedBy`) VALUES
(1, 'Debito'),
(2, 'Credito');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `loans`
--

CREATE TABLE `loans` (
  `idLoan` int(11) NOT NULL,
  `id_VDues` int(11) NOT NULL,
  `FkidAccount` int(11) DEFAULT NULL,
  `perceivedDate` date DEFAULT NULL,
  `amortization` int(11) DEFAULT NULL,
  `interest` int(11) DEFAULT NULL,
  `balance` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `subaccounts`
--

CREATE TABLE `subaccounts` (
  `idSubAccount` int(4) NOT NULL,
  `subAccount` varchar(25) NOT NULL,
  `FkidAccount` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `subaccounts`
--

INSERT INTO `subaccounts` (`idSubAccount`, `subAccount`, `FkidAccount`) VALUES
(0, 'Sin Cuenta', 0),
(311, 'GastosVarios', 31),
(511, 'Iberia', 51),
(512, 'British', 51),
(513, 'Vuelos', 51),
(521, 'Galicia', 52),
(522, 'Santander', 52),
(523, 'Frances', 52),
(3211, 'Galicia1', 321),
(3212, 'Galicia2', 321),
(3213, 'Frances1', 321),
(3214, 'Frances2', 321),
(3215, 'GaliciaAdel', 321),
(3216, 'SantanderAdel', 321),
(3217, 'FrancesAdel', 321),
(3221, 'Galicia', 322),
(3222, 'Santander', 322),
(3223, 'Frances', 322),
(3351, 'Mesoterapia', 335),
(3352, 'Minoxidil', 335);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `accountingitems`
--
ALTER TABLE `accountingitems`
  ADD PRIMARY KEY (`idAccountingItem`);

--
-- Indices de la tabla `accountingmethods`
--
ALTER TABLE `accountingmethods`
  ADD PRIMARY KEY (`idAccountingMethod`);

--
-- Indices de la tabla `accountingtransactions`
--
ALTER TABLE `accountingtransactions`
  ADD PRIMARY KEY (`idAccountingTransaction`),
  ADD KEY `FkidVAccount_idx` (`FkidVAccount`),
  ADD KEY `FkidSubAccount_idx` (`FkidSubAccount`),
  ADD KEY `FkidVIncreasedBy_idx` (`FkidVIncreasedBY`),
  ADD KEY `FkidCity_idx` (`FkidCity`),
  ADD KEY `FkidDues_idx` (`FkidDues`),
  ADD KEY `accountingtransactions_ibfk_4` (`FKidCountry`);

--
-- Indices de la tabla `accounts`
--
ALTER TABLE `accounts`
  ADD PRIMARY KEY (`idAccount`),
  ADD KEY `FkidAccountItem_idx` (`FkidAccountingItem`),
  ADD KEY `FkidAccountType_idx` (`FkidAccountType`),
  ADD KEY `FkidIncreasedBy_idx` (`FkidIncreasedBy`),
  ADD KEY `FkidAccountingMethod_idx` (`FkidAccountingMethod`),
  ADD KEY `FkidCurrency_idx` (`FkidCurrency`);

--
-- Indices de la tabla `accounttypes`
--
ALTER TABLE `accounttypes`
  ADD PRIMARY KEY (`idAccountType`);

--
-- Indices de la tabla `cities`
--
ALTER TABLE `cities`
  ADD PRIMARY KEY (`idCity`),
  ADD KEY `fkidCountry_idx` (`FkidCountry`);

--
-- Indices de la tabla `countries`
--
ALTER TABLE `countries`
  ADD PRIMARY KEY (`idCountry`);

--
-- Indices de la tabla `currencies`
--
ALTER TABLE `currencies`
  ADD PRIMARY KEY (`idCurrency`);

--
-- Indices de la tabla `datacard`
--
ALTER TABLE `datacard`
  ADD PRIMARY KEY (`idDate`);

--
-- Indices de la tabla `dues`
--
ALTER TABLE `dues`
  ADD PRIMARY KEY (`idDues`);

--
-- Indices de la tabla `exchange`
--
ALTER TABLE `exchange`
  ADD PRIMARY KEY (`idExchange`,`dateCoti`),
  ADD KEY `restri1` (`FKidCurrency`);

--
-- Indices de la tabla `increasedby`
--
ALTER TABLE `increasedby`
  ADD PRIMARY KEY (`idIncreasedBy`);

--
-- Indices de la tabla `loans`
--
ALTER TABLE `loans`
  ADD PRIMARY KEY (`idLoan`,`id_VDues`);

--
-- Indices de la tabla `subaccounts`
--
ALTER TABLE `subaccounts`
  ADD PRIMARY KEY (`idSubAccount`),
  ADD KEY `FkidAccount_idx` (`FkidAccount`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `accountingtransactions`
--
ALTER TABLE `accountingtransactions`
  MODIFY `idAccountingTransaction` int(7) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1199;

--
-- AUTO_INCREMENT de la tabla `datacard`
--
ALTER TABLE `datacard`
  MODIFY `idDate` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `exchange`
--
ALTER TABLE `exchange`
  MODIFY `idExchange` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=111;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `accountingtransactions`
--
ALTER TABLE `accountingtransactions`
  ADD CONSTRAINT `FkidVAccount` FOREIGN KEY (`FkidVAccount`) REFERENCES `accounts` (`idAccount`),
  ADD CONSTRAINT `accountingtransactions_ibfk_1` FOREIGN KEY (`FkidCity`) REFERENCES `cities` (`idCity`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `accountingtransactions_ibfk_2` FOREIGN KEY (`FkidDues`) REFERENCES `dues` (`idDues`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `accountingtransactions_ibfk_3` FOREIGN KEY (`FkidSubAccount`) REFERENCES `subaccounts` (`idSubAccount`),
  ADD CONSTRAINT `accountingtransactions_ibfk_4` FOREIGN KEY (`FKidCountry`) REFERENCES `countries` (`idCountry`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `accounts`
--
ALTER TABLE `accounts`
  ADD CONSTRAINT `FkidAccountItem` FOREIGN KEY (`FkidAccountingItem`) REFERENCES `accountingitems` (`idAccountingItem`),
  ADD CONSTRAINT `FkidAccountType` FOREIGN KEY (`FkidAccountType`) REFERENCES `accounttypes` (`idAccountType`),
  ADD CONSTRAINT `FkidAccountingMethod` FOREIGN KEY (`FkidAccountingMethod`) REFERENCES `accountingmethods` (`idAccountingMethod`),
  ADD CONSTRAINT `FkidCurrency` FOREIGN KEY (`FkidCurrency`) REFERENCES `currencies` (`idCurrency`),
  ADD CONSTRAINT `FkidIncreasedBy` FOREIGN KEY (`FkidIncreasedBy`) REFERENCES `increasedby` (`idIncreasedBy`);

--
-- Filtros para la tabla `cities`
--
ALTER TABLE `cities`
  ADD CONSTRAINT `fkidCountry` FOREIGN KEY (`FkidCountry`) REFERENCES `countries` (`idCountry`);

--
-- Filtros para la tabla `exchange`
--
ALTER TABLE `exchange`
  ADD CONSTRAINT `restri1` FOREIGN KEY (`FKidCurrency`) REFERENCES `currencies` (`idCurrency`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `subaccounts`
--
ALTER TABLE `subaccounts`
  ADD CONSTRAINT `FkidAccount` FOREIGN KEY (`FkidAccount`) REFERENCES `accounts` (`idAccount`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
