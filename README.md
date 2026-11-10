# STACK 2026 by GDGoC ITB — Workspace Riset & Blueprint Tim `Pray First`
## Kasus 1: Kampus dan Pembelajaran yang Lebih Cerdas (*Smarter Campus and Learning*)

* **Team Name:** `Pray First`
* **Members:**
  1. **Allfridhoo Prima Anjaynata Saragi** *(Team Leader — Telkom University Surabaya)*
  2. **Mikhael Yuli Ananda Elvan Permana** *(Member — Universitas Negeri Surabaya / UNESA)*
  3. **Nathanael Christian Putra** *(Member — Telkom University Surabaya)*

Repositori ini memuat seluruh materi riset 3 kampus (**ITB, Telkom University Surabaya, dan UNESA**), blueprint teknis, draf abstrak resmi siap submit, skema database, dan pembagian kerja tim untuk kompetisi **STACK 2026 Hackathon oleh GDG on Campus Institut Teknologi Bandung**.

---

## 📁 Struktur Folder Workspace

```
p:\Hackaton Google\
├── .gitignore
├── README.md
├── ITB/                          # Hasil wawancara & validasi lapangan asli dari mahasiswa ITB
│   └── pertanyaan.md             # Bukti validasi masalah TA terlantar, Tubes free-rider, & Line himpunan
├── cris/                         # Folder kerja & riset Cris (Telkom University Surabaya - Semester 3)
│   ├── saran.md                  # Konsep KuliahPaham / StudyPulse & 7 repo inti
│   ├── Permasalah saya.md        # Diagnosis masalah pembelajaran di kelas & penurunan IPK
│   └── 100_repositori_github_penyelamat_akademik.md
├── edo/                          # Folder master blueprint, arsitektur, database, & submissions (Tim Inti)
│   ├── MASTER_BLUEPRINT_STACK2026.md
│   ├── STACK2026_READY_TO_SUBMIT_ABSTRACTS_AND_ARCHITECTURE.md
│   ├── STACK2026_PROPOSAL_VIDEO_AND_DECK_TEMPLATES.md
│   ├── supabase_schema.sql       # Skema Database PostgreSQL + pgvector + Realtime Handover Triggers
│   ├── generate_abstract_pdf.py
│   ├── generate_gradsync_pdf.py  # Generator PDF Abstrak Resmi Siap Submit (Tim Pray First)
│   ├── submissions/              # Output PDF & HTML Abstrak Resmi (FINAL_AcademiaFlow_Abstract.pdf)
│   ├── Riset google/             # Data riset kompetisi & bedah aturan handbook
│   └── omninook-app/             # Fondasi awal project Next.js
└── mike/                         # Folder kerja & riset Mike (Universitas Negeri Surabaya / UNESA)
    ├── keluhan unesa.md          # Data observasi riil masalah birokrasi, dospem, server 504, & WA anxiety
    ├── Proposal & Tech Blueprint Hackathon GDG ITB.md # Ide ScaffoldAI (Socratic Tutor)
    └── Koleksi 100 Repositori GitHub untuk Kasus 1.md # Direktori 100 repo open-source pendukung
```

---

## 🌟 Konsep Final Terkunci: `AcademiaFlow` ("1 Portal for Everything")
Platform pendamping siklus akademik mahasiswa berbasis *Zero-Friction 1-Click PDF Schedule Import* yang menyatukan 100% ide **Edo + Mike + Cris** dan divalidasi langsung oleh studi kasus **ITB**:
1. **Modul 1 (Awal Semester — Ide Edo + Mike + Validasi ITB):** *Smart KRS Planner, Weekly Syllabus/Practicum Preview, Circle Class Sync & Live WebSocket Quota Indicator (Anti-F5 Server Crash)*.
2. **Modul 2 (Tengah Semester — Ide Cris + Edo + Mike + Validasi ITB):**
   * **Tab A (*StudyPulse / KuliahPaham*):** Drop rekaman suara dosen + slide PDF -> transkrip sinkron nomor slide (`faster-whisper`), penjelasan ulang bahasa mahasiswa & Socratic hints (`RAGFlow` + Gemini), kuis latihan ujian *Active Recall* (`ts-fsrs`), dan catatan kolaboratif sekelas (`BlockNote` + `Yjs`).
   * **Tab B (*Accountable Groupwork Engine*):** Auto-cari jam kosong bersama, pembagian sub-tugas dengan *Realtime Relay Handover Notification*, *Digital Contribution Logbook* (menggantikan lembar kontribusi manual ITB), & tombol lapor/eskalasi resmi ke dosen.
3. **Modul 3 (Semester 5–7 — Ide Edo + Validasi ITB):** *Adaptive Opportunity Hub* (papan beasiswa/lomba anti-tenggelam dari poster Line Himpunan/WA), katalog *Verified Campus MoU Internships* (simulasi konversi 20 SKS), *TAK/SKKM Tracker*, & *Alumni Insider Directory* (WA/IG/LinkedIn).
4. **Modul 4 (Tingkat Akhir — Solusi Masalah #1 Terparah di ITB + Ide Mike & Edo):** Transparansi kuota dosbing & *Semantic Topic Matching*, *In-App Consultation Ticket* (anti-cemas chat WA dosen), *1-Click Digital Logbook Approval* (anti-bolak-balik antar-kampus), serta *21-Day Inactivity SLA Tracker & 1-Click Smart Advisor Rebalancing* untuk Kaprodi.
