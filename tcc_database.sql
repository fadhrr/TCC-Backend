-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 31 Jan 2024 pada 05.02
-- Versi server: 10.4.28-MariaDB
-- Versi PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tcc_database`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `admins`
--

CREATE TABLE `admins` (
  `id` varchar(40) NOT NULL,
  `user_id` varchar(40) NOT NULL,
  `role` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `admins`
--

INSERT INTO `admins` (`id`, `user_id`, `role`, `created_at`, `updated_at`) VALUES
('1', '1', 'admin', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
('2', '2', 'admin', '2024-01-26 10:28:43', '2024-01-26 10:28:43');

-- --------------------------------------------------------

--
-- Struktur dari tabel `categories`
--

CREATE TABLE `categories` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `name` varchar(255) NOT NULL,
  `slug` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `categories`
--

INSERT INTO `categories` (`id`, `name`, `slug`, `created_at`, `updated_at`) VALUES
(1, 'Array', 'array', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(2, 'Sorting', 'sorting', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(3, 'Dynamic Programming', 'dynamic-programming', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(4, 'Graph Theory', 'graph-theory', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(5, 'String', 'string', '2024-01-26 10:28:43', '2024-01-26 10:28:43');

-- --------------------------------------------------------

--
-- Struktur dari tabel `contests`
--

CREATE TABLE `contests` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `admin_id` varchar(40) NOT NULL,
  `title` varchar(255) NOT NULL,
  `slug` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `start_time` timestamp NULL DEFAULT NULL,
  `end_time` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `contests`
--

INSERT INTO `contests` (`id`, `admin_id`, `title`, `slug`, `description`, `start_time`, `end_time`, `created_at`, `updated_at`) VALUES
(1, '1', 'Contest Pertama', 'contest-pertama', 'Deskripsi contest pertama.', '2024-01-26 10:28:43', '2024-02-02 10:28:43', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(2, '2', 'Contest Kedua', 'contest-kedua', 'Deskripsi contest kedua.', '2024-02-05 10:28:43', '2024-02-12 10:28:43', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(3, '1', 'Contest Ketiga', 'contest-ketiga', 'Deskripsi contest ketiga.', '2024-02-15 10:28:43', '2024-02-22 10:28:43', '2024-01-26 10:28:43', '2024-01-26 10:28:43');

-- --------------------------------------------------------

--
-- Struktur dari tabel `failed_jobs`
--

CREATE TABLE `failed_jobs` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `uuid` varchar(255) NOT NULL,
  `connection` text NOT NULL,
  `queue` text NOT NULL,
  `payload` longtext NOT NULL,
  `exception` longtext NOT NULL,
  `failed_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `languages`
--

CREATE TABLE `languages` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `name` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `languages`
--

INSERT INTO `languages` (`id`, `name`, `created_at`, `updated_at`) VALUES
(1, 'Java', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(2, 'C++', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(3, 'C', '2024-01-26 10:28:42', '2024-01-26 10:28:42');

-- --------------------------------------------------------

--
-- Struktur dari tabel `migrations`
--

CREATE TABLE `migrations` (
  `id` int(10) UNSIGNED NOT NULL,
  `migration` varchar(255) NOT NULL,
  `batch` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `migrations`
--

INSERT INTO `migrations` (`id`, `migration`, `batch`) VALUES
(1, '2014_10_12_000000_create_users_table', 1),
(2, '2014_10_12_100000_create_password_reset_tokens_table', 1),
(3, '2019_08_19_000000_create_failed_jobs_table', 1),
(4, '2019_12_14_000001_create_personal_access_tokens_table', 1),
(5, '2024_01_26_162704_create_admins_table', 1),
(6, '2024_01_26_162737_create_contests_table', 1),
(7, '2024_01_26_162746_create_problems_table', 1),
(8, '2024_01_26_163015_create_categories_table', 1),
(9, '2024_01_26_163156_create_test_cases_table', 1),
(10, '2024_01_26_163229_create_submissions_table', 1),
(11, '2024_01_26_163238_create_languages_table', 1);

-- --------------------------------------------------------

--
-- Struktur dari tabel `password_reset_tokens`
--

CREATE TABLE `password_reset_tokens` (
  `email` varchar(255) NOT NULL,
  `token` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `personal_access_tokens`
--

CREATE TABLE `personal_access_tokens` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `tokenable_type` varchar(255) NOT NULL,
  `tokenable_id` bigint(20) UNSIGNED NOT NULL,
  `name` varchar(255) NOT NULL,
  `token` varchar(64) NOT NULL,
  `abilities` text DEFAULT NULL,
  `last_used_at` timestamp NULL DEFAULT NULL,
  `expires_at` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `problems`
--

CREATE TABLE `problems` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `title` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `time_limit` int(11) NOT NULL,
  `memory_limit` int(11) NOT NULL,
  `input_format` text NOT NULL,
  `sample_input` text NOT NULL,
  `output_format` text NOT NULL,
  `sample_output` text NOT NULL,
  `constraints` text NOT NULL,
  `explanation` text DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `problems`
--

INSERT INTO `problems` (`id`, `title`, `description`, `time_limit`, `memory_limit`, `input_format`, `sample_input`, `output_format`, `sample_output`, `constraints`, `explanation`, `created_at`, `updated_at`) VALUES
(1, 'Penjumlahan Sederhana', 'Buatlah program yang menerima dua bilangan bulat dan mengeluarkan hasil penjumlahannya.', 1, 16, 'Dua baris berisi satu bilangan bulat tiap baris.', '3\n5', 'Satu baris berisi hasil penjumlahan kedua bilangan.', '8', 'Bilangan yang diinputkan merupakan bilangan bulat dalam rentang -10^9 hingga 10^9.', 'Program harus membaca dua bilangan (3 dan 5), dan mengeluarkan hasil penjumlahannya (8).', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(2, 'Menghitung Faktorial', 'Buatlah program yang menghitung faktorial dari sebuah bilangan bulat positif.', 2, 32, 'Satu baris berisi satu bilangan bulat n (0 ≤ n ≤ 10).', '5', 'Satu baris berisi hasil faktorial dari n.', '120', 'Program harus dapat menangani nilai n dari 0 hingga 10.', 'Program harus menghitung 5! (5 faktorial), yang merupakan hasil perkalian 5 × 4 × 3 × 2 × 1 = 120.', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(3, 'Bilangan Prima', 'Buatlah program yang menentukan apakah suatu bilangan bulat positif adalah bilangan prima atau bukan.', 3, 64, 'Satu baris berisi satu bilangan bulat n (1 ≤ n ≤ 10^5).', '11', 'Satu baris berisi \"YA\" jika n adalah bilangan prima, dan \"BUKAN\" jika tidak.', 'YA', 'Program harus dapat menangani nilai n dari 1 hingga 10^5.', 'Program harus mengecek apakah bilangan 11 adalah bilangan prima atau tidak. Karena 11 hanya dapat dibagi oleh 1 dan 11, maka bilangan tersebut adalah bilangan prima.', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(4, 'Penyusunan Angka', 'Andi memiliki sebuah array berisi n bilangan bulat. Dia ingin menyusun ulang array tersebut sehingga bilangan-bilangan yang berdekatan memiliki perbedaan absolut maksimum. Bantulah Andi menemukan susunan yang memenuhi kondisi tersebut.', 4, 128, 'Baris pertama berisi satu bilangan bulat n (1 ≤ n ≤ 10^5), jumlah bilangan dalam array. Baris kedua berisi n bilangan bulat yang dipisahkan oleh spasi, masing-masing bernilai antara -10^9 hingga 10^9.', '6\n3 5 1 8 2 7', 'Satu baris berisi susunan ulang array yang memenuhi kondisi.', '7 2 8 1 5 3', 'Program harus dapat menangani nilai n dari 1 hingga 10^5.', 'Susunan ulang yang memenuhi kondisi adalah [7, 2, 8, 1, 5, 3]. Perbedaan absolut antara bilangan berdekatan adalah maksimum.', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(5, 'Deret Fibonacci Termodifikasi', 'Diberikan sebuah deret Fibonacci termodifikasi sebagai berikut: F(1) = a, F(2) = b, dan F(n) = F(n-1)^2 + F(n-2) untuk n > 2. Tulislah program untuk menghitung nilai F(n) untuk suatu n yang diberikan.', 5, 256, 'Satu baris berisi dua bilangan bulat a dan b (1 ≤ a, b ≤ 10^9) yang merupakan nilai awal deret Fibonacci termodifikasi. Baris kedua berisi satu bilangan bulat n (1 ≤ n ≤ 10^5).', '2 5\n4', 'Satu baris berisi nilai F(n) dari deret termodifikasi.', '181', 'Program harus dapat menangani nilai a, b, dan n hingga 10^9.', 'Deret termodifikasi untuk a = 2, b = 5 adalah: 2, 5, 29, 870, 756250. Nilai F(4) dari deret ini adalah 181.', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(6, 'Menentukan Bilangan Genap atau Ganjil', 'Buatlah program yang menerima satu bilangan bulat dan menentukan apakah bilangan tersebut genap atau ganjil.', 1, 16, 'Satu baris berisi satu bilangan bulat.', '7', 'Satu baris berisi \"GENAP\" jika bilangan genap dan \"GANJIL\" jika bilangan ganjil.', 'GANJIL', 'Bilangan yang diinputkan merupakan bilangan bulat dalam rentang -10^9 hingga 10^9.', 'Program harus menentukan apakah bilangan 7 adalah genap atau ganjil dan mengeluarkan hasil \"GANJIL\".', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(7, 'Menyusun String', 'Buatlah program yang menerima sebuah string dan mengembalikan string baru yang terdiri dari karakter-karakter unik yang disusun dalam urutan abjad.', 2, 32, 'Satu baris berisi sebuah string.', 'programming', 'Satu baris berisi string baru yang terdiri dari karakter-karakter unik dalam urutan abjad.', 'agimmnoprr', 'Panjang string tidak melebihi 1000 karakter.', 'Program harus menyusun karakter-karakter unik dari string \"programming\" dalam urutan abjad, sehingga menghasilkan string \"agimmnoprr\".', '2024-01-26 10:28:42', '2024-01-26 10:28:42');

-- --------------------------------------------------------

--
-- Struktur dari tabel `problem_categories`
--

CREATE TABLE `problem_categories` (
  `id` int(11) NOT NULL,
  `problem_id` int(10) UNSIGNED NOT NULL,
  `category_id` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `problem_categories`
--

INSERT INTO `problem_categories` (`id`, `problem_id`, `category_id`) VALUES
(1, 2, 3),
(2, 1, 4),
(3, 2, 1),
(4, 3, 3);

-- --------------------------------------------------------

--
-- Struktur dari tabel `submissions`
--

CREATE TABLE `submissions` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `user_id` varchar(40) NOT NULL,
  `problem_id` bigint(20) UNSIGNED NOT NULL,
  `language_id` bigint(20) UNSIGNED NOT NULL,
  `status` varchar(255) NOT NULL,
  `time` int(11) NOT NULL,
  `memory` int(11) NOT NULL,
  `code` text NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `submissions`
--

INSERT INTO `submissions` (`id`, `user_id`, `problem_id`, `language_id`, `status`, `time`, `memory`, `code`, `created_at`, `updated_at`) VALUES
(1, '1', 1, 1, 'Accepted', 10, 256, '#include <iostream>\\nint main() { std::cout << \"Hello, World!\"; return 0; }', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(2, '2', 3, 2, 'Wrong Answer', 15, 512, '#include <stdio.h>\\nint main() { printf(\"Wrong Answer\\n\"); return 0; }', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(3, '1', 6, 3, 'Compile Error', 5, 128, 'def print_message():\\n    print(\"Compile Error\")', '2024-01-26 10:28:43', '2024-01-26 10:28:43');

-- --------------------------------------------------------

--
-- Struktur dari tabel `test_cases`
--

CREATE TABLE `test_cases` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `problem_id` bigint(20) UNSIGNED NOT NULL,
  `input` varchar(255) NOT NULL,
  `output` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `test_cases`
--

INSERT INTO `test_cases` (`id`, `problem_id`, `input`, `output`, `created_at`, `updated_at`) VALUES
(1, 1, '3\n5', '8', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(2, 2, '5', '120', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(3, 3, '11', 'YA', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(4, 4, '6\n3 5 1 8 2 7', '7 2 8 1 5 3', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(5, 5, '2 5\n4', '181', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(6, 6, '7', 'GANJIL', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(7, 7, 'programming', 'agimmnoprr', '2024-01-26 10:28:42', '2024-01-26 10:28:42');

-- --------------------------------------------------------

--
-- Struktur dari tabel `users`
--

CREATE TABLE `users` (
  `id` varchar(40) NOT NULL,
  `name` varchar(255) NOT NULL,
  `nim` varchar(255) DEFAULT NULL,
  `score` int(11) NOT NULL DEFAULT 0,
  `email` varchar(255) NOT NULL,
  `email_verified_at` timestamp NULL DEFAULT NULL,
  `remember_token` varchar(100) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `
--

INSERT INTO `users` (`id`, `name`, `nim`, `score`, `email`, `email_verified_at`, `remember_token`, `created_at`, `updated_at`) VALUES
('1', 'Admin User', 'A12345', 150, 'admin@example.com', NULL, NULL, '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
('2', 'John Doe', 'B67890', 100, 'john.doe@example.com', NULL, NULL, '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
('3', 'Jane Smith', 'C54321', 120, 'jane.smith@example.com', NULL, NULL, '2024-01-26 10:28:43', '2024-01-26 10:28:43');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `admins`
--
ALTER TABLE `admins`
  ADD PRIMARY KEY (`id`),
  ADD KEY `admins_user_id_foreign` (`user_id`);

--
-- Indeks untuk tabel `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `contests`
--
ALTER TABLE `contests`
  ADD PRIMARY KEY (`id`),
  ADD KEY `contests_admin_id_foreign` (`admin_id`);

--
-- Indeks untuk tabel `failed_jobs`
--
ALTER TABLE `failed_jobs`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `failed_jobs_uuid_unique` (`uuid`);

--
-- Indeks untuk tabel `languages`
--
ALTER TABLE `languages`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `migrations`
--
ALTER TABLE `migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `password_reset_tokens`
--
ALTER TABLE `password_reset_tokens`
  ADD PRIMARY KEY (`email`);

--
-- Indeks untuk tabel `personal_access_tokens`
--
ALTER TABLE `personal_access_tokens`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `personal_access_tokens_token_unique` (`token`),
  ADD KEY `personal_access_tokens_tokenable_type_tokenable_id_index` (`tokenable_type`,`tokenable_id`);

--
-- Indeks untuk tabel `problems`
--
ALTER TABLE `problems`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `problem_categories`
--
ALTER TABLE `problem_categories`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `submissions`
--
ALTER TABLE `submissions`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `test_cases`
--
ALTER TABLE `test_cases`
  ADD PRIMARY KEY (`id`),
  ADD KEY `test_cases_problem_id_foreign` (`problem_id`);

--
-- Indeks untuk tabel `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_email_unique` (`email`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `categories`
--
ALTER TABLE `categories`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT untuk tabel `contests`
--
ALTER TABLE `contests`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT untuk tabel `failed_jobs`
--
ALTER TABLE `failed_jobs`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `languages`
--
ALTER TABLE `languages`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT untuk tabel `migrations`
--
ALTER TABLE `migrations`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT untuk tabel `personal_access_tokens`
--
ALTER TABLE `personal_access_tokens`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `problems`
--
ALTER TABLE `problems`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT untuk tabel `problem_categories`
--
ALTER TABLE `problem_categories`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT untuk tabel `submissions`
--
ALTER TABLE `submissions`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT untuk tabel `test_cases`
--
ALTER TABLE `test_cases`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `admins`
--
ALTER TABLE `admins`
  ADD CONSTRAINT `admins_user_id_foreign` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Ketidakleluasaan untuk tabel `contests`
--
ALTER TABLE `contests`
  ADD CONSTRAINT `contests_admin_id_foreign` FOREIGN KEY (`admin_id`) REFERENCES `admins` (`id`);

--
-- Ketidakleluasaan untuk tabel `test_cases`
--
ALTER TABLE `test_cases`
  ADD CONSTRAINT `test_cases_problem_id_foreign` FOREIGN KEY (`problem_id`) REFERENCES `problems` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
