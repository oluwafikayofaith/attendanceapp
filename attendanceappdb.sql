-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 02, 2023 at 08:47 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `attendanceappdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `acadyear`
--

CREATE TABLE `acadyear` (
  `acadyear_id` int(11) NOT NULL,
  `year_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `startdate` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `enddate` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `acadyear`
--

INSERT INTO `acadyear` (`acadyear_id`, `year_name`, `startdate`, `enddate`) VALUES
(1, '2021/2022', '2021-02-10', '2022-05-31'),
(13, '2022/2023', '2022-04-20', '2023-09-21');

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `admin_id` int(11) NOT NULL,
  `admin_username` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `admin_pwd` varchar(120) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`admin_id`, `admin_username`, `admin_pwd`) VALUES
(5, 'admin', 'pbkdf2:sha256:260000$8lws3cd17n1QD1Bf$bfafaa63f0547235774091c4f47b9ac748b1f7db4b1ab3c2e8efb98e8893bc05');

-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

CREATE TABLE `attendance` (
  `attendance_id` int(11) NOT NULL,
  `timein` datetime DEFAULT NULL,
  `attendance_studentid` int(11) DEFAULT NULL,
  `attendance_timetableid` int(11) DEFAULT NULL,
  `attendance_courseid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `attendance`
--

INSERT INTO `attendance` (`attendance_id`, `timein`, `attendance_studentid`, `attendance_timetableid`, `attendance_courseid`) VALUES
(1, '2023-03-01 15:11:15', 1, 9, 13);

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE `course` (
  `course_id` int(11) NOT NULL,
  `course_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `course_code` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `course_levelid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`course_id`, `course_name`, `course_code`, `course_levelid`) VALUES
(12, 'Biology science', 'bio 101', 1),
(13, 'chemistry science', 'chem 101', 1),
(15, 'Use of English', 'Eng 102', 1),
(16, 'Introduction to comp', 'CSC 101', 1);

-- --------------------------------------------------------

--
-- Table structure for table `lecturercourse`
--

CREATE TABLE `lecturercourse` (
  `lecturercourse_id` int(11) NOT NULL,
  `lecturercourse_courseid` int(11) DEFAULT NULL,
  `lecturercourse_lecturerid` int(11) DEFAULT NULL,
  `lecturercourse_acadyearid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `lecturercourse`
--

INSERT INTO `lecturercourse` (`lecturercourse_id`, `lecturercourse_courseid`, `lecturercourse_lecturerid`, `lecturercourse_acadyearid`) VALUES
(8, 12, 1, 13),
(9, 13, 2, 13),
(11, 16, NULL, 13),
(12, 15, 6, 13);

-- --------------------------------------------------------

--
-- Table structure for table `lecturers`
--

CREATE TABLE `lecturers` (
  `lecturer_id` int(11) NOT NULL,
  `lecturer_fullname` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `lecturer_pwd` varchar(120) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `lecturer_cpwd` varchar(120) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `lecturer_email` varchar(120) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `lecturer_add` varchar(120) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `lecturer_phone` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `lecturer_status` enum('1','0') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `lecturers`
--

INSERT INTO `lecturers` (`lecturer_id`, `lecturer_fullname`, `lecturer_pwd`, `lecturer_cpwd`, `lecturer_email`, `lecturer_add`, `lecturer_phone`, `lecturer_status`) VALUES
(1, 'Faith James', 'pbkdf2:sha256:260000$4jUMAq6TYffivgOU$bcf232fac46fad049a232618c9f47200b1ed3a6ee7b2a634d356ca9241417bb8', 'pbkdf2:sha256:260000$BM8A0wPRtDrN2Ew3$9e9a0e18deacc82048de0dd0452c0e3fa0dd12169e6ad1a9bb6f6629bcabc76c', 'faithjames@gmail.com', 'Ikeja,Lagos', '0908765433677', '0'),
(2, 'Ibikunle Henry', 'pbkdf2:sha256:260000$wJzobAvXQi4U1hHk$9d9c00e32ad9dd327421dad2b430ef1bc775144b917a20540465d5a669809448', 'pbkdf2:sha256:260000$oN9jNuz5iAVfnffH$29d1f8fa1f0c6c7e82fe2db04ae2e1ba3d34c1c13aec1cc676f77ae3215ab402', 'ibikunle@gmail.com', 'Apapa Lagos', '0908765433677', '0'),
(4, 'Abolade Abolade', 'pbkdf2:sha256:260000$59781i5TIEeKk2w8$f97034862ed7bdb13f7b867891503368a20a9c067de0c4a21860e9913c27eef0', 'pbkdf2:sha256:260000$fnmIM5yV6lJkJIZH$0c9befb349c1e52094978b27ce5e4fe7b54564e4e1c74d05ce8af28f8ab32eb4', 'ab@gmail.com', 'ikeja', '0908765433677', '0'),
(6, 'William Emifi', 'pbkdf2:sha256:260000$UvumRkg4HEJomYIY$e05bc80760463e11e83f5b810fcefa39e606bb6867c55a20a0bdc311b8b87a17', 'pbkdf2:sha256:260000$lgCcoI0hgktPqm7n$2af6f5cfb1c30cac06da3326763b7c6677c69f95245b60de47b1a53a4b10b9b6', 'willy@yahoo.com', 'Apapa Lagos', '050605050404', '0'),
(7, 'Preston Ololade', 'pbkdf2:sha256:260000$p9APJBaJWPGa3Aox$f8ef001d2f3775a76d59db19f8a57792c4bb6111f228de5a06868c93fe8e25b4', 'pbkdf2:sha256:260000$EUvlJQYbzfTr01DQ$ca386cddceac0520cba50bb8397695b891e5a2c896e18ca16e8280249e717394', 'prest@gmail.com', 'ogba Lagos', '0908765433677', '0');

-- --------------------------------------------------------

--
-- Table structure for table `level`
--

CREATE TABLE `level` (
  `level_id` int(11) NOT NULL,
  `level_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `level`
--

INSERT INTO `level` (`level_id`, `level_name`) VALUES
(1, '100 level'),
(2, '200 level'),
(3, '300 level'),
(4, '400 level'),
(5, '500 level'),
(6, '600 level');

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `student_id` int(11) NOT NULL,
  `student_fullname` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `student_add` varchar(120) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `student_phone` varchar(120) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `student_pwd` varchar(120) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `student_cpwd` varchar(120) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `student_email` varchar(120) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `student_status` enum('1','0') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '0',
  `student_dob` datetime DEFAULT NULL,
  `student_matno` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `student_pix` varchar(120) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `student_levelid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`student_id`, `student_fullname`, `student_add`, `student_phone`, `student_pwd`, `student_cpwd`, `student_email`, `student_status`, `student_dob`, `student_matno`, `student_pix`, `student_levelid`) VALUES
(1, 'Preston Ololade', 'ogba Lagos', '050605050404', 'pbkdf2:sha256:260000$tg2SdcF61eqqTZN4$71b332412fb874a24502b21ea0ba7cf31865df82ceab7e7b2e606da461e64d2b', 'pbkdf2:sha256:260000$upqPlKM84s5H5rMw$4b15badf4244db1b29caeaa62bc110b9c52fb484dc7fb0bdd43fe2ac9f7c2a81', 'prest@gmail.com', '0', '2023-02-26 22:57:52', 'csc/2022/190', '', 1),
(2, 'William Emifi', 'Apapa Lagos', '050605050404', 'pbkdf2:sha256:260000$fg1fxJ6Dad2ywNoO$e34d1bf74cbe9a9c24c050e53195e7b6a716a79642239e2745cb5b937d2b2af0', 'pbkdf2:sha256:260000$ijlpZ7bEebOToiUE$b4c0d7455ce0849095e18f5c5a59da991cdbe951078085c808a85adec0164c66', 'willy@yahoo.com', '0', '2023-02-26 22:58:43', 'csc/2022/192', '', 1),
(3, 'Faith James', 'Ikeja,Lagos', '0908765433677', 'pbkdf2:sha256:260000$F59ejovooc3QeUD9$9cdd69e119402c64cfe5bb436eba7efd7e18f17849e407fee652448cf0b3c57d', 'pbkdf2:sha256:260000$c3UVgareWHUaXHO3$0a9453c84a9d3c7d127f2f30b7601900d34123cdd85b71335dadd714fd534b1b', 'faithjames@gmail.com', '0', '2023-02-26 22:59:53', 'csc/2022/01', '', 1),
(4, 'Francis Olamilekan', 'Ikeja,Lagos', '050605050404', 'pbkdf2:sha256:260000$2w0TpihR6IUd27pg$c39c8ade50bc7369693e9e641ac049b582ecabf278520d9ca8c289c6bd780488', 'pbkdf2:sha256:260000$ZYdmAs3Sj9oxvwlY$23f7b1470695307b1e55f1a62c847f747de3f328a6ef0cf831e479d5b1eceff1', 'francis@gmail.com', '0', '2023-02-26 23:00:38', 'csc/2022/02', '', 1),
(5, 'Yakubu Gowon', 'Lagos island', '050605050404', 'pbkdf2:sha256:260000$C5ws65lwbcaHAaOB$06a5a751ebd2ef2f9250ee6fb40ff20ef519537b2bdc3933c0336ae820d4c296', 'pbkdf2:sha256:260000$KoZ7RvHu6ICOQS47$765a097477d8f5db3a3311c461b7f06dd58c6bce5d45242137059175459465cd', 'yk@yahoo.com', '0', '2023-02-26 23:02:00', 'csc/2022/08', '', 2);

-- --------------------------------------------------------

--
-- Table structure for table `timetable`
--

CREATE TABLE `timetable` (
  `timetable_id` int(11) NOT NULL,
  `time` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `day` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `timetable_acadyearid` int(11) DEFAULT NULL,
  `timetable_courseid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `timetable`
--

INSERT INTO `timetable` (`timetable_id`, `time`, `day`, `timetable_acadyearid`, `timetable_courseid`) VALUES
(9, '08:00am', 'Monday', 13, 15),
(12, '12:10', 'Thursday', 13, 13),
(13, '02:30pm', 'Friday', 13, 16);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `acadyear`
--
ALTER TABLE `acadyear`
  ADD PRIMARY KEY (`acadyear_id`);

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`admin_id`);

--
-- Indexes for table `attendance`
--
ALTER TABLE `attendance`
  ADD PRIMARY KEY (`attendance_id`),
  ADD KEY `attendance_studentid` (`attendance_studentid`),
  ADD KEY `attendance_timetableid` (`attendance_timetableid`),
  ADD KEY `attendance_courseid` (`attendance_courseid`);

--
-- Indexes for table `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`course_id`),
  ADD KEY `course_levelid` (`course_levelid`);

--
-- Indexes for table `lecturercourse`
--
ALTER TABLE `lecturercourse`
  ADD PRIMARY KEY (`lecturercourse_id`),
  ADD KEY `lecturercourse_courseid` (`lecturercourse_courseid`),
  ADD KEY `lecturercourse_lecturerid` (`lecturercourse_lecturerid`),
  ADD KEY `lecturercourse_acadyearid` (`lecturercourse_acadyearid`);

--
-- Indexes for table `lecturers`
--
ALTER TABLE `lecturers`
  ADD PRIMARY KEY (`lecturer_id`),
  ADD UNIQUE KEY `lecturer_email` (`lecturer_email`);

--
-- Indexes for table `level`
--
ALTER TABLE `level`
  ADD PRIMARY KEY (`level_id`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`student_id`),
  ADD UNIQUE KEY `student_matno` (`student_matno`),
  ADD KEY `student_levelid` (`student_levelid`);

--
-- Indexes for table `timetable`
--
ALTER TABLE `timetable`
  ADD PRIMARY KEY (`timetable_id`),
  ADD KEY `timetable_acadyearid` (`timetable_acadyearid`),
  ADD KEY `timetable_courseid` (`timetable_courseid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `acadyear`
--
ALTER TABLE `acadyear`
  MODIFY `acadyear_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `attendance`
--
ALTER TABLE `attendance`
  MODIFY `attendance_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `course`
--
ALTER TABLE `course`
  MODIFY `course_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `lecturercourse`
--
ALTER TABLE `lecturercourse`
  MODIFY `lecturercourse_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `lecturers`
--
ALTER TABLE `lecturers`
  MODIFY `lecturer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `level`
--
ALTER TABLE `level`
  MODIFY `level_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `student_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `timetable`
--
ALTER TABLE `timetable`
  MODIFY `timetable_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `attendance`
--
ALTER TABLE `attendance`
  ADD CONSTRAINT `attendance_ibfk_1` FOREIGN KEY (`attendance_studentid`) REFERENCES `students` (`student_id`),
  ADD CONSTRAINT `attendance_ibfk_2` FOREIGN KEY (`attendance_timetableid`) REFERENCES `timetable` (`timetable_id`),
  ADD CONSTRAINT `attendance_ibfk_3` FOREIGN KEY (`attendance_courseid`) REFERENCES `course` (`course_id`);

--
-- Constraints for table `course`
--
ALTER TABLE `course`
  ADD CONSTRAINT `course_ibfk_1` FOREIGN KEY (`course_levelid`) REFERENCES `level` (`level_id`);

--
-- Constraints for table `lecturercourse`
--
ALTER TABLE `lecturercourse`
  ADD CONSTRAINT `lecturercourse_ibfk_1` FOREIGN KEY (`lecturercourse_courseid`) REFERENCES `course` (`course_id`),
  ADD CONSTRAINT `lecturercourse_ibfk_2` FOREIGN KEY (`lecturercourse_lecturerid`) REFERENCES `lecturers` (`lecturer_id`),
  ADD CONSTRAINT `lecturercourse_ibfk_3` FOREIGN KEY (`lecturercourse_acadyearid`) REFERENCES `acadyear` (`acadyear_id`);

--
-- Constraints for table `students`
--
ALTER TABLE `students`
  ADD CONSTRAINT `students_ibfk_1` FOREIGN KEY (`student_levelid`) REFERENCES `level` (`level_id`);

--
-- Constraints for table `timetable`
--
ALTER TABLE `timetable`
  ADD CONSTRAINT `timetable_ibfk_1` FOREIGN KEY (`timetable_acadyearid`) REFERENCES `acadyear` (`acadyear_id`),
  ADD CONSTRAINT `timetable_ibfk_2` FOREIGN KEY (`timetable_courseid`) REFERENCES `course` (`course_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
