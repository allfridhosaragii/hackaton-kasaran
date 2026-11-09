# GDG on Campus ITB Hackathon Proposal
## Kasus 1: Kampus dan Pembelajaran yang Lebih Cerdas (Smart Campus & Smarter Learning)

---

### 1. Informasi Proyek
* **Judul Proyek**: **ScaffoldAI** *(Adaptive Socratic Companion & Affective Learning Intervention)*
* **Kategori**: Kasus 1 – Kampus dan Pembelajaran yang Lebih Cerdas
* **Format Solusi**: Web-based Intelligent Learning Environment

---

### 2. Latar Belakang & Rumusan Masalah (*The Problem Statement*)

#### Realita Mahasiswa:
1. **The "Silent Struggle" & Cognitive Overload**:
   Saat belajar materi teknis (kodingan, algoritma, kalkulus, sistem komputer) secara mandiri, mahasiswa kerap mengalami *cognitive overload* dan kebuntuan (*stuck*). Keengganan bertanya di forum besar atau langsung ke dosen membuat mahasiswa pasif dan menunda tugas (*academic procrastination*).
2. **Ketergantungan LLM Generik Tanpa Pemahaman**:
   Banyak mahasiswa menggunakan LLM umum (seperti ChatGPT murni) untuk menyelesaikan tugas dengan cara *copy-paste* jawaban mentah. Hal ini menyelesaikan tugas dalam jangka pendek, tetapi mengikis pemahaman konsep fundamental (*illusion of competence*).
3. **Ketiadaan Sinyal Balik Dosen/Pengajar**:
   Dosen tidak mengetahui titik mana dalam silabus materi yang paling membingungkan mahasiswa secara riil di luar jam kelas tatap muka.

---

### 3. Solusi: ScaffoldAI

Platform web edukasi cerdas yang berfungsi sebagai **Tutor Sokratik Adaptif** dengan kemampuan membaca dinamika kognitif mahasiswa secara *real-time*.

#### Pilar Fitur Utama:
1. **Socratic AI Guidance (Scaffolding Engine)**:
   * Alih-alih memberikan jawaban akhir atau kode jadi, asisten membimbing mahasiswa lewat analogi, petunjuk bertahap (*multi-level hints*), dan pertanyaan reflektif untuk memancing pemahaman mandiri.
2. **Real-Time Confusion / Frustration Detector (Client-Side)**:
   * Membaca sinyal afektif belajar secara *privacy-first* di sisi browser tanpa mengirim rekaman video ke server:
     * *Behavioral signal*: Jeda ketik yang lama, frekuensi *backspace/undo* berlebihan saat mengerjakan soal, atau pengulangan error kode yang identik.
     * *Visual cue (opsional via webcam)*: Deteksi ekspresi mikro kebingungan/frustrasi (*brow furrowing*, tatapan bingung) menggunakan model lokal ringan.
3. **Dynamic Difficulty Adjustment (DDA)**:
   * Ketika sistem mendeteksi frustrasi tinggi, AI menurunkan tingkat kesulitan penjelasan (menggunakan analogi dunia nyata atau visual).
   * Ketika pemahaman mahasiswa lancar, sistem menaikkan level pertanyaan uji konsep (*concept-check challenge*).
4. **Learning Pulse Dashboard**:
   * **Sisi Mahasiswa**: Riwayat topik yang sudah dikuasai vs topik yang sering membuat *stuck*.
   * **Sisi Pengajar / Asisten Lab**: Agregasi analitik anonim mengenai bab mana yang paling sering memicu kebingungan mahasiswa di kelas.

---

### 4. Referensi Repositori GitHub untuk Bedah Kode

Berikut repositori open-source yang dapat dijadikan acuan arsitektur dan komponen teknis:

#### A. Layer Deteksi Afektif & Computer Vision (Client-Side / Privacy-First)
* **[justadudewhohacks/face-api.js](https://github.com/justadudewhohacks/face-api.js)**
  * *Tujuan*: Model deteksi ekspresi wajah dan facial landmark berbasis TensorFlow.js yang berjalan langsung di browser pengguna.
* **[google/mediapipe](https://github.com/google/mediapipe)**
  * *Tujuan*: Toolkit resmi Google untuk pelacakan mata (*gaze tracking*) dan *face mesh* berlatensi sangat rendah di web.

#### B. Layer Tutor Sokratik & RAG Materi Kuliah
* **[open-webui/open-webui](https://github.com/open-webui/open-webui)**
  * *Tujuan*: Desain antarmuka chat berbasis AI yang modular, manajemen prompt sistem terstruktur, dan penanganan konteks percakapan.
* **[Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm)**
  * *Tujuan*: Implementasi RAG (*Retrieval-Augmented Generation*) siap pakai agar mahasiswa dapat mengunggah slide kuliah (PDF) untuk dijadikan batas pengetahuan asisten AI.
* **[stanford-oval/storm](https://github.com/stanford-oval/storm)**
  * *Tujuan*: Arsitektur sintesis pengetahuan yang berorientasi pada riset dan perumusan pertanyaan berbasis konteks akademik.

#### C. Layer UI Dashboard & Web Foundation
* **[shadcn-ui/taxonomy](https://github.com/shadcn-ui/taxonomy)**
  * *Tujuan*: Boilerplate web modern berbasis Next.js App Router, Tailwind CSS, dan autentikasi yang rapi untuk pengerjaan cepat saat hackathon.
* **[tremorlabs/tremor](https://github.com/tremorlabs/tremor)**
  * *Tujuan*: Pustaka visualisasi data React untuk membangun visual analitik retensi belajar mahasiswa secara cepat dan elegan.

---

### 5. Arsitektur Teknis Sistem

```
┌─────────────────────────────────────────────────────────────┐
│                     Client Browser (User)                   │
│                                                             │
│  [ Next.js UI / Workspace ] ─── [ Code & Text Editor ]      │
│               │                                │            │
│               ▼                                ▼            │
│  [ MediaPipe / Face-api.js ]        [ Keystroke Monitor ]   │
│   (Client-side Emotion Det.)         (Behavioral Clues)     │
└──────────────────────────────┬──────────────────────────────┘
                               │ State (Confusion Index)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                    Backend Orchestrator                     │
│               (Next.js Server Actions / FastAPI)            │
│                                                             │
│  • Scaffold Engine (Prompt Strategy: Socratic / Analogy)    │
│  • Context Injector (Vector Search over Course Materials)   │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                     Data & Model Layer                      │
│                                                             │
│  • Gemini API (LLM Backbone dengan JSON mode & Schema)      │
│  • Supabase (PostgreSQL + pgvector untuk RAG + Auth)        │
└─────────────────────────────────────────────────────────────┘
```

---

### 6. Rencana Pembagian Tugas Tim (3–4 Orang)

| Role | Fokus Tanggung Jawab | Output Kunci |
| :--- | :--- | :--- |
| **Frontend Engineer** | Mengembangkan antarmuka interaktif: chat workspace, editor kode/teks, dan dashboard metrik pemahaman. | UI Next.js + Tailwind + Tremor Chart |
| **AI / Prompt Engineer** | Merancang logika RAG materi, *system prompt* Sokratik bertingkat (*hints*, analogi, evaluasi), dan tuning Gemini API. | Pipeline Gemini API + Dynamic Prompt Handler |
| **Client-Side / ML Engineer** | Mengintegrasikan detektor afektif di browser (Face-api / MediaPipe) atau logika *keystroke behavioral analysis*. | Modul deteksi afektif lokal (*privacy-safe*) |
| **Backend & Integrator** | Menyiapkan skema basis data, sistem autentikasi, API endpoint, serta menyusun materi presentasi/pitch deck. | Supabase Setup + Slide Pitch Hackathon |

---

### 7. Keunggulan Kompetitif di Mata Juri GDG
1. **Bukan Sekadar Chatbot**: Menggunakan pendekatan pedagogi terstruktur (*Socratic Method*) sehingga tidak melanggar integritas akademik kampus.
2. **Privacy-Preserving**: Analisis ekspresi wajah atau gestur dilakukan 100% lokal di browser pengguna tanpa mengirim *stream* video ke server.
3. **Mengoptimalkan Ekosistem Google/GDG**: Memanfaatkan model multimodal Gemini untuk penalaran silabus dan MediaPipe untuk interaksi *client-side*.