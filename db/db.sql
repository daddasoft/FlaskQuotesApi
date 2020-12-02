-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 25, 2020 at 03:50 PM
-- Server version: 8.0.13-4
-- PHP Version: 7.2.24-0ubuntu0.18.04.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `8wophxXBD1`
--

-- --------------------------------------------------------

--
-- Table structure for table `apikeys`
--

CREATE TABLE `apikeys` (
  `user_id` int(11) DEFAULT NULL,
  `token` varchar(20) DEFAULT NULL,
  `expireDate` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `quotes`
--

CREATE TABLE `quotes` (
  `id` bigint(20) NOT NULL,
  `body` text NOT NULL,
  `author` varchar(50) NOT NULL DEFAULT 'Uknown',
  `createdBy` int(11) NOT NULL,
  `category` varchar(50) NOT NULL DEFAULT 'other',
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `quotes`
--

INSERT INTO `quotes` (`id`, `body`, `author`, `createdBy`, `category`, `createdAt`, `updatedAt`) VALUES
(185, 'Forty is the old age of youth; fifty is the youth of old age.', 'Victor Hugo', 19, 'Life', '2020-11-21 01:50:59', '2020-11-21 01:50:59'),
(186, 'Beauty, without expression, tires.', 'Ralph Waldo Emerson', 19, 'Beauty', '2020-11-21 01:52:18', '2020-11-21 01:52:18'),
(187, 'It is amazing how complete is the delusion that beauty is goodness.', 'Leo Tolstoy', 19, 'Beauty', '2020-11-21 01:52:42', '2020-11-21 01:52:42'),
(188, 'A business absolutely devoted to service will have only one worry about\nprofits. They will be embarrassingly large', 'Henry Ford', 19, 'Business', '2020-11-21 01:53:16', '2020-11-21 01:53:16'),
(189, 'By working faithfully eight hours a day you may eventually get to be boss and\nwork twelve hours a day.', 'Robert Frost', 19, 'Beauty', '2020-11-21 01:54:10', '2020-11-21 01:54:10'),
(191, 'Failure is simply the opportunity to begin again, this time more intelligently.', 'Henry Ford', 19, 'Success', '2020-11-21 02:15:02', '2020-11-21 02:15:02'),
(192, 'Success is walking from failure to failure with no loss of enthusiasm.', 'Winston Churchill', 19, 'Success', '2020-11-21 02:15:48', '2020-11-21 02:15:48'),
(193, 'Eighty percent of success is showing up.', 'Woody Allen', 19, 'Success', '2020-11-21 02:22:19', '2020-11-21 02:22:19'),
(194, 'Everything we do affects other people.', 'Luke Ford', 19, 'other', '2020-11-21 02:28:54', '2020-11-21 02:28:54'),
(195, 'The difference between the old ballplayer and the new ballplayer is the jersey.\nThe old ballplayer cared about the name on the front. The new ballplayer cares\nabout the name on the back.', 'Steve Garvey', 19, 'Sports', '2020-11-21 02:51:38', '2020-11-21 02:51:38'),
(196, 'Never leave that till tomorrow which you can do today', 'Benjamin Franklin', 19, 'Success', '2020-11-21 02:52:14', '2020-11-21 02:52:14'),
(197, 'I will tell you how to become rich. Close the doors. Be fearful when others are\ngreedy. Be greedy when others are fearful.', 'Warren Buffet', 19, 'Money', '2020-11-21 02:53:06', '2020-11-21 02:53:06'),
(198, 'Love is composed of a single soul inhabiting two bodies.', 'Aristotle', 19, 'Love', '2020-11-21 03:02:05', '2020-11-21 03:02:05'),
(199, 'Love is friendship, set on fire.', 'Jeremy Taylor', 19, 'Love', '2020-11-21 03:02:19', '2020-11-21 03:02:19'),
(200, 'It is not a lack of love, but a lack of friendship that makes unhappy marriages.', 'Friedrich Nietzsche', 19, 'Love', '2020-11-21 03:02:49', '2020-11-21 03:02:49'),
(201, 'Love is like a virus. It can happen to anybody at\nany time.', 'Maya Angelou', 19, 'Love', '2020-11-21 03:03:24', '2020-11-21 03:03:24'),
(202, 'The only rock I know that stays steady, the only institution I know that works is\nthe family.', 'Lee Iacocca', 19, 'Family', '2020-11-21 03:04:06', '2020-11-21 03:04:06'),
(203, 'You know the only people who are always sure about the proper way to raise\nchildren ? Those who’ve never had any.', 'Bill Cosby', 19, 'Family', '2020-11-21 03:04:39', '2020-11-21 03:04:39'),
(204, 'Mistakes are always forgivable, if one has the courage to admit them.', 'Bruce Lee', 19, 'Courage', '2020-11-21 03:06:01', '2020-11-21 03:06:01'),
(205, 'The greatest discovery of all time is that a person can change his future by\nmerely changing his attitude.', 'Oprah Winfrey', 19, 'Change', '2020-11-21 03:07:04', '2020-11-21 03:07:04'),
(206, 'Consider how hard it is to change yourself and you’ll understand what little\nchance you have in trying to change others.', 'Jacob M. Braude', 19, 'Change', '2020-11-21 03:07:28', '2020-11-21 03:07:28'),
(207, 'A real entrepreneur is somebody who has no safety net underneath them.', 'Henry Kravis', 19, 'Business', '2020-11-21 03:08:05', '2020-11-21 03:08:05'),
(208, 'Beauty is only skin deep, but ugly goes clean to the bone.', 'Dorothy Parker', 19, 'Beauty', '2020-11-21 03:08:53', '2020-11-21 03:08:53'),
(209, 'Middle age is when you’re sitting at home on a Saturday night and the telephone rings and you hope it isn’t for you.', 'Ogden Nash', 26, 'other', '2020-11-21 03:12:56', '2020-11-21 03:12:56'),
(210, 'I do not think much of a man who is not wiser today than he was yesterday.', 'Abraham Lincoln', 19, 'Change', '2020-11-21 14:29:35', '2020-11-21 14:29:35'),
(211, 'If you can\'t sleep, then get up and do something instead of lying there and worrying. It\'s the worry that gets you, not the loss of sleep.', 'Dale Carnegie', 19, 'Success', '2020-11-21 14:30:47', '2020-11-21 14:30:47'),
(212, 'Are you bored with life? Then throw yourself into some work you believe in with all your heart, live for it, die for it, and you will find happiness that you had thought could never be yours.', 'Dale Carnegie', 19, 'other', '2020-11-21 14:31:51', '2020-11-21 14:31:51'),
(213, 'Mistakes are painful when they happen, but years later a collection of mistakes is what is called experience.', 'Dennis Waitley', 19, 'Success', '2020-11-21 14:34:21', '2020-11-21 14:34:21'),
(214, 'You must learn from your past mistakes, but not lean on your past successes.', 'Dennis Waitley', 19, 'Success', '2020-11-21 14:34:59', '2020-11-21 14:34:59'),
(215, 'I try to learn from the past, but I plan for the future by focusing exclusively on the present. That\'s were the fun is.', 'Donald Trump', 19, 'Courage', '2020-11-21 14:35:43', '2020-11-21 14:35:43'),
(216, 'You become what you think about.', 'Earl Nightingale', 19, 'Change', '2020-11-21 14:36:24', '2020-11-21 14:36:24'),
(217, 'For every disciplined effort there is a multiple reward.', 'Jim Rohn', 19, 'Courage', '2020-11-21 15:07:12', '2020-11-21 15:07:12'),
(218, 'The book you don\'t read cant help.', 'Jim Rohn', 19, 'Science', '2020-11-21 15:09:25', '2020-11-21 15:09:25'),
(223, 'You know you\'re in love when you can\'t fall asleep because reality is finally better than your dreams.', 'Dr. Seuss', 19, 'Love', '2020-12-04 15:42:34', '2020-12-04 15:42:34'),
(224, 'A friend is someone who knows all about you and still loves you.', 'Elbert Hubbard', 19, 'Love', '2020-12-04 15:43:48', '2020-12-04 15:43:48'),
(226, 'hgfghfghf', 'hellllooo', 19, 'Children', '2020-12-16 12:32:41', '2020-12-16 12:32:41'),
(227, 'The greatest glory in living lies not in never falling, but in rising every time we fall.', 'Nelson Mandela', 28, 'other', '2020-12-21 14:57:09', '2020-12-21 14:57:09'),
(229, 'The way to get started is to quit talking and begin doing.', 'Walt Disney', 28, 'Change', '2020-12-21 14:58:25', '2020-12-21 14:58:25'),
(230, 'If life were predictable it would cease to be life, and be without flavor.', 'Eleanor Roosevelt', 28, 'other', '2020-12-21 14:59:20', '2020-12-21 14:59:20');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(25) NOT NULL,
  `email` varchar(30) NOT NULL,
  `password` varchar(100) NOT NULL,
  `role` varchar(10) NOT NULL DEFAULT 'user',
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `email`, `password`, `role`, `created_at`, `updated_at`) VALUES
(19, 'daddasoft', 'studio.dadda@gmail.com', 'pbkdf2:sha256:150000$lFtKH9uO$52241c336cbbcf166cd186d320a61ee947520720e5d90512aa2d1d1965668f57', 'user', '2020-11-19 13:52:47', '2020-11-19 13:52:47'),
(26, 'daddasoft99', 'dadda@gmail.com', 'pbkdf2:sha256:150000$BqXmeaXz$7970bea04323c3008db119a518662f618ad2bd2372892620ff45e416826d6c76', 'user', '2020-11-21 03:11:01', '2020-11-21 03:11:01'),
(27, 'helloclass', 'helloclass@me.com', 'pbkdf2:sha256:150000$lI3BJjbF$46cc2cf27337227c8870aca133a947c67044a8a4c2d437db417c44c09637fdb0', 'user', '2020-11-23 10:51:13', '2020-11-23 10:51:13'),
(28, 'daddadadda', 'studio.soft@gmail.com', 'pbkdf2:sha256:150000$2a7FeU6p$ab761bb0529059e4b1fb60b4bbd5d92d608451c7faa7a083a93f9a0bbd80e0cf', 'user', '2020-12-21 14:55:19', '2020-12-21 14:55:19');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `apikeys`
--
ALTER TABLE `apikeys`
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `quotes`
--
ALTER TABLE `quotes`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `quotes`
--
ALTER TABLE `quotes`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=231;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `apikeys`
--
ALTER TABLE `apikeys`
  ADD CONSTRAINT `apikeys_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
