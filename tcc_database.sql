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
  `role` int(2) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `admins`
--

INSERT INTO `admins` (`id`, `user_id`, `role`, `created_at`, `updated_at`) VALUES
('1', '1', 2, '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
('2', '2', 2, '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
('3', '3', 1, '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
('4', '4', 1, '2024-01-26 10:28:43', '2024-01-26 10:28:43');

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
(4, 'Graph', 'graph', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(5, 'String', 'string', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(6, 'Backtracking', 'backtracking', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(7, 'Greedy ', 'greedy-', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(8, 'Tree', 'tree', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(9, 'Divide and Conquer', 'divide-and-conquer', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(10, 'Bit Manipulation', 'bit-manipulation', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(11, 'Geometry', 'geometry', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(12, 'Number Theory', 'number-theory', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(13, 'Searching', 'searching', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(14, 'Binary Search', 'binary-search', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(15, 'Hashing', 'hashing', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(16, 'Stack', 'stack', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(17, 'Queue', 'queue', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(18, 'Linked List', 'linked-list', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(19, 'Segment Tree', 'segment-tree', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(20, 'Fenwick Tree (Binary Indexed Tree)', 'fenwick-tree', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(21, 'Disjoint Set Union', 'disjoint-set-union', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(22, 'Trie', 'trie', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(23, 'Heap/Priority Queue', 'heap-priority-queue', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(24, 'Game Theory', 'game-theory', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(25, 'Network Flow', 'network-flow', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(26, 'String Algorithms', 'string-algorithms', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(27, 'Computational Geometry', 'computational-geometry', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(28, 'Persistent Data Structures', 'persistent-data-structures', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(29, 'Math', 'math', '2024-01-26 10:28:43', '2024-01-26 10:28:43');
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
(1, '1', 'Contest Pertama', 'contest-pertama', 'Deskripsi contest pertama.', '2024-01-26 10:00:00', '2024-02-02 10:28:43', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(2, '2', 'Contest Kedua', 'contest-kedua', 'Deskripsi contest kedua.', '2024-01-26 10:28:43', '2024-02-12 10:28:43', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(3, '1', 'Contest Ketiga', 'contest-ketiga', 'Deskripsi contest ketiga.', '2024-01-26 10:28:43', '2024-02-22 10:28:43', '2024-01-26 10:28:43', '2024-01-26 10:28:43');
--
-- Struktur dari tabel `local_contests`
--

CREATE TABLE `local_contests` (
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
-- Dumping data untuk tabel `local_contests`
--

INSERT INTO `local_contests` (`id`, `admin_id`, `title`, `slug`, `description`, `start_time`, `end_time`, `created_at`, `updated_at`) VALUES
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
(1, 'C++', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(2, 'C', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(3, 'Python', '2024-01-26 10:28:42', '2024-01-26 10:28:42');

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
(1, 'Hallo, kamu!', 'Linus ingin membuat sebuah robot yang dapat mengeluarkan sapaan terhadap nama yang dituliskan di programnya. Sebagai contoh, bila diinputkan “Andre” maka robotnya akan menyapa “Halo, Andre!”. Kamu ditunjuk sebagai programmer yang membuat sistem dasarnya. Bantulah Linus untuk membuat programnya.', 1, 16, 'Sebuah nama yang ingin disapa', 'Ikhwan', 'Sebuah baris yang mengeluarkan panggilan dari nama tersebut.', 'Halo, Ikhwan!', 'Nama yang diinputkan terdiri dari huruf-huruf alfabet dan panjang nama tidak melebihi 100 karakter.', 'Program harus membaca nama yang diinputkan, dan mengeluarkan panggilan sesuai format yang diminta.', '2024-02-12 08:00:00', '2024-02-12 08:00:00'),
(2, 'Penjumlahan Sederhana', 'Linus sedang belajar penjumlahan. Bantulah ia dengan membuat program yang menerima input dua bilangan bulat a dan b dan mengeluarkan hasil penjumlahannya.', 1, 16, 'Dua baris berisi satu bilangan bulat tiap baris.', '3\n5', 'Satu baris berisi hasil penjumlahan kedua bilangan.', '8', 'Bilangan yang diinputkan merupakan bilangan bulat dalam rentang -10^9 hingga 10^9.', 'Program harus membaca dua bilangan (3 dan 5), dan mengeluarkan hasil penjumlahannya (8).', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(3, 'Kalkulator', 'Linus sedang kewalahan dengan barang dagangannya. Ia kelihatan kesulitan dalam menghitung jumlah, harga dan lain sebagainya. Oleh karena itu, Linus meminta anda untuk membuat kalkulator sederhana yang dapat menyelesaikan operasi dua angka. Kalkulator tersebut dapat menyelesaikan +, -, x dan /.', 1, 16, 'a o b, dimana a dan b adalah sebuah bilangan bulat dan o adalah operasi +, -, x atau /', '3 + 2', 'Sebuah hasil dari operasi matematika tersebut. Bila operasi tersebut pembagian, maka keluarkan hasil dalam bentuk float/double dengan presisi 2 dibelakang koma.', '5', 'Bilangan yang diinputkan merupakan bilangan bulat dalam rentang -10^9 hingga 10^9. Operasi yang diizinkan adalah +, -, x, dan /.', 'Program harus membaca dua bilangan dan satu operator, dan mengeluarkan hasil operasi matematika sesuai dengan operator yang diberikan.', '2024-02-12 08:00:00', '2024-02-12 08:00:00'),
(4, 'Jalan-jalan ke kota', 'Misalkan Linus ingin pergi dari kota a ke kota b dengan menaiki pesawat. Dimana koordinat kota a adalah (x1, y1) dan kota b (x2, y2). Untuk menentukan jarak Manhattan yang harus ditempuh Linus, kita cukup menghitung selisih absolut dari koordinat x dan y, lalu menjumlahkannya.Rumus jarak Manhattan = |x1 - x2| + |y1 - y2|.', 1, 16, 'Sebuah baris berisi empat buah bilangan bulat x1, y1, x2, dan y2.', '-1 -1 1 1', 'Sebuah baris berisi sebuah bilangan bulat yang merupakan jarak Manhattan dari kedua titik tersebut.', '4', '-100.000 ≤ x1, y1, x2, y2 ≤ 100.000.', 'Jarak Manhattan dapat dihitung dengan menjumlahkan selisih absolut dari koordinat x dan y antara kedua titik.', '2024-02-12 08:00:00', '2024-02-12 08:00:00'),
(5, 'Mencari terbesar dan terkecil', 'Linus sedang belajar tentang statistika. Ia ingin mencari nilai terbesar dan terkecil dari sejumlah N bilangan. Bantulah Linus untuk menemukan nilai terbesar dan terkecil dari sejumlah N bilangan tersebut.', 1, 16, 'Sebuah baris berisi sebuah bilangan bulat N (1 ≤ N ≤ 100) yang menyatakan banyaknya bilangan. Baris berikutnya berisi N buah bilangan bulat yang dipisahkan oleh spasi.', '5\n3 2 3 4 5', 'Sebuah baris berisi dua bilangan bulat yang dipisahkan oleh spasi, yang menyatakan nilai terbesar dan terkecil dari N bilangan tersebut.', '5 2', '1 ≤ N ≤ 100\n-10^9 ≤ Bilangan ≤ 10^9\n', 'Program harus membaca jumlah bilangan dan daftar bilangan, kemudian mengeluarkan nilai terbesar dan terkecil dari daftar tersebut.', '2024-02-12 08:00:00', '2024-02-12 08:00:00'),
(6, 'Pola segitiga yang tidak biasa', 'Linus sedang belajar tentang pola segitiga. Ia menemukan sebuah pola segitiga yang tidak biasa. Anda ditantang untuk membuat program yang dapat menampilkan pola segitiga tersebut.', 1, 16, 'Sebuah bilangan bulat N', '6', 'Pola dengan ukuran N', '0\n12\n345\n6789\n01234\n567890', '1 ≤ N ≤ 100\n', 'Program harus membaca nilai N, kemudian menampilkan pola segitiga yang sesuai dengan aturan yang diberikan.', '2024-02-12 08:00:00', '2024-02-12 08:00:00'),
(7, 'Menghitung Faktorial', 'Buatlah program yang menghitung faktorial dari sebuah bilangan bulat positif.', 2, 32, 'Satu baris berisi satu bilangan bulat n (0 ≤ n ≤ 10).', '5', 'Satu baris berisi hasil faktorial dari n.', '120', 'Program harus dapat menangani nilai n dari 0 hingga 10.', 'Program harus menghitung 5! (5 faktorial), yang merupakan hasil perkalian 5 × 4 × 3 × 2 × 1 = 120.', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(8, 'Bilangan Prima', 'Buatlah program yang menentukan apakah suatu bilangan bulat positif adalah bilangan prima atau bukan.', 3, 64, 'Satu baris berisi satu bilangan bulat n (1 ≤ n ≤ 10^5).', '11', 'Satu baris berisi \"YA\" jika n adalah bilangan prima, dan \"BUKAN\" jika tidak.', 'YA', 'Program harus dapat menangani nilai n dari 1 hingga 10^5.', 'Program harus mengecek apakah bilangan 11 adalah bilangan prima atau tidak. Karena 11 hanya dapat dibagi oleh 1 dan 11, maka bilangan tersebut adalah bilangan prima.', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(9, 'Penyusunan Angka', 'Linus memiliki sebuah array berisi n bilangan bulat. Dia ingin menyusun ulang array tersebut sehingga bilangan-bilangan yang berdekatan memiliki perbedaan absolut maksimum. Bantulah Linus menemukan susunan yang memenuhi kondisi tersebut.', 4, 128, 'Baris pertama berisi satu bilangan bulat n (1 ≤ n ≤ 10^5), jumlah bilangan dalam array. Baris kedua berisi n bilangan bulat yang dipisahkan oleh spasi, masing-masing bernilai antara -10^9 hingga 10^9.', '6\n3 5 1 8 2 7', 'Satu baris berisi susunan ulang array yang memenuhi kondisi.', '7 2 8 1 5 3', 'Program harus dapat menangani nilai n dari 1 hingga 10^5.', 'Susunan ulang yang memenuhi kondisi adalah [7, 2, 8, 1, 5, 3]. Perbedaan absolut antara bilangan berdekatan adalah maksimum.', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(10, 'Deret Fibonacci Termodifikasi', 'Diberikan sebuah deret Fibonacci termodifikasi sebagai berikut: F(1) = a, F(2) = b, dan F(n) = F(n-1)^2 + F(n-2) untuk n > 2. Tulislah program untuk menghitung nilai F(n) untuk suatu n yang diberikan.', 5, 256, 'Satu baris berisi dua bilangan bulat a dan b (1 ≤ a, b ≤ 10^9) yang merupakan nilai awal deret Fibonacci termodifikasi. Baris kedua berisi satu bilangan bulat n (1 ≤ n ≤ 10^5).', '2 5\n4', 'Satu baris berisi nilai F(n) dari deret termodifikasi.', '181', 'Program harus dapat menangani nilai a, b, dan n hingga 10^9.', 'Deret termodifikasi untuk a = 2, b = 5 adalah: 2, 5, 29, 870, 756250. Nilai F(4) dari deret ini adalah 181.', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(11, 'Menentukan Bilangan Genap atau Ganjil', 'Buatlah program yang menerima satu bilangan bulat dan menentukan apakah bilangan tersebut genap atau ganjil.', 1, 16, 'Satu baris berisi satu bilangan bulat.', '7', 'Satu baris berisi \"GENAP\" jika bilangan genap dan \"GANJIL\" jika bilangan ganjil.', 'GANJIL', 'Bilangan yang diinputkan merupakan bilangan bulat dalam rentang -10^9 hingga 10^9.', 'Program harus menentukan apakah bilangan 7 adalah genap atau ganjil dan mengeluarkan hasil \"GANJIL\".', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(12, 'Menyusun String', 'Buatlah program yang menerima sebuah string dan mengembalikan string baru yang terdiri dari karakter-karakter unik yang disusun dalam urutan abjad.', 2, 32, 'Satu baris berisi sebuah string.', 'programming', 'Satu baris berisi string baru yang terdiri dari karakter-karakter unik dalam urutan abjad.', 'agimmnoprr', 'Panjang string tidak melebihi 1000 karakter.', 'Program harus menyusun karakter-karakter unik dari string \"programming\" dalam urutan abjad, sehingga menghasilkan string \"agimmnoprr\".', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(13, 'Balik Daftar', 'Linus sedang belajar tentang list. Ia ingin membalik sebuah list. Karena kesusahan, Linus meminta bantuan anda. Ia memberikan anda data list dalam beberapa baris. Tampilkan list tersebut dalam urutan terbalik', 1, 16, 'Beberapa baris, masing-masing berisi sebuah bilangan bulat.', '15\n6\n2021\n', 'Sejumlah baris sebanyak masukan, berisi bilangan-bilangan dalam urutan terbalik.', '2021\n6\n15\n', 'Terdapat antara 1 sampai dengan 100 baris.', 'Program harus membaca beberapa baris bilangan bulat, kemudian menampilkan bilangan-bilangan tersebut dalam urutan terbalik.', '2024-02-12 08:00:00', '2024-02-12 08:00:00'),
(14, 'MalaM', 'Linus sedang belajar tentang palindrom. Ia ingin mencari tahu apakah sebuah kata tersebut merupakan palindrom atau bukan. Bantulah Linus untuk menentukan apakah sebuah kata tersebut merupakan palindrom atau bukan.\n Palindrome adalah kata yang jika dibalik akan tetap sama. Contoh kata palindrom adalah, \'malam\', \'kodok\', dan \'radar\'.', 1, 16, 'Sebuah baris berisi sebuah kata yang terdiri dari huruf kecil (1 ≤ |kata| ≤ 100)', 'malam', 'Sebuah baris berisi \'YA\' jika kata tersebut merupakan palindrom, dan \'BUKAN\' jika kata tersebut bukan merupakan palindrom.', 'YA', '1 ≤ |kata| ≤ 100\n', 'Program harus membaca sebuah kata, kemudian menentukan apakah kata tersebut merupakan palindrom atau bukan.', '2024-02-12 08:00:00', '2024-02-12 08:00:00');

CREATE TABLE `local_problems` (
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
-- Dumping data untuk tabel `local_problems`
--

INSERT INTO `local_problems` (`id`, `title`, `description`, `time_limit`, `memory_limit`, `input_format`, `sample_input`, `output_format`, `sample_output`, `constraints`, `explanation`, `created_at`, `updated_at`) VALUES
(1, 'Penjumlahan Sederhana', 'Buatlah program yang menerima dua bilangan bulat dan mengeluarkan hasil penjumlahannya.', 1, 16, 'Dua baris berisi satu bilangan bulat tiap baris.', '3\n5', 'Satu baris berisi hasil penjumlahan kedua bilangan.', '8', 'Bilangan yang diinputkan merupakan bilangan bulat dalam rentang -10^9 hingga 10^9.', 'Program harus membaca dua bilangan (3 dan 5), dan mengeluarkan hasil penjumlahannya (8).', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(2, 'Menghitung Faktorial', 'Buatlah program yang menghitung faktorial dari sebuah bilangan bulat positif.', 2, 32, 'Satu baris berisi satu bilangan bulat n (0 ≤ n ≤ 10).', '5', 'Satu baris berisi hasil faktorial dari n.', '120', 'Program harus dapat menangani nilai n dari 0 hingga 10.', 'Program harus menghitung 5! (5 faktorial), yang merupakan hasil perkalian 5 × 4 × 3 × 2 × 1 = 120.', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(3, 'Bilangan Prima', 'Buatlah program yang menentukan apakah suatu bilangan bulat positif adalah bilangan prima atau bukan.', 3, 64, 'Satu baris berisi satu bilangan bulat n (1 ≤ n ≤ 10^5).', '11', 'Satu baris berisi \"YA\" jika n adalah bilangan prima, dan \"BUKAN\" jika tidak.', 'YA', 'Program harus dapat menangani nilai n dari 1 hingga 10^5.', 'Program harus mengecek apakah bilangan 11 adalah bilangan prima atau tidak. Karena 11 hanya dapat dibagi oleh 1 dan 11, maka bilangan tersebut adalah bilangan prima.', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(4, 'Penyusunan Angka', 'Linus memiliki sebuah array berisi n bilangan bulat. Dia ingin menyusun ulang array tersebut sehingga bilangan-bilangan yang berdekatan memiliki perbedaan absolut maksimum. Bantulah Linus menemukan susunan yang memenuhi kondisi tersebut.', 4, 128, 'Baris pertama berisi satu bilangan bulat n (1 ≤ n ≤ 10^5), jumlah bilangan dalam array. Baris kedua berisi n bilangan bulat yang dipisahkan oleh spasi, masing-masing bernilai antara -10^9 hingga 10^9.', '6\n3 5 1 8 2 7', 'Satu baris berisi susunan ulang array yang memenuhi kondisi.', '7 2 8 1 5 3', 'Program harus dapat menangani nilai n dari 1 hingga 10^5.', 'Susunan ulang yang memenuhi kondisi adalah [7, 2, 8, 1, 5, 3]. Perbedaan absolut antara bilangan berdekatan adalah maksimum.', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
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
(1, 1, 5), -- Soal 1 - String
(2, 2, 29), -- Soal 2 - Math
(3, 3, 29), -- Soal 3 - String
(4, 3, 5), -- Soal 3 - Arithmetic
(5, 4, 11), -- Soal 4 - Geometry
(6, 5, 1), -- Soal 5 - Array
(7, 6, 16), -- Soal 6 - Pattern
(8, 7, 32), -- Soal 7 - Recursion
(9, 8, 64), -- Soal 8 - Prime Numbers
(10, 9, 2), -- Soal 9 - Sorting
(11, 10, 3), -- Soal 10 - Dynamic Programming
(15, 11, 16), -- Soal 11 - Conditional Statements
(16, 12, 5), -- Soal 12 - String
(17, 13, 1), -- Soal 13 - Array
(18, 14, 5), -- Soal 14 - String
(19, 5, 29), -- Soal 14 - Conditional Statements
(20, 6, 16), -- Soal 14 - Pattern
(21, 9, 2), -- Soal 14 - Sorting
(22, 12, 5), -- Soal 14 - String
(23, 13, 1), -- Soal 14 - Array
(24, 14, 5); -- Soal 14 - String




-- Struktur dari tabel `local_problem_categories`
--

CREATE TABLE `local_problem_categories` (
  `id` int(11) NOT NULL,
  `problem_id` int(10) UNSIGNED NOT NULL,
  `category_id` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `local_problem_categories`
--
--

INSERT INTO `local_problem_categories` (`id`, `problem_id`, `category_id`) VALUES
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
  `status` varchar(3) NULL DEFAULT NULL,
  `time` float(5,3) NOT NULL,
  `memory` int(11) NOT NULL,
  `code` text NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `submissions`
--

INSERT INTO `submissions` (`id`, `user_id`, `problem_id`, `language_id`, `status`, `time`, `memory`, `code`, `created_at`, `updated_at`) VALUES
(1, '1', 1, 1, 'AC', 0.001, 256, '#include <iostream>\\nint main() { std::cout << \"Hello, World!\"; return 0; }', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(2, '2', 3, 2, 'WA', 0.15, 512, '#include <stdio.h>\\nint main() { printf(\"WA\\n\"); return 0; }', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(3, '1', 6, 3, 'CTE', 0.15, 128, 'def print_message():\\n    print(\"CE\")', '2024-01-26 10:28:43', '2024-01-26 10:28:43');


--
-- Struktur dari tabel `contest_submissions`
--

CREATE TABLE `contest_submissions` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `user_id` varchar(40) NOT NULL,
  `contest_id` bigint(20) UNSIGNED NOT NULL,
  `problem_id` bigint(20) UNSIGNED NOT NULL,
  `language_id` bigint(20) UNSIGNED NOT NULL,
  `status` varchar(3) NULL DEFAULT NULL,
  `time` float(5,3) NOT NULL,
  `memory` int(11) NOT NULL,
  `code` text NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `contest_submissions`
--

INSERT INTO `contest_submissions` (`id`, `user_id`, `contest_id`, `problem_id`, `language_id`, `status`, `time`, `memory`, `code`, `created_at`, `updated_at`) VALUES
(1,'1', 1 , 1, 1, 'WA', 0.001, 256, '#include <iostream>\\nint main() { std::cout << \"Hello, World!\"; return 0; }', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(2,'2', 1 , 4, 1, 'WA', 0.15, 512, '#include <stdio.h>\\nint main() { printf(\"WA\\n\"); return 0; }', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(3,'1', 1 , 1, 3, 'CTE', 0.15, 128, 'def print_message():\\n    print(\"CE\")', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(4,'1', 1 , 1, 1, 'WA', 0.001, 256, '#include <iostream>\\nint main() { std::cout << \"Hello, World!\"; return 0; }', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(5,'1', 1 , 1, 1, 'AC', 0.001, 256, '#include <iostream>\\nint main() { std::cout << \"Hello, World!\"; return 0; }', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(6,'1', 1 , 2, 1, 'AC', 0.001, 256, '#include <iostream>\\nint main() { std::cout << \"Hello, World!\"; return 0; }', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(7,'1', 1 , 3, 1, 'RTE', 0.001, 256, '#include <iostream>\\nint main() { std::cout << \"Hello, World!\"; return 0; }', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(8,'1', 1 , 4, 1, 'WA', 0.001, 256, '#include <iostream>\\nint main() { std::cout << \"Hello, World!\"; return 0; }', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(9,'2', 1 , 2, 1, 'RTE', 0.15, 512, '#include <stdio.h>\\nint main() { printf(\"WA\\n\"); return 0; }', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(10,'2', 1 , 3, 1, 'AC', 0.15, 512, '#include <stdio.h>\\nint main() { printf(\"WA\\n\"); return 0; }', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(11,'3', 1 , 1, 1, 'AC', 0.15, 512, '#include <stdio.h>\\nint main() { printf(\"WA\\n\"); return 0; }', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(12,'3', 1 , 2, 1, 'AC', 0.15, 512, '#include <stdio.h>\\nint main() { printf(\"WA\\n\"); return 0; }', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(13,'3', 1 , 3, 1, 'WA', 0.15, 512, '#include <stdio.h>\\nint main() { printf(\"WA\\n\"); return 0; }', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(14,'3', 1 , 3, 1, 'RTE', 0.15, 512, '#include <stdio.h>\\nint main() { printf(\"WA\\n\"); return 0; }', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(15,'3', 1 , 3, 1, 'CTE', 0.15, 512, '#include <stdio.h>\\nint main() { printf(\"WA\\n\"); return 0; }', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(16,'3', 1 , 4, 1, 'RTE', 0.15, 512, '#include <stdio.h>\\nint main() { printf(\"WA\\n\"); return 0; }', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(17,'3', 1 , 4, 1, 'CTE', 0.15, 512, '#include <stdio.h>\\nint main() { printf(\"WA\\n\"); return 0; }', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(18,'3', 1 , 4, 1, 'AC', 0.15, 512, '#include <stdio.h>\\nint main() { printf(\"WA\\n\"); return 0; }', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(19,'3', 1 , 4, 1, 'CTE', 0.15, 512, '#include <stdio.h>\\nint main() { printf(\"WA\\n\"); return 0; }', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(20,'4', 1 , 1, 1, 'AC', 0.001, 256, '#include <iostream>\\nint main() { std::cout << \"Hello, World!\"; return 0; }', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(21,'4', 1 , 2, 1, 'AC', 0.001, 256, '#include <iostream>\\nint main() { std::cout << \"Hello, World!\"; return 0; }', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(22,'4', 1 , 3, 1, 'AC', 0.001, 256, '#include <iostream>\\nint main() { std::cout << \"Hello, World!\"; return 0; }', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(23,'4', 1 , 4, 1, 'AC', 0.001, 256, '#include <iostream>\\nint main() { std::cout << \"Hello, World!\"; return 0; }', '2024-01-26 10:28:43', '2024-01-26 10:28:43');


CREATE TABLE `local_submissions` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `user_id` varchar(40) NOT NULL,
  `problem_id` bigint(20) UNSIGNED NOT NULL,
  `language_id` bigint(20) UNSIGNED NOT NULL,
  `status` varchar(3) NULL DEFAULT NULL,
  `time` float(5,3) NOT NULL,
  `memory` int(11) NOT NULL,
  `code` text NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `local_submissions`
--

INSERT INTO `local_submissions` (`id`, `user_id`, `problem_id`, `language_id`, `status`, `time`, `memory`, `code`, `created_at`, `updated_at`) VALUES
(1, '1', 1, 1, 'AC', 0.001, 256, '#include <iostream>\\nint main() { std::cout << \"Hello, World!\"; return 0; }', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(2, '2', 3, 2, 'WA', 0.15, 512, '#include <stdio.h>\\nint main() { printf(\"WA\\n\"); return 0; }', '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
(3, '1', 6, 3, 'CTE', 0.15, 128, 'def print_message():\\n    print(\"CE\")', '2024-01-26 10:28:43', '2024-01-26 10:28:43');

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
(1, 1, 'Andre', 'Halo, Andre!', '2024-02-12 08:00:00', '2024-02-12 08:00:00'),
(2, 1, 'Linus', 'Halo, Linus!', '2024-02-12 08:00:00', '2024-02-12 08:00:00'),
(3, 1, 'Ikhwan', 'Halo, Ikhwan!', '2024-02-12 08:00:00', '2024-02-12 08:00:00'),
(4, 2, '3\n5', '8', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(5, 2, '-10\n20', '10', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(6, 2, '1000000000\n-1000000000', '0', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(7, 3, '3 + 2', '5', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(8, 3, '10 - 7', '3', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(9, 3, '4 x 6', '24', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(10, 3, '15 / 3', '5.00', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(11, 4, '-1 -1 1 1', '4', '2024-02-12 08:00:00', '2024-02-12 08:00:00'),
(12, 4, '0 0 5 5', '10', '2024-02-12 08:00:00', '2024-02-12 08:00:00'),
(13, 4, '-10 -10 -5 -5', '10', '2024-02-12 08:00:00', '2024-02-12 08:00:00'),
(14, 5, '5\n3 2 3 4 5', '5 2', '2024-02-12 08:00:00', '2024-02-12 08:00:00'),
(15, 5, '3\n10 0 -5', '10 -5', '2024-02-12 08:00:00', '2024-02-12 08:00:00'),
(16, 5, '4\n-1000000000 -999999999 999999999 1000000000', '1000000000 -1000000000', '2024-02-12 08:00:00', '2024-02-12 08:00:00'),
(17, 6, '6', '0\n12\n345\n6789\n01234\n567890', '2024-02-12 08:00:00', '2024-02-12 08:00:00'),
(18, 6, '3', '0\n12\n345', '2024-02-12 08:00:00', '2024-02-12 08:00:00'),
(19, 6, '8', '0\n12\n345\n6789\n01234\n567890\n1234567\n89012345', '2024-02-12 08:00:00', '2024-02-12 08:00:00'),
(20, 7, '5', '120', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(21, 7, '0', '1', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(22, 7, '10', '3628800', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(23, 8, '11', 'YA', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(24, 8, '17', 'YA', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(25, 8, '25', 'BUKAN', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(26, 9, '6\n3 5 1 8 2 7', '7 2 8 1 5 3', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(27, 9, '4\n10 20 30 40', '40 10 30 20', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(28, 9, '5\n-5 -10 -3 -1 -8', '-8 -1 -10 -3 -5', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(29, 10, '2 5\n4', '181', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(30, 10, '1 1\n5', '8', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(31, 10, '3 4\n3', '29', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(32, 11, '7', 'GANJIL', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(33, 11, '10', 'GENAP', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(34, 11, '0', 'GENAP', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(35, 12, 'programming', 'agimmnoprr', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(36, 12, 'hello', 'ehlo', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(37, 12, 'openai', 'aeinop', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(38, 13, '15\n6\n2021\n', '2021\n6\n15\n', '2024-02-12 08:00:00', '2024-02-12 08:00:00'),
(39, 13, '10\n20\n30\n40\n', '40\n30\n20\n10\n', '2024-02-12 08:00:00', '2024-02-12 08:00:00'),
(40, 13, '5\n4\n3\n2\n1\n', '1\n2\n3\n4\n5\n', '2024-02-12 08:00:00', '2024-02-12 08:00:00'),
(41, 14, 'malam', 'YA', '2024-02-12 08:00:00', '2024-02-12 08:00:00'),
(42, 14, 'kodok', 'YA', '2024-02-12 08:00:00', '2024-02-12 08:00:00'),
(43, 14, 'radar', 'YA', '2024-02-12 08:00:00', '2024-02-12 08:00:00'),
(44, 14, 'pagi', 'BUKAN', '2024-02-12 08:00:00', '2024-02-12 08:00:00');


--
-- Struktur dari tabel `local_test_cases`
--

CREATE TABLE `local_test_cases` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `problem_id` bigint(20) UNSIGNED NOT NULL,
  `input` varchar(255) NOT NULL,
  `output` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `local_test_cases`
--

INSERT INTO `local_test_cases` (`id`, `problem_id`, `input`, `output`, `created_at`, `updated_at`) VALUES
(1, 1, '3\n5', '8', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(2, 2, '5', '120', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(3, 3, '11', 'YA', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(4, 4, '6\n3 5 1 8 2 7', '7 2 8 1 5 3', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(5, 5, '2 5\n4', '181', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(6, 6, '7', 'GANJIL', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(7, 7, 'programming', 'agimmnoprr', '2024-01-26 10:28:42', '2024-01-26 10:28:42');

-- --------------------------------------------------------

--
-- Struktur dari tabel `test_case_results`
--

CREATE TABLE `test_case_results` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `submission_id` bigint(20) UNSIGNED NOT NULL,
  `status` varchar(3) NULL DEFAULT NULL,
  `time` float(5,3) NULL DEFAULT NULL,
  `memory` int(11) NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `test_case_results`
--

INSERT INTO `test_case_results` (`id`, `submission_id`, `status`, `time`, `memory`, `created_at`) VALUES
(1, 1, 'AC', 0.10, 256, '2024-01-26 10:28:43'),
(2, 1, 'WA', 0.15, 512, '2024-01-26 10:28:43'),
(3, 1, 'CTE', 0.15, 128, '2024-01-26 10:28:43'),
(4, 2, 'AC', 0.15, 512, '2024-01-26 10:28:43'),
(5, 2, 'WA', 0.15, 512, '2024-01-26 10:28:43'),
(6, 3, 'CTE', 0.5, 128, '2024-01-26 10:28:43');
--
-- Struktur dari tabel `local_test_case_results`
--

CREATE TABLE `local_test_case_results` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `submission_id` bigint(20) UNSIGNED NOT NULL,
  `status` varchar(3) NULL DEFAULT NULL,
  `time` float(5,3) NULL DEFAULT NULL,
  `memory` int(11) NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `local_test_case_results`
--

INSERT INTO `local_test_case_results` (`id`, `submission_id`, `status`, `time`, `memory`, `created_at`) VALUES
(1, 1, 'AC', 0.10, 256, '2024-01-26 10:28:43'),
(2, 1, 'WA', 0.15, 512, '2024-01-26 10:28:43'),
(3, 1, 'CTE', 0.15, 128, '2024-01-26 10:28:43'),
(4, 2, 'AC', 0.15, 512, '2024-01-26 10:28:43'),
(5, 2, 'WA', 0.15, 512, '2024-01-26 10:28:43'),
(6, 3, 'CTE', 0.5, 128, '2024-01-26 10:28:43');


--
-- Struktur tabel `contest_participants`
--

CREATE TABLE `contest_participants` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `contest_id` bigint(20) UNSIGNED NOT NULL,
  `user_id` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `contest_participants` (`id`, `contest_id`,`user_id`) VALUES
(1, 1, '1'),
(2, 1, '2'),
(3, 2, '1'),
(4, 2, '3'),
(5, 1, '3'),
(6, 1, '4');

--
-- Struktur tabel `local_contest_participants`
--

CREATE TABLE `local_contest_participants` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `contest_id` bigint(20) UNSIGNED NOT NULL,
  `user_id` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `local_contest_participants` (`id`, `contest_id`,`user_id`) VALUES
(1, 1, '1'),
(2, 1, '2'),
(3, 2, '1'),
(4, 2, '3'),
(5, 1, '3'),
(6, 1, '4');

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
('3', 'Jane Smith', 'C54321', 120, 'jane.smith@example.com', NULL, NULL, '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
('4', 'Fajry', '2108107010059', 300, 'Fajry.smith@example.com', NULL, NULL, '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
('3ndoWdxlZAaANAHO5Ke5TTu6KZx2', 'alfnsnfff', '12345678', 0, 'asep@gmail.com', NULL, NULL, '2024-02-19 11:33:03', '2024-02-19 11:33:03'),
('jNziwj73vyUOunOsT87LvCeqlDr2', 'alfnsnff', '2108107010047', 200, 'alfnsnff@gmail.com', NULL, NULL, '2024-01-26 10:28:43', '2024-01-26 10:28:43'),
('8tq1NXekcPQ7PJWOBYhURBGvzvv1', '12312312312', '1231231231', 120, 'tester@gmail.com', NULL, NULL, '2024-02-19 11:35:01', '2024-02-19 11:35:01'),
('hKNPEPnnMhXq9oAdiuIYcnO3ZRm1', 'test1', '123456', 120, 'alfan.s.nufi@gmail.com', NULL, NULL, '2024-02-19 11:16:39', '2024-02-19 11:16:39'),
('iUzNaWaDYTNYJcPIsVrWKnuYIZD3', 'riparuk', '2108107010073', 120, 'faruqirifa@gmail.com', NULL, NULL, '2024-02-18 22:20:40', '2024-02-18 22:20:40'),
('MXvSL2vzZHSyA1UeFEy8Qd5mlqp2', 'alfnsnff', '2108107010047', 120, 'alfan.nufi@gmail.com', NULL, NULL, '2024-02-19 11:43:45', '2024-02-19 11:43:45'),
('nqtXNLbE5KTp4ttQ090VWJWrpK43', 'Papazy', 'fajryjobs@gmail.com', 120, 'fajry@mhs.usk.ac.id', NULL, NULL, '2024-02-18 21:55:45', '2024-02-18 21:55:45'),
('OeK8F2zbetdA8V3kBIGJlBvMPNf2', 'Papazy', '2108107010059', 120, 'fajryjobs@gmail.com', NULL, NULL, '2024-02-18 22:42:06', '2024-02-18 22:42:06'),
('yRnMjVEdgcTDz0zPuttWzfGMpBI2', 'wwer', '123', 120, 'jenni.blackpink@gmail.com', NULL, NULL, '2024-02-19 11:17:41', '2024-02-19 11:17:41');

--
-- Struktur dari tabel `contest_problems`
--

CREATE TABLE `contest_problems` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `contest_id` bigint(20) UNSIGNED NOT NULL,
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
-- Struktur dari tabel `contest problem_categories`
--

CREATE TABLE `contest_problem_categories` (
  `id` int(11) NOT NULL,
  `problem_id` int(10) UNSIGNED NOT NULL,
  `category_id` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `contest problem_categories`
--

INSERT INTO `contest_problem_categories` (`id`, `problem_id`, `category_id`) VALUES
(1, 1, 5), -- Soal 1 - String
(2, 2, 29), -- Soal 2 - Math
(3, 3, 29); -- Soal 3 - String


--
-- Dumping data untuk tabel `contest_problems`
--

INSERT INTO `contest_problems` (`id`, `contest_id`, `title`,`description`, `time_limit`, `memory_limit`, `input_format`, `sample_input`, `output_format`, `sample_output`, `constraints`, `explanation`, `created_at`, `updated_at`) VALUES
(1,1, 'Hallo, kamu!', 'Linus ingin membuat sebuah robot yang dapat mengeluarkan sapaan terhadap nama yang dituliskan di programnya. Sebagai contoh, bila diinputkan “Andre” maka robotnya akan menyapa “Halo, Andre!”. Kamu ditunjuk sebagai programmer yang membuat sistem dasarnya. Bantulah Linus untuk membuat programnya.', 1, 16, 'Sebuah nama yang ingin disapa', 'Ikhwan', 'Sebuah baris yang mengeluarkan panggilan dari nama tersebut.', 'Halo, Ikhwan!', 'Nama yang diinputkan terdiri dari huruf-huruf alfabet dan panjang nama tidak melebihi 100 karakter.', 'Program harus membaca nama yang diinputkan, dan mengeluarkan panggilan sesuai format yang diminta.', '2024-02-12 08:00:00', '2024-02-12 08:00:00'),
(2,1, 'Penjumlahan Sederhana', 'Linus sedang belajar penjumlahan. Bantulah ia dengan membuat program yang menerima input dua bilangan bulat a dan b dan mengeluarkan hasil penjumlahannya.', 1, 16, 'Dua baris berisi satu bilangan bulat tiap baris.', '3\n5', 'Satu baris berisi hasil penjumlahan kedua bilangan.', '8', 'Bilangan yang diinputkan merupakan bilangan bulat dalam rentang -10^9 hingga 10^9.', 'Program harus membaca dua bilangan (3 dan 5), dan mengeluarkan hasil penjumlahannya (8).', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(3,1, 'Kalkulator', 'Linus sedang kewalahan dengan barang dagangannya. Ia kelihatan kesulitan dalam menghitung jumlah, harga dan lain sebagainya. Oleh karena itu, Linus meminta anda untuk membuat kalkulator sederhana yang dapat menyelesaikan operasi dua angka. Kalkulator tersebut dapat menyelesaikan +, -, x dan /.', 1, 16, 'a o b, dimana a dan b adalah sebuah bilangan bulat dan o adalah operasi +, -, x atau /', '3 + 2', 'Sebuah hasil dari operasi matematika tersebut. Bila operasi tersebut pembagian, maka keluarkan hasil dalam bentuk float/double dengan presisi 2 dibelakang koma.', '5', 'Bilangan yang diinputkan merupakan bilangan bulat dalam rentang -10^9 hingga 10^9. Operasi yang diizinkan adalah +, -, x, dan /.', 'Program harus membaca dua bilangan dan satu operator, dan mengeluarkan hasil operasi matematika sesuai dengan operator yang diberikan.', '2024-02-12 08:00:00', '2024-02-12 08:00:00'),
(4,1, 'Hallo, kamu!', 'Linus ingin membuat sebuah robot yang dapat mengeluarkan sapaan terhadap nama yang dituliskan di programnya. Sebagai contoh, bila diinputkan “Andre” maka robotnya akan menyapa “Halo, Andre!”. Kamu ditunjuk sebagai programmer yang membuat sistem dasarnya. Bantulah Linus untuk membuat programnya.', 1, 16, 'Sebuah nama yang ingin disapa', 'Ikhwan', 'Sebuah baris yang mengeluarkan panggilan dari nama tersebut.', 'Halo, Ikhwan!', 'Nama yang diinputkan terdiri dari huruf-huruf alfabet dan panjang nama tidak melebihi 100 karakter.', 'Program harus membaca nama yang diinputkan, dan mengeluarkan panggilan sesuai format yang diminta.', '2024-02-12 08:00:00', '2024-02-12 08:00:00'),
(5,2, 'Penjumlahan Sederhana', 'Linus sedang belajar penjumlahan. Bantulah ia dengan membuat program yang menerima input dua bilangan bulat a dan b dan mengeluarkan hasil penjumlahannya.', 1, 16, 'Dua baris berisi satu bilangan bulat tiap baris.', '3\n5', 'Satu baris berisi hasil penjumlahan kedua bilangan.', '8', 'Bilangan yang diinputkan merupakan bilangan bulat dalam rentang -10^9 hingga 10^9.', 'Program harus membaca dua bilangan (3 dan 5), dan mengeluarkan hasil penjumlahannya (8).', '2024-01-26 10:28:42', '2024-01-26 10:28:42'),
(6,2, 'Kalkulator', 'Linus sedang kewalahan dengan barang dagangannya. Ia kelihatan kesulitan dalam menghitung jumlah, harga dan lain sebagainya. Oleh karena itu, Linus meminta anda untuk membuat kalkulator sederhana yang dapat menyelesaikan operasi dua angka. Kalkulator tersebut dapat menyelesaikan +, -, x dan /.', 1, 16, 'a o b, dimana a dan b adalah sebuah bilangan bulat dan o adalah operasi +, -, x atau /', '3 + 2', 'Sebuah hasil dari operasi matematika tersebut. Bila operasi tersebut pembagian, maka keluarkan hasil dalam bentuk float/double dengan presisi 2 dibelakang koma.', '5', 'Bilangan yang diinputkan merupakan bilangan bulat dalam rentang -10^9 hingga 10^9. Operasi yang diizinkan adalah +, -, x, dan /.', 'Program harus membaca dua bilangan dan satu operator, dan mengeluarkan hasil operasi matematika sesuai dengan operator yang diberikan.', '2024-02-12 08:00:00', '2024-02-12 08:00:00');


--
-- Strultur dari tabel `local_contest_problems`
--

CREATE TABLE `local_contest_problems` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `contest_id` bigint(20) UNSIGNED NOT NULL,
  `problem_id` bigint(20) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `local_contest_problems`
--

INSERT INTO `local_contest_problems` (`id`, `contest_id`, `problem_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 2, 4),
(5, 2, 5),
(6, 2, 6),
(7, 2, 7);


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
-- Indeks untuk tabel `local_contests`
--
ALTER TABLE `local_contests`
  ADD PRIMARY KEY (`id`),
  ADD KEY `local_contests_admin_id_foreign` (`admin_id`);

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
-- Indeks untuk tabel `local_problems`
--
ALTER TABLE `local_problems`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `problem_categories`
--
ALTER TABLE `problem_categories`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `contest problem_categories`
--
ALTER TABLE `contest_problem_categories`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `submissions`
--
ALTER TABLE `submissions`
  ADD PRIMARY KEY (`id`);
--
-- Indeks untuk tabel `local_submissions`
--
ALTER TABLE `local_submissions`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `contest_submissions`
--
ALTER TABLE `contest_submissions`
  ADD PRIMARY KEY (`id`);
--
-- Indeks untuk tabel `contest_participants`
--
ALTER TABLE `contest_participants`
  ADD PRIMARY KEY (`id`);
--
-- Indeks untuk tabel `local_contest_participants`
--
ALTER TABLE `local_contest_participants`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `test_cases`
--
ALTER TABLE `test_cases`
  ADD PRIMARY KEY (`id`),
  ADD KEY `test_cases_problem_id_foreign` (`problem_id`);


-- Indeks untuk tabel `test_case_results`
--
ALTER TABLE `test_case_results`
  ADD PRIMARY KEY (`id`),
  ADD KEY `test_cases__results_submission_id_foreign` (`submission_id`);
--

-- Indeks untuk tabel `local_test_case_results`
--
ALTER TABLE `local_test_case_results`
  ADD PRIMARY KEY (`id`),
  ADD KEY `local_test_cases__results_submission_id_foreign` (`submission_id`);
--
-- Indeks untuk tabel `local_test_cases`
--
ALTER TABLE `local_test_cases`
  ADD PRIMARY KEY (`id`),
  ADD KEY `local_test_cases_problem_id_foreign` (`problem_id`);

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
-- AUTO_INCREMENT untuk tabel `local_contests`
--
ALTER TABLE `local_contests`
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
-- AUTO_INCREMENT untuk tabel `local_problems`
--
ALTER TABLE `local_problems`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT untuk tabel `problem_categories`
--
ALTER TABLE `problem_categories`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT untuk tabel `contest_problem_categories`
--
ALTER TABLE `contest_problem_categories`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT untuk tabel `submissions`
--
ALTER TABLE `submissions`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
  
--
-- AUTO_INCREMENT untuk tabel `local_submissions`
--
ALTER TABLE `local_submissions`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
  
--
-- AUTO_INCREMENT untuk tabel `contest_submissions`
--
ALTER TABLE `contest_submissions`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
  
--
-- AUTO_INCREMENT untuk tabel `contest_participants`
--
ALTER TABLE `contest_participants`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
  
--
-- AUTO_INCREMENT untuk tabel `local_contest_participants`
--
ALTER TABLE `local_contest_participants`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT untuk tabel `test_cases`
--
ALTER TABLE `test_cases`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT untuk tabel `test_case_results`
--
ALTER TABLE `test_case_results`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT untuk tabel `local_test_cases`
--
ALTER TABLE `local_test_cases`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

-- AUTO_INCREMENT untuk tabel `local_test_case_results`
--
ALTER TABLE `local_test_case_results`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
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
-- Ketidakleluasaan untuk tabel `local_contests`
--
ALTER TABLE `local_contests`
  ADD CONSTRAINT `local_contests_admin_id_foreign` FOREIGN KEY (`admin_id`) REFERENCES `admins` (`id`);

--
-- Ketidakleluasaan untuk tabel `test_cases`
--
ALTER TABLE `test_cases`
  ADD CONSTRAINT `test_cases_problem_id_foreign` FOREIGN KEY (`problem_id`) REFERENCES `problems` (`id`);
COMMIT;
--
-- Ketidakleluasaan untuk tabel `local_test_cases`
--
ALTER TABLE `local_test_cases`
  ADD CONSTRAINT `local_test_cases_problem_id_foreign` FOREIGN KEY (`problem_id`) REFERENCES `problems` (`id`);
COMMIT;

--
-- Ketidakleluasaan untuk tabel `contest_submissions`
--
ALTER TABLE `contest_submissions`
  ADD CONSTRAINT `contest_submissions_contest_id_foreign` FOREIGN KEY (`contest_id`) REFERENCES `contests` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
