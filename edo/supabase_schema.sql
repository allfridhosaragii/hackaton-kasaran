-- ============================================================================
-- ACADEMIAFLOW ("1 PORTAL FOR EVERYTHING") — SUPABASE POSTGRESQL + PGVECTOR SCHEMA
-- STACK 2026 by GDGoC ITB (Case 1: Smarter Campus and Learning)
-- Covers all 4 Student Lifecycle Modules:
--   Module 1: Smart KRS Planner, Circle Class Sync & Course/Practicum Preview
--   Module 2: Accountable Groupwork Engine, Relay Handover & Anti-Free-Rider
--   Module 3: Adaptive Opportunity Hub (Sem 5-7), MoU SKS Simulator, TAK & Alumni Insider
--   Module 4: Thesis (TA 1 & 2) 21-Day SLA Tracker & Smart Advisor Rebalancing
-- ============================================================================

-- 1. Enable Required Extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "vector";

-- ============================================================================
-- CORE USER PROFILES & TAK/SKKM TRACKER
-- ============================================================================
CREATE TABLE public.profiles (
    id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
    full_name TEXT NOT NULL,
    student_id TEXT UNIQUE,                        -- NIM (e.g. Telkom / ITB NIM)
    role TEXT NOT NULL DEFAULT 'student'
        CHECK (role IN ('student', 'lecturer', 'kaprodi', 'alumni')),
    campus_name TEXT NOT NULL DEFAULT 'Telkom University Surabaya',
    major TEXT NOT NULL,                           -- e.g. 'Informatika / STI'
    cohort_year INT NOT NULL DEFAULT 2024,
    origin_class TEXT DEFAULT 'IF-01',             -- Kelas asal sejak Semester 1 (untuk Circle Class Sync)
    semester INT NOT NULL DEFAULT 1,               -- Menentukan mode UI adaptif (Sem 1-4 vs Sem 5-7 Magang vs Sem 7-8 TA)
    gpa_estimate NUMERIC(3,2) DEFAULT 3.50,
    tak_points_current INT NOT NULL DEFAULT 0,     -- Poin TAK / SKKM terkumpul saat ini
    tak_points_target INT NOT NULL DEFAULT 60,     -- Syarat minimum TAK / SKKM untuk sidang kelulusan
    enrolled_courses TEXT[] DEFAULT '{}',          -- Hasil parse PDF KSM/KRS (1-Click Import)
    free_slots JSONB DEFAULT '[]'::jsonb,          -- Blok jam kosong mingguan hasil ekstraksi PDF KSM/KRS
    skills TEXT[] DEFAULT '{}',                    -- Skill otomatis dari mata kuliah + sertifikat
    whatsapp_contact TEXT,                         -- Opsional (khusus Alumni / Mahasiswa yang opt-in)
    instagram_handle TEXT,
    linkedin_url TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Tabel Sertifikat & Poin Keaktifan (TAK / SKKM) + Pengingat Kedaluwarsa
CREATE TABLE public.student_certificates (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
    title TEXT NOT NULL,                           -- e.g. 'Juara 1 Hackathon / Sertifikat AWS / Kepanitiaan'
    category TEXT NOT NULL                         -- 'competition', 'organization', 'certification', 'seminar'
        CHECK (category IN ('competition', 'organization', 'certification', 'seminar')),
    tak_points INT NOT NULL DEFAULT 5,
    issued_date DATE NOT NULL DEFAULT CURRENT_DATE,
    expires_at DATE,                               -- Untuk pengingat masa berlaku sertifikat kompetensi/bahasa
    file_url TEXT,
    verified BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- ============================================================================
-- MODULE 1: SMART KRS PLANNER, CIRCLE CLASS SYNC & COURSE PREVIEW
-- ============================================================================
CREATE TABLE public.course_catalog (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    course_code TEXT NOT NULL UNIQUE,              -- e.g. 'IF2110'
    course_name TEXT NOT NULL,                     -- e.g. 'Algoritma & Struktur Data'
    credits_sks INT NOT NULL DEFAULT 3,
    target_semester INT NOT NULL DEFAULT 3,
    is_mandatory BOOLEAN NOT NULL DEFAULT TRUE,    -- Matkul Wajib Paket vs Pilihan (Elective)
    has_practicum BOOLEAN NOT NULL DEFAULT FALSE,  -- Info apakah ada Praktikum & jadwal rilis modulnya
    practicum_details TEXT,                        -- e.g. 'Praktikum 2 minggu sekali di Lab Pemrograman, menggunakan bahasa C/Python'
    weekly_syllabus JSONB DEFAULT '[]'::jsonb,     -- Array 14 minggu: topik tiap minggu, bobot UTS/UAS/Tubes
    lecturer_team JSONB DEFAULT '[]'::jsonb,       -- Daftar dosen pengampu + gaya mengajar (review santun dari kating)
    parallel_classes JSONB DEFAULT '[]'::jsonb,    -- Daftar kelas paralel (01, 02, 03), jadwal hari/jam, dan kuota kursi
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Simulasi KRS Bareng Circle (Cohort / Circle Class Sync)
CREATE TABLE public.circle_krs_plans (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    circle_name TEXT NOT NULL,                     -- e.g. 'Circle Kelas 01 Sem 1'
    creator_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
    member_ids UUID[] NOT NULL DEFAULT '{}',       -- Daftar anggota circle yang ingin satu kelas paralel
    recommended_combination JSONB NOT NULL DEFAULT '[]'::jsonb, -- Plan A, Plan B, Plan C kelas paralel bebas bentrok
    conflict_score INT NOT NULL DEFAULT 0,         -- 0 = Bebas bentrok 100%
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- ============================================================================
-- MODULE 2: ACCOUNTABLE GROUPWORK ENGINE, RELAY HANDOVER & ANTI-FREE-RIDER
-- ============================================================================
CREATE TABLE public.group_projects (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    course_code TEXT NOT NULL,                     -- e.g. 'IF2110'
    project_title TEXT NOT NULL,                   -- e.g. 'Tugas Besar 1: Sistem Antrean Rumah Sakit'
    lecturer_id UUID REFERENCES public.profiles(id) ON DELETE SET NULL,
    group_name TEXT NOT NULL,                      -- e.g. 'Kelompok 04 - Kelas 01'
    formation_mode TEXT NOT NULL DEFAULT 'student_choice'
        CHECK (formation_mode IN ('lecturer_assigned', 'student_choice', 'smart_balanced')),
    deadline TIMESTAMPTZ NOT NULL,
    intersected_free_slots JSONB DEFAULT '[]'::jsonb, -- Hasil Auto-Find Jam Kosong Bersama dari KRS anggota
    shared_notes_markdown TEXT DEFAULT '',         -- Catatan kolaboratif (BlockNote / Yjs)
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE public.group_members (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    project_id UUID NOT NULL REFERENCES public.group_projects(id) ON DELETE CASCADE,
    user_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
    role_in_group TEXT DEFAULT 'Member',           -- e.g. 'Project Lead', 'Backend', 'UI/UX', 'Dokumentasi'
    contribution_percentage NUMERIC(5,2) DEFAULT 0.00, -- Dihitung otomatis dari bobot sub-tugas yang diselesaikan
    last_active_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(project_id, user_id)
);

-- Sub-Tugas dengan Sistem Estafet (Relay Handover) & Bukti Kontribusi
CREATE TABLE public.project_tasks (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    project_id UUID NOT NULL REFERENCES public.group_projects(id) ON DELETE CASCADE,
    title TEXT NOT NULL,                           -- e.g. 'Bagian 1: Desain ERD & Skema Database'
    description TEXT,
    assigned_to UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
    depends_on_task_id UUID REFERENCES public.project_tasks(id) ON DELETE SET NULL, -- Task prasyarat sebelum task ini jalan
    next_assignee_id UUID REFERENCES public.profiles(id) ON DELETE SET NULL,        -- Siapa yang otomatis dinotifikasi saat task ini selesai!
    weight_points INT NOT NULL DEFAULT 25,         -- Bobot kontribusi untuk analitik dosen
    status TEXT NOT NULL DEFAULT 'todo'
        CHECK (status IN ('blocked', 'todo', 'in_progress', 'completed')),
    evidence_link TEXT,                            -- Link commit Git / PR / file / screenshot bukti kerja
    due_at TIMESTAMPTZ,
    completed_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Notifikasi Estafet Real-Time (Triggered via Supabase Realtime saat teman selesai)
CREATE TABLE public.handover_notifications (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    project_id UUID NOT NULL REFERENCES public.group_projects(id) ON DELETE CASCADE,
    from_user_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
    to_user_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
    completed_task_id UUID NOT NULL REFERENCES public.project_tasks(id) ON DELETE CASCADE,
    next_task_id UUID REFERENCES public.project_tasks(id) ON DELETE SET NULL,
    message TEXT NOT NULL,                         -- e.g. 'Budi telah menyelesaikan Desain ERD! Sekarang giliranmu mengerjakan API Endpoint.'
    is_read BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Jalur Lapor / Eskalasi Resmi ke Dosen (Anti-Free-Rider & Bukti Log Objektif)
CREATE TABLE public.lecturer_escalations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    project_id UUID NOT NULL REFERENCES public.group_projects(id) ON DELETE CASCADE,
    reporter_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
    reported_member_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
    reason_category TEXT NOT NULL                  -- 'unresponsive_48h', 'missed_deadline', 'zero_contribution'
        CHECK (reason_category IN ('unresponsive_48h', 'missed_deadline', 'zero_contribution')),
    details TEXT NOT NULL,
    system_activity_snapshot JSONB NOT NULL DEFAULT '{}'::jsonb, -- Bukti otomatis dari log sistem (0 task selesai, lewat deadline)
    status TEXT NOT NULL DEFAULT 'pending_review'
        CHECK (status IN ('pending_review', 'pinged_by_lecturer', 'grade_adjusted', 'resolved')),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- ============================================================================
-- MODULE 3: ADAPTIVE OPPORTUNITY HUB (SEM 5-7), MOU SKS SIMULATOR & ALUMNI INSIDER
-- ============================================================================
CREATE TABLE public.campus_opportunities (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title TEXT NOT NULL,                           -- e.g. 'Software Engineer Intern - Telkom Indonesia (MoU Partner)'
    organization_name TEXT NOT NULL,               -- e.g. 'PT Telkom Indonesia / Bank BCA / Djarum Foundation'
    opportunity_type TEXT NOT NULL                 -- 'internship_mou', 'scholarship', 'competition', 'research'
        CHECK (opportunity_type IN ('internship_mou', 'scholarship', 'competition', 'research')),
    is_campus_mou_partner BOOLEAN NOT NULL DEFAULT FALSE, -- True = Kerjasama resmi kampus (jaminan konversi SKS)
    convertible_sks INT NOT NULL DEFAULT 0,        -- e.g. 20 SKS (MBKM / Geladi) atau 3 SKS (KP ITB)
    convertible_courses TEXT[] DEFAULT '{}',       -- Daftar kode matkul yang otomatis terkonversi tanpa perlu tunggu dosen wali lama
    min_semester INT NOT NULL DEFAULT 1,           -- Filter otomatis (misal Sem 5-7 untuk Magang)
    min_gpa NUMERIC(3,2) NOT NULL DEFAULT 0.00,
    eligible_majors TEXT[] DEFAULT '{}',
    deadline TIMESTAMPTZ NOT NULL,
    source_poster_url TEXT,
    application_link TEXT,
    embedding vector(768),                         -- Untuk pencocokan semantik dengan CV/skill mahasiswa
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Jejaring Alumni Insider di Perusahaan Mitra (Untuk Tanya Jawab WA / IG / LinkedIn)
CREATE TABLE public.alumni_company_insiders (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    organization_name TEXT NOT NULL,               -- Nama perusahaan mitra
    alumni_name TEXT NOT NULL,
    graduation_year INT NOT NULL,
    major TEXT NOT NULL,
    current_role TEXT NOT NULL,                    -- e.g. 'Cloud Engineer (Ex-Intern 2024)'
    internship_tips TEXT,                          -- Tips singkat lolos seleksi di perusahaan tersebut
    whatsapp_number TEXT,                          -- Kontak WA opt-in untuk tanya-tanya adik tingkat
    instagram_handle TEXT,
    linkedin_url TEXT,
    is_available_for_qa BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- ============================================================================
-- MODULE 4: THESIS (TA 1 & 2) 21-DAY SLA TRACKER & SMART ADVISOR REBALANCING
-- ============================================================================
CREATE TABLE public.thesis_supervisions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    student_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
    primary_advisor_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
    backup_advisor_id UUID REFERENCES public.profiles(id) ON DELETE SET NULL,
    thesis_title TEXT NOT NULL,
    research_topic_tags TEXT[] NOT NULL DEFAULT '{}', -- e.g. ['Computer Vision', 'NLP', 'IoT', 'Cybersecurity']
    current_chapter TEXT NOT NULL DEFAULT 'Bab 1 - Pendahuluan',
    last_student_submission_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    last_advisor_feedback_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    sla_status TEXT NOT NULL DEFAULT 'on_track'
        CHECK (sla_status IN ('on_track', 'warning_14d', 'breached_21d_ghosting', 'rebalanced')),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Logbook Bimbingan & Revisi per Bab (Cadangan Aman Anti-Server Down)
CREATE TABLE public.thesis_revision_logs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    supervision_id UUID NOT NULL REFERENCES public.thesis_supervisions(id) ON DELETE CASCADE,
    chapter_name TEXT NOT NULL,                    -- e.g. 'Bab 3 - Metodologi & Arsitektur Sistem'
    student_draft_url TEXT NOT NULL,
    student_notes TEXT,
    advisor_feedback TEXT,
    status TEXT NOT NULL DEFAULT 'awaiting_review'
        CHECK (status IN ('awaiting_review', 'revision_needed', 'approved')),
    submitted_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    reviewed_at TIMESTAMPTZ
);

-- Rekomendasi Oper/Rebalancing Dosen Pembimbing Otomatis untuk Kaprodi (Jika Lewat SLA 21 Hari)
CREATE TABLE public.advisor_rebalance_requests (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    supervision_id UUID NOT NULL REFERENCES public.thesis_supervisions(id) ON DELETE CASCADE,
    previous_advisor_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
    recommended_new_advisor_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
    days_unresponsive INT NOT NULL DEFAULT 21,
    topic_match_score NUMERIC(5,2) NOT NULL DEFAULT 92.50, -- Kecocokan keahlian riset dosen pengganti
    new_advisor_active_quota INT NOT NULL DEFAULT 4,       -- Sisa kuota bimbingan dosen pengganti
    kaprodi_approval_status TEXT NOT NULL DEFAULT 'pending_kaprodi'
        CHECK (kaprodi_approval_status IN ('pending_kaprodi', 'approved_transferred', 'declined')),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- ============================================================================
-- AUTOMATED TRIGGERS & FUNCTIONS FOR REALTIME RELAY & SLA DETECTION
-- ============================================================================

-- Function 1: Otomatis Kirim Notifikasi Estafet (Relay Handover) Saat Anggota Menyelesaikan Sub-Tugas
CREATE OR REPLACE FUNCTION public.handle_task_completion_handover()
RETURNS TRIGGER
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    IF NEW.status = 'completed' AND OLD.status <> 'completed' THEN
        NEW.completed_at := NOW();

        -- Buka kunci (unblock) sub-tugas berikutnya yang bergantung pada tugas ini
        UPDATE public.project_tasks
        SET status = 'todo'
        WHERE depends_on_task_id = NEW.id AND status = 'blocked';

        -- Buat notifikasi otomatis ke anggota berikutnya
        IF NEW.next_assignee_id IS NOT NULL THEN
            INSERT INTO public.handover_notifications (
                project_id, from_user_id, to_user_id, completed_task_id, message
            ) VALUES (
                NEW.project_id,
                NEW.assigned_to,
                NEW.next_assignee_id,
                NEW.id,
                'Sub-tugas "' || NEW.title || '" telah diselesaikan! Sekarang giliran Anda melanjutkan bagian berikutnya.'
            );
        END IF;
    END IF;
    RETURN NEW;
END;
$$;

CREATE TRIGGER trg_task_handover
BEFORE UPDATE ON public.project_tasks
FOR EACH ROW
EXECUTE FUNCTION public.handle_task_completion_handover();

-- Function 2: Deteksi Otomatis SLA 21 Hari Dosen Pembimbing Tidak Merespons
CREATE OR REPLACE FUNCTION public.check_thesis_21d_sla()
RETURNS INT
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
DECLARE
    flagged_count INT := 0;
BEGIN
    UPDATE public.thesis_supervisions
    SET sla_status = 'breached_21d_ghosting'
    WHERE sla_status IN ('on_track', 'warning_14d')
      AND last_student_submission_at > last_advisor_feedback_at
      AND NOW() - last_student_submission_at >= INTERVAL '21 days';

    GET DIAGNOSTICS flagged_count = ROW_COUNT;
    RETURN flagged_count;
END;
$$;
