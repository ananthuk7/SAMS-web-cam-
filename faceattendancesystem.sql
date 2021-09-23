-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 07, 2021 at 07:47 PM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.3.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `faceattendancesystem`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `username` text NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `username`, `password`) VALUES
(1, 'Rajesh', 'Rajesh');

-- --------------------------------------------------------

--
-- Table structure for table `studentattendance`
--

CREATE TABLE `studentattendance` (
  `id` int(11) NOT NULL,
  `StudentName` text DEFAULT NULL,
  `teacher_id` int(11) DEFAULT NULL,
  `period_no` int(11) DEFAULT NULL,
  `LogDate` text DEFAULT NULL,
  `LogTime` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `studentattendance`
--

INSERT INTO `studentattendance` (`id`, `StudentName`, `teacher_id`, `period_no`, `LogDate`, `LogTime`) VALUES
(1, 'abhi', 1, 1, '07-08-21', '20:54:18'),
(2, 'sidharth', 1, 1, '07-08-21', '20:54:20'),
(3, 'athul', 1, 1, '07-08-21', '20:54:55'),
(4, 'devasree', 1, 1, '07-08-21', '20:56:05'),
(5, 'ananthu', 1, 1, '07-08-21', '20:56:43'),
(6, 'anisree', 1, 1, '07-08-21', 'edited'),
(7, 'abhi', 1, 2, '07-08-21', '21:02:05'),
(8, 'sidharth', 1, 2, '07-08-21', '21:02:06'),
(9, 'athul', 1, 2, '07-08-21', '21:02:37'),
(10, 'devasree', 1, 2, '07-08-21', '21:03:54'),
(11, 'ananthu', 1, 2, '07-08-21', '21:04:36'),
(12, 'abhi', 1, 4, '07-08-21', '21:10:03'),
(13, 'sidharth', 1, 4, '07-08-21', '21:10:04'),
(14, 'athul', 1, 4, '07-08-21', '21:10:39'),
(15, 'devasree', 1, 4, '07-08-21', '21:11:49'),
(16, 'ananthu', 1, 4, '07-08-21', '21:12:27'),
(17, 'abhi', 1, 5, '07-08-21', '21:21:43'),
(18, 'devasree', 1, 5, '07-08-21', '21:22:05'),
(19, 'ananthu', 1, 5, '07-08-21', '21:23:10'),
(20, 'abhi', 1, 6, '07-08-21', '21:27:43'),
(21, 'devasree', 1, 6, '07-08-21', '21:28:04'),
(22, 'ananthu', 1, 6, '07-08-21', '21:29:09'),
(23, 'abhi', 1, 7, '07-08-21', '21:35:38'),
(24, 'devasree', 1, 7, '07-08-21', '21:35:58'),
(25, 'ananthu', 1, 7, '07-08-21', '21:37:03');

-- --------------------------------------------------------

--
-- Table structure for table `studentreg`
--

CREATE TABLE `studentreg` (
  `StudentID` int(11) NOT NULL,
  `StudentName` text DEFAULT NULL,
  `Department` text DEFAULT NULL,
  `Address` text DEFAULT NULL,
  `DOB` text DEFAULT NULL,
  `Age` text DEFAULT NULL,
  `DOJ` text DEFAULT NULL,
  `PHNO` text DEFAULT NULL,
  `Email` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `studentreg`
--

INSERT INTO `studentreg` (`StudentID`, `StudentName`, `Department`, `Address`, `DOB`, `Age`, `DOJ`, `PHNO`, `Email`) VALUES
(1001, 'abhi', 'CSE', 'Kannur', '11/11/93', '22', '12/12/21', '5678900876', 'abhi@gmail.com'),
(1002, 'ananthu', 'CSE', 'asdf', '17/02/96', '25', '12/11/21', '2345678', 'astgh@h.co'),
(1003, 'anisree', 'CSE', 'sgdh', '16/02/99', '21', '11/11/2124356789', '6754324567', 'asvfhjk@yj.co'),
(1004, 'athul', 'CSE', 'adsfvx, sdf', '21/12/99', '21', '11/11/20', '234567865', 'sdgdf@gh.do'),
(1005, 'devasree', 'CSE', 'sdfs fefge', '10/11/98', '24', '11/11/20', '234567asdfsa', 'szcs@hjk.co'),
(1006, 'sidharth', 'CSE', 'sadf dfg', '23/12/99', '22', '12/11/20', '345678654', 'sadhj@gm.co');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `studentattendance`
--
ALTER TABLE `studentattendance`
  ADD PRIMARY KEY (`id`),
  ADD KEY `teacher_id` (`teacher_id`);

--
-- Indexes for table `studentreg`
--
ALTER TABLE `studentreg`
  ADD PRIMARY KEY (`StudentID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `studentattendance`
--
ALTER TABLE `studentattendance`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `studentattendance`
--
ALTER TABLE `studentattendance`
  ADD CONSTRAINT `studentattendance_ibfk_1` FOREIGN KEY (`teacher_id`) REFERENCES `admin` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
