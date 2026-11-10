-- ============================================================================
-- ACADEMIAFLOW ("1 PORTAL FOR EVERYTHING") — SUPABASE POSTGRESQL + PGVECTOR SCHEMA
-- STACK 2026 by GDGoC ITB (Case 1: Smarter Campus and Learning)
-- Unified Team Blueprint (Edo + Mike + Cris + Field Validation from ITB, Telkom, UNESA):
--   Module 1 (Edo + Mike + ITB): Smart KRS Planner, Circle Class Sync, Realtime Quota & Course Preview
--   Module 2A (Cris + Mike): StudyPulse Lecture Mastery (Audio + Slide -> Transcript, Socratic RAG, FSRS Quiz, Shared Notes)
--   Module 2B (Edo + ITB): Accountable Groupwork Engine, Relay Handover, Digital Contribution Logbook & Escalation
--   Module 3 (Edo + ITB): Adaptive Opportunity Hub (Sem 5-7), MoU 20-SKS Simulator, TAK & Alumni Insider
--   Module 4 (Edo + Mike + ITB #1 Priority): Thesis 21-Day SLA, Transparent Quota, In-App Consultation Ticket, 1-Click Approval & Smart Rebalancing
-- ============================================================================

-- 1. Enable Required Extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "vector";

-- ============================================================================
-- CORE USER PROFILES, ADVISOR QUOTA & TAK/SKKM TRACKER
-- ============================================================================
CREATE TABLE public.profiles (
    id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
    full_name TEXT NOT NULL,
    student_id TEXT UNIQUE,                        -- NIM / NIP (ITB / Telkom / UNESA)
    role TEXT NOT NULL DEFAULT 'student'
        CHECK (role IN ('student', 'lecturer', 'kaprodi', 'alumni')),
    campus_name TEXT NOT NULL DEFAULT 'Telkom University Surabaya',
    major TEXT NOT NULL,                           -- e.g. 'Informatika / STI / Mikrobiologi'
    cohort_year INT NOT NULL DEFAULT 2024,
    origin_class TEXT DEFAULT 'IF-01',             -- Kelas asal sejak Semester 1 (untuk Circle Class Sync)
    semester INT NOT NULL DEFAULT 1,               -- Menentukan mode UI adaptif (Sem 1-4 vs Sem 5-7 Magang vs Sem 7-8 TA)
    gpa_estimate NUMERIC(3,2) DEFAULT 3.50,
    tak_points_current INT NOT NULL DEFAULT 0,     -- Poin TAK / SKKM terkumpul saat ini
    tak_points_target INT NOT NULL DEFAULT 60,     -- Syarat minimum TAK / SKKM untuk sidang kelulusan
    enrolled_courses TEXT[] DEFAULT '{}',          -- Hasil parse PDF KSM/KRS (1-Click Import)
    free_slots JSONB DEFAULT '[]'::jsonb,          -- Blok jam kosong mingguan hasil ekstraksi PDF KSM/KRS
    skills TEXT[] DEFAULT '{}',                    -- Skill otomatis dari mata kuliah + sertifikat
    research_expertise_embedding vector(768),      -- Khusus Dosen: Vektor keahlian riset untuk Semantic Dosbing Matching (Ide Mike)
    advisor_quota_max INT DEFAULT 10,              -- Transparansi kuota bimbingan dosen (Solusi Masalah #9 ITB & UNESA)
    advisor_quota_used INT DEFAULT 0,
    whatsapp_contact TEXT,                         -- Opsional (khusus Alumni opt-in / Bot Notification)
    instagram_handle TEXT,
    linkedin_url TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Tabel Sertifikat & Poin Keaktifan (TAK / SKKM) + Pengingat Kedaluwarsa
CREATE TABLE public.student_certificates (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    category TEXT NOT NULL
        CHECK (category IN ('competition', 'organization', 'certification', 'seminar')),
    tak_points INT NOT NULL DEFAULT 5,
    issued_date DATE NOT NULL DEFAULT CURRENT_DATE,
    expires_at DATE,
    file_url TEXT,
    verified BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- ============================================================================
-- MODULE 1: SMART KRS PLANNER, CIRCLE CLASS SYNC, REALTIME QUOTA & COURSE PREVIEW
-- ============================================================================
CREATE TABLE public.course_catalog (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    course_code TEXT NOT NULL UNIQUE,              -- e.g. 'IF2110'
    course_name TEXT NOT NULL,                     -- e.g. 'Algoritma & Struktur Data'
    credits_sks INT NOT NULL DEFAULT 3,
    target_semester INT NOT NULL DEFAULT 3,
    is_mandatory BOOLEAN NOT NULL DEFAULT TRUE,    -- Matkul Wajib Paket vs Pilihan
    has_practicum BOOLEAN NOT NULL DEFAULT FALSE,  -- Info Praktikum & jadwal modulnya
    practicum_details TEXT,
    weekly_syllabus JSONB DEFAULT '[]'::jsonb,     -- Array 14 minggu: topik tiap minggu, bobot UTS/UAS/Tubes
    lecturer_team JSONB DEFAULT '[]'::jsonb,       -- Review kating yang spesifik & real (Validasi No. 3 ITB)
    parallel_classes JSONB DEFAULT '[]'::jsonb,    -- Daftar kelas paralel (01, 02, 03) + kuota real-time via WebSocket (Solusi Anti-F5 Mike)
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE public.circle_krs_plans (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    circle_name TEXT NOT NULL,                     -- e.g. 'Circle Kelas 01 Sem 1'
    creator_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
    member_ids UUID[] NOT NULL DEFAULT '{}',
    recommended_combination JSONB NOT NULL DEFAULT '[]'::jsonb, -- Plan A, Plan B, Plan C kelas paralel bebas bentrok
    conflict_score INT NOT NULL DEFAULT 0,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- ============================================================================
-- MODULE 2A: STUDYPULSE / KULIAHPAHAM LECTURE MASTERY (IDE CRIS + SOCRATIC AI MIKE)
-- ============================================================================
CREATE TABLE public.lecture_study_sessions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    course_code TEXT NOT NULL,
    week_number INT NOT NULL DEFAULT 1,
    session_title TEXT NOT NULL,                   -- e.g. 'Minggu 4: Tree & Graph Traversal'
    slide_pdf_url TEXT,                            -- File PPT/PDF dosen yang di-drop mahasiswa
    audio_recording_url TEXT,                      -- Rekaman suara HP saat dosen mengajar
    slide_synced_transcript JSONB DEFAULT '[]'::jsonb, -- Hasil faster-whisper + markitdown yang sinkron nomor slide
    simplified_explanation_md TEXT,                -- Penjelasan ulang bahasa mahasiswa + analogi Socratic bertahap
    shared_class_notes_md TEXT DEFAULT '',         -- Catatan kolaboratif real-time sekelas (BlockNote + Yjs)
    created_by UUID REFERENCES public.profiles(id) ON DELETE SET NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Potongan Vektor Slide & Rekaman Dosen untuk Tanya-Jawab Anti-Halusinasi (RAGFlow / pgvector)
CREATE TABLE public.lecture_knowledge_chunks (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    session_id UUID NOT NULL REFERENCES public.lecture_study_sessions(id) ON DELETE CASCADE,
    slide_number INT NOT NULL DEFAULT 1,
    audio_timestamp_sec INT,
    content TEXT NOT NULL,
    embedding vector(768)
);

-- Kuis Latihan Ujian & Spaced Repetition (ts-fsrs — Penyelamat UTS/UAS Ide Cris)
CREATE TABLE public.active_recall_flashcards (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
    session_id UUID REFERENCES public.lecture_study_sessions(id) ON DELETE CASCADE,
    course_code TEXT NOT NULL,
    question TEXT NOT NULL,
    socratic_hint TEXT,                            -- Petunjuk bertahap sebelum membuka jawaban (Ide Mike)
    answer TEXT NOT NULL,
    slide_citation TEXT,                           -- e.g. 'Slide 12 (Menit 34:10)'
    due_date TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    stability NUMERIC NOT NULL DEFAULT 0,
    difficulty NUMERIC NOT NULL DEFAULT 0,
    reps INT NOT NULL DEFAULT 0,
    lapses INT NOT NULL DEFAULT 0,
    fsrs_state INT NOT NULL DEFAULT 0,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- ============================================================================
-- MODULE 2B: ACCOUNTABLE GROUPWORK ENGINE, RELAY HANDOVER & ANTI-FREE-RIDER (IDE EDO + ITB)
-- ============================================================================
CREATE TABLE public.group_projects (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    course_code TEXT NOT NULL,
    project_title TEXT NOT NULL,                   -- e.g. 'Tugas Besar 1 IF2110'
    lecturer_id UUID REFERENCES public.profiles(id) ON DELETE SET NULL,
    group_name TEXT NOT NULL,
    formation_mode TEXT NOT NULL DEFAULT 'lecturer_assigned'
        CHECK (formation_mode IN ('lecturer_assigned', 'student_choice', 'smart_balanced')),
    deadline TIMESTAMPTZ NOT NULL,
    intersected_free_slots JSONB DEFAULT '[]'::jsonb, -- Hasil Auto-Find Jam Kosong Bersama dari KRS anggota
    shared_notes_markdown TEXT DEFAULT '',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE public.group_members (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    project_id UUID NOT NULL REFERENCES public.group_projects(id) ON DELETE CASCADE,
    user_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
    role_in_group TEXT DEFAULT 'Member',
    contribution_percentage NUMERIC(5,2) DEFAULT 0.00, -- Digitalisasi Lembar Kontribusi ITB secara otomatis!
    last_active_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(project_id, user_id)
);

CREATE TABLE public.project_tasks (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    project_id UUID NOT NULL REFERENCES public.group_projects(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    description TEXT,
    assigned_to UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
    depends_on_task_id UUID REFERENCES public.project_tasks(id) ON DELETE SET NULL,
    next_assignee_id UUID REFERENCES public.profiles(id) ON DELETE SET NULL,        -- Penerima notifikasi estafet otomatis
    weight_points INT NOT NULL DEFAULT 25,
    status TEXT NOT NULL DEFAULT 'todo'
        CHECK (status IN ('blocked', 'todo', 'in_progress', 'completed')),
    evidence_link TEXT,                            -- Bukti commit Git / PR / file kerja
    due_at TIMESTAMPTZ,
    completed_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE public.handover_notifications (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    project_id UUID NOT NULL REFERENCES public.group_projects(id) ON DELETE CASCADE,
    from_user_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
    to_user_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
    completed_task_id UUID NOT NULL REFERENCES public.project_tasks(id) ON DELETE CASCADE,
    message TEXT NOT NULL,
    is_read BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE public.lecturer_escalations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    project_id UUID NOT NULL REFERENCES public.group_projects(id) ON DELETE CASCADE,
    reporter_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
    reported_member_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
    reason_category TEXT NOT NULL
        CHECK (reason_category IN ('unresponsive_48h', 'missed_deadline', 'zero_contribution')),
    details TEXT NOT NULL,
    system_activity_snapshot JSONB NOT NULL DEFAULT '{}'::jsonb, -- Bukti objektif log kontribusi untuk Dosen
    status TEXT NOT NULL DEFAULT 'pending_review'
        CHECK (status IN ('pending_review', 'pinged_by_lecturer', 'grade_adjusted', 'resolved')),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- ============================================================================
-- MODULE 3: ADAPTIVE OPPORTUNITY HUB (SEM 5-7), MOU SKS SIMULATOR & ALUMNI INSIDER
-- ============================================================================
CREATE TABLE public.campus_opportunities (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title TEXT NOT NULL,
    organization_name TEXT NOT NULL,
    opportunity_type TEXT NOT NULL
        CHECK (opportunity_type IN ('internship_mou', 'scholarship', 'competition', 'research')),
    is_campus_mou_partner BOOLEAN NOT NULL DEFAULT FALSE,
    convertible_sks INT NOT NULL DEFAULT 0,        -- e.g. 20 SKS (MBKM/Geladi) atau KP
    convertible_courses TEXT[] DEFAULT '{}',
    min_semester INT NOT NULL DEFAULT 1,
    min_gpa NUMERIC(3,2) NOT NULL DEFAULT 0.00,
    eligible_majors TEXT[] DEFAULT '{}',
    deadline TIMESTAMPTZ NOT NULL,
    source_poster_url TEXT,                        -- Poster dari Line Himpunan ITB / WA Angkatan yang diekstrak PaddleOCR
    application_link TEXT,
    embedding vector(768),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE public.alumni_company_insiders (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    organization_name TEXT NOT NULL,
    alumni_name TEXT NOT NULL,
    graduation_year INT NOT NULL,
    major TEXT NOT NULL,
    current_role TEXT NOT NULL,
    internship_tips TEXT,
    whatsapp_number TEXT,
    instagram_handle TEXT,
    linkedin_url TEXT,
    is_available_for_qa BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- ============================================================================
-- MODULE 4: THESIS (TA 1 & 2) 21-DAY SLA, IN-APP CONSULTATION TICKET & REBALANCING
-- (Menjawab Masalah #1 Paling Parah di ITB & Keluhan Birokrasi/WA UNESA)
-- ============================================================================
CREATE TABLE public.thesis_supervisions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    student_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
    primary_advisor_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
    backup_advisor_id UUID REFERENCES public.profiles(id) ON DELETE SET NULL,
    thesis_title TEXT NOT NULL,
    research_topic_tags TEXT[] NOT NULL DEFAULT '{}',
    topic_embedding vector(768),                   -- Untuk Semantic Matching Topik Mahasiswa vs Pakar Dosen (Ide Mike)
    current_chapter TEXT NOT NULL DEFAULT 'Bab 1 - Pendahuluan',
    rubric_checklist JSONB DEFAULT '[]'::jsonb,    -- Rubrik evaluasi standar agar penilaian antardosen adil (Ide Mike)
    last_student_submission_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    last_advisor_feedback_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    sla_status TEXT NOT NULL DEFAULT 'on_track'
        CHECK (sla_status IN ('on_track', 'warning_14d', 'breached_21d_ghosting', 'rebalanced')),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Sistem Tiket Konsultasi Terjadwal & 1-Click Approval Logbook (Menghilangkan Messaging Anxiety WA & Bolak-Balik Kampus — Ide Mike)
CREATE TABLE public.thesis_consultation_tickets (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    supervision_id UUID NOT NULL REFERENCES public.thesis_supervisions(id) ON DELETE CASCADE,
    chapter_name TEXT NOT NULL,
    polite_template_message TEXT NOT NULL,         -- Pesan terstandarisasi sopan otomatis (bebas cemas etika WA)
    student_draft_url TEXT NOT NULL,
    git_commit_evidence TEXT,
    scheduled_slot TIMESTAMPTZ,                    -- Slot jadwal konsultasi ala Cal.com
    advisor_feedback TEXT,
    one_click_approval_status TEXT NOT NULL DEFAULT 'awaiting_review'
        CHECK (one_click_approval_status IN ('awaiting_review', 'revision_needed', 'approved_signed')),
    digital_signature_hash TEXT,                   -- Paraf digital resmi 1-klik (tanpa kejar dosen antar-kampus)
    submitted_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    reviewed_at TIMESTAMPTZ
);

CREATE TABLE public.advisor_rebalance_requests (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    supervision_id UUID NOT NULL REFERENCES public.thesis_supervisions(id) ON DELETE CASCADE,
    previous_advisor_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
    recommended_new_advisor_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
    days_unresponsive INT NOT NULL DEFAULT 21,
    topic_match_score NUMERIC(5,2) NOT NULL DEFAULT 94.00,
    new_advisor_available_quota INT NOT NULL DEFAULT 3,
    kaprodi_approval_status TEXT NOT NULL DEFAULT 'pending_kaprodi'
        CHECK (kaprodi_approval_status IN ('pending_kaprodi', 'approved_transferred', 'declined')),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- ============================================================================
-- AUTOMATED TRIGGERS FOR REALTIME RELAY HANDOVER & 21-DAY THESIS SLA
-- ============================================================================
CREATE OR REPLACE FUNCTION public.handle_task_completion_handover()
RETURNS TRIGGER
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    IF NEW.status = 'completed' AND OLD.status <> 'completed' THEN
        NEW.completed_at := NOW();

        UPDATE public.project_tasks
        SET status = 'todo'
        WHERE depends_on_task_id = NEW.id AND status = 'blocked';

        IF NEW.next_assignee_id IS NOT NULL THEN
            INSERT INTO public.handover_notifications (
                project_id, from_user_id, to_user_id, completed_task_id, message
            ) VALUES (
                NEW.project_id,
                NEW.assigned_to,
                NEW.next_assignee_id,
                NEW.id,
                'Sub-tugas "' || NEW.title || '" telah selesai! Sekarang giliran Anda melanjutkan bagian berikutnya.'
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
