# STACK 2026 by GDGoC ITB — Workspace Riset & Blueprint Tim
## Kasus 1: Kampus dan Pembelajaran yang Lebih Cerdas (*Smarter Campus and Learning*)

Repositori ini memuat seluruh materi riset, blueprint teknis, draf abstrak resmi, skema database, dan pembagian riset anggota tim untuk kompetisi **STACK 2026 Hackathon oleh GDG on Campus Institut Teknologi Bandung**.

---

## 📁 Struktur Folder Workspace

```
p:\Hackaton Google\
├── .gitignore
├── README.md
├── cris/                         # Folder kerja & riset Cris (Telkom University Surabaya - Semester 3)
│   └── .gitkeep
├── edo/                          # Folder master blueprint, arsitektur, database, & submissions (Edo / Tim Inti)
│   ├── MASTER_BLUEPRINT_STACK2026.md
│   ├── STACK2026_READY_TO_SUBMIT_ABSTRACTS_AND_ARCHITECTURE.md
│   ├── STACK2026_PROPOSAL_VIDEO_AND_DECK_TEMPLATES.md
│   ├── supabase_schema.sql       # Skema Database PostgreSQL + pgvector + Realtime Handover Triggers
│   ├── generate_abstract_pdf.py
│   ├── generate_gradsync_pdf.py  # Generator PDF Abstrak Resmi Siap Submit
│   ├── submissions/              # Output PDF & HTML Abstrak (300-500 kata, 7 Bagian Wajib)
│   ├── Riset google/             # Data riset kompetisi & bedah aturan handbook
│   └── omninook-app/             # Fondasi awal project Next.js
└── mike/                         # Folder kerja & riset Mike (Universitas Negeri Surabaya / UNESA)
    ├── keluhan unesa.md          # Data observasi riil masalah birokrasi, dospem, server, & bimbingan
    ├── Proposal & Tech Blueprint Hackathon GDG ITB.md # Ide ScaffoldAI
    └── Koleksi 100 Repositori GitHub untuk Kasus 1.md # Direktori 100 repo open-source pendukung
```

---

## 🌟 Konsep Utama: `AcademiaFlow` ("1 Portal for Everything")
Platform pendamping siklus akademik mahasiswa berbasis *Zero-Friction 1-Click PDF Schedule Import* yang menyatukan 4 pilar:
1. **Awal Semester:** *Smart KRS Planner, Weekly Syllabus/Practicum Preview & Circle Class Sync*
2. **Tengah Semester:** *Accountable Groupwork Engine, Task Relay Handover Notifications & Anti-Free-Rider Analytics*
3. **Semester 5–7:** *Adaptive Opportunity Hub, Verified Campus MoU Internships (Konversi 20 SKS), TAK/SKKM Tracker & Alumni Insider Directory*
4. **Tingkat Akhir:** *Thesis (TA 1 & 2) 21-Day Inactivity SLA Tracker, In-App Consultation Booking & Smart Advisor Rebalancing*
