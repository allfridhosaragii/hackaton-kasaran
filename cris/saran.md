1. Web Seperti Apa yang Mau Dibuat?
Nama konsepnya KuliahPaham (atau StudyPulse).
Bentuknya adalah Web Workspace Belajar & Penyelamat Ujian Mahasiswa.

Alur kerjanya simpel: Mahasiswa tinggal drop rekaman suara HP waktu dosen ngajar + file slide kuliah (PPT/PDF).

Sistem langsung otomatis mecah itu jadi: transkrip yang sinkron dengan nomor slide, penjelasan ulang konsep sulit dengan bahasa mahasiswa yang gampang dipahami, kuis latihan ujian (active recall), dan ruang catatan kolaboratif bareng teman sekelas.

2. Alasan & Landasan Masalah (Why)
Masalah Lapangan: Banyak dosen di kelas cara ngajarnya monoton, malas nerangin panjang lebar (cuma baca poin slide), atau penjelasannya lompat-lompat.

Efek ke Mahasiswa: Mahasiswa sungkan/takut nanya di kelas, akhirnya waktu pulang beneran nggak ngerti apa-apa.

Ujungnya: Begitu UTS/UAS tiba, belajar pakai sistem kebut semalam (SKS) cuma dengan modal baca ulang slide yang nggak mereka pahami. Akibatnya nilai anjlok dan IPK turun drastis. Mahasiswa butuh jembatan dari 'materi mentah dosen' ke 'pemahaman riil siap ujian'.

3. Tujuannya (Goals & Outcome)
Paham Mandiri Tanpa Ketergantungan Dosen: Mengubah materi dosen yang kaku jadi modul belajar interaktif yang sabar nerangin step-by-step sampai mahasiswa paham.

Dongkrak Nilai Ujian: Mengubah cara belajar pasif (baca slide) jadi belajar aktif lewat kuis prediksi ujian dan pengulangan berkala (spaced repetition).

Kolaborasi Sebaya: Ada ruang buat teman sekelas saling melengkapi catatan atau ngasih penjelasan versi teman (tutor sebaya).

4. Dari 100 Repo Kemarin, Mana Saja yang Benar-Benar Dipakai?
Kita cuma filter dan pakai 7 repo inti ini supaya realistis selesai dan nggak bikin pusing:

openai/whisper (atau faster-whisper): Mesin transkrip suara dosen jadi teks otomatis.

microsoft/markitdown + docling: Pengekstrak slide PDF/PPT dosen dan rumus matematika biar jadi teks rapi.

infiniflow/ragflow: Otak AI (RAG)-nya. Mahasiswa bisa tanya jawab materi yang belum dimengerti khusus dari sumber rekaman & slide dosen tadi (nggak halusinasi ngawur).

ts-fsrs: Algoritma pembuat kuis & jadwal review otomatis ke memori mahasiswa biar siap ujian.

BlockNote + yjs: Editor web buat catatan bareng teman sekelas secara real-time kayak Notion/Google Docs.

supabase: Backend utama (database materi, auth akun kampus, dan vector search).

shadcn-admin + Next.js: Kerangka tampilan web biar dashboard-nya cepat jadi, rapi, dan kelihatan siap pakai.

Gimana menurutmu alur produknya? Kalau konsep ini udah oke, kita bisa langsung bagi tugas: siapa yang megang frontend UI-nya dan siapa yang narik API backend-nya."

Pesan di atas langsung menjawab 4 poin yang dia minta: bentuk web, alasan, tujuan, dan daftar repo pilihan.