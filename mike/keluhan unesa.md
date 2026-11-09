1. Masalah Alokasi Dosen Pembimbing (DPL Magang / Dospem Skripsi)
  Ketimpangan Ekstrem Beban Dosen (Popularity Bias)
    Detail Lapangan: Dosen yang dikenal santai, ramah, dan cepat merespons chat di WhatsApp menjadi rebutan utama hingga kuota habis dalam hitungan 30–60 detik. Sebaliknya, dosen yang dinilai perfeksionis, jarang dikenal angkatan bawah, atau berstatus struktural kuotanya sering tersisa banyak.
    Dampak: Terjadi polarisasi tajam. Beberapa dosen membimbing belasan mahasiswa sekaligus hingga overloaded, sementara dosen lain hanya membimbing segelintir mahasiswa.
    Kebutuhan Solusi: Batasan kuota ketat (hard ceiling) yang terdistribusi secara otomatis dan transparan.
  Sistem "Siapa Cepat Dia Dapat" yang Diskriminatif
    Detail Lapangan: Pemilihan dosen lewat Google Form atau portal konvensional menempatkan mahasiswa dari daerah dengan sinyal internet lambat atau perangkat berspesifikasi rendah pada posisi yang sangat dirugikan.
    Dampak: Mahasiswa yang kalah kecepatan jaringan terpaksa masuk ke kuota dosen sisa yang sama sekali tidak mereka minati.
    Kebutuhan Solusi: Sistem pemilihan berbasis input preferensi berjangka (misal: dibuka selama 48 jam) yang diselesaikan menggunakan algoritma Stable Matching (Gale-Shapley), bukan adu cepat klik (click-speed race).
  Ketidakcocokan Topik dengan Kepakaran Dosen (Topic Mismatch)
   Detail Lapangan: Mahasiswa jurusan teknologi/rekayasa perangkat lunak yang magang di industri teknologi (mengerjakan full-stack dev, cloud microservices, atau data pipelines) sering mendapatkan DPL yang kepakarannya murni di bidang administrasi, manajemen pendidikan, atau teori dasar.
    Dampak: Diskusi bimbingan 20 SKS kehilangan nilai esensial. Dosen tidak dapat memberikan masukan teknis mendalam terhadap arsitektur sistem yang dibangun mahasiswa di tempat magang, dan proses bimbingan terdegradasi menjadi sekadar formalitas tanda tangan administratif.
   * Kebutuhan Solusi: Algoritma pencocokan semantik (Semantic Matching Engine) yang membandingkan kata kunci proposal/deskripsi pekerjaan magang mahasiswa dengan rekam jejak riset dan publikasi dosen.
2. Masalah Infrastruktur & Kerapuhan Sistem Portal Kampus
 Server Crash & Bad Gateway Saat Jam Puncak (High-Concurrency Failure)
   Detail Lapangan: Setiap pembukaan pendaftaran logistik akademik serentak (KRS, DPL Magang, seminar), portal kampus sering mengalami HTTP 504 Gateway Timeout atau Internal Server Error akibat ribuan mahasiswa mengakses secara bersamaan.
    Dampak: Mahasiswa panik, proses pendaftaran terputus di tengah jalan, dan mahasiswa harus terus-menerus menekan tombol refresh.
    Kebutuhan Solusi: Arsitektur backend berbasis antrean (queue engine) dengan Redis/In-Memory Cache untuk menahan lonjakan traffic jutaan request tanpa menumbangkan database utama.
  Terjadinya Double-Booking dan Race Condition
   Detail Lapangan: Di layar mahasiswa A dan B kuota dosen masih tertulis sisa "1", lalu keduanya menekan tombol submit pada milidetik yang sama. Karena tidak ada mekanisme penguncian transaksi, data masuk ganda dan kuota melebihi batas atau salah satu data mahasiswa mengalami korupsi.
   * Dampak: Pembatalan sepihak oleh admin jurusan di kemudian hari, memicu kebingungan dan komplain mahasiswa.
   * Kebutuhan Solusi: Implementasi distributed locking (seperti Redis Lock) atau pessimistic locking pada basis data transaksional pendaftaran.
 * F5 Bombardment Akibat Ketiadaan Status Real-time
   * Detail Lapangan: Mahasiswa tidak tahu apakah sisa slot dosen masih ada atau sudah penuh secara langsung tanpa memuat ulang (reload) halaman berulang kali.
   * Dampak: Ribuan mahasiswa melakukan spam refresh per detik, yang mempercepat kelebihan beban server (self-inflicted DDoS).
   * Kebutuhan Solusi: Indikator kuota real-time berbasis WebSocket, sehingga angka kuota berkurang secara otomatis di layar semua mahasiswa tanpa perlu me-refresh halaman.
3. Masalah Komunikasi, Validasi Berkas, & Birokrasi
 * Bottleneck Pengesahan Logbook dan Lembar Persetujuan
   * Detail Lapangan: Mahasiswa magang atau tugas akhir harus mengejar dosen di kampus (sering kali harus berpindah antar-kampus seperti Ketintang dan Lidah Wetan) hanya demi meminta paraf mingguan atau tanda tangan persetujuan seminar.
   * Dampak: Dosen yang sedang bertugas luar kota, dinas rapat, atau mengajar jadwal padat membuat berkas mahasiswa tertumpuk berhari-hari hingga berminggu-minggu, memperlambat proses kelulusan.
   * Kebutuhan Solusi: Sistem validasi instan one-click approval terintegrasi bot (misal: notifikasi ringkas langsung ke akun Telegram/WhatsApp resmi dosen yang memiliki tombol [Setujui] / [Beri Catatan]).
 * Kecemasan Etika Berkomunikasi (Messaging Anxiety)
   * Detail Lapangan: Mahasiswa sering merasa serba salah saat menghubungi dosen lewat WhatsApp—apakah formatnya sudah cukup sopan, kapan waktu yang tepat, dan takut jika pesan dianggap lancang. Ketika pesan hanya dibaca tanpa dibalas, mahasiswa ragu melakukan follow-up.
   * Dampak: Komunikasi tersendat, logbook magang terlambat disetujui, dan mahasiswa mengalami stres psikologis.
   * Kebutuhan Solusi: Sistem tiket pesan dan penentuan slot konsultasi terjadwal langsung di dalam platform akademik, sehingga interaksi memiliki template terstandarisasi dan tidak menginvasi ruang privat WhatsApp dosen.
 * Disparitas Standar dan Ketidakjelasan Rubrik Evaluasi
   * Detail Lapangan: Satu dosen meloloskan logbook magang hanya dengan laporan satu paragraf, sementara dosen lain menuntut lampiran bukti log commit kode, foto kerja harian, dan revisi berulang kali tanpa ada indikator mutu resmi di portal.
   * Dampak: Ketidakadilan penilaian antarmahasiswa satu angkatan dan kebingungan terhadap ekspektasi luaran tugas akhir/magang.
   * Kebutuhan Solusi: Rubrik evaluasi logbook dan kemajuan tugas akhir yang terstruktur di dashboard dosen dan mahasiswa dengan parameter kriteria yang jelas.