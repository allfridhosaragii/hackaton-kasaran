# 📚 ENSIKLOPEDIA 100 REPOSITORI GITHUB TERBAIK: SISTEM PENYELAMAT PEMAHAMAN KULIAH & IPK MAHASISWA

Dokumen ini memuat kurasi **100 repositori open-source teruji** (*high-stars*, aktif, dan siap pakai) yang dikelompokkan ke dalam **10 kategori arsitektur teknologi**. Ekosistem ini ditujukan untuk membangun solusi mandiri mahasiswa, platform tutor sebaya (*peer mentoring*), pemrosesan materi kuliah, hingga otomasi persiapan ujian.

---

## DAFTAR ISI KATALOG REPOSITORI (10 KATEGORI)

1. [Transkripsi Audio Dosen, Speech-to-Text & Diarization (10 Repo)](#kategori-1-transkripsi-audio-dosen-speech-to-text--diarization)
2. [Ekstraksi Dokumen, OCR Papan Tulis & Formulasi LaTeX (10 Repo)](#kategori-2-ekstraksi-dokumen-ocr-papan-tulis--formulasi-latex)
3. [AI Tutoring, RAG Pembelajaran & Asisten Socratic (10 Repo)](#kategori-3-ai-tutoring-rag-pembelajaran--asisten-socratic)
4. [Memory Layer, Knowledge Graph & Visualisasi Konsep (10 Repo)](#kategori-4-memory-layer-knowledge-graph--visualisasi-konsep)
5. [Active Recall, Spaced Repetition (FSRS) & Gamifikasi Ujian (10 Repo)](#kategori-5-active-recall-spaced-repetition-fsrs--gamifikasi-ujian)
6. [Kolaborasi Mahasiswa Real-Time, Editor & Kanvas Rumus (10 Repo)](#kategori-6-kolaborasi-mahasiswa-real-time-editor--kanvas-rumus)
7. [Live Class Backchannel, Tanya-Jawab Anonim & WebRTC (10 Repo)](#kategori-7-live-class-backchannel-tanya-jawab-anonim--webrtc)
8. [Integrasi LMS Kampus, Kalender Tugas & Notifikasi (10 Repo)](#kategori-8-integrasi-lms-kampus-kalender-tugas--notifikasi)
9. [Scraping Materi Terbuka, Bank Soal & Paper Akademik (10 Repo)](#kategori-9-scraping-materi-terbuka-bank-soal--paper-akademik)
10. [Full-Stack Accelerators, Database Reaktif & Dashboard Analitik (10 Repo)](#kategori-10-full-stack-accelerators-database-reaktif--dashboard-analitik)

---

## KATEGORI 1: TRANSKRIPSI AUDIO DOSEN, SPEECH-TO-TEXT & DIARIZATION

Mengubah rekaman suara dosen berdurasi 2–3 jam yang monoton menjadi teks bersih ber-timestamp, memisahkan suara dosen vs pertanyaan mahasiswa, dan memudahkan pencarian poin penting.

1. **[openai/whisper](https://github.com/openai/whisper)** (Python) — Standar industri pengenalan suara (ASR) multi-bahasa dengan ketahanan tinggi terhadap aksen dan istilah teknis.
2. **[m-bain/whisperX](https://github.com/m-bain/whisperX)** (Python) — ASR dengan *word-level timestamps* dan *speaker diarization* untuk memetakan siapa yang sedang berbicara di kelas.
3. **[ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp)** (C/C++) — Implementasi Whisper super ringan berbasis C/C++ yang dapat berjalan langsung di laptop mahasiswa tanpa kartu grafis khusus.
4. **[SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper)** (Python) — Reimplementasi Whisper menggunakan CTranslate2, menghasilkan transkripsi hingga 4x lebih cepat dengan memori lebih hemat.
5. **[QuentinFuxa/WhisperLiveKit](https://github.com/QuentinFuxa/WhisperLiveKit)** (Python) — Transkripsi streaming real-time langsung saat perkuliahan berlangsung di dalam ruang kelas.
6. **[chidiwilliams/buzz](https://github.com/chidiwilliams/buzz)** (Python) — Aplikasi desktop siap pakai untuk transkripsi dan penerjemahan audio kuliah secara offline.
7. **[Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily)** (Rust/TypeScript) — Asisten pencatat audio kuliah lokal open-source dengan ringkasan otomatis dan penanda topik bahasan.
8. **[Vaibhavs10/insanely-fast-whisper](https://github.com/Vaibhavs10/insanely-fast-whisper)** (Python) — Pipeline akselerasi Hugging Face yang mampu mentranskripsi rekaman audio 2 jam dalam waktu di bawah 2 menit.
9. **[thewh1teagle/vibe](https://github.com/thewh1teagle/vibe)** (TypeScript/Rust) — Aplikasi transkripsi audio/video multiplatform dengan antarmuka modern dan penandaan segmen.
10. **[nexmoe/VidBee](https://github.com/nexmoe/VidBee)** (TypeScript) — Mengunduh rekaman video kelas online, mentranskripsi dialog, serta memproduksi ringkasan dan peta pikiran otomatis.

---

## KATEGORI 2: EKSTRAKSI DOKUMEN, OCR PAPAN TULIS & FORMULASI LATEX

Membaca slide presentasi dosen yang padat, mengonversi foto papan tulis penuh coretan menjadi teks digital, dan mengekstrak rumus matematika kompleks.

11. **[microsoft/markitdown](https://github.com/microsoft/markitdown)** (Python) — Konversi dokumen serbaguna (PPTX, PDF, DOCX, XLSX, gambar) menjadi format Markdown terstruktur untuk LLM.
12. **[PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)** (Python) — Toolkit OCR multi-bahasa ultra-akurat untuk mendeteksi teks pada slide dosen dan foto papan tulis buram.
13. **[opendatalab/MinerU](https://github.com/opendatalab/MinerU)** (Python) — Mesin pemroses dokumen akademik kompleks: ekstraksi rumus, tabel, dan diagram dari diktat PDF.
14. **[lukas-blecher/LaTeX-OCR](https://github.com/lukas-blecher/LaTeX-OCR)** (Python) — `pix2tex`: Mengubah screenshot atau foto rumus matematika di papan tulis menjadi kode LaTeX instan.
15. **[docling-project/docling](https://github.com/docling-project/docling)** (Python) — Parser dokumen dari IBM untuk pemahaman layout akademik tingkat lanjut dan parsing formula.
16. **[datalab-to/marker](https://github.com/datalab-to/marker)** (Python) — Mengonversi buku teks perkuliahan dan PDF materi menjadi Markdown bersih tanpa kehilangan struktur hirarki.
17. **[Stirling-Tools/Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF)** (Java/TypeScript) — Suite utilitas lengkap untuk OCR, manipulasi, pemisahan, dan kompresi PDF modul kuliah.
18. **[PDFMathTranslate/PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate)** (Python) — Menerjemahkan buku teks asing ke Bahasa Indonesia dengan mempertahankan posisi rumus dan tabel matematika secara presisi.
19. **[facebookresearch/nougat](https://github.com/facebookresearch/nougat)** (Python) — Model neural dari Meta AI untuk membaca dokumen saintifik dan memformatnya kembali ke representasi teks/LaTeX.
20. **[datalab-to/surya](https://github.com/datalab-to/surya)** (Python) — Model deteksi urutan baca, analisis tata letak multi-kolom, dan segmentasi tabel untuk dokumen silabus perkuliahan.

---

## KATEGORI 3: AI TUTORING, RAG PEMBELAJARAN & ASISTEN SOCRATIC

Membangun "asisten dosen virtual" yang menjawab keraguan mahasiswa, membimbing langkah demi langkah, dan menurunkan konsep rumit menjadi analogi sederhana.

21. **[arc53/DocsGPT](https://github.com/arc53/DocsGPT)** (Python) — Platform RAG open-source untuk berdialog langsung dengan silabus, buku teks rujukan, dan bank modul kuliah.
22. **[infiniflow/ragflow](https://github.com/infiniflow/ragflow)** (Go/Python) — Mesin RAG berbasis *deep document understanding* dengan kutipan nomor halaman presisi pada setiap jawaban.
23. **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** (Python) — Sistem bimbingan belajar personal berbasis kurikulum universitas yang berfokus pada pedagogi interaktif.
24. **[langgenius/dify](https://github.com/langgenius/dify)** (Python/TypeScript) — Framework orkestrasi alur kerja AI untuk membangun bot pembimbing Socratic dan penilai tugas mahasiswa.
25. **[langflow-ai/langflow](https://github.com/langflow-ai/langflow)** (Python) — Antarmuka visual berbasis node untuk merancang alur tanya-jawab materi kuliah secara modular.
26. **[Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm)** (JavaScript) — Workspace full-stack desktop/web untuk mengelompokkan dokumen per mata kuliah ke dalam ruang chat terpisah.
27. **[open-webui/open-webui](https://github.com/open-webui/open-webui)** (Svelte/Python) — Antarmuka obrolan AI serbaguna dengan manajemen peran pengguna, dokumen RAG, dan integrasi multi-model.
28. **[khoj-ai/khoj](https://github.com/khoj-ai/khoj)** (Python) — Asisten *Second Brain* personal yang dapat mencari jawaban dari catatan lokal maupun referensi daring.
29. **[MODSetter/SurfSense](https://github.com/MODSetter/SurfSense)** (Python) — Alternatif NotebookLM open-source untuk merangkum dan mengeksplorasi materi pelajaran berbasis privasi.
30. **[binary-husky/gpt_academic](https://github.com/binary-husky/gpt_academic)** (Python) — Antarmuka khusus untuk analisis mendalam modul akademik, bedah kode tugas praktikum, dan laporan ilmiah.

---

## KATEGORI 4: MEMORY LAYER, KNOWLEDGE GRAPH & VISUALISASI KONSEP

Memetakan hubungan antar-bab yang sering dilewati dosen, menyimpan riwayat kesulitan belajar mahasiswa, dan memvisualisasikan peta konsep besar mata kuliah.

31. **[mem0ai/mem0](https://github.com/mem0ai/mem0)** (Python) — Lapisan memori cerdas untuk mencatat kelemahan spesifik mahasiswa lintas sesi belajar.
32. **[microsoft/graphrag](https://github.com/microsoft/graphrag)** (Python) — RAG berbasis Knowledge Graph modular untuk menghubungkan konsep dari materi awal hingga materi akhir semester.
33. **[HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)** (Python) — Arsitektur Graph RAG berkecepatan tinggi untuk menghubungkan entitas teori dan rumus secara terstruktur.
34. **[markmap/markmap](https://github.com/markmap/markmap)** (TypeScript) — Mengonversi ringkasan Markdown kuliah menjadi Mindmap hierarkis interaktif langsung di peramban.
35. **[mermaid-js/mermaid](https://github.com/mermaid-js/mermaid)** (TypeScript) — Pembangkit diagram alir, grafik urutan logika, dan peta alur konsep perkuliahan berbasis sintaks teks.
36. **[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)** (Python) — Mengubah repositori kode praktikum dan dokumen teori menjadi graf berbobot relasi eksplisit.
37. **[varunshenoy/GraphGPT](https://github.com/varunshenoy/GraphGPT)** (JavaScript) — Ekstrapolasi teks catatan kuliah bebas menjadi grafik konsep visual secara langsung di layar.
38. **[neo4j-labs/llm-graph-builder](https://github.com/neo4j-labs/llm-graph-builder)** (Python) — Pembangun graf otomatis dari file PDF kuliah ke dalam basis data grafik Neo4j.
39. **[logseq/logseq](https://github.com/logseq/logseq)** (Clojure/JS) — Platform manajemen pengetahuan berbasis grafik relasi dua arah (*bidirectional links*) dan *outliner*.
40. **[siyuan-note/siyuan](https://github.com/siyuan-note/siyuan)** (TypeScript/Go) — Sistem manajemen basis pengetahuan terstruktur dengan fokus pada hierarki dokumen dan visualisasi keterkaitan blok data.

---

## KATEGORI 5: ACTIVE RECALL, SPACED REPETITION (FSRS) & GAMIFIKASI UJIAN

Melatih mahasiswa menghadapi soal ujian analitis melalui pengulangan terjadwal, algoritma retensi memori, dan simulasi bank soal.

41. **[open-spaced-repetition/ts-fsrs](https://github.com/open-spaced-repetition/ts-fsrs)** (TypeScript) — Library algoritma *Free Spaced Repetition Scheduler* untuk penjadwalan kuis adaptif.
42. **[ankitects/anki](https://github.com/ankitects/anki)** (Rust/Python) — Perangkat lunak kartu memori (*flashcard*) berbasis pengulangan berjarak paling teruji di dunia akademik.
43. **[open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki)** (Python) — Optimizer machine learning untuk menghitung parameter retensi memori mahasiswa berdasarkan riwayat jawaban.
44. **[andymatuschak/orbit](https://github.com/andymatuschak/orbit)** (TypeScript) — Platform untuk menyisipkan pertanyaan pengingat aktif langsung di sela-sela bacaan teks modul kuliah.
45. **[st3v3nmw/obsidian-spaced-repetition](https://github.com/st3v3nmw/obsidian-spaced-repetition)** (TypeScript) — Mesin review flashcard dari teks catatan harian untuk memitigasi kurva lupa (*forgetting curve*).
46. **[nagisanzenin/engram](https://github.com/nagisanzenin/engram)** (Python) — Platform belajar berbasis bukti (*evidence-based learning*) yang memaksa pembuktian pemahaman dari prinsip pertama (*first principles*).
47. **[ankidroid/Anki-Android](https://github.com/ankidroid/Anki-Android)** (Kotlin/Java) — Klien Android untuk review flashcard rumus kapan saja secara mobile.
48. **[designfuchen/word-atlas](https://github.com/designfuchen/word-atlas)** (TypeScript) — Implementasi web modern untuk review materi istilah akademik berbasis algoritma FSRS.
49. **[echo-loop/Echo-Loop](https://github.com/echo-loop/Echo-Loop)** (Dart/Flutter) — Aplikasi latihan pemahaman audio berbasis algoritma review pengulangan bertahap.
50. **[modocache/MDCSwipeToChoose](https://github.com/modocache/MDCSwipeToChoose)** (Objective-C) — Komponen UI interaktif geser kartu (swipe kanan/kiri) untuk simulasi kuis cepat antar-mahasiswa.

---

## KATEGORI 6: KOLABORASI MAHASISWA REAL-TIME, EDITOR & KANVAS RUMUS

Memfasilitasi kerja kelompok, penulisan rangkuman bareng satu angkatan, dan coret-coret papan tulis virtual saat sesi tutor sebaya (*peer instruction*).

51. **[excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)** (TypeScript) — Papan tulis virtual kolaboratif bergaya sketsa tangan untuk membedah rumus dan diagram secara live.
52. **[tldraw/tldraw](https://github.com/tldraw/tldraw)** (TypeScript) — SDK kanvas tak terbatas (*infinite canvas*) untuk membangun papan kerja visual interaktif.
53. **[TypeCellOS/BlockNote](https://github.com/TypeCellOS/BlockNote)** (TypeScript) — Rich-text editor berbasis blok (Notion-style) yang mendukung kolaborasi real-time multi-pengguna.
54. **[yjs/yjs](https://github.com/yjs/yjs)** (JavaScript) — Framework CRDT terdepan di dunia untuk sinkronisasi dokumen bersama tanpa tabrakan data (*zero conflict*).
55. **[toeverything/AFFiNE](https://github.com/toeverything/AFFiNE)** (TypeScript) — Penggabungan ruang kerja kanvas bebas dan dokumen blok untuk kolaborasi persiapan ujian kelompok.
56. **[AppFlowy-IO/AppFlowy](https://github.com/AppFlowy-IO/AppFlowy)** (Flutter/Rust) — Alternatif Notion open-source untuk manajemen pembagian materi belajar kelompok.
57. **[outline/outline](https://github.com/outline/outline)** (TypeScript) — Basis pengetahuan dan wiki kelompok super cepat untuk menghimpun catatan resmi satu kelas.
58. **[plait-board/drawnix](https://github.com/plait-board/drawnix)** (TypeScript) — Papan kanvas all-in-one yang mengintegrasikan mindmap, flowchart, dan coretan diagram teknis.
59. **[overleaf/overleaf](https://github.com/overleaf/overleaf)** (TypeScript/JavaScript) — Editor LaTeX kolaboratif berbasis web untuk penulisan laporan praktikum dan pembahasan tugas hitungan bersama.
60. **[docmost/docmost](https://github.com/docmost/docmost)** (TypeScript) — Platform dokumentasi dan catatan tim kolaboratif real-time dengan editor teks bersih.

---

## KATEGORI 7: LIVE CLASS BACKCHANNEL, TANYA-JAWAB ANONIM & WEBRTC

Menghilangkan rasa takut bertanya kepada dosen yang intimidatif melalui forum tanya anonim di kelas dan memfasilitasi panggilan diskusi belajar antar-teman.

61. **[livekit/livekit](https://github.com/livekit/livekit)** (Go/TypeScript) — Infrastruktur WebRTC real-time untuk membangun ruang belajar audio-video kelompok dengan latensi rendah.
62. **[jitsi/jitsi-meet](https://github.com/jitsi/jitsi-meet)** (JavaScript/TypeScript) — Platform video konferensi open-source siap pakai untuk sesi asistensi online tutor sebaya.
63. **[tinode/chat](https://github.com/tinode/chat)** (Go/JavaScript) — Server obrolan instan ringan untuk forum backchannel kelas dan tanya-jawab tanpa identitas.
64. **[screego/server](https://github.com/screego/server)** (Go/TypeScript) — Berbagi layar (*screen sharing*) beresolusi tinggi khusus untuk asistensi koding atau bedah soal matematika.
65. **[netless-io/flat](https://github.com/netless-io/flat)** (TypeScript) — Ruang kelas virtual komprehensif dengan papan tulis interaktif, video, dan manajemen dokumen kuliah.
66. **[pion/webrtc](https://github.com/pion/webrtc)** (Go) — Implementasi WebRTC murni untuk membangun kanal audio latensi ultra-rendah antar-anggota kelompok belajar.
67. **[peers/peerjs](https://github.com/peers/peerjs)** (TypeScript) — Pembungkus API WebRTC sederhana untuk membangun fitur kolaborasi P2P browser-to-browser.
68. **[RocketChat/Rocket.Chat](https://github.com/RocketChat/Rocket.Chat)** (TypeScript) — Platform komunikasi tim untuk membangun ruang diskusi terpisah per mata kuliah dengan thread tanya-jawab.
69. **[localsend/localsend](https://github.com/localsend/localsend)** (Dart/Flutter) — Berbagi file modul dan rekaman kuliah lintas perangkat tanpa internet melalui jaringan Wi-Fi lokal kampus.
70. **[SnapDrop/snapdrop](https://github.com/SnapDrop/snapdrop)** (JavaScript) — Berbagi dokumen instan antar peramban mahasiswa yang berada di ruang kelas yang sama via WebRTC.

---

## KATEGORI 8: INTEGRASI LMS KAMPUS, KALENDER TUGAS & NOTIFIKASI

Mengambil jadwal tugas, modul, dan silabus dari portal universitas secara otomatis agar mahasiswa tidak ketinggalan tenggat akibat minimnya instruksi dosen.

71. **[Faixiang/Moodle-MCP](https://github.com/Faixiang/Moodle-MCP)** (Python) — Server Model Context Protocol untuk membaca pengumuman, materi, dan tenggat tugas langsung dari Moodle kampus.
72. **[C0D3D3V/Moodle-DL](https://github.com/C0D3D3V/Moodle-DL)** (Python) — Utilitas otomatis untuk mengunduh semua slide, PDF, dan berkas tugas dari portal akademik universitas.
73. **[Berserk-hub150/moodle-ai-skill-navigator](https://github.com/Berserk-hub150/moodle-ai-skill-navigator)** (PHP) — Plugin asisten navigasi materi kuliah berbasis AI yang diintegrasikan ke dalam ekosistem Moodle.
74. **[moodle/moodle](https://github.com/moodle/moodle)** (PHP) — Platform dasar Learning Management System yang digunakan oleh mayoritas perguruan tinggi.
75. **[instructure/canvas-lms](https://github.com/instructure/canvas-lms)** (Ruby/JavaScript) — Platform LMS modern dengan dokumentasi API terbuka untuk sinkronisasi jadwal kuliah dan tugas.
76. **[classroomio/classroomio](https://github.com/classroomio/classroomio)** (TypeScript/Svelte) — Platform kelas virtual modern berbasis Supabase untuk pembuatan kursus kilat persiapan ujian (*crash course*).
77. **[openedx/openedx-platform](https://github.com/openedx/openedx-platform)** (Python) — Platform kursus daring terbuka skala global (edX) untuk referensi struktur kurikulum baku.
78. **[oppia/oppia](https://github.com/oppia/oppia)** (Python/TypeScript) — Sistem pembelajaran terpandu dengan evaluasi adaptif berdasarkan kesalahan jawaban mahasiswa.
79. **[francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis)** (PHP) — Sistem manajemen informasi akademik untuk pelacakan absensi dan kalender evaluasi belajar.
80. **[n8n-io/n8n](https://github.com/n8n-io/n8n)** (TypeScript) — Platform alur kerja otomatisasi untuk menarik pengumuman tugas dari portal kampus dan mengirimkan notifikasi ke Telegram/WhatsApp.

---

## KATEGORI 9: SCRAPING MATERI TERBUKA, BANK SOAL & PAPER AKADEMIK

Mencari bahan penjelasan alternatif dari universitas kelas dunia saat penjelasan dosen di kelas tidak memadai.

81. **[dzhng/deep-research](https://github.com/dzhng/deep-research)** (TypeScript) — Agen penjelajah web otomatis untuk mencari materi alternatif, pembahasan soal, dan literatur akademik.
82. **[firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)** (TypeScript) — Mesin pengubah halaman web artikel edukasi dan modul online menjadi format Markdown bersih.
83. **[unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)** (Python) — Web crawler open-source berkecepatan tinggi yang dioptimalkan untuk ekstraksi data bagi model bahasa besar.
84. **[ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai)** (Python) — Pipeline ekstraksi data berbasis grafik untuk mengambil arsip soal latihan dari portal web terbuka.
85. **[Alibaba-NLP/DeepResearch](https://github.com/Alibaba-NLP/DeepResearch)** (Python) — Agen riset ilmiah untuk menelusuri literatur pendukung dan penjelasan konsep teoritis.
86. **[langchain-ai/local-deep-researcher](https://github.com/langchain-ai/local-deep-researcher)** (Python) — Agen riset akademik mandiri yang berjalan sepenuhnya secara lokal di komputer pribadi.
87. **[Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar)** (Python) — Asisten riset terstruktur untuk mengeksplorasi eksperimen dan kajian teori akademik.
88. **[zaidmukaddam/scira](https://github.com/zaidmukaddam/scira)** (TypeScript) — Mesin pencari AI minimalis dengan fokus pada pencarian dokumen ilmiah dan referensi video YouTube edukatif.
89. **[mukulpatnaik/researchgpt](https://github.com/mukulpatnaik/researchgpt)** (Python) — Dialog interaktif berbasis LLM terhadap berkas PDF paper penelitian dan modul ilmiah.
90. **[54yyyu/zotero-mcp](https://github.com/54yyyu/zotero-mcp)** (Python) — Menghubungkan basis data kepustakaan jurnal Zotero mahasiswa dengan model AI melalui protokol MCP.

---

## KATEGORI 10: FULL-STACK ACCELERATORS, DATABASE REAKTIF & DASHBOARD ANALITIK

Fondasi pengembangan aplikasi tangguh (*anti-crash* saat demonstrasi) untuk memvisualisasikan data peningkatan nilai mahasiswa dan mengelola sistem belajar terpadu.

91. **[supabase/supabase](https://github.com/supabase/supabase)** (TypeScript/Postgres) — Backend-as-a-Service lengkap: autentikasi mahasiswa, database PostgreSQL reaktif, `pgvector`, dan penyimpanan file modul.
92. **[pubkey/rxdb](https://github.com/pubkey/rxdb)** (TypeScript) — Database lokal reaktif untuk aplikasi web/mobile agar mahasiswa tetap bisa belajar saat jaringan internet kampus terputus.
93. **[appwrite/appwrite](https://github.com/appwrite/appwrite)** (TypeScript) — Platform BaaS modular untuk manajemen user, database dokumen, dan fungsi komputasi serverless.
94. **[fastapi/full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template)** (Python/TypeScript) — Template arsitektur web modern (FastAPI + React + Tailwind + PostgreSQL) untuk pipeline AI/OCR perkuliahan.
95. **[CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit)** (TypeScript) — Framework untuk mengintegrasikan agen AI langsung ke dalam komponen UI aplikasi React/Next.js.
96. **[PostHog/posthog](https://github.com/PostHog/posthog)** (Python/TypeScript) — Platform analitik perilaku pengguna untuk mengukur durasi belajar dan kenaikan skor latihan soal mahasiswa.
97. **[satnaing/shadcn-admin](https://github.com/satnaing/shadcn-admin)** (TypeScript) — Template dashboard admin berbasis React dan Shadcn UI untuk memantau nilai dan rekapitulasi evaluasi kelas.
98. **[udecode/plate](https://github.com/udecode/plate)** (TypeScript) — Kerangka kerja editor teks modular berbasis React untuk membangun aplikasi catatan belajar pintar.
99. **[assistant-ui/assistant-ui](https://github.com/assistant-ui/assistant-ui)** (TypeScript) — Komponen antarmuka chat AI profesional siap pakai untuk aplikasi bimbingan belajar web.
100. **[DavidHDev/react-bits](https://github.com/DavidHDev/react-bits)** (JavaScript/React) — Koleksi animasi dan komponen antarmuka modern untuk menyusun platform edukasi yang memotivasi mahasiswa.

---

## MATRIKS PEMETAAN MASALAH KULIAH DENGAN KOMBINASI STACK

Berikut adalah panduan praktis memilih kombinasi repositori di atas untuk mengatasi masalah spesifik di kampus:

| Kendala di Kampus | Dampak Negatif | Kombinasi Repositori Rekomendasi | Output Solusi Nyata |
| :--- | :--- | :--- | :--- |
| **Dosen sekadar membaca slide tanpa penjelasan** | Mahasiswa bosan, tidak menangkap konsep dasar, dan mengantuk di kelas | `m-bain/whisperX` + `opendatalab/MinerU` + `souzatharsis/podcastfy` | Audio kuliah diubah menjadi transkrip terindeks + podcast penjelasan konsep santai |
| **Dosen enggan menurunkan rumus di papan tulis** | Mahasiswa gagal di ujian hitungan karena tidak tahu asal rumus | `lukas-blecher/LaTeX-OCR` + `excalidraw/excalidraw` + `HKUDS/DeepTutor` | Konversi foto coretan papan tulis ke LaTeX + panduan penurunan rumus langkah-demi-langkah |
| **Mahasiswa takut/malu bertanya di kelas** | Kebingungan menumpuk hingga menjelang ujian akhir | `tinode/chat` + `TypeCellOS/BlockNote` + `supabase/supabase` | Papan pertanyaan kelas live dan anonim yang dapat dijawab oleh asisten atau tutor sebaya |
| **Materi kuliah terlalu banyak dan cepat lupa** | Nilai UTS/UAS anjlok karena sistem kebut semalam (*cramming*) | `open-spaced-repetition/ts-fsrs` + `markmap/markmap` + `ankitects/anki` | Pembuatan peta pikiran visual materi semesteran + kuis review otomatis berbasis kurva lupa |
| **Soal ujian jauh lebih sulit dari contoh di kelas** | Banyak mahasiswa mendapat nilai D atau E | `dzhng/deep-research` + `infiniflow/ragflow` + `arc53/DocsGPT` | Bank soal prediktif dengan tingkat kesulitan bertahap dari materi terbuka universitas top |
