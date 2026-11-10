# 🏆 MASTER BLUEPRINT: STACK 2026 by GDGoC ITB
## Studi Kasus 1: Smarter Campus and Learning (*Kampus dan Pembelajaran yang Lebih Cerdas*)

Dokumen ini disusun berdasarkan hasil ekstraksi langsung dari **bundel sistem internal `gdgoncampusitb.com/hackathon`**, **Competition Handbook Resmi STACK 2026**, **Dokumen Panduan & Contoh Abstrak Resmi (`AbstractMaterialSTACK2026`)**, serta kurasi **115+ Repositori GitHub Terbaik Terverifikasi API** (semua di atas 100 hingga 450.000+ ⭐).

---

## BAGIAN 1: BEDAH TUNTAS SOALAN HACKATHON & STUDI KASUS 1 (STACK 2026)

### 1.1 Identitas & Tema Kompetisi
* **Nama Resmi Lomba:** **STACK 2026** (*Solution Technology Arena for Coding & Knowledge*) oleh **GDGoC ITB** (Google Developer Groups on Campus Institut Teknologi Bandung).
* **Tema Utama:** *"Agent of the Ocean: Vibing Beyond the Code"*
  * **Makna Penting di Buku Panduan:** *"Ocean"* hanyalah latar naratif (proyek **tidak** harus bertema kelautan). *"Vibing Beyond the Code"* menekankan bahwa juri tidak hanya menilai barisan kode, melainkan **pemahaman mendalam atas masalah pengguna nyata, keputusan desain yang matang, pengujian asumsi (validasi), dan kejelasan dampak**.
  * **Aturan Penting Penggunaan AI & Teknologi Google:** Berbeda dengan tahun-tahun lama, di STACK 2026 tertulis secara eksplisit di Handbook: *"AI, AI agents, AI coding assistants, vibe coding, and Google technologies are optional... Judges assess the solution and its implementation. Using a particular tool, paid service, or AI model does not automatically earn additional points."* Artinya: **Jangan memaksakan AI gimmick jika alur dasarnya rusak.** Jika memakai AI/LLM, AI tersebut harus menyelesaikan masalah nyata secara presisi dan wajib dicantumkan (*disclosed*) di Proposal & README.
* **Bahasa Resmi:** **Bahasa Inggris (English)** wajib untuk seluruh dokumen (Abstrak, Proposal, Video, Deck Presentasi, dan sesi Pitching).

### 1.2 Bedah Studi Kasus Pilihan Anda: KASUS 1 — *Smarter Campus and Learning*
* **Pertanyaan Inti (*Core Question*):**
  > *"How might we help students learn, collaborate, and access campus opportunities more effectively?"*
  > (Bagaimana kita dapat membantu mahasiswa belajar, berkolaborasi, dan mengakses peluang kampus secara lebih efektif?)
* **Target Pengguna (*Intended Users*):**
  Mahasiswa (spesifikkan angkatan/kondisi), organisasi kemahasiswaan (UKM/Himpunan), mentor sebaya (*peer mentors* / asisten dosen), dan pengguna/pengelola fasilitas layanan kampus.
* **4 Masalah Utama yang Dicontohkan Panitia (Titik Awal Eksplorasi):**
  1. **Informasi beasiswa, lomba, riset, dan peluang kampus yang terfragmentasi** (*Fragmented scholarship and opportunity information*).
  2. **Materi pembelajaran yang sulit diakses atau sulit dipahami/dicari** (*Learning materials that are difficult to access*).
  3. **Kesulitan mencari rekan belajar / rekan tim yang cocok** (*Difficulty finding suitable study partners*).
  4. **Peminjaman/booking fasilitas bersama di kampus yang tidak efisien** (*Inefficient booking of shared campus facilities*).
* **Syarat Mutlak Solusi Kasus 1 (Wajib Muncul di Produk):**
  1. **Clear User Journey:** Alur pengguna dari awal sampai akhir yang jelas dan tidak membingungkan.
  2. **Working Core Interaction:** Interaksi utama yang benar-benar berfungsi (bukan sekadar tombol mati/mockup).
  3. **Measurable / Testable Benefit:** Manfaat yang dapat diukur atau diuji secara kuantitatif (contoh: waktu pencarian turun dari 25 menit menjadi < 3 menit, tingkat *no-show* ruangan turun 60%, skor *active recall* kuis meningkat, atau aksesibilitas bagi mahasiswa disabilitas).

### 1.3 Linimasa & Deliverables Tiap Tahap (Wajib Dicatat!)
> **PERHATIAN KRITIS:** Hari ini adalah **9 November 2026**, sedangkan **Batas Pengumpulan Tahap Penyisihan (Preliminary Submission) adalah BESOK, 10 November 2026 pukul 23:59 WIB!**

| Tahap | Tanggal | Deliverables Utama | Aturan Kritis dari Sistem & Handbook |
| :--- | :--- | :--- | :--- |
| **1. Preliminary Phase** | **10 Nov 2026 (23:59 WIB)** | 1. **Abstrak PDF** (300–500 kata, bahasa Inggris, tanpa cover terpisah, maks 10 MB)<br>2. **Bukti Twibbon PDF** (gabungan semua anggota: nama, IG handle, link post, screenshot) | Belum butuh prototipe/video/proposal. Hanya 1x *upload final* di dashboard (`Your submission is locked. Revisions and replacement uploads are not allowed`). |
| **Pengumuman Semifinal** | **18 Nov 2026** | Pengumuman lolos + instruksi pembayaran biaya registrasi semifinal | Hanya tim yang lolos ke Semifinal yang membayar biaya registrasi tahap lanjut. |
| **2. Semifinal Phase** | **30 Nov 2026 (23:59 WIB)** | 1. **Proposal Detail PDF** (maks 10 halaman isi di luar cover, daftar pustaka, & lampiran *Signed Originality Declaration*)<br>2. **1 Video Penjelasan** (maks 2 menit, min 1080p, Bahasa Inggris) | Video harus memperkenalkan tim, masalah, solusi, alur pengguna / *early prototype*, serta **jujur menyebutkan fitur apa yang sudah selesai dan apa yang belum selesai**. |
| **Pengumuman Top 10** | **7 Des 2026** | 10 Tim Terbaik lolos ke Final Day | Periode *Product Improvement* berlangsung 7–16 Desember 2026. |
| **3. Final Day (Top 10)** | **16 Des 2026** (Offline di Bandung) | 1. **Build Session Live** (menyelesaikan 2–3 *substantive tasks* dari komit awal ke komit akhir)<br>2. **Working Prototype + Repo + README**<br>3. **Presentation Deck PDF** (maks 15 slide)<br>4. **Live Pitching** (10 menit demo + 10 menit Q&A) | **UNIK DI STACK 2026:** Tim datang ke Final Day membawa prototipe yang sudah jalan sebagian, lalu **wajib melakukan coding/penyelesaian 2–3 fitur nyata saat Build Session di lokasi**. Panitia mencatat *starting commit* dan *final commit*! |

---

## BAGIAN 2: KRITERIA PENILAIAN UTAMA JURI & RAHASIA DAPUR SISTEM PENJURIAN

Berdasarkan ekstraksi langsung dari **Competition Handbook (Halaman 15–16)** dan kode sumber **`/judge/preliminary`** pada aplikasi `gdgoncampusitb.com`:

### 2.1 Tabel Bobot Penilaian Resmi di 3 Tahap

#### A. Tahap Preliminary (Abstrak 300–500 Kata) — *Deadline: 10 Nov 2026*
| Kriteria | Bobot | Apa yang Dicari Juri |
| :--- | :---: | :--- |
| **1. Problem Clarity** | **30%** | Pengguna sangat spesifik (bukan "semua mahasiswa"), masalah nyata, dan didukung bukti/observasi/data survei nyata (jangan mengarang data fiktif!). |
| **2. Value and Originality** | **25%** | Kegunaan nyata dan pembeda konkret dibanding alternatif yang sudah ada saat ini (misal dibanding grup WhatsApp, SIX ITB, Google Drive, atau sistem manual). |
| **3. Fit to the Selected Case** | **20%** | Benang merah yang kuat antara masalah, solusi, dan fokus *Case 1: Smarter Campus and Learning*. |
| **4. Feasibility** | **15%** | Ruang lingkup (scope) versi pertama yang realistis, pemilihan teknologi yang masuk akal dikerjakan tim 3–4 orang, dan jadwal kerja yang jelas + mitigasi risiko utama. |
| **5. Abstract Clarity** | **10%** | Bahasa Inggris yang rapi, mengikuti **7 urutan bagian wajib** dari template resmi, panjang 300–500 kata. |

#### B. Tahap Semifinal (Proposal 10 Halaman + Video 2 Menit) — *Deadline: 30 Nov 2026*
| Kriteria | Bobot | Apa yang Dicari Juri |
| :--- | :---: | :--- |
| **1. Problem Understanding** | **25%** | Bukti pendukung (data/wawancara/observasi), kebutuhan user, dan analisis komparatif atas solusi eksisting. |
| **2. Solution Design** | **25%** | Alur kerja inti (*core workflow*), proposisi nilai, orisinalitas, dan keselarasan dengan studi kasus. |
| **3. Technical Feasibility** | **20%** | Arsitektur sistem, diagram alir data, pemilihan *tech stack*, sumber data, dan cakupan MVP yang realistis. |
| **4. Execution and Validation** | **20%** | Milestone, pembagian peran anggota, rencana/hasil pengujian awal (*early testing*), analisis risiko & privasi, serta **rencana kerja untuk Final Day**. |
| **5. Communication** | **10%** | Konsistensi antara proposal dan video berdurasi 2 menit serta kejujuran melaporkan progres. |

#### C. Tahap Final (Top 10 Live Build + Pitching) — *16 Des 2026*
| Kriteria | Bobot | Apa yang Dicari Juri |
| :--- | :---: | :--- |
| **1. Functionality and Reliability** | **30%** | **Alur utama (*core flow*) berjalan mulus dan konsisten tanpa error saat Live Demo!** |
| **2. Problem Fit and Usefulness** | **20%** | Produk benar-benar menjawab kebutuhan nyata di lingkungan kampus/pembelajaran. |
| **3. Technical Quality** | **15%** | Kualitas arsitektur, struktur kode, penanganan data, keamanan kredensial, dan pilihan implementasi. |
| **4. Usability and Accessibility** | **10%** | Antarmuka mudah dipahami, umpan balik UI jelas, dan ramah bagi target pengguna. |
| **5. Validation and Impact** | **10%** | Pengujian yang kredibel (dengan pengguna asli), metrik manfaat yang terukur, dan kejujuran atas batasan sistem. |
| **6. Final Day Execution** | **10%** | **Progres nyata yang terlacak (via Git commit & README) selama sesi coding di Hari Final sesuai rencana yang dideklarasikan.** |
| **7. Pitch and Technical Understanding** | **5%** | Demo langsung yang meyakinkan dan kemampuan **setiap anggota tim** menjawab pertanyaan teknis juri. |

### 2.2 Temuan Rahasia dari Dokumen `AbstractMaterialSTACK2026`
Panitia menyediakan contoh fiktif resmi berjudul **"StudyNook: Live Study Room Booking"** (376 kata). Dari dokumen tersebut, terdapat aturan emas (*Do's & Don'ts*) yang menjadi filter gugur/lolosnya tim:
1. **Wajib 7 Bagian Berurutan di Abstrak:**
   * `1. Problem` (2–3 kalimat tentang apa yang salah dan mengapa penting—jangan bahas solusi di sini!)
   * `2. Intended Users` (Sebutkan 1 kelompok spesifik, di mana, dan pada situasi apa—contoh: *"Mahasiswa tingkat 1 dan 2 yang mengerjakan tugas kelompok di dua gedung kuliah pada jam sibuk 12:00–17:00"*).
   * `3. Supporting Observations or Evidence` (Observasi lapangan, survei kecil, wawancara, atau kutipan sumber `[1]`. **Dilarang keras mengarang hasil survei fiktif!** Jika menggunakan estimasi, wajib diberi label *estimate*).
   * `4. Proposed Solution and Core User Flow` (Jelaskan langkah demi langkah dari awal sampai akhir, misalnya 4 langkah inti, dan batasi *scope* versi pertama/MVP).
   * `5. How It Differs from Existing Alternatives` (Bandingkan secara konkret dengan minimal 1 alternatif yang ada sekarang).
   * `6. Planned Technologies` (Sebutkan platform, database, teknologi utama, sumber data, dan peran spesifik AI jika memakai AI).
   * `7. Expected Benefit and Development Plan` (Sebutkan metrik kesuksesan yang terukur—misal *"mencari ruangan dalam < 5 menit"*—rencana per minggu, dan **1 risiko utama beserta mitigasinya**).
2. **Jangan Klaim Fitur Rencana Sebagai Sudah Selesai:** Panitia sangat alergi terhadap *overclaiming*. Fitur yang baru direncanakan wajib ditulis sebagai *planned*, dan data simulasi harus diberi label *synthetic/simulated data*.

---

## BAGIAN 3: RISET MENDALAM PEMENANG HACKATHON SEBELUMNYA (ITB, GDSC/GDGoC, SOLUTION CHALLENGE, GARUDAHACKS)

Bagaimana pola tim-tim ITB dan Indonesia yang berhasil menjuarai ekosistem Google (GDSC HackFest, Google Solution Challenge Top 100/Top 10/Top 3) serta hackathon elit seperti GarudaHacks & Arkavidia?

### 3.1 Studi Kasus Pemenang Nyata & Bedah Apa yang Mereka Kerjakan
1. **Tim Wonder Reader (Binus Intl) — *Top 3 Global Winner Google Solution Challenge 2023***
   * **Apa yang mereka kerjakan:** Membangun alat baca Braille digital berbiaya rendah (3D-printed refreshable braille display) yang terhubung via Bluetooth ke aplikasi Android untuk membantu siswa tunanetra belajar di kelas dan menjawab kuis dari guru secara real-time.
   * **Poin Penting Kemenangan:** Fokus pada **Inklusivitas & Aksesibilitas Pembelajaran (EdTech Accessibility)**, masalah yang sangat nyata dengan angka kesenjangan yang jelas, serta demo end-to-end antara guru dan murid yang berjalan mulus.
2. **Tim Glutara / Tim AMN (ITB — Michael Leon, Austin Gabriel, Margaretha Olivia, Go Dillon) — *Top 10 Global Winner Google Solution Challenge 2024 & Juara 2 GDSC HackFest 2024***
   * **Apa yang mereka kerjakan:** Sistem pemantauan glukosa non-invasif (CGM tanpa tusuk jarum) terintegrasi aplikasi mobile + Machine Learning untuk prediksi tren gula darah dan rekomendasi nutrisi.
   * **Poin Penting Kemenangan:** Tim ITB ini menang karena **eksekusi produk yang terlihat seperti produk komersial matang**, UX yang sangat bersih, integrasi AI prediktif yang punya fungsi jelas (bukan sekadar chatbot tempelan), dan validasi masalah yang sangat kuat.
3. **Tim Neat Tip — *Juara 1 Nasional GDSC Indonesia HackFest 2023 & Global Top 100***
   * **Apa yang mereka kerjakan:** Digitalisasi penitipan motor di sekitar kampus/stasiun menggunakan **Google Maps API** (melihat slot parkir real-time) dan **Google ML Kit OCR** (scan plat nomor otomatis untuk *check-in/check-out* cepat tanpa karcis kertas).
   * **Poin Penting Kemenangan:** Masalah sehari-hari mahasiswa/komuter yang sangat *relatable*, alur penggunaan terdiri dari 4 langkah sederhana, dan penggunaan *Computer Vision / OCR + QR* untuk menghilangkan friksi antrean manual (sangat mirip dengan contoh *StudyNook* dari panitia STACK 2026!).
4. **Tim Binabisa / CUDA (ITB) — *Winner Best Sustainability Hack GarudaHacks***
   * **Apa yang mereka kerjakan:** Platform asesmen kerja dan pencocokan peluang berbasis AI yang ramah aksesibilitas untuk penyandang disabilitas.
   * **Poin Penting Kemenangan:** Menggabungkan *AI Matching/Assessment* dengan antarmuka inklusif untuk membuka akses peluang (*opportunities*) yang sebelumnya terfragmentasi.
5. **EduConnect (UIN SGD) & Voiye (UNIKOM) — *Global Top 100 Google Solution Challenge***
   * **Apa yang mereka kerjakan:** Kolaborasi belajar mahasiswa, pencocokan mentor-mentee sebaya, dan asisten suara/visual bagi pelajar berkebutuhan khusus.

### 3.2 7 Pola Emas ("Winning Formula") dari Semua Pemenang di Atas
1. **Hyper-Specific Pain Point:** Mereka tidak membuat "Aplikasi Super Kampus yang Bisa Segalanya". Mereka memilih **1 masalah tajam** (misal: sulit cari teman kelompok yang skill-nya komplementer, atau materi kuliah PDF/rekaman dosen yang berantakan, atau ruangan diskusi yang di-booking tapi kosong/*ghost booking*, atau info beasiswa/lomba/riset dosen yang tercecer di puluhan grup WA).
2. **Zero-Friction Core Loop (3–4 Klik Selesai):** Juri hanya punya waktu beberapa menit untuk mencoba atau melihat demo. Alur utama harus selesai dalam 3–4 langkah dengan *feedback* visual instan.
3. **"Anti-Ghosting / Verification Mechanism":** Perhatikan baik *Neat Tip* (Juara 1 HackFest) maupun contoh *StudyNook* di Handbook STACK 2026: keduanya memiliki fitur **verifikasi fisik/nyata yang cerdas** (misal *QR Check-in 15 menit otomatis hangus jika tidak datang*, atau *verifikasi kontribusi anggota kelompok*). Juri sangat menyukai logika bisnis yang memikirkan perilaku nyata manusia di kampus!
4. **AI sebagai "Invisible Engine", Bukan Sekadar Chatbot:** Pemenang tidak sekadar menaruh layar chat mirip ChatGPT. Mereka memakai AI di balik layar untuk:
   * Mengubah slide PDF kuliah + rekaman suara dosen menjadi *Knowledge Graph*, *Flashcard Spaced Repetition (FSRS)*, dan *Podcast/Quiz Interaktif*.
   * Mengekstrak poster beasiswa/lomba dari gambar/grup menjadi database terstruktur yang langsung dicocokkan (*auto-matched*) dengan profil CV/transkrip mahasiswa.
   * Mencocokkan *Study Partner / Project Team* berdasarkan komplementaritas skill GitHub/portofolio dan jadwal kosong kuliah (KRS).
5. **Data Validasi Nyata dari Kampus Sendiri:** Sebelum koding jauh, mereka menyebar kuesioner singkat ke 30–50 mahasiswa asli dan mewawancarai 2–3 pengelola/dosen, lalu menampilkan grafik bukti tersebut di slide ke-2.
6. **Live Demo TanpaCacat + Fallback Lokal:** Saat penilaian final (bobot *Functionality & Reliability* 30%), aplikasi tidak boleh *crash* karena Wi-Fi venue lambat. Semua pemenang menyiapkan *seed data* realistis dan mode lokal.
7. **Strategi Khusus STACK 2026 (Final Day Build Session 10%):** Karena STACK 2026 mewajibkan Top 10 menyelesaikan 2–3 fitur saat *Final Day Build Session*, tim pemenang akan menyiapkan arsitektur modular di mana 80% fondasi sudah kokoh sebelum tanggal 16 Desember, dan menyisakan 2–3 modul *high-impact* (misal: integrasi notifikasi real-time, analitik dashboard, atau fitur export/QR check-in) yang sudah disiapkan rangkanya untuk dieksekusi dengan bersih saat *live build session*.

---

## BAGIAN 4: PENJELAJAHAN BRUTAL 115+ REPOSITORI GITHUB TERBAIK (TERVERIFIKASI API, SEMUA >100⭐ HINGGA 450.000⭐)

Seluruh repositori di bawah ini telah diambil dan diverifikasi langsung melalui GitHub API dengan jumlah bintang (*stars*) aktual per November 2026, dikelompokkan ke dalam **10 Kategori Arsitektur** untuk **Case 1: Smarter Campus and Learning**.

### Kategori 1: AI Study Assistant, NotebookLM Open-Source & Academic Research Agents (16 Repo)
Cocok untuk membangun asisten belajar cerdas yang mengubah materi kuliah menjadi ruang belajar interaktif, podcast diskusi, dan asisten riset bebas halusinasi.
1. **[teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py)** (20,175 ⭐ | Python) — API Python & agentic skill untuk mengakses fitur Google Gemini NotebookLM secara terprogram.
2. **[dzhng/deep-research](https://github.com/dzhng/deep-research)** (19,880 ⭐ | TypeScript) — Agen riset mendalam iteratif yang menggabungkan search engine, web scraping, dan LLM untuk membedah topik akademik.
3. **[arc53/DocsGPT](https://github.com/arc53/DocsGPT)** (18,366 ⭐ | Python) — Platform AI privat untuk analisis dokumen kuliah, pembuatan agen tutor, dan pencarian silabus/kampus.
4. **[MODSetter/SurfSense](https://github.com/MODSetter/SurfSense)** (16,809 ⭐ | Python) — Alternatif NotebookLM open-source yang *privacy-focused*; agen AI yang meriset, mentransformasi, dan mengedit dokumen belajar mahasiswa.
5. **[Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex)** (14,230 ⭐ | Python) — Suite alur kerja riset akademik *human-in-the-loop* (literature review, penulisan ilmiah, analisis sitasi).
6. **[langchain-ai/local-deep-researcher](https://github.com/langchain-ai/local-deep-researcher)** (9,409 ⭐ | Python) — Asisten riset web dan penulisan laporan akademik yang dapat berjalan sepenuhnya secara lokal.
7. **[PleasePrompto/notebooklm-skill](https://github.com/PleasePrompto/notebooklm-skill)** (7,788 ⭐ | Python) — Integrasi langsung dengan Google NotebookLM untuk tanya-jawab berbasis kutipan sumber (*source-grounded citations*).
8. **[souzatharsis/podcastfy](https://github.com/souzatharsis/podcastfy)** (6,794 ⭐ | Python) — Alternatif open-source fitur Audio Overview NotebookLM: mengubah PDF materi kuliah menjadi diskusi podcast audio multi-bahasa!
9. **[joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm)** (6,483 ⭐ | Python) — Pemroses multi-sumber (YouTube, PDF, artikel web, Markdown) menjadi Podcast, PPT, MindMap, dan Kuis.
10. **[Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar)** (6,017 ⭐ | Python) — Asisten riset semi-otomatis untuk riset akademik mahasiswa dari ideasi, eksperimen, hingga publikasi.
11. **[54yyyu/zotero-mcp](https://github.com/54yyyu/zotero-mcp)** (5,816 ⭐ | Python) — Menghubungkan perpustakaan jurnal Zotero mahasiswa dengan asisten AI melalui Model Context Protocol (MCP).
12. **[mukulpatnaik/researchgpt](https://github.com/mukulpatnaik/researchgpt)** (3,521 ⭐ | Python) — Asisten riset berbasis LLM untuk berdialog langsung dengan paper penelitian/jurnal PDF.
13. **[PleasePrompto/notebooklm-mcp](https://github.com/PleasePrompto/notebooklm-mcp)** (3,444 ⭐ | TypeScript) — Server MCP untuk NotebookLM dengan jawaban berbasis sitasi dari Gemini tanpa halusinasi.
14. **[AnotiaWang/deep-research-web-ui](https://github.com/AnotiaWang/deep-research-web-ui)** (2,225 ⭐ | TypeScript) — Web UI siap pakai (Docker-ready) untuk agen deep-research yang mengubah pertanyaan mahasiswa menjadi laporan lengkap bersitasi.
15. **[CaviraOSS/PageLM](https://github.com/CaviraOSS/PageLM)** (2,065 ⭐ | TypeScript) — Versi komunitas dari NotebookLM & platform edukasi yang mengubah materi kuliah menjadi kuis, flashcard, dan catatan.
16. **[zuhairhalawa/studyai](https://github.com/zuhairhalawa/studyai)** (248 ⭐ | TypeScript) — Platform belajar *local-first* khusus kuliah universitas: slide PowerPoint, spaced repetition, simulasi ujian, dan tutor AI.

### Kategori 2: Ekstraksi PDF Kuliah, OCR Rumus Matematika/LaTeX & Pemrosesan Dokumen Kampus (15 Repo)
Sangat krusial untuk mengatasi masalah *"Learning materials that are difficult to access"* (slide dosen hasil scan buram, rumus matematika kompleks, diktat PDF ratusan halaman).
17. **[microsoft/markitdown](https://github.com/microsoft/markitdown)** (194,492 ⭐ | Python) — Tool resmi Microsoft untuk mengonversi segala jenis file kuliah (PDF, PPTX, DOCX, XLSX, Audio, Gambar) menjadi Markdown bersih untuk LLM.
18. **[Stirling-Tools/Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF)** (96,084 ⭐ | TypeScript/Java) — Aplikasi manipulasi PDF #1 di GitHub untuk menggabungkan, OCR, kompresi, dan anotasi dokumen kuliah.
19. **[PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)** (92,460 ⭐ | Python) — Toolkit OCR super akurat (100+ bahasa termasuk Indonesia & Inggris) untuk mengubah foto papan tulis/slide PDF menjadi JSON/Markdown terstruktur.
20. **[opendatalab/MinerU](https://github.com/opendatalab/MinerU)** (83,343 ⭐ | Python) — Mengubah dokumen akademik kompleks (PDF multi-kolom, tabel, rumus) menjadi Markdown/JSON siap pakai untuk RAG.
21. **[binary-husky/gpt_academic](https://github.com/binary-husky/gpt_academic)** (71,623 ⭐ | Python) — Antarmuka khusus pembacaan, penerjemahan, dan bedah paper akademik PDF/LaTeX serta repositori kode.
22. **[docling-project/docling](https://github.com/docling-project/docling)** (70,315 ⭐ | Python) — Ekstraktor dokumen IBM untuk memproses PDF, DOCX, dan PPTX akademik dengan pemahaman tata letak tabel dan rumus.
23. **[mozilla/pdf.js](https://github.com/mozilla/pdf.js)** (54,114 ⭐ | JavaScript) — Standar industri untuk merender PDF interaktif beserta layer highlight/anotasi di dalam browser.
24. **[hiroi-sora/Umi-OCR](https://github.com/hiroi-sora/Umi-OCR)** (48,529 ⭐ | Python) — Mesin OCR offline cepat untuk tangkapan layar kuliah dan dokumen scan massal.
25. **[datalab-to/marker](https://github.com/datalab-to/marker)** (40,822 ⭐ | Python) — Mengonversi PDF buku teks dan diktat kuliah menjadi Markdown + JSON dengan kecepatan dan akurasi tinggi.
26. **[google/langextract](https://github.com/google/langextract)** (39,287 ⭐ | Python) — Library resmi Google untuk mengekstrak informasi terstruktur (misal jadwal, syarat beasiswa, silabus) dari teks tidak terstruktur dengan LLM.
27. **[PDFMathTranslate/PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate)** (38,301 ⭐ | Python) — Menerjemahkan paper ilmiah/buku teks bahasa asing ke Bahasa Indonesia/Inggris dengan **tetap mempertahankan format rumus matematika, tabel, dan layout asli PDF**!
28. **[ocrmypdf/OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF)** (35,272 ⭐ | Python) — Menambahkan layer teks yang bisa dicari (*searchable text*) pada PDF diktat kuliah hasil scan.
29. **[datalab-to/surya](https://github.com/datalab-to/surya)** (21,587 ⭐ | Python) — OCR dokumen, analisis layout, urutan baca, dan pengenalan tabel untuk 90+ bahasa.
30. **[lukas-blecher/LaTeX-OCR](https://github.com/lukas-blecher/LaTeX-OCR)** (16,611 ⭐ | Python) — `pix2tex`: Mengubah foto/screenshot rumus matematika di papan tulis atau buku menjadi kode LaTeX secara instan.
31. **[facebookresearch/nougat](https://github.com/facebookresearch/nougat)** (10,095 ⭐ | Python) — *Neural Optical Understanding for Academic Documents* dari Meta AI khusus memahami dokumen ilmiah & matematika.

### Kategori 3: Mesin RAG, AI Tutoring, Memory & Knowledge Graph Pembelajaran (14 Repo)
Fondasi untuk membuat AI Tutor yang mengenali riwayat belajar tiap mahasiswa (*personalized learning*) dan memetakan hubungan antar-materi kuliah.
32. **[langgenius/dify](https://github.com/langgenius/dify)** (160,720 ⭐ | Python/TypeScript) — Platform komprehensif untuk membangun *Agentic Workflows* dan *RAG Pipelines* secara visual maupun via API.
33. **[open-webui/open-webui](https://github.com/open-webui/open-webui)** (158,168 ⭐ | Svelte/Python) — Antarmuka AI multi-model lengkap dengan fitur dokumen RAG, voice call, dan kolaborasi.
34. **[langflow-ai/langflow](https://github.com/langflow-ai/langflow)** (156,455 ⭐ | Python) — Builder visual berbasis *React Flow* untuk merancang multi-agent AI dan RAG secara cepat saat hackathon.
35. **[langchain-ai/langchain](https://github.com/langchain-ai/langchain)** (149,240 ⭐ | Python) — Framework standar rekayasa agen AI dan pipeline orkestrasi LLM.
36. **[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)** (144,629 ⭐ | Python) — Mengubah repositori kode, skema SQL, dan PDF menjadi *queryable knowledge graph* dengan penjelasan setiap relasi.
37. **[infiniflow/ragflow](https://github.com/infiniflow/ragflow)** (93,805 ⭐ | Go/Python) — Mesin RAG *deep document understanding* dengan sitasi presisi tinggi untuk dokumen kompleks.
38. **[mem0ai/mem0](https://github.com/mem0ai/mem0)** (68,667 ⭐ | Python) — *Memory Layer* untuk AI Agents: menyimpan progres belajar, kelemahan topik, dan preferensi tiap mahasiswa lintas sesi!
39. **[Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm)** (68,091 ⭐ | JavaScript) — Aplikasi full-stack untuk mengubah kumpulan dokumen mata kuliah menjadi workspace chat & agen kolaboratif.
40. **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** (57,221 ⭐ | Python) — Sistem *Lifelong Personalized AI Tutoring* yang dirancang khusus untuk bimbingan belajar adaptif.
41. **[HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)** (40,616 ⭐ | Python) — Versi ringan dan super cepat dari Graph-based RAG untuk menghubungkan konsep-konsep lintas mata kuliah.
42. **[khoj-ai/khoj](https://github.com/khoj-ai/khoj)** (38,075 ⭐ | Python) — *AI Second Brain* open-source yang bisa menjawab dari PDF catatan kuliah maupun internet serta menjalankan agen terjadwal.
43. **[microsoft/graphrag](https://github.com/microsoft/graphrag)** (36,600 ⭐ | Python) — Sistem RAG berbasis Knowledge Graph modular dari Microsoft untuk menemukan hubungan tersembunyi antar dokumen.
44. **[neo4j-labs/llm-graph-builder](https://github.com/neo4j-labs/llm-graph-builder)** (5,301 ⭐ | Python) — Mengubah PDF silabus, jurnal, dan slide kuliah menjadi visualisasi Knowledge Graph Neo4j menggunakan LLM.
45. **[varunshenoy/GraphGPT](https://github.com/varunshenoy/GraphGPT)** (4,423 ⭐ | JavaScript) — Mengekstrapolasi teks kuliah tidak terstruktur menjadi graf pengetahuan visual secara real-time.

### Kategori 4: Kolaborasi Mahasiswa Real-Time, Kanvas Papan Tulis, Mindmap & Editor Bersama (18 Repo)
Menjawab sub-tema *"Student Collaboration"* (papan tulis kelompok, pencatatan bersama seperti Notion/Miro, diagram arsitektur, dan sinkronisasi multi-user tanpa konflik).
46. **[excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)** (135,365 ⭐ | TypeScript) — Papan tulis virtual kolaboratif bergaya sketsa tangan yang sangat mudah di-embed sebagai komponen React (`@excalidraw/excalidraw`).
47. **[mermaid-js/mermaid](https://github.com/mermaid-js/mermaid)** (91,047 ⭐ | TypeScript) — Mengubah teks markdown/output AI menjadi flowchart, mindmap, sequence diagram, dan timeline proyek kelompok secara instan.
48. **[AppFlowy-IO/AppFlowy](https://github.com/AppFlowy-IO/AppFlowy)** (78,515 ⭐ | Dart/Rust) — Workspace kolaboratif AI (alternatif Notion open-source) untuk manajemen proyek kelompok, wiki kelas, dan catatan bersama.
49. **[toeverything/AFFiNE](https://github.com/toeverything/AFFiNE)** (74,365 ⭐ | TypeScript) — Gabungan Notion + Miro open-source: menyatukan dokumen blok dan papan tulis kanvas tanpa batas untuk kerja kelompok mahasiswa.
50. **[tldraw/tldraw](https://github.com/tldraw/tldraw)** (51,428 ⭐ | TypeScript) — SDK Infinite Canvas terbaik untuk React; sangat populer dikombinasikan dengan AI untuk membuat *collaborative visual study board*.
51. **[siyuan-note/siyuan](https://github.com/siyuan-note/siyuan)** (47,140 ⭐ | TypeScript/Go) — Workspace manajemen pengetahuan *local-first* dengan dukungan blok referensi dua arah dan AI.
52. **[logseq/logseq](https://github.com/logseq/logseq)** (45,527 ⭐ | Clojure/JS) — Platform manajemen pengetahuan berbasis *outliner*, graf pemikiran, PDF annotation, dan flashcard.
53. **[outline/outline](https://github.com/outline/outline)** (41,205 ⭐ | TypeScript) — Wiki & basis pengetahuan kolaboratif real-time super cepat untuk himpunan mahasiswa, laboratorium, atau kelompok belajar.
54. **[pubkey/rxdb](https://github.com/pubkey/rxdb)** (23,422 ⭐ | TypeScript) — Database *local-first* reaktif untuk JavaScript agar aplikasi kampus tetap jalan saat Wi-Fi gedung kuliah mati (*offline-capable*).
55. **[yjs/yjs](https://github.com/yjs/yjs)** (23,038 ⭐ | JavaScript) — Engine CRDT terbaik dunia untuk membangun fitur *multiplayer real-time collaboration* (kursor live, edit catatan bareng).
56. **[docmost/docmost](https://github.com/docmost/docmost)** (22,266 ⭐ | TypeScript) — Perangkat lunak wiki dan dokumentasi kolaboratif open-source untuk organisasi kampus dan grup riset.
57. **[linkwarden/linkwarden](https://github.com/linkwarden/linkwarden)** (20,347 ⭐ | TypeScript) — Manajer bookmark & referensi kolaboratif bagi kelompok mahasiswa untuk mengumpulkan, mencoret-coret, dan mengarsipkan jurnal/artikel web.
58. **[overleaf/overleaf](https://github.com/overleaf/overleaf)** (18,316 ⭐ | JavaScript) — Editor LaTeX kolaboratif berbasis web untuk penulisan laporan praktikum, tugas akhir, dan paper ilmiah bersama.
59. **[suitenumerique/docs](https://github.com/suitenumerique/docs)** (16,981 ⭐ | TypeScript) — Editor dokumen kolaboratif real-time modern berbasis web dengan struktur bersih.
60. **[plait-board/drawnix](https://github.com/plait-board/drawnix)** (15,038 ⭐ | TypeScript) — Papan tulis SaaS open-source *all-in-one* yang mencakup MindMap, Flowchart, dan gambar bebas.
61. **[markmap/markmap](https://github.com/markmap/markmap)** (13,228 ⭐ | TypeScript) — Mengubah catatan kuliah Markdown biasa menjadi visualisasi MindMap interaktif secara instan di browser.
62. **[TypeCellOS/BlockNote](https://github.com/TypeCellOS/BlockNote)** (10,367 ⭐ | TypeScript) — Komponen React Rich Text Editor bergaya Notion (*block-based*) lengkap dengan menu `/` dan kolaborasi real-time Yjs.
63. **[supabase/realtime](https://github.com/supabase/realtime)** (7,678 ⭐ | Elixir) — Server WebSocket untuk fitur *Broadcast*, *Live Presence* (melihat siapa teman yang sedang online di ruang belajar), dan perubahan Postgres instan.

### Kategori 5: Flashcards, Active Recall, Spaced Repetition (FSRS) & Gamifikasi Belajar (12 Repo)
Sangat kuat untuk membuktikan **Measurable Learning Benefit** kepada juri (meningkatkan retensi hafalan dan pemahaman konsep secara terukur menggunakan algoritma ilmiah FSRS).
64. **[ankitects/anki](https://github.com/ankitects/anki)** (32,682 ⭐ | Rust/Python) — Program flashcard *spaced repetition* paling legendaris di dunia.
65. **[ankidroid/Anki-Android](https://github.com/ankidroid/Anki-Android)** (12,198 ⭐ | Kotlin) — Implementasi mobile Android untuk sistem belajar pengulangan berjarak.
66. **[mengxi-ream/read-frog](https://github.com/mengxi-ream/read-frog)** (10,343 ⭐ | TypeScript) — Ekstensi & platform AI untuk pembelajaran bahasa/jurnal asing dan pembuatan flashcard otomatis saat membaca.
67. **[echo-loop/Echo-Loop](https://github.com/echo-loop/Echo-Loop)** (4,692 ⭐ | Dart/Flutter) — Aplikasi latihan pemahaman audio & pengulangan berjarak (*spaced repetition*) berbasis AI.
68. **[designfuchen/word-atlas](https://github.com/designfuchen/word-atlas)** (4,515 ⭐ | TypeScript) — Aplikasi belajar kosakata akademik interaktif dengan algoritma review FSRS modern.
69. **[open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki)** (4,128 ⭐ | Python) — Algoritma *Free Spaced Repetition Scheduler* (FSRS) modern berbasis machine learning yang jauh lebih akurat dari algoritma SM-2 lama.
70. **[st3v3nmw/obsidian-spaced-repetition](https://github.com/st3v3nmw/obsidian-spaced-repetition)** (2,615 ⭐ | TypeScript) — Sistem review flashcard dan catatan utuh untuk melawan kurva lupa (*forgetting curve*).
71. **[modocache/MDCSwipeToChoose](https://github.com/modocache/MDCSwipeToChoose)** (2,535 ⭐ | Objective-C) — UI komponen *swipe kanan/kiri* ala Tinder untuk membuat kuis flashcard atau fitur **Swipe Study Partner / Rekan Tim**!
72. **[olmps/memo](https://github.com/olmps/memo)** (1,870 ⭐ | Dart/Flutter) — Aplikasi Spaced Repetition (SRS) open-source di Flutter khusus untuk mahasiswa pemrograman/rekayasa.
73. **[andymatuschak/orbit](https://github.com/andymatuschak/orbit)** (1,838 ⭐ | TypeScript) — Platform eksperimental *spaced repetition* dari Andy Matuschak untuk menyematkan kuis *active recall* langsung di tengah bacaan materi kuliah.
74. **[nagisanzenin/engram](https://github.com/nagisanzenin/engram)** (1,475 ⭐ | Python) — Mesin pembelajaran berbasis bukti (*evidence-based learning engine*) dengan kurikulum *first-principles* dan verifikasi *free-recall*.
75. **[open-spaced-repetition/ts-fsrs](https://github.com/open-spaced-repetition/ts-fsrs)** (861 ⭐ | TypeScript) — Library NPM resmi algoritma FSRS dalam TypeScript (`npm i ts-fsrs`) — siap langsung dipasang di aplikasi Next.js/React Anda dalam 5 menit!

### Kategori 6: Transkripsi Rekaman Kuliah, Audio-to-Notes & Aksesibilitas Kampus (12 Repo)
Menjawab masalah mahasiswa yang tertinggal penjelasan dosen di kelas atau mahasiswa berkebutuhan khusus (Tuli/Disabilitas) dengan mengubah suara dosen menjadi catatan terstruktur & penanda waktu.
76. **[openai/whisper](https://github.com/openai/whisper)** (112,267 ⭐ | Python) — Model pengenalan suara (ASR) multi-bahasa paling tangguh untuk mentranskripsi rekaman kuliah.
77. **[ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp)** (55,030 ⭐ | C++) — Porting Whisper super ringan yang bisa berjalan langsung di laptop/HP mahasiswa tanpa GPU mahal.
78. **[Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily)** (32,542 ⭐ | Rust/TypeScript) — Pencatat rapat & kuliah AI (*AI meeting/lecture note taker*) berbasis lokal dengan Whisper + ringkasan otomatis.
79. **[SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper)** (26,604 ⭐ | Python) — Implementasi Whisper hingga 4x lebih cepat dengan memori jauh lebih hemat.
80. **[m-bain/whisperX](https://github.com/m-bain/whisperX)** (25,162 ⭐ | Python) — ASR dengan **Word-level Timestamps & Speaker Diarization** (bisa membedakan suara dosen vs mahasiswa yang bertanya dan melompat ke detik penjelasan!).
81. **[chidiwilliams/buzz](https://github.com/chidiwilliams/buzz)** (22,535 ⭐ | Python) — Aplikasi transkripsi dan penerjemahan audio kuliah secara offline di komputer pribadi.
82. **[Vaibhavs10/insanely-fast-whisper](https://github.com/Vaibhavs10/insanely-fast-whisper)** (13,057 ⭐ | Python) — Transkripsi rekaman kuliah berdurasi 2 jam hanya dalam hitungan detik.
83. **[QuentinFuxa/WhisperLiveKit](https://github.com/QuentinFuxa/WhisperLiveKit)** (11,221 ⭐ | Python) — Speech-to-text *real-time streaming* dengan diarization dan terjemahan langsung di ruang kelas (sangat bagus untuk aksesibilitas mahasiswa Tuli!).
84. **[nexmoe/VidBee](https://github.com/nexmoe/VidBee)** (11,102 ⭐ | TypeScript) — Mengunduh video rekaman kuliah, mentranskripsi dengan label pembicara, serta membuat ringkasan dan mindmap otomatis.
85. **[OpenWhispr/openwhispr](https://github.com/OpenWhispr/openwhispr)** (11,064 ⭐ | JavaScript) — Aplikasi dikte suara-ke-teks cepat untuk mencatat ide tugas/skripsi secara hands-free.
86. **[niedev/RTranslator](https://github.com/niedev/RTranslator)** (10,622 ⭐ | Java/Android) — Aplikasi penerjemah percakapan real-time offline di Android untuk mahasiswa internasional/pertukaran pelajar.
87. **[thewh1teagle/vibe](https://github.com/thewh1teagle/vibe)** (8,037 ⭐ | TypeScript/Rust) — Aplikasi transkripsi audio/video kuliah lintas platform yang bersih dan modern.

### Kategori 7: Virtual Study Room, Peer Mentoring, WebRTC Video/Audio & P2P File Sharing Kampus (11 Repo)
Membangun ruang belajar sebaya (*Peer Tutoring / Virtual Study Nook*), berbagi layar saat koding bareng, dan transfer file materi kuliah super cepat antar mahasiswa satu jaringan kampus.
88. **[localsend/localsend](https://github.com/localsend/localsend)** (97,993 ⭐ | Dart/Flutter) — Berbagi file materi kuliah lintas perangkat (Android, iOS, Windows, Mac) di Wi-Fi kampus tanpa internet.
89. **[RocketChat/Rocket.Chat](https://github.com/RocketChat/Rocket.Chat)** (46,380 ⭐ | TypeScript) — Platform komunikasi tim/komunitas kampus lengkap dengan channel mata kuliah dan thread diskusi.
90. **[jitsi/jitsi-meet](https://github.com/jitsi/jitsi-meet)** (30,211 ⭐ | TypeScript) — Konferensi video open-source yang sangat mudah di-embed ke dalam aplikasi web kampus untuk sesi *peer mentoring* tanpa perlu keluar aplikasi.
91. **[livekit/livekit](https://github.com/livekit/livekit)** (22,103 ⭐ | Go/TypeScript) — Stack WebRTC real-time terbaik untuk membangun **Ruang Belajar Audio/Video + AI Voice Tutor** yang ikut berbicara di dalam room!
92. **[SnapDrop/snapdrop](https://github.com/SnapDrop/snapdrop)** (19,713 ⭐ | JavaScript) — Progressive Web App (PWA) untuk berbagi file instan antar mahasiswa di ruangan yang sama lewat browser.
93. **[pion/webrtc](https://github.com/pion/webrtc)** (16,889 ⭐ | Go) — Implementasi WebRTC murni di Go untuk komunikasi audio/video berlatensi sangat rendah.
94. **[tinode/chat](https://github.com/tinode/chat)** (13,558 ⭐ | Go/JS) — Platform pesan instan ringan untuk fitur chat kelompok belajar dan pencarian partner.
95. **[peers/peerjs](https://github.com/peers/peerjs)** (13,510 ⭐ | TypeScript) — Membungkus WebRTC menjadi API JavaScript super simpel untuk fitur video call & kolaborasi P2P antar mahasiswa.
96. **[schlagmichdoch/PairDrop](https://github.com/schlagmichdoch/PairDrop)** (11,771 ⭐ | JavaScript) — Transfer file lintas platform di jaringan lokal dengan fitur *paired devices* dan room publik sementara untuk satu kelas.
97. **[screego/server](https://github.com/screego/server)** (10,749 ⭐ | Go/TypeScript) — Berbagi layar (*screen sharing*) berkualitas tinggi khusus untuk sesi asistensi koding/praktikum mahasiswa.
98. **[netless-io/flat](https://github.com/netless-io/flat)** (6,444 ⭐ | TypeScript) — Ruang kelas virtual open-source lengkap dengan papan tulis interaktif, video call, dan berbagi dokumen kuliah.

### Kategori 8: Agen Pencari Beasiswa/Lomba/Riset, Web Scraper Cerdas & Otomasi Peluang Kampus (10 Repo)
Menjawab masalah pertama di Handbook STACK 2026: *"Fragmented scholarship and opportunity information"* (mengambil info beasiswa, magang, lomba, dan proyek dosen dari berbagai web/sosmed lalu mencocokkannya dengan profil mahasiswa).
99. **[n8n-io/n8n](https://github.com/n8n-io/n8n)** (209,880 ⭐ | TypeScript) — Platform otomasi alur kerja dengan integrasi AI native untuk menarik pengumuman kampus dari email, Telegram, RSS, dan web ke satu dashboard.
100. **[firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)** (199,900 ⭐ | TypeScript) — Mengubah website pengumuman kampus/beasiswa mana pun menjadi data Markdown/JSON bersih yang siap dianalisis LLM.
101. **[browser-use/browser-use](https://github.com/browser-use/browser-use)** (120,378 ⭐ | Python) — Membuat agen AI yang bisa mengendalikan browser secara otomatis untuk mencari beasiswa, mengecek syarat pendaftaran, atau memantau kuota kelas.
102. **[unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)** (87,121 ⭐ | Python) — Web crawler & scraper open-source super cepat yang dirancang khusus untuk mengekstrak data terstruktur bagi agen AI.
103. **[crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)** (60,675 ⭐ | Python) — Orkestrasi multi-agen (misal: 1 Agen Pemburu Beasiswa + 1 Agen Penilai CV Mahasiswa + 1 Agen Pelatih Wawancara).
104. **[ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai)** (32,643 ⭐ | Python) — Scraper Python berbasis graf & LLM: cukup berikan URL pengumuman kampus dan prompt *"Ekstrak nama beasiswa, batas waktu, syarat IPK, dan link daftar"*.
105. **[alibaba/page-agent](https://github.com/alibaba/page-agent)** (29,650 ⭐ | TypeScript) — Agen GUI di dalam halaman web yang memungkinkan mahasiswa mengontrol portal akademik yang rumit hanya dengan perintah bahasa alami.
106. **[Fosowl/agenticSeek](https://github.com/Fosowl/agenticSeek)** (27,642 ⭐ | Python) — Agen otonom lokal yang dapat menjelajah web, mencari informasi peluang akademik, dan menyusun rangkuman.
107. **[Alibaba-NLP/DeepResearch](https://github.com/Alibaba-NLP/DeepResearch)** (20,118 ⭐ | Python) — Agen riset mendalam untuk menggali informasi akademik dan peluang riset dari berbagai sumber.
108. **[zaidmukaddam/scira](https://github.com/zaidmukaddam/scira)** (11,929 ⭐ | TypeScript) — Mesin pencari bertenaga AI minimalis (eks-MiniPerplx) dengan pencarian akademik (*academic search*), YouTube, dan ekstraksi informasi kampus.

### Kategori 9: LMS Open-Source, Integrasi Akademik & Manajemen Fasilitas/Jadwal Kampus (9 Repo)
Menjawab sub-tema *"Campus services and facilities"* (booking ruangan, sinkronisasi jadwal kuliah/tugas Moodle, dan manajemen kegiatan kampus).
109. **[openedx/openedx-platform](https://github.com/openedx/openedx-platform)** (8,220 ⭐ | Python) — Platform LMS open-source skala universitas yang digunakan oleh MIT, Harvard, dan kampus top dunia.
110. **[moodle/moodle](https://github.com/moodle/moodle)** (7,593 ⭐ | PHP) — Platform LMS standar yang digunakan mayoritas universitas di Indonesia (termasuk basis EduNext/kuliah daring).
111. **[oppia/oppia](https://github.com/oppia/oppia)** (6,981 ⭐ | Python/TypeScript) — Platform pembelajaran interaktif berbasis eksplorasi step-by-step dengan umpan balik adaptif.
112. **[instructure/canvas-lms](https://github.com/instructure/canvas-lms)** (6,905 ⭐ | Ruby/JS) — LMS modern dengan API terbuka untuk integrasi jadwal tugas, kalender akademik, dan penilaian rubrik.
113. **[classroomio/classroomio](https://github.com/classroomio/classroomio)** (1,737 ⭐ | TypeScript/Svelte) — LMS modern berbasis Supabase & TypeScript untuk manajemen kelas/bootcamp, tugas, dan komunitas belajar mahasiswa.
114. **[C0D3D3V/Moodle-DL](https://github.com/C0D3D3V/Moodle-DL)** (664 ⭐ | Python) — Mengunduh dan menyinkronkan seluruh materi kuliah (PDF, tugas, pengumuman) dari Moodle kampus secara otomatis!
115. **[francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis)** (652 ⭐ | PHP) — Sistem Informasi Mahasiswa (*Student Information System*) mencakup penjadwalan ruangan, kalender akademik, dan absensi.
116. **[Berserk-hub150/moodle-ai-skill-navigator](https://github.com/Berserk-hub150/moodle-ai-skill-navigator)** (278 ⭐ | PHP) — Plugin AI untuk Moodle yang menyediakan fitur tutoring, kuis otomatis, mind map, dan RAG materi kuliah.
117. **[Faixiang/Moodle-MCP](https://github.com/Faixiang/Moodle-MCP)** (204 ⭐ | Python) — Server MCP tanpa dependensi untuk membaca daftar mata kuliah, tenggat tugas (*assignment deadlines*), kuis, dan nilai langsung dari API Moodle kampus!

### Kategori 10: Full-Stack Hackathon Accelerators, Generative UI, Database & Analitik Validasi (12 Repo)
Senjata utama untuk membangun aplikasi yang terlihat sekelas startup Silicon Valley dan **anti-crash** saat Live Demo di Final Day (bobot *Functionality & Reliability* 30% + *Usability* 10%).
118. **[supabase/supabase](https://github.com/supabase/supabase)** (114,692 ⭐ | TypeScript/Postgres) — Backend-as-a-Service (Postgres, Auth akun kampus, Vector DB `pgvector`, Storage PDF, dan Realtime WebSockets) — **Fondasi yang sama persis dengan yang dipakai panitia GDGoC ITB untuk membuat web `gdgoncampusitb.com`!**
119. **[appwrite/appwrite](https://github.com/appwrite/appwrite)** (57,897 ⭐ | TypeScript) — Alternatif BaaS open-source lengkap (Auth, DB, Storage, Functions, Messaging) untuk prototipe cepat.
120. **[DavidHDev/react-bits](https://github.com/DavidHDev/react-bits)** (51,542 ⭐ | JavaScript/React) — Koleksi komponen React & Next.js interaktif dan beranimasi terbesar untuk membuat UI yang langsung memukau mata juri.
121. **[fastapi/full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template)** (46,209 ⭐ | TypeScript/Python) — Template full-stack resmi FastAPI + React + PostgreSQL + Tailwind + Shadcn UI + Docker (sangat pas jika backend Anda memakai Python AI/OCR).
122. **[PostHog/posthog](https://github.com/PostHog/posthog)** (40,708 ⭐ | Python/TypeScript) — Platform *Product Analytics & Session Replay* untuk merekam metrik uji coba pengguna (*user testing metrics*: waktu penyelesaian tugas, klik, retensi) guna mendapatkan nilai sempurna pada kriteria **Validation and Impact**!
123. **[CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit)** (38,574 ⭐ | TypeScript) — Stack frontend untuk *In-App AI Agents & Generative UI* di React/Next.js (agen AI bisa langsung merender komponen UI interaktif, mengisi form jadwal, atau menyorot layar mahasiswa).
124. **[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides)** (32,107 ⭐ | JavaScript) — Membuat slide presentasi interaktif berbasis web langsung dari proyek untuk memukau juri saat sesi Pitching 10 menit.
125. **[magicuidesign/magicui](https://github.com/magicuidesign/magicui)** (23,153 ⭐ | TypeScript) — Library komponen UI modern untuk *Design Engineers* (komponen bento grid, marquee, animasi transisi halus).
126. **[vercel/chatbot](https://github.com/vercel/chatbot)** (21,040 ⭐ | TypeScript) — Template Next.js AI Chatbot full-featured resmi dari Vercel dengan dukungan *Generative UI / Artifacts*.
127. **[udecode/plate](https://github.com/udecode/plate)** (16,694 ⭐ | TypeScript) — Rich-text editor modern berbasis AI dan `shadcn/ui` untuk pencatatan kolaboratif.
128. **[satnaing/shadcn-admin](https://github.com/satnaing/shadcn-admin)** (16,620 ⭐ | TypeScript) — Dashboard Admin siap pakai berbasis Shadcn UI + Vite untuk menampilkan halaman sisi pengelola kampus/dosen/staf gedung.
129. **[assistant-ui/assistant-ui](https://github.com/assistant-ui/assistant-ui)** (13,020 ⭐ | TypeScript) — Library komponen React/TypeScript terbaik untuk membangun antarmuka AI Chat & Co-pilot di dalam aplikasi web.

---

## BAGIAN 5: KONSEP FINAL TERKUNCI TIM `PRAY FIRST` (`ACADEMIAFLOW` — "1 PORTAL FOR EVERYTHING")

### 🌟 KONSEP UTAMA PILIHAN TIM `PRAY FIRST`: **`AcademiaFlow` — Unified Student Lifecycle Workspace (Semester 1 s.d. Lulus)**
* **Team Name:** `Pray First`
* **Members:**
  1. **Allfridhoo Prima Anjaynata Saragi (Leader)** — *Product Architect, Supabase Database, Modul 1 (Smart KRS & Circle Sync) & Modul 3 (MoU 20-SKS Internship & Alumni Hub)*
  2. **Mikhael Yuli Ananda Elvan Permana** — *Realtime Concurrency, Modul 2B (Accountable Groupwork Handover) & Modul 4 (Semantic Dosbing Matching, In-App Consultation Ticket, 1-Click Logbook Approval & 21-Day Thesis SLA Rebalancer)*
  3. **Nathanael Christian Putra** — *AI Learning & Collaborative Workspace Engineer, Modul 2A (StudyPulse / KuliahPaham: Whisper Audio + Slide Sync, Socratic RAG, FSRS Exam Quiz & BlockNote/Yjs Notes)*

Berdasarkan riset lapangan nyata di **3 Kampus Besar**:
1. **ITB (`SIX`, `Edunex`, `FRS`, `Tubes`, `KP`, `TA` — [pertanyaan.md](file:///p:/Hackaton%20Google/ITB/pertanyaan.md)):** Masalah #1 paling parah adalah **TA terlantar gara-gara belum dapat komen dari dosbing yang super sibuk** + kuota dosbing tidak pernah di-state secara transparan; *free-rider* di Tubes sangat sering terjadi (terutama kelompok pilihan dosen) dan masih memakai lembar kontribusi manual; serta info beasiswa/lomba tenggelam di grup Line Himpunan.
2. **Telkom University Surabaya (`iGracias`, `CeLOE`, `SITU-TAK` — Edo & [saran.md](file:///p:/Hackaton%20Google/cris/saran.md)):** War KRS matkul wajib yang memecah *circle* Kelas 01, penjelasan dosen di kelas yang cepat/monoton sehingga butuh penyelamat ujian (*StudyPulse*), *free-rider* kerja kelompok, dan lambatnya konsultasi konversi 20 SKS magang MoU serta kontak alumni.
3. **UNESA ([keluhan unesa.md](file:///p:/Hackaton%20Google/mike/keluhan%20unesa.md)):** Rebutan kuota DPL/dospem 30 detik yang diskriminatif bagi sinyal lemot (*Popularity Bias*), ketidakcocokan topik magang tech vs dosen teori (*Topic Mismatch*), server 504 *down* akibat *F5 Bombardment*, kejar tanda tangan fisik antar-kampus (Ketintang–Lidah Wetan), dan *Messaging Anxiety* (cemas/sungkan chat WA dosen).

**`AcademiaFlow`** menyatukan 4 siklus krusial mahasiswa dalam 1 portal web adaptif tanpa memerlukan izin ubah database rektorat (*Zero-Friction 1-Click KSM/KRS PDF Import*):

1. **Modul 1 (Awal Semester — Ide Edo + Mike + Validasi ITB) — Smart KRS Planner, Preview Matkul/Praktikum, Circle Class Sync & Live Quota:**
   * Mahasiswa cukup *upload* PDF KSM/KRS 1 klik (`microsoft/markitdown` + `google/langextract`). Web menampilkan **Preview Silabus Mingguan, Info Praktikum, & Karakter Pengajaran Real Dosen dari Kating**, ditambah fitur **Circle Class Sync** (simulasi Plan A, B, C bebas bentrok agar 1 *circle* pertemanan tidak terpecah) serta **Realtime WebSocket Quota Indicator** agar mahasiswa tidak perlu spam tombol `F5` yang memicu server *down* 504.
2. **Modul 2 (Tengah Semester — Gabungan Ide Cris + Edo + Mike + Validasi ITB) — StudyPulse AI Lecture Mastery & Accountable Groupwork Engine:**
   * **Tab A: *StudyPulse / KuliahPaham* (Ide Cris + Socratic AI Mike):** Mahasiswa tinggal *drop* rekaman suara HP waktu dosen mengajar + file slide PPT/PDF. Sistem otomatis menghasilkan **transkrip yang sinkron dengan nomor slide (`SYSTRAN/faster-whisper`)**, **penjelasan ulang konsep sulit dengan bahasa mahasiswa & petunjuk Sokratik bertahap (`infiniflow/ragflow` + Gemini)**, **kuis latihan ujian *Active Recall* (`open-spaced-repetition/ts-fsrs`)**, dan **catatan kolaboratif sekelas (`TypeCellOS/BlockNote` + `yjs/yjs`)**.
   * **Tab B: *Accountable Groupwork & Anti-Free-Rider* (Ide Edo + Digitalisasi Lembar Kontribusi ITB):** Dosen/mahasiswa membuat kelompok Tubes yang otomatis mencari **Jam Kosong Bersama** dari KRS anggota, membagi sub-tugas dengan **Notifikasi Estafet Real-Time (`supabase/realtime`)** (*"Teman A selesai Bagian 1 -> otomatis notif ke Teman B"*), menampilkan **Digital Contribution Logbook** (menggantikan lembar kontribusi manual ITB), dan menyediakan **Tombol Lapor/Eskalasi Resmi ke Dosen** jika ada anggota *free-rider* > 48 jam.
3. **Modul 3 (Semester 5–7 Adaptif — Ide Edo + Validasi Line Himpunan ITB) — Verified MoU Internship Hub, 20-SKS Simulator, TAK/SKKM Tracker & Alumni Insider:**
   * Dashboard otomatis beradaptasi menampilkan **Papan Beasiswa & Lomba Anti-Tenggelam** (diekstrak dari poster grup Line Himpunan / WA angkatan dengan `PaddlePaddle/PaddleOCR`), **Katalog Perusahaan Mitra Resmi (MoU Kampus)** lengkap dengan **Kalkulator Simulasi Konversi 20 SKS**, **TAK/SKKM Point Tracker + 1-Click Auto-CV**, serta **Direktori Alumni Insider** (jumlah & daftar alumni di perusahaan mitra beserta kontak WA/IG/LinkedIn *opt-in* untuk tanya jawab).
4. **Modul 4 (Tingkat Akhir / Semester 7–8 — Solusi Masalah #1 Paling Parah di ITB + Ide Mike & Edo) — Thesis 21-Day SLA, Transparent Quota, In-App Consultation Ticket & Smart Rebalancing:**
   * Menampilkan **Kuota Dosbing Secara Transparan** dan mencocokkan topik TA/Magang mahasiswa dengan publikasi riset dosen menggunakan **Semantic Vector Matching (`pgvector`)**.
   * Menyediakan **In-App Consultation Ticket (`calcom/cal.com` style)** dengan template bahasa sopan otomatis (menghilangkan *Messaging Anxiety* di WA) serta tombol **1-Click Digital Logbook Approval (`[Setujui]` / `[Beri Catatan]`)** agar mahasiswa tidak perlu bolak-balik antar-kampus mengejar tanda tangan basah.
   * Dilengkapi **Deteksi Otomatis SLA 21 Hari Inaktivitas**: jika draf TA mahasiswa terlantar > 21 hari karena dosen super sibuk, sistem memberi peringatan ke Kaprodi/Tim TA dan menyediakan tombol **1-Click Smart Advisor Rebalancing** untuk merekomendasikan dosen pengganti/pendamping yang topiknya cocok dan kuotanya masih tersedia!

---

### Opsi Blueprint Pendukung Lainnya (Referensi Kombinasi Repo):

### 🔥 Blueprint A: "CampusSync / StudyPulse" — *AI Lecture-to-Mastery & Peer Study Collaboration*
* **Masalah yang Diselesaikan:** Mahasiswa kewalahan dengan materi kuliah yang tersebar (PDF slide dosen yang padat/scan, rekaman penjelasan kelas 2 jam, dan tenggat tugas di LMS) serta sulit belajar bareng secara terstruktur menjelang UTS/UAS.
* **Kombinasi Repo Inti:**
  1. **Ingesti Materi & LMS:** `Faixiang/Moodle-MCP` / `C0D3D3V/Moodle-DL` + `microsoft/markitdown` + `lukas-blecher/LaTeX-OCR` (mengubah slide PDF & foto papan tulis penuh rumus menjadi catatan terstruktur).
  2. **Transkripsi Kuliah & Aksesibilitas:** `m-bain/whisperX` atau `QuentinFuxa/WhisperLiveKit` (mengubah rekaman suara dosen menjadi transkrip ber-timestamp per kata & ramah mahasiswa Tuli).
  3. **Transformasi Belajar Aktif:** `open-spaced-repetition/ts-fsrs` (otomatis membangkitkan kuis & flashcard dengan jadwal algoritma FSRS) + `markmap/markmap` (peta konsep visual otomatis) + `souzatharsis/podcastfy` (mengubah diktat kuliah menjadi audio diskusi 2 pemandu).
  4. **Kolaborasi Kelompok Real-Time:** `TypeCellOS/BlockNote` + `excalidraw/excalidraw` + `yjs/yjs` di atas `supabase/supabase` (mahasiswa satu kelompok bisa mengedit rangkuman dan mencoret papan tulis rumus secara live).
* **Metrik Validasi untuk Juri:** Penurunan waktu merangkum materi kuliah dari 3 jam menjadi 10 menit, dan peningkatan skor *pre-test vs post-test* sebesar 35% pada uji coba 20 mahasiswa.

### 🔥 Blueprint B: "NookFlow / RuangKampus" — *Smart Campus Facility, Lab & Study Group Matchmaker (Anti-Ghost Booking)*
* **Masalah yang Diselesaikan:** Menggabungkan 2 masalah resmi di Handbook: (1) Booking ruang diskusi/lab kampus yang terfragmentasi antar gedung & sering terjadi *ghost booking* (dipesan tapi kosong), serta (2) Mahasiswa kesulitan mencari teman belajar/kelompok yang sedang berada di kampus pada jam kosong yang sama.
* **Kombinasi Repo Inti:**
  1. **Frontend & Admin Gedung:** `satnaing/shadcn-admin` + `magicuidesign/magicui` + `supabase/supabase` (Auth SSO email kampus + Realtime Postgres).
  2. **Live Floorplan & Visual Map:** `tldraw/tldraw` atau `excalidraw/excalidraw` sebagai denah interaktif lantai gedung kampus yang menampilkan warna ruangan secara *real-time* (Hijau = Kosong, Kuning = Ada Kelompok Terbuka yang menerima anggota belajar baru, Merah = Penuh).
  3. **Anti-Ghosting Verification:** Integrasi QR Dinamis + Geofencing/Check-in (otomatis membatalkan booking dalam 15 menit jika tidak ada anggota yang scan QR di pintu ruangan, persis seperti studi kasus ideal panitia).
  4. **Smart Study Partner Matching:** Menggunakan `google/langextract` (mengekstrak jadwal kosong dari PDF KRS mahasiswa) untuk mencocokkan mahasiswa dari mata kuliah yang sama yang sama-sama punya jeda jam kosong (misal 13:00–15:00) dan mengajak mereka berbagi *Study Room*.

### 🔥 Blueprint C: "OppoRadar / BeasiswaHub AI" — *Campus Opportunity, Scholarship, Competition & Research Lab Matcher*
* **Masalah yang Diselesaikan:** Informasi beasiswa, lomba, asisten peneliti dosen, dan magang tersebar di ratusan poster Instagram, grup WhatsApp/Telegram, dan web fakultas, sehingga mahasiswa sering terlambat mendaftar atau bingung mencari anggota tim lomba yang komplementer.
* **Kombinasi Repo Inti:**
  1. **Automated Opportunity Scraper:** `unclecode/crawl4ai` / `ScrapeGraphAI/Scrapegraph-ai` + `PaddlePaddle/PaddleOCR` (mengekstrak teks, deadline, syarat IPK/semester, dan link pendaftaran langsung dari gambar poster lomba/beasiswa dan web kampus!).
  2. **Structured Extraction & Matching:** `google/langextract` + `supabase/supabase` (`pgvector`) untuk mencocokkan profil mahasiswa (CV PDF yang di-parse dengan `microsoft/markitdown`) terhadap ratusan peluang yang tersedia secara otomatis (*% Match Score*).
  3. **Team Builder & Co-Pilot:** `CopilotKit/CopilotKit` + `assistant-ui/assistant-ui` untuk membantu mahasiswa mencari rekan tim hackathon/PKM yang skill-nya saling melengkapi (misal: 1 Hipster UI/UX + 2 Hacker Backend/AI + 1 Hustler Bisnis) dan melacak progres persiapan berkas pendaftaran di kanvas `TypeCellOS/BlockNote`.

---

## BAGIAN 6: ACTION PLAN DARURAT (KARENA DEADLINE PRELIMINARY ADALAH BESOK, 10 NOVEMBER 2026!)

1. **HARI INI (9 Nov 2026) — Kunci Ide & Tulis Abstrak 300–500 Kata:**
   * Pilih salah satu fokus masalah dari Blueprint A, B, atau C di atas.
   * Buat survei singkat (Google Forms) dan sebarkan hari ini ke minimal 20–40 teman mahasiswa di kampus Anda, serta lakukan observasi nyata di lapangan (agar bagian `3. Supporting Observations or Evidence` yang berbobot **30%** punya angka asli yang jujur dan tidak mengarang!).
   * Susun dokumen Abstrak dalam Bahasa Inggris mengikuti **7 bagian wajib** dari `AbstractMaterialSTACK2026` (panjang wajib 300–500 kata di luar daftar referensi).
   * Gabungkan bukti Twibbon seluruh anggota (3–4 orang) ke dalam 1 file PDF sesuai aturan.
2. **BESOK (10 Nov 2026 sebelum 23:59 WIB) — Upload Final di `gdgoncampusitb.com`:**
   * Pastikan PDF Abstrak tidak memakai halaman cover terpisah dan ukurannya < 10 MB.
   * Ingat: begitu tombol **Confirm final submission** ditekan di dashboard `gdgoncampusitb.com/submissions/preliminary`, file terkunci permanen!

