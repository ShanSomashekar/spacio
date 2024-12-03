-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Dec 03, 2024 at 06:33 PM
-- Server version: 10.11.9-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `u919924273_workspace`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Bookings`
--

CREATE TABLE `Bookings` (
  `BookingID` int(11) NOT NULL,
  `SpaceID` int(11) NOT NULL,
  `MemberID` int(11) DEFAULT NULL,
  `StartTime` datetime NOT NULL,
  `EndTime` datetime NOT NULL,
  `Status` varchar(50) DEFAULT NULL,
  `Price` int(11) NOT NULL,
  `checkin` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `Bookings`
--

INSERT INTO `Bookings` (`BookingID`, `SpaceID`, `MemberID`, `StartTime`, `EndTime`, `Status`, `Price`, `checkin`) VALUES
(1, 209, 13, '2024-11-28 18:58:06', '2024-11-28 19:58:06', NULL, 0, 0),
(2, 105, 14, '2024-11-28 00:00:00', '2024-11-28 00:00:00', 'Booked', 0, 0),
(3, 108, 14, '2024-11-12 16:31:00', '2024-11-30 16:31:00', NULL, 0, 0),
(4, 106, 14, '2024-11-28 16:37:00', '2024-11-29 16:37:00', 'Booked', 0, 0),
(5, 303, NULL, '2024-11-29 17:00:00', '2024-12-29 17:00:00', 'Booked', 0, 0),
(6, 202, NULL, '2024-11-29 18:29:00', '2024-12-02 18:29:00', NULL, 0, 0),
(7, 202, NULL, '2024-11-29 18:29:00', '2024-12-02 18:29:00', NULL, 0, 0),
(8, 202, NULL, '2024-11-29 18:29:00', '2024-12-02 18:29:00', NULL, 0, 0),
(9, 202, NULL, '2024-11-29 18:29:00', '2024-12-02 18:29:00', NULL, 0, 0),
(10, 202, NULL, '2024-11-29 18:29:00', '2024-12-02 18:29:00', NULL, 0, 0),
(11, 202, NULL, '2024-11-29 18:29:00', '2024-12-02 18:29:00', NULL, 0, 0),
(12, 202, NULL, '2024-11-29 18:29:00', '2024-12-02 18:29:00', NULL, 0, 0),
(13, 202, NULL, '2024-11-29 18:29:00', '2024-12-02 18:29:00', NULL, 0, 0),
(14, 202, NULL, '2024-11-29 18:29:00', '2024-12-02 18:29:00', NULL, 0, 0),
(15, 202, NULL, '2024-11-29 18:29:00', '2024-12-02 18:29:00', NULL, 0, 0),
(16, 202, NULL, '2024-11-29 18:29:00', '2024-12-02 18:29:00', NULL, 0, 0),
(17, 202, NULL, '2024-11-29 18:29:00', '2024-12-02 18:29:00', NULL, 0, 0),
(18, 202, NULL, '2024-11-29 18:29:00', '2024-12-02 18:29:00', NULL, 0, 0),
(19, 202, NULL, '2024-11-29 18:29:00', '2024-12-02 18:29:00', NULL, 0, 0),
(20, 202, NULL, '2024-11-29 18:29:00', '2024-12-02 18:29:00', NULL, 0, 0),
(21, 202, NULL, '2024-11-29 18:29:00', '2024-12-02 18:29:00', NULL, 0, 0),
(22, 202, NULL, '2024-11-29 18:29:00', '2024-12-02 18:29:00', NULL, 0, 0),
(23, 109, 14, '2024-11-29 19:42:00', '2024-12-06 19:42:00', NULL, 0, 0),
(24, 102, 21, '2024-12-05 09:00:00', '2024-12-05 17:00:00', 'Confirmed', 0, 0),
(25, 103, 22, '2024-12-06 10:00:00', '2024-12-06 14:00:00', 'Confirmed', 0, 0),
(26, 104, 23, '2024-12-07 11:00:00', '2024-12-07 13:00:00', 'Cancelled', 0, 0),
(27, 105, 24, '2024-12-08 15:00:00', '2024-12-08 18:00:00', 'Confirmed', 0, 0),
(28, 106, 25, '2024-12-09 09:00:00', '2024-12-09 12:00:00', 'Pending', 0, 0),
(29, 107, 26, '2024-12-10 08:30:00', '2024-12-10 16:30:00', 'Confirmed', 0, 0),
(30, 108, 27, '2024-12-11 10:00:00', '2024-12-11 14:00:00', 'Pending', 0, 0),
(31, 109, 28, '2024-12-12 09:00:00', '2024-12-12 18:00:00', 'Confirmed', 0, 0),
(32, 110, 29, '2024-12-13 08:00:00', '2024-12-13 15:00:00', 'Confirmed', 0, 0),
(33, 201, 30, '2024-12-14 10:00:00', '2024-12-14 12:00:00', 'Confirmed', 0, 0),
(34, 202, 21, '2024-12-15 09:30:00', '2024-12-15 17:30:00', 'Confirmed', 0, 0),
(35, 203, 22, '2024-12-16 11:00:00', '2024-12-16 14:00:00', 'Cancelled', 0, 0),
(36, 204, 23, '2024-12-17 08:00:00', '2024-12-17 12:00:00', 'Pending', 0, 0),
(37, 205, 24, '2024-12-18 14:00:00', '2024-12-18 18:00:00', 'Confirmed', 0, 0),
(38, 206, 25, '2024-12-19 10:00:00', '2024-12-19 13:00:00', 'Confirmed', 0, 0),
(39, 207, 26, '2024-12-20 15:00:00', '2024-12-20 19:00:00', 'Pending', 0, 0),
(40, 208, 27, '2024-12-21 12:00:00', '2024-12-21 16:00:00', 'Confirmed', 0, 0),
(41, 209, 28, '2024-12-22 09:00:00', '2024-12-22 11:00:00', 'Confirmed', 0, 0),
(42, 210, 29, '2024-12-23 10:00:00', '2024-12-23 14:00:00', 'Confirmed', 0, 0),
(43, 301, 30, '2024-12-24 09:00:00', '2024-12-24 18:00:00', 'Confirmed', 0, 0),
(44, 109, 14, '2024-12-02 09:53:00', '2024-12-11 21:54:00', NULL, 0, 0),
(48, 108, 43, '2024-12-03 19:14:00', '2024-12-03 20:15:00', NULL, 0, 0),
(49, 208, 43, '2024-12-04 19:30:00', '2024-12-04 23:30:00', NULL, 0, 0),
(50, 202, 42, '2024-12-15 20:46:00', '2024-12-18 20:46:00', NULL, 1650, 0),
(53, 205, 42, '2024-12-01 20:50:00', '2024-12-07 20:50:00', NULL, 18000, 0),
(55, 109, 42, '2024-12-03 12:06:00', '2024-12-04 12:06:00', NULL, 450, 0),
(56, 206, 42, '2024-12-01 12:07:00', '2024-12-12 12:07:00', NULL, 9350, 0),
(58, 1001, 42, '2024-12-03 13:24:00', '2024-12-17 13:24:00', NULL, 14000, 0);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(8, 'manager', 'booking'),
(7, 'manager', 'member'),
(9, 'manager', 'space'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-11-21 23:51:34.641650'),
(2, 'auth', '0001_initial', '2024-11-21 23:51:35.943494'),
(3, 'admin', '0001_initial', '2024-11-21 23:51:36.274097'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-11-21 23:51:36.374023'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-11-21 23:51:36.471651'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-11-21 23:51:36.802547'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-11-21 23:51:36.944134'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-11-21 23:51:37.085954'),
(9, 'auth', '0004_alter_user_username_opts', '2024-11-21 23:51:37.178572'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-11-21 23:51:37.334531'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-11-21 23:51:37.438029'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-11-21 23:51:37.550333'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-11-21 23:51:37.692068'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-11-21 23:51:37.834318'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-11-21 23:51:38.007022'),
(16, 'auth', '0011_update_proxy_permissions', '2024-11-21 23:51:38.239326'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-11-21 23:51:38.387251'),
(18, 'sessions', '0001_initial', '2024-11-21 23:51:38.629551'),
(19, 'manager', '0001_initial', '2024-11-25 05:34:12.590935'),
(20, 'members', '0001_initial', '2024-11-27 23:11:14.838070');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('4ufo73vjrjg7v86e1hnnhhugdquna91k', 'eyJlbXBsb3llZV9pZCI6MTgsIm11c3RfY2hhbmdlX3Bhc3N3b3JkIjpmYWxzZSwidXNlciI6NDJ9:1tIXZz:jkMFcvSfW0CBbWSfR-B1K4My5ETF1Ldh-9_hGuDmS2Y', '2024-12-17 18:24:59.145105'),
('jqw30n7orul2xjh0r030qbo6ywk3vlmi', 'eyJlbXBsb3llZV9pZCI6MTgsIm11c3RfY2hhbmdlX3Bhc3N3b3JkIjpmYWxzZSwidXNlciI6NDN9:1tIIkh:epaw7FUnH6qdNDu_rF8Pg8ty4LGdTBdExlKcAmH5G5Y', '2024-12-17 02:35:03.325030'),
('pqg7tcgcxrplbo7k29ef4l8hfvdsubrk', 'eyJ1c2VyIjo0MiwiZW1wbG95ZWVfaWQiOjE4LCJtdXN0X2NoYW5nZV9wYXNzd29yZCI6ZmFsc2V9:1tIGkW:l6VWRftnpRBWntLzF1lk_EJR_CZYbnp2x3wIVJe2SYk', '2024-12-17 00:26:44.284947');

-- --------------------------------------------------------

--
-- Table structure for table `Employees`
--

CREATE TABLE `Employees` (
  `EmployeeID` int(11) NOT NULL,
  `FirstName` varchar(50) NOT NULL,
  `LastName` varchar(50) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `PhoneNumber` varchar(15) DEFAULT NULL,
  `Position` varchar(50) NOT NULL,
  `Department` varchar(50) DEFAULT NULL,
  `HireDate` date NOT NULL,
  `Salary` decimal(10,2) DEFAULT NULL,
  `PasswordHash` varchar(256) NOT NULL,
  `PasswordSalt` varchar(256) NOT NULL,
  `MustChangePassword` tinyint(1) NOT NULL DEFAULT 1,
  `IsActive` tinyint(1) NOT NULL DEFAULT 0 COMMENT 'Indicates if the employee account is active',
  `CreatedAt` timestamp NULL DEFAULT current_timestamp(),
  `AadharID` varchar(12) DEFAULT NULL,
  `TempPassword` varchar(255) DEFAULT NULL COMMENT 'Temporary password for first-time login',
  `PasswordChanged` tinyint(1) DEFAULT 0 COMMENT 'Track if password has been updated by the employee',
  `Role` enum('Super Admin','Admin','Employee') NOT NULL DEFAULT 'Employee' COMMENT 'Defines the role of the employee'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `Employees`
--

INSERT INTO `Employees` (`EmployeeID`, `FirstName`, `LastName`, `Email`, `PhoneNumber`, `Position`, `Department`, `HireDate`, `Salary`, `PasswordHash`, `PasswordSalt`, `MustChangePassword`, `IsActive`, `CreatedAt`, `AadharID`, `TempPassword`, `PasswordChanged`, `Role`) VALUES
(1, 'Ravi', 'Patel', 'ravi.patel@coworking.com', '9876543210', 'Community Manager', 'Community', '2022-01-10', '65000.00', '', '', 1, 1, '2024-12-02 03:26:02', '123412345678', NULL, 0, 'Employee'),
(2, 'Neha', 'Sharma', 'neha.sharma@coworking.com', '9123456789', 'Facility Manager', 'Operations', '2021-05-20', '70000.00', '', '', 1, 1, '2024-12-02 03:26:02', '234523456789', NULL, 0, 'Employee'),
(3, 'Amit', 'Kumar', 'amit.kumar@coworking.com', '9998776655', 'Customer Support Executive', 'Support', '2020-03-15', '45000.00', '', '', 1, 1, '2024-12-02 03:26:02', '345634567890', NULL, 0, 'Employee'),
(4, 'Anjali', 'Mehta', 'anjali.mehta@coworking.com', '9201234567', 'Sales Executive', 'Sales', '2022-09-10', '55000.00', '', '', 1, 1, '2024-12-02 03:26:02', '456745678901', NULL, 0, 'Employee'),
(5, 'Vikram', 'Reddy', 'vikram.reddy@coworking.com', '9333345678', 'Operations Supervisor', 'Operations', '2023-06-01', '60000.00', '', '', 1, 1, '2024-12-02 03:26:02', '567856789012', NULL, 0, 'Employee'),
(6, 'Deepika', 'Gupta', 'deepika.gupta@coworking.com', '9712345678', 'Event Manager', 'Events', '2021-07-25', '65000.00', '', '', 1, 1, '2024-12-02 03:26:02', '678967890123', NULL, 0, 'Employee'),
(7, 'Manoj', 'Verma', 'manoj.verma@coworking.com', '9301122334', 'Tech Support', 'IT', '2020-11-10', '50000.00', '', '', 1, 1, '2024-12-02 03:26:02', '789078901234', NULL, 0, 'Employee'),
(8, 'Seema', 'Singh', 'seema.singh@coworking.com', '9402112233', 'Marketing Executive', 'Marketing', '2022-04-18', '60000.00', '', '', 1, 1, '2024-12-02 03:26:02', '890189012345', NULL, 0, 'Employee'),
(9, 'Suresh', 'Iyer', 'suresh.iyer@coworking.com', '9603344556', 'Operations Manager', 'Operations', '2020-12-01', '75000.00', '', '', 1, 1, '2024-12-02 03:26:02', '901290123456', NULL, 0, 'Employee'),
(10, 'Priya', 'Bhatia', 'priya.bhatia@coworking.com', '9601234567', 'Admin Assistant', 'Admin', '2019-08-10', '40000.00', '', '', 1, 1, '2024-12-02 03:26:02', '101201234567', NULL, 0, 'Employee'),
(11, 'Admin', 'User', 'admin@gmail.com', NULL, 'Admin', NULL, '2024-12-02', NULL, '240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9', '', 1, 1, '2024-12-02 15:23:37', NULL, NULL, 0, 'Admin'),
(12, 'Emp ', 'Emp ', 'Emp1@gmail.com', '7779503763', 'CD Manager ', 'Sales', '2024-12-11', '60000.00', '694d35bbef1882720cbd5bc1348983b7de401d215eb2e333ce2c6b9e2ebf35a8', '', 0, 0, '2024-12-02 15:35:22', NULL, NULL, 0, 'Employee'),
(13, 'Emp2', 'EmpE', 'e1@gmail.com', '1234567899', 'Marketer', 'Marketing', '2024-12-04', '35000.00', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', '', 0, 0, '2024-12-02 15:41:55', NULL, NULL, 0, 'Employee'),
(14, 'Admin', 'User', 'admin@example.com', '1234567890', 'System Admin', 'IT', '2024-12-01', '100000.00', 'b4d2c695bfb9e8799fa5673a8fa9f8b5fd79992f1ec28d9bc830b1c0e897a327ce287dfe73117d3995b9d8fa7e31be0f3edbe8a2730a2120e741d72fefc3a681', '8c6d726fa1449ecb92a2a804e08080a0', 1, 1, '2024-12-02 16:25:13', NULL, NULL, 0, 'Super Admin'),
(16, 'Admin', 'User', 'admin1@example.com', '1234567890', 'System Admin', 'IT', '2024-12-01', '100000.00', '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918', '', 1, 1, '2024-12-02 16:29:00', NULL, NULL, 0, 'Super Admin'),
(18, 'Admin', 'User', 'admin@spacio.com', '1234567890', 'System Admin', 'IT', '0000-00-00', '100000.00', '987abb896213f27c0eca3300fb7d8031834d8b0aa6f0dd17daed9ac45e9d2d83', 'fc2554d17217ae54601517567cce80ca', 0, 1, '0000-00-00 00:00:00', '213214241', '', 1, 'Super Admin'),
(20, 'Admin', 'Test', 'admintest@example.com', '1234567890', 'System Admin', 'IT', '0000-00-00', '100000.00', 'b4d2c695bfb9e8799fa5673a8fa9f8b5fd79992f1ec28d9bc830b1c0e897a327ce287dfe73117d3995b9d8fa7e31be0f3edbe8a2730a2120e741d72fefc3a681', '8c6d726fa1449ecb92a2a804e08080a0', 1, 1, '2024-12-02 20:10:00', 'None', 'None', 0, 'Admin');

-- --------------------------------------------------------

--
-- Table structure for table `Enquiries`
--

CREATE TABLE `Enquiries` (
  `EnquiryID` int(11) NOT NULL,
  `LeadID` int(11) DEFAULT NULL,
  `Name` varchar(100) DEFAULT NULL,
  `ContactNumber` varchar(15) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `EnquiryDate` date DEFAULT NULL,
  `Source` varchar(50) DEFAULT NULL,
  `Message` text DEFAULT NULL,
  `FollowUpStatus` varchar(50) DEFAULT NULL,
  `FollowUpDate` date DEFAULT NULL,
  `Notes` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Invoices`
--

CREATE TABLE `Invoices` (
  `InvoiceID` int(11) NOT NULL,
  `BookingID` int(11) DEFAULT NULL,
  `IssueDate` date DEFAULT NULL,
  `DueDate` date DEFAULT NULL,
  `Amount` decimal(10,2) DEFAULT NULL,
  `TaxAmount` decimal(5,2) DEFAULT NULL,
  `AdditionalFees` decimal(5,2) DEFAULT NULL,
  `total` int(11) NOT NULL,
  `Status` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `Invoices`
--

INSERT INTO `Invoices` (`InvoiceID`, `BookingID`, `IssueDate`, `DueDate`, `Amount`, `TaxAmount`, `AdditionalFees`, `total`, `Status`) VALUES
(9, 48, '2024-12-03', '2024-12-10', '0.00', '0.00', '5.00', 5, 'Pending'),
(10, 1, '2024-12-03', NULL, '591.50', NULL, NULL, 0, 'Unpaid'),
(11, 2, '2024-12-03', NULL, '844.34', NULL, NULL, 0, 'Paid'),
(12, 3, '2024-12-03', NULL, '719.05', NULL, NULL, 0, 'Unpaid'),
(13, 4, '2024-12-03', NULL, '62.93', NULL, NULL, 0, 'Unpaid'),
(14, 5, '2024-12-03', NULL, '724.14', NULL, NULL, 0, 'Unpaid'),
(15, 6, '2024-12-03', NULL, '192.32', NULL, NULL, 0, 'Paid'),
(16, 7, '2024-12-03', NULL, '136.85', NULL, NULL, 0, 'Unpaid'),
(17, 8, '2024-12-03', NULL, '869.24', NULL, NULL, 0, 'Paid'),
(18, 9, '2024-12-03', NULL, '283.86', NULL, NULL, 0, 'Unpaid'),
(19, 10, '2024-12-03', NULL, '570.22', NULL, NULL, 0, 'Unpaid'),
(20, 11, '2024-12-03', NULL, '279.44', NULL, NULL, 0, 'Unpaid'),
(21, 12, '2024-12-03', NULL, '177.40', NULL, NULL, 0, 'Unpaid'),
(22, 13, '2024-12-03', NULL, '855.67', NULL, NULL, 0, 'Unpaid'),
(23, 14, '2024-12-03', NULL, '661.06', NULL, NULL, 0, 'Paid'),
(24, 15, '2024-12-03', NULL, '859.18', NULL, NULL, 0, 'Unpaid'),
(25, 16, '2024-12-03', NULL, '374.81', NULL, NULL, 0, 'Paid'),
(26, 17, '2024-12-03', NULL, '388.70', NULL, NULL, 0, 'Paid'),
(27, 18, '2024-12-03', NULL, '12.10', NULL, NULL, 0, 'Paid'),
(28, 19, '2024-12-03', NULL, '731.61', NULL, NULL, 0, 'Paid'),
(29, 20, '2024-12-03', NULL, '791.67', NULL, NULL, 0, 'Paid');

-- --------------------------------------------------------

--
-- Table structure for table `Members`
--

CREATE TABLE `Members` (
  `MemberID` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `ContactNumber` varchar(15) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Address` text DEFAULT NULL,
  `Company` varchar(255) DEFAULT NULL,
  `GST` varchar(15) DEFAULT NULL,
  `PasswordHash` varchar(255) NOT NULL,
  `PasswordSalt` varchar(255) NOT NULL,
  `AadharID` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `Members`
--

INSERT INTO `Members` (`MemberID`, `Name`, `ContactNumber`, `Email`, `Address`, `Company`, `GST`, `PasswordHash`, `PasswordSalt`, `AadharID`) VALUES
(1, 'test111', '9742295790', 'test123@gmail.com', NULL, NULL, NULL, '89a8b26833c33a822521b6b7df9b857f86559181c40b55e5669038f57d12c618', '1adf6c8ca147800a3e59c579b3a9655c', '2313123'),
(2, 'Amit Sharma', '9812345678', 'amit.sharma@gmail.com', '123 MG Road, Mumbai', 'Tech Innovators', '27AAAAA0000A1Z5', 'hashedPassword1', 'randomSalt1', '123412341234'),
(3, 'Priya Gupta', '9823456789', 'priya.gupta@gmail.com', '45 Park Street, Kolkata', 'Green Energy Pvt Ltd', '19BBBBB1111B2Z6', 'hashedPassword2', 'randomSalt2', '234523452345'),
(4, 'Rahul Verma', '9876543210', 'rahul.verma@gmail.com', '67 Palace Road, Bangalore', 'Blue Oceans Inc', NULL, 'hashedPassword3', 'randomSalt3', '345634563456'),
(5, 'Sneha Iyer', '9765432109', 'sneha.iyer@gmail.com', '89 Anna Nagar, Chennai', 'Urban Creators', '33CCCC2222C3Z7', 'hashedPassword4', 'randomSalt4', '456745674567'),
(6, 'Arjun Singh', '9898765432', 'arjun.singh@gmail.com', '12 Main Road, Delhi', 'Growth Hackers', NULL, 'hashedPassword5', 'randomSalt5', '567856785678'),
(7, 'Neha Mishra', '9776543210', 'neha.mishra@gmail.com', '98 GT Road, Pune', 'Eco Solutions', '29DDDDD3333D4Z8', 'hashedPassword6', 'randomSalt6', '678967896789'),
(8, 'Kiran Desai', '9887654321', 'kiran.desai@gmail.com', '45 Cross Road, Ahmedabad', NULL, NULL, 'hashedPassword7', 'randomSalt7', '789078907890'),
(9, 'Manoj Kumar', '9897654321', 'manoj.kumar@gmail.com', '32 Hill View, Jaipur', 'Next Ventures', '08EEEEE4444E5Z9', 'hashedPassword8', 'randomSalt8', '890189018901'),
(10, 'Ananya Roy', '9871234567', 'ananya.roy@gmail.com', '71 Circular Road, Hyderabad', NULL, NULL, 'hashedPassword9', 'randomSalt9', '901290129012'),
(11, 'Ravi Nair', '9811122233', 'ravi.nair@gmail.com', '23 Ashok Nagar, Trivandrum', 'Clean Water Co.', '32FFFFFF5555F6Z', 'hashedPassword10', 'randomSalt10', '012301230123'),
(12, 'Meera Pillai', '9845566778', 'meera.pillai@gmail.com', '12 MG Road, Kochi', 'Design Hub', '15GGGGG6666G7Z2', 'hashedPassword11', 'randomSalt11', '123401234012'),
(13, 'Vivek Malhotra', '9876545678', 'vivek.malhotra@gmail.com', '54 GT Road, Chandigarh', 'Tech Giants', NULL, 'hashedPassword12', 'randomSalt12', '234512345123'),
(14, 'Ishita Das', '9832323456', 'ishita.das@gmail.com', '67 Sector 5, Noida', 'Foodies United', '21HHHHH7777H8Z3', 'hashedPassword13', 'randomSalt13', '345623456234'),
(15, 'Rajesh Patil', '9811234568', 'rajesh.patil@gmail.com', '43 Main Street, Goa', 'Adventure Travels', '18IIIII8888I9Z4', 'hashedPassword14', 'randomSalt14', '456734567345'),
(16, 'Divya Kapoor', '9833322345', 'divya.kapoor@gmail.com', '98 Outer Ring Road, Gurgaon', 'Smart Living Ltd', NULL, 'hashedPassword15', 'randomSalt15', '567845678456'),
(17, 'Nikhil Chawla', '9875536789', 'nikhil.chawla@gmail.com', '56 Residency Road, Lucknow', NULL, NULL, 'hashedPassword16', 'randomSalt16', '678956789567'),
(18, 'Simran Kaur', '9898895678', 'simran.kaur@gmail.com', '23 MG Road, Amritsar', 'Golden Threads', '03JJJJJ9999J0Z5', 'hashedPassword17', 'randomSalt17', '789067890678'),
(19, 'Abhishek Jain', '9813456789', 'abhishek.jain@gmail.com', '45 Sector 14, Faridabad', 'Startup Studio', '31KKKKK0000K1Z6', 'hashedPassword18', 'randomSalt18', '890178901789'),
(20, 'Pooja Reddy', '9891234567', 'pooja.reddy@gmail.com', '78 Jubilee Hills, Hyderabad', 'Reddy Corp', '29LLLLL1111L2Z7', 'hashedPassword19', 'randomSalt19', '901289012890'),
(21, 'Ajay Mehta', '9814456678', 'ajay.mehta@gmail.com', '15 New Market, Jaipur', 'Bright Minds Pvt Ltd', '08MMMMM2222M3Z8', 'hashedPassword21', 'randomSalt21', '123451234512'),
(22, 'Ritika Chopra', '9823344556', 'ritika.chopra@gmail.com', '78 Hill Road, Pune', NULL, NULL, 'hashedPassword22', 'randomSalt22', '234562345623'),
(23, 'Kunal Aggarwal', '9845567889', 'kunal.aggarwal@gmail.com', '98 Residency Road, Bangalore', 'Code Breakers', '27NNNNN3333N4Z9', 'hashedPassword23', 'randomSalt23', '345673456734'),
(24, 'Shreya Sen', '9871122334', 'shreya.sen@gmail.com', '34 Park Street, Kolkata', 'Creative Solutions', NULL, 'hashedPassword24', 'randomSalt24', '456784567845'),
(25, 'Deepak Gupta', '9823345678', 'deepak.gupta@gmail.com', '12 MG Road, Indore', NULL, NULL, 'hashedPassword25', 'randomSalt25', '567895678956'),
(26, 'Aarti Kulkarni', '9765567788', 'aarti.kulkarni@gmail.com', '23 Anna Nagar, Chennai', 'Health First Pvt Ltd', '22OOOOO4444O5Z1', 'hashedPassword26', 'randomSalt26', '678906789067'),
(27, 'Sanjay Bhardwaj', '9893345567', 'sanjay.bhardwaj@gmail.com', '67 Palace Road, Delhi', 'NextGen Startups', '07PPPPP5555P6Z2', 'hashedPassword27', 'randomSalt27', '789017890178'),
(28, 'Poonam Rathi', '9845561234', 'poonam.rathi@gmail.com', '89 Ashok Nagar, Jaipur', 'Dream Events', NULL, 'hashedPassword28', 'randomSalt28', '890128901289'),
(29, 'Ankit Rawat', '9817788990', 'ankit.rawat@gmail.com', '34 MG Road, Dehradun', NULL, NULL, 'hashedPassword29', 'randomSalt29', '901239012390'),
(30, 'Madhuri Dixit', '9823445566', 'madhuri.dixit@gmail.com', '56 Residency Road, Mumbai', 'Film Makers Inc', '18QQQQQ6666Q7Z3', 'hashedPassword30', 'randomSalt30', '012340123401'),
(31, 'Rajiv Kapoor', '9873345567', 'rajiv.kapoor@gmail.com', '78 Outer Ring Road, Gurgaon', 'Gadget Geeks', '03RRRRR7777R8Z4', 'hashedPassword31', 'randomSalt31', '123451234592'),
(32, 'Kavita Menon', '9765677888', 'kavita.menon@gmail.com', '45 Cross Road, Kochi', NULL, NULL, 'hashedPassword32', 'randomSalt32', '234562345620'),
(33, 'Siddharth Deshmukh', '9891122334', 'siddharth.deshmukh@gmail.com', '67 MG Road, Pune', 'Smart Gadgets Ltd', '22SSSSS8888S9Z5', 'hashedPassword33', 'randomSalt33', '345673456034'),
(34, 'Rohini Naidu', '9845563456', 'rohini.naidu@gmail.com', '23 Park Street, Bangalore', 'Foodies Delight', NULL, 'hashedPassword34', 'randomSalt34', '456784567945'),
(35, 'Varun Khanna', '9812233445', 'varun.khanna@gmail.com', '56 Residency Road, Chandigarh', 'EduStart', '31TTTTT9999T0Z6', 'hashedPassword35', 'randomSalt35', '567898678956'),
(36, 'Tanya Bhagat', '9823345567', 'tanya.bhagat@gmail.com', '98 Circular Road, Hyderabad', NULL, NULL, 'hashedPassword36', 'randomSalt36', '678906689067'),
(37, 'Naveen Joshi', '9813345567', 'naveen.joshi@gmail.com', '34 Ashok Nagar, Trivandrum', 'Bright Future Pvt Ltd', '28UUUUU0000U1Z7', 'hashedPassword37', 'randomSalt37', '789017890108'),
(38, 'Isha Bansal', '9832233445', 'isha.bansal@gmail.com', '45 GT Road, Jaipur', 'Golden Threads', '08VVVVV1111V2Z8', 'hashedPassword38', 'randomSalt38', '890128901209'),
(39, 'Rohan Seth', '9845562345', 'rohan.seth@gmail.com', '12 Residency Road, Bangalore', 'Tech Solutions', NULL, 'hashedPassword39', 'randomSalt39', '901239012090'),
(40, 'Amrita Bose', '9872233445', 'amrita.bose@gmail.com', '78 MG Road, Kolkata', NULL, NULL, 'hashedPassword40', 'randomSalt40', '012300123401'),
(41, 'Shanm', '12345678990', 'shans@gmail.com', 'dhfa', 'DSH F', 'H DKJ', 'd4736b50f0c52aa8fe67505b4c6e2215754e7a4692ccd015eac673f871d3d2fd', 'ac8b2c53c5c140c777358d278a7d2601', '1234567899'),
(42, 'Shans', '1234566', 'ss@gmail.com', NULL, NULL, NULL, 'd8fd807e69687852bc7cfbb1af73361f54ca833f8e7603b196134fc5f4ba2e4f', 'a799eecc7975454c563bd729e9afdb3e', '122'),
(43, 'John Doe', '7031234567', 'johndoe@gmail.com', '1701 Patrick Henry Drive, Blacksburg, VA, 24060', 'John Doe Inc.', 'abcd00000987654', 'd4089ab65e287208183d8e5a971a00de0c480fc7ebb0c751612244e7546a87b3', '3a63f93beefd263b78bf8ae20f14a7c7', '123456789000');

-- --------------------------------------------------------

--
-- Table structure for table `Payments`
--

CREATE TABLE `Payments` (
  `PaymentID` int(11) NOT NULL,
  `InvoiceID` int(11) DEFAULT NULL,
  `MemberID` int(11) DEFAULT NULL,
  `PaymentDate` date DEFAULT NULL,
  `Amount` decimal(10,2) DEFAULT NULL,
  `PaymentMethod` varchar(50) DEFAULT NULL,
  `Status` varchar(50) DEFAULT NULL,
  `TransactionID` varchar(50) DEFAULT NULL,
  `LateFee` decimal(5,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `price`
--

CREATE TABLE `price` (
  `priceid` int(11) NOT NULL,
  `spaceid` int(11) NOT NULL,
  `HourlyPrice` decimal(10,2) NOT NULL,
  `MonthlyPrice` decimal(10,2) NOT NULL,
  `DailyPrice` decimal(10,2) NOT NULL,
  `YearlyPrice` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `price`
--

INSERT INTO `price` (`priceid`, `spaceid`, `HourlyPrice`, `MonthlyPrice`, `DailyPrice`, `YearlyPrice`) VALUES
(3, 103, '100.00', '2500.00', '1000.00', '10000.00'),
(4, 105, '200.00', '6000.00', '2500.00', '20000.00'),
(5, 106, '80.00', '2000.00', '750.00', '9000.00'),
(6, 107, '60.00', '1800.00', '600.00', '7000.00'),
(7, 108, '150.00', '4000.00', '1200.00', '15000.00'),
(8, 109, '45.00', '1300.00', '450.00', '5000.00'),
(9, 110, '300.00', '9000.00', '3500.00', '30000.00'),
(10, 201, '90.00', '2500.00', '1000.00', '12000.00'),
(11, 202, '55.00', '1600.00', '550.00', '7000.00'),
(12, 203, '180.00', '5000.00', '2000.00', '17000.00'),
(13, 204, '50.00', '1400.00', '500.00', '6000.00'),
(14, 205, '250.00', '8000.00', '3000.00', '25000.00'),
(15, 206, '85.00', '2200.00', '850.00', '10000.00'),
(16, 207, '70.00', '2000.00', '700.00', '8000.00'),
(17, 208, '200.00', '5500.00', '2200.00', '20000.00'),
(18, 209, '48.00', '1400.00', '480.00', '5000.00'),
(19, 210, '320.00', '9500.00', '3600.00', '35000.00'),
(20, 301, '95.00', '2700.00', '1100.00', '13000.00'),
(21, 302, '60.00', '1800.00', '600.00', '7500.00'),
(22, 303, '190.00', '5200.00', '2100.00', '18000.00'),
(23, 304, '52.00', '1450.00', '520.00', '6500.00'),
(24, 305, '280.00', '8500.00', '3200.00', '30000.00'),
(25, 306, '88.00', '2300.00', '880.00', '11000.00'),
(26, 307, '65.00', '1900.00', '650.00', '8000.00'),
(27, 308, '210.00', '6000.00', '2400.00', '22000.00'),
(28, 309, '50.00', '1500.00', '500.00', '5500.00'),
(29, 310, '350.00', '10000.00', '4000.00', '40000.00'),
(30, 401, '100.00', '2800.00', '1200.00', '14000.00'),
(31, 402, '70.00', '2000.00', '700.00', '8000.00'),
(32, 403, '200.00', '5800.00', '2300.00', '20000.00'),
(33, 404, '55.00', '1600.00', '550.00', '6000.00'),
(34, 405, '300.00', '9000.00', '3500.00', '35000.00'),
(35, 406, '92.00', '2400.00', '920.00', '12000.00'),
(36, 407, '75.00', '2100.00', '750.00', '9000.00'),
(37, 408, '220.00', '6300.00', '2500.00', '22000.00'),
(38, 409, '50.00', '1500.00', '500.00', '5500.00'),
(39, 410, '340.00', '9700.00', '3800.00', '37000.00'),
(40, 501, '105.00', '2900.00', '1250.00', '15000.00'),
(41, 502, '65.00', '1900.00', '650.00', '7500.00'),
(42, 503, '210.00', '6000.00', '2400.00', '22000.00'),
(43, 504, '58.00', '1650.00', '580.00', '6000.00'),
(44, 505, '320.00', '9600.00', '3800.00', '38000.00'),
(45, 1001, '90.00', '2500.00', '1000.00', '12000.00'),
(46, 1002, '85.00', '2300.00', '900.00', '11000.00');

-- --------------------------------------------------------

--
-- Table structure for table `Spaces`
--

CREATE TABLE `Spaces` (
  `SpaceID` int(11) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Location` varchar(255) DEFAULT NULL,
  `Type` varchar(50) NOT NULL,
  `Capacity` int(11) DEFAULT NULL,
  `OccupationStatus` varchar(25) DEFAULT NULL,
  `Amenities` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `Spaces`
--

INSERT INTO `Spaces` (`SpaceID`, `Name`, `Location`, `Type`, `Capacity`, `OccupationStatus`, `Amenities`) VALUES
(102, 'Common Lounge A', 'Bangalore', 'Common Area', 12, 'Available', 'WiFi, Coffee Machine, Bean Bags'),
(103, 'Conference Room Beta', 'Bangalore', 'Conference Room', 20, 'Occupied', 'WiFi, Projector, Whiteboard'),
(104, 'Hotspot Desk A', 'Bangalore', 'Hotspot Desk', 8, 'Available', 'WiFi, Power Outlets, Standing Desks'),
(105, 'Event Space A', 'Bangalore', 'Event Space', 50, 'Booked', 'WiFi, AV System, Catering Service'),
(106, 'Private Cabin Beta', 'Bangalore', 'Private Cabin', 2, 'Booked', 'WiFi, Filing Cabinet, Quiet Zone'),
(107, 'Common Lounge B', 'Bangalore', 'Common Area', 10, 'Occupied', 'WiFi, Bean Bags, Lounge Chairs'),
(108, 'Conference Room Gamma', 'Bangalore', 'Conference Room', 18, 'Available', 'WiFi, Interactive Screen, Projector'),
(109, 'Hotspot Desk B', 'Bangalore', 'Hotspot Desk', 6, 'Available', 'WiFi, Charging Ports, Flexible Seating'),
(110, 'Event Space B', 'Bangalore', 'Event Space', 100, 'Occupied', 'WiFi, AV System, Catering Service'),
(201, 'Private Cabin Gamma', 'Bangalore', 'Private Cabin', 4, 'Available', 'WiFi, Ergonomic Chair, Monitor'),
(202, 'Common Lounge C', 'Bangalore', 'Common Area', 15, 'Available', 'WiFi, Coffee Machine, Charging Points'),
(203, 'Conference Room Delta', 'Bangalore', 'Conference Room', 25, 'Occupied', 'WiFi, Screen, Video Conference'),
(204, 'Hotspot Desk C', 'Bangalore', 'Hotspot Desk', 10, 'Available', 'WiFi, Height Adjustable Tables'),
(205, 'Event Space C', 'Bangalore', 'Event Space', 70, 'Available', 'WiFi, AV System, Event Setup'),
(206, 'Private Cabin Delta', 'Bangalore', 'Private Cabin', 3, 'Available', 'WiFi, Monitor, Quiet Environment'),
(207, 'Common Lounge D', 'Bangalore', 'Common Area', 20, 'Occupied', 'WiFi, Lounge Chairs, Coffee Machine'),
(208, 'Conference Room Epsilon', 'Bangalore', 'Conference Room', 30, 'Available', 'WiFi, Projector, Sound System'),
(209, 'Hotspot Desk D', 'Bangalore', 'Hotspot Desk', 8, 'Available', 'WiFi, Individual Power Outlets'),
(210, 'Event Space D', 'Bangalore', 'Event Space', 150, 'Available', 'WiFi, AV System, Catering Service'),
(301, 'Private Cabin Zeta', 'Bangalore', 'Private Cabin', 2, 'Available', 'WiFi, Noise-Canceling Environment'),
(302, 'Common Lounge E', 'Bangalore', 'Common Area', 18, 'Occupied', 'WiFi, Lounge Chairs, Coffee Machine'),
(303, 'Conference Room Zeta', 'Bangalore', 'Conference Room', 40, 'Available', 'WiFi, Interactive Screen, Video Conferencing'),
(304, 'Hotspot Desk E', 'Bangalore', 'Hotspot Desk', 12, 'Available', 'WiFi, Adjustable Workspaces'),
(305, 'Event Space E', 'Bangalore', 'Event Space', 200, 'Available', 'WiFi, AV System, Catering Service'),
(306, 'Private Cabin Eta', 'Bangalore', 'Private Cabin', 4, 'Occupied', 'WiFi, Monitor, Ergonomic Chair'),
(307, 'Common Lounge F', 'Bangalore', 'Common Area', 14, 'Available', 'WiFi, Bean Bags, Coffee Machine'),
(308, 'Conference Room Theta', 'Bangalore', 'Conference Room', 22, 'Available', 'WiFi, Projector, Whiteboard'),
(309, 'Hotspot Desk F', 'Bangalore', 'Hotspot Desk', 5, 'Available', 'WiFi, Charging Ports, Height Adjustable Tables'),
(310, 'Event Space F', 'Bangalore', 'Event Space', 120, 'Occupied', 'WiFi, AV System, Catering Service'),
(401, 'Private Cabin Iota', 'Bangalore', 'Private Cabin', 3, 'Available', 'WiFi, Monitor, Noise-Canceling Environment'),
(402, 'Common Lounge G', 'Bangalore', 'Common Area', 25, 'Available', 'WiFi, Charging Ports, Coffee Bar'),
(403, 'Conference Room Kappa', 'Bangalore', 'Conference Room', 35, 'Occupied', 'WiFi, Projector, Sound System'),
(404, 'Hotspot Desk G', 'Bangalore', 'Hotspot Desk', 7, 'Available', 'WiFi, Individual Power Outlets'),
(405, 'Event Space G', 'Bangalore', 'Event Space', 160, 'Available', 'WiFi, AV System, Catering Service'),
(406, 'Private Cabin Lambda', 'Bangalore', 'Private Cabin', 2, 'Occupied', 'WiFi, Filing Cabinet, Quiet Zone'),
(407, 'Common Lounge H', 'Bangalore', 'Common Area', 20, 'Available', 'WiFi, Bean Bags, Lounge Chairs'),
(408, 'Conference Room Mu', 'Bangalore', 'Conference Room', 18, 'Available', 'WiFi, Screen, Projector'),
(409, 'Hotspot Desk H', 'Bangalore', 'Hotspot Desk', 6, 'Available', 'WiFi, Charging Ports, Flexible Seating'),
(410, 'Event Space H', 'Bangalore', 'Event Space', 140, 'Occupied', 'WiFi, AV System, Event Setup'),
(501, 'Private Cabin Nu', 'Bangalore', 'Private Cabin', 4, 'Available', 'WiFi, Ergonomic Chair, Quiet Zone'),
(502, 'Common Lounge I', 'Bangalore', 'Common Area', 15, 'Occupied', 'WiFi, Coffee Machine, Bean Bags'),
(503, 'Conference Room Xi', 'Bangalore', 'Conference Room', 20, 'Available', 'WiFi, Interactive Screen, Projector'),
(504, 'Hotspot Desk I', 'Bangalore', 'Hotspot Desk', 10, 'Available', 'WiFi, Adjustable Workspaces'),
(505, 'Event Space I', 'Bangalore', 'Event Space', 170, 'Available', 'WiFi, AV System, Catering Service'),
(1001, 'Private Cabin Alpha', 'Bangalore', 'Private Cabin', 3, 'Available', 'WiFi, Ergonomic Chair, Monitor'),
(1002, 'Private Cabin', 'Basavanagudi', 'Private Cabin ', 5, 'Avaliable ', 'wifi, house keeping, printer, lan'),
(100043, 'lkdjflkH', 'jehfkj', 'fhej wkh ', 11, 'dhkj ', 'h fjksh hfjk fh');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `Bookings`
--
ALTER TABLE `Bookings`
  ADD PRIMARY KEY (`BookingID`),
  ADD KEY `SpaceID` (`SpaceID`),
  ADD KEY `MemberID` (`MemberID`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `Employees`
--
ALTER TABLE `Employees`
  ADD PRIMARY KEY (`EmployeeID`),
  ADD UNIQUE KEY `Email` (`Email`),
  ADD UNIQUE KEY `UC_Email` (`Email`),
  ADD UNIQUE KEY `AadharID` (`AadharID`),
  ADD UNIQUE KEY `UC_AadharID` (`AadharID`);

--
-- Indexes for table `Enquiries`
--
ALTER TABLE `Enquiries`
  ADD PRIMARY KEY (`EnquiryID`);

--
-- Indexes for table `Invoices`
--
ALTER TABLE `Invoices`
  ADD PRIMARY KEY (`InvoiceID`),
  ADD KEY `BookingID` (`BookingID`);

--
-- Indexes for table `Members`
--
ALTER TABLE `Members`
  ADD PRIMARY KEY (`MemberID`),
  ADD UNIQUE KEY `Email` (`Email`),
  ADD UNIQUE KEY `AadharID` (`AadharID`);

--
-- Indexes for table `Payments`
--
ALTER TABLE `Payments`
  ADD PRIMARY KEY (`PaymentID`),
  ADD KEY `InvoiceID` (`InvoiceID`),
  ADD KEY `MemberID` (`MemberID`);

--
-- Indexes for table `price`
--
ALTER TABLE `price`
  ADD PRIMARY KEY (`priceid`),
  ADD UNIQUE KEY `spaceid` (`spaceid`);

--
-- Indexes for table `Spaces`
--
ALTER TABLE `Spaces`
  ADD PRIMARY KEY (`SpaceID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `Bookings`
--
ALTER TABLE `Bookings`
  MODIFY `BookingID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=59;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `Employees`
--
ALTER TABLE `Employees`
  MODIFY `EmployeeID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `Invoices`
--
ALTER TABLE `Invoices`
  MODIFY `InvoiceID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `Members`
--
ALTER TABLE `Members`
  MODIFY `MemberID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;

--
-- AUTO_INCREMENT for table `price`
--
ALTER TABLE `price`
  MODIFY `priceid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Bookings`
--
ALTER TABLE `Bookings`
  ADD CONSTRAINT `Bookings_ibfk_1` FOREIGN KEY (`SpaceID`) REFERENCES `Spaces` (`SpaceID`),
  ADD CONSTRAINT `Bookings_ibfk_2` FOREIGN KEY (`MemberID`) REFERENCES `Members` (`MemberID`);

--
-- Constraints for table `Enquiries`
--
ALTER TABLE `Enquiries`
  ADD CONSTRAINT `Enquiries_ibfk_1` FOREIGN KEY (`LeadID`) REFERENCES `Leads` (`LeadID`);

--
-- Constraints for table `Invoices`
--
ALTER TABLE `Invoices`
  ADD CONSTRAINT `Invoices_ibfk_1` FOREIGN KEY (`BookingID`) REFERENCES `Bookings` (`BookingID`);

--
-- Constraints for table `Payments`
--
ALTER TABLE `Payments`
  ADD CONSTRAINT `Payments_ibfk_1` FOREIGN KEY (`InvoiceID`) REFERENCES `Invoices` (`InvoiceID`),
  ADD CONSTRAINT `Payments_ibfk_2` FOREIGN KEY (`MemberID`) REFERENCES `Members` (`MemberID`);

--
-- Constraints for table `price`
--
ALTER TABLE `price`
  ADD CONSTRAINT `fk_spaceid` FOREIGN KEY (`spaceid`) REFERENCES `Spaces` (`SpaceID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
