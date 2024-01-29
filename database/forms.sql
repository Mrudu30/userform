-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 29, 2024 at 02:32 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `forms`
--

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `f_name` varchar(20) NOT NULL,
  `l_name` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `mobno` int(10) NOT NULL,
  `gender` varchar(6) NOT NULL,
  `hobbies` varchar(100) NOT NULL,
  `country` varchar(20) NOT NULL,
  `address` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `f_name`, `l_name`, `email`, `mobno`, `gender`, `hobbies`, `country`, `address`) VALUES
(14, 'xyz', 'cxgf', 'mrudanisongade@gmail.com', 1234455667, 'male', 'Reading', 'India', 'wertyuioop'),
(15, 'sdfsdf', 'cxgf', 'fgdfdfgfdfghfhsdfdf@fgfdg.io', 1234565678, 'male', 'Reading,Writing', 'India', 'yhjjkkllll'),
(17, 'sdfsdf', 'cxgf', 'mrudanisongade@gmail.com', 1232543645, 'male', 'Reading', 'Canada', 'sfdgfghgfh'),
(18, 'xyghghghghghghghghgh', 'arer', 'mrudanisongade@gmail.com', 2147483647, 'male', 'Reading,Writing', 'India', 'dfgdhggjhgjk');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
