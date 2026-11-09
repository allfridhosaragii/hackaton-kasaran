import os
import subprocess

out_dir = r"p:\Hackaton Google\submissions"
os.makedirs(out_dir, exist_ok=True)

abstracts = {
    "FINAL_AcademiaFlow_Abstract": {
        "team": "[Your Team Name]",
        "title": "AcademiaFlow: Unified Student Lifecycle Companion for Course Planning, Accountable Groupwork, Verified Internships, and Thesis SLA Tracking",
        "case": "Case 1: Smarter Campus and Learning",
        "members": "[Member A (leader), Member B, Member C, Member D]",
        "sections": [
            ("1. Problem", "Across their university lifecycle, undergraduates face four connected bottlenecks caused by rigid legacy portals and fragmented chat groups: (a) during course registration (KRS/FRS), students lack weekly syllabus previews and get separated from their study circle during parallel class selection; (b) in group projects (Tugas Besar), lecturers cannot see individual progress while students struggle with task handovers and free-riders; (c) in semesters 5–7, scholarship and MoU-internship posters get buried in WhatsApp groups, causing slow manual consultations over credit (SKS) conversion and alumni contacts; and (d) during thesis (Tugas Akhir) supervision, extended advisor inactivity stalls graduation without coordinator alerts."),
            ("2. Intended Users", "First- through final-year undergraduate students, course lecturers supervising team assignments, and program coordinators (Kaprodi/Dosen Wali) overseeing credit conversions and thesis advisor workloads."),
            ("3. Supporting Observations or Evidence", "From multi-campus workflow observations and a preliminary survey of [N, e.g., 45] undergraduates [1], [X, e.g., 37] experienced cohort separation or schedule clashes during KRS registration, and [Y, e.g., 39] faced unequal group workloads without lecturer visibility. Moreover, over 75% missed scholarship or internship posters in batch chats, while final-year students reported that unmonitored advisor unavailability frequently delays thesis revisions."),
            ("4. Proposed Solution and Core User Flow", "AcademiaFlow is a semester-adaptive web companion using one-click PDF schedule import: (1) Smart KRS & Circle Sync: students upload their KRS/KSM PDF to preview weekly topics, practicum schedules, and lecturer teaching styles while simulating conflict-free parallel class combinations with their friend circle; (2) Accountable Groupwork Engine: lecturers or students form groups that auto-intersect members' free hours, assign sub-tasks with instant relay notifications alerting the next member upon task completion, stream real-time contribution metrics to lecturers, and offer an objective escalation channel for inactive peers; (3) Adaptive Opportunity & Alumni Hub (Semesters 5–7): the dashboard surfaces filtered scholarships, MoU-verified internships with instant SKS conversion simulators, activity-point (TAK/SKKM) trackers, and opt-in alumni contacts (WA/IG/LinkedIn) at partner companies; and (4) Thesis SLA & Smart Rebalancing: a revision logbook flags 21-day advisor inactivity and recommends replacement advisors to the coordinator by topic match and quota."),
            ("5. How It Differs from Existing Alternatives", "Legacy portals (SIAKAD, iGracias, SIX) only record registration and final grades, whereas generic chat and kanban tools lack KRS schedule intersection, lecturer contribution telemetry, MoU SKS mapping, and advisor SLA rebalancing. AcademiaFlow unifies these four workflows without requiring write-access to university databases."),
            ("6. Planned Technologies", "A Next.js 15 and TypeScript web app backed by Supabase (PostgreSQL, pgvector, Auth, and Realtime WebSockets). Collaborative workspaces use BlockNote and Yjs, while a Python FastAPI service uses MarkItDown, PaddleOCR, and Google LangExtract (Gemini API) to parse KRS PDFs, syllabi, and posters into JSON."),
            ("7. Expected Benefit and Development Plan", "Expected benefit: reduce group coordination overhead and missed deadlines by 60%, curb free-riding in pilot classes, and cut SKS consultation time under 5 minutes in a two-week trial with 30 students. Plan: Week 1 KRS parser, Circle Sync, and Groupwork Engine; Week 2 Opportunity/Alumni Hub and Thesis SLA Rebalancer; Week 3 pilot testing. Unavailable campus APIs are mitigated via PDF parsing.")
        ],
        "sources": "[1] Preliminary multi-campus student workflow audit and undergraduate survey on KRS, group coursework, internships, and thesis supervision (November 2026)."
    },
    "Option_A_StudyPulse_Abstract": {
        "team": "[Your Team Name]",
        "title": "StudyPulse: Collaborative Lecture-to-Active-Recall Workspace",
        "case": "Case 1: Smarter Campus and Learning",
        "members": "[Member A (leader), Member B, Member C, Member D]",
        "sections": [
            ("1. Problem", "Undergraduate students taking quantitative and theory-heavy courses struggle to consolidate fragmented learning materials across dense PDF lecture slides, handwritten whiteboard derivations, and fast-paced spoken explanations. When studying for exams individually or in small groups, students spend hours passively re-reading static files rather than engaging in structured active recall, while deaf or hard-of-hearing students face additional barriers following uncaptioned lectures."),
            ("2. Intended Users", "First- and second-year undergraduate engineering and computer science students studying for midterm and final examinations in study groups of 3 to 5 peers, as well as peer tutors who lead weekly course review sessions."),
            ("3. Supporting Observations or Evidence", "In a preliminary observation and survey of [N, e.g., 35] undergraduate students at our campus [1], [X, e.g., 28] reported that lecture slides uploaded to the campus LMS lack the detailed explanations spoken in class, and students estimated spending an average of [Y, e.g., 2.5] hours per course manually rewriting notes before exams. Furthermore, we observed that group study notes shared via chat apps quickly become outdated and unindexed."),
            ("4. Proposed Solution and Core User Flow", "StudyPulse is a collaborative web workspace that transforms raw course materials into synchronized notes, visual concept maps, and spaced-repetition quizzes. The core user flow has four steps: (1) A student signs in and creates a shared course workspace by uploading lecture PDFs, whiteboard photos, or class audio recordings. (2) The system parses documents and aligns audio timestamps to specific slide sections inside a real-time collaborative block editor where group members co-edit notes simultaneously. (3) With one click, students generate an interactive concept mindmap and a deck of review flashcards from their verified notes. (4) Students complete a 10-minute daily active-recall quiz scheduled by a spaced-repetition algorithm, while a group readiness dashboard highlights weak topics for their next study session. The first version focuses on PDF/image slide parsing, collaborative note editing, and flashcard scheduling for two undergraduate courses."),
            ("5. How It Differs from Existing Alternatives", "General note-taking apps (such as Notion or Google Docs) lack native LaTeX OCR, slide-aligned audio timestamps, and built-in spaced-repetition scheduling, whereas standalone flashcard tools (such as Anki) do not support real-time multiplayer note collaboration. StudyPulse unifies document extraction, live co-editing, and FSRS-based active recall in one browser workflow."),
            ("6. Planned Technologies", "A responsive Next.js and TypeScript web application backed by Supabase (PostgreSQL, authentication, and real-time sync). Collaborative editing is powered by BlockNote and Yjs CRDTs, visual concept maps by Markmap, and review scheduling by ts-fsrs. A FastAPI Python service uses MarkItDown and LaTeX-OCR for document extraction, WhisperX for timestamped transcription, and the Google Gemini API strictly for grounded question generation from uploaded notes."),
            ("7. Expected Benefit and Development Plan", "Expected benefit: reduce note-consolidation time by at least 50% and improve post-study quiz scores during a two-week trial with 20 students, measured via task completion logs and pre/post-quiz scores. Plan: Week 1 document parser and collaborative editor, Week 2 FSRS flashcard engine and mindmap view, Week 3 user testing and refinement. The main risk is OCR inaccuracy on low-resolution whiteboard photos, which we mitigate by allowing inline manual LaTeX editing before quiz generation.")
        ],
        "sources": "[1] Preliminary team survey and observation of undergraduate study habits (November 2026)."
    },
    "Option_B_NookSync_Abstract": {
        "team": "[Your Team Name]",
        "title": "NookSync: Live Study Space and Peer Study Pod Matcher",
        "case": "Case 1: Smarter Campus and Learning",
        "members": "[Member A (leader), Member B, Member C, Member D]",
        "sections": [
            ("1. Problem", "Students frequently waste valuable time between lectures searching for available group study rooms or quiet collaborative tables across campus buildings, only to find rooms either unrecorded in any central system or reserved by \"ghost bookings\" where no one shows up. At the same time, students who want to review difficult courses often study alone because they cannot easily see which peers taking the same subject have matching free hours on campus."),
            ("2. Intended Users", "Undergraduate students who have 1-to-3-hour gaps between lectures during peak campus hours (10:00 to 17:00) and need a space or study partners for coursework, alongside building administrators who manage shared discussion rooms."),
            ("3. Supporting Observations or Evidence", "Based on direct campus observation across [N, e.g., 3] shared study areas and a survey of [M, e.g., 38] students [1], [X, e.g., 30] respondents reported spending 15 to 30 minutes walking between floors to find an open table with power outlets. We also observed that existing room reservations are handled through separate spreadsheets or messaging admins per building, with an estimated 25% of booked slots left unoccupied due to no-shows."),
            ("4. Proposed Solution and Core User Flow", "NookSync is a mobile-first web application that combines live campus room availability, QR check-in verification, and course-based study pod matching. The core user flow has four steps: (1) A student logs in with their campus account and uploads their semester course schedule PDF once to detect their weekly free time slots and enrolled courses. (2) On the interactive building floorplan, the student views real-time room statuses: Green (Available), Yellow (Open Study Pod accepting peers for a specific course), or Red (Full). (3) The student either books an available room for up to two hours or joins an existing Open Study Pod studying the same course during their free gap. (4) Upon arriving, at least one member must scan a dynamic QR code at the room within 15 minutes; otherwise, the system automatically releases the room for other students. The initial version covers two campus buildings and 15 study spaces."),
            ("5. How It Differs from Existing Alternatives", "Current campus booking forms operate in isolated silos without real-time occupancy updates or no-show release rules, while group chats require manual coordination to find study partners. NookSync uniquely links physical space booking with automated 15-minute QR check-in enforcement and schedule-aware \"Open Study Pod\" matching."),
            ("6. Planned Technologies", "A mobile-responsive React and Next.js web application using Supabase PostgreSQL and Supabase Realtime WebSockets for instant status updates, interactive floorplans built with the tldraw canvas SDK, and a Shadcn UI dashboard for building staff. We plan to use MarkItDown and Google LangExtract (powered by Gemini) solely during onboarding to parse course codes and free time blocks from student schedule PDFs."),
            ("7. Expected Benefit and Development Plan", "Expected benefit: cut average room and study-partner search time to under 3 minutes and reduce unclaimed ghost bookings by over 60%, measured from check-in logs during a two-week pilot with 25 students. Plan: Week 1 database, floorplan UI, and booking logic; Week 2 QR auto-release and schedule parser; Week 3 pilot test and bug fixes. The main risk is physical QR code tampering, which we mitigate using rotating time-based tokens displayed on a staff tablet or verified via campus Wi-Fi/geolocation bounds.")
        ],
        "sources": "[1] Campus study space observation and student survey conducted by the team (November 2026)."
    },
    "Option_C_CompassAI_Abstract": {
        "team": "[Your Team Name]",
        "title": "CompassAI: Campus Opportunity Tracker and Complementary Team Matcher",
        "case": "Case 1: Smarter Campus and Learning",
        "members": "[Member A (leader), Member B, Member C, Member D]",
        "sections": [
            ("1. Problem", "Information about scholarships, academic competitions, research assistantships, and campus grants is heavily fragmented across dozens of WhatsApp groups, Instagram posters, and faculty noticeboards. Consequently, students miss critical deadlines because requirements are buried inside unstructured poster images, and many qualified students fail to participate in competitions or research projects because they cannot find teammates with complementary technical and non-technical skills in time."),
            ("2. Intended Users", "Undergraduate students seeking scholarships, hackathons, PKM grants, or faculty research opportunities, as well as student organizations and laboratory coordinators who publish recruitment announcements."),
            ("3. Supporting Observations or Evidence", "In a survey of [N, e.g., 42] undergraduate students [1], [X, e.g., 34] stated they had missed at least one scholarship or competition deadline in the past year because announcements were buried in chat histories. Additionally, [Y, e.g., 29] respondents reported canceling plans to join a competition due to difficulty finding teammates outside their immediate major. Our review of 50 recent campus announcements showed that over 70% were distributed exclusively as image posters without searchable text or calendar links."),
            ("4. Proposed Solution and Core User Flow", "CompassAI is a web platform that converts scattered campus announcements into structured, eligibility-matched opportunities and connects students into balanced project teams. The core user flow has four steps: (1) A student signs in and completes a skill and academic profile (GPA range, major, semester, and skills) or uploads their CV PDF. (2) Student organizations or users submit opportunity poster images or webpage links, which the platform automatically extracts into structured cards showing deadlines, GPA/semester eligibility, and required roles. (3) The student browses a personalized feed ranked by eligibility match, saves an opportunity to their deadline tracker, and clicks \"Find Teammates.\" (4) The student filters or matches with peers who have complementary roles (such as backend developer, UI/UX designer, or business analyst) for that specific event and opens a shared preparation checklist. The first version supports scholarships and student competitions at our university."),
            ("5. How It Differs from Existing Alternatives", "Social media feeds and chat groups cannot filter opportunities by a student's GPA, semester, or major, and general job boards do not support campus competition team formation. CompassAI differs by turning raw poster images into structured eligibility filters and matching students based on complementary team roles rather than identical backgrounds."),
            ("6. Planned Technologies", "A Next.js and TypeScript web platform backed by Supabase (PostgreSQL, pgvector, and authentication). Poster image and webpage extraction are handled by a Python FastAPI service using PaddleOCR, Crawl4AI, MarkItDown, and Google LangExtract (with Gemini structured outputs) to parse deadlines and eligibility criteria into JSON."),
            ("7. Expected Benefit and Development Plan", "Expected benefit: reduce time spent searching and verifying opportunity eligibility from 30 minutes to under 2 minutes, and enable teams to form within 48 hours during a two-week test with 30 students. Plan: Week 1 opportunity database and OCR/web extraction pipeline, Week 2 eligibility matching and team finder flow, Week 3 campus user testing. The main risk is inaccurate OCR extraction from stylized posters, which we address through a mandatory human confirmation preview before publishing any listing.")
        ],
        "sources": "[1] Student survey on scholarship and competition information access and audit of 50 campus announcements (November 2026)."
    },
    "Option_D_OmniNook_GoldenThread_Abstract": {
        "team": "[Your Team Name]",
        "title": "OmniNook: QR-Verified Study Pods with Shared Canvas and Grounded Course RAG",
        "case": "Case 1: Smarter Campus and Learning",
        "members": "[Member A (leader), Member B, Member C, Member D]",
        "sections": [
            ("1. Problem", "Undergraduate students face two connected barriers when studying between lectures: shared campus discussion rooms suffer from fragmented availability info and \"ghost bookings\" where reserved spaces sit empty, and once students finally gather—or try to find peers taking the same course—they lack a unified workspace to co-solve visual problems and query dense lecture PDFs together."),
            ("2. Intended Users", "First- and second-year undergraduate students who study in small groups or seek course peers during 1-to-3-hour gaps between classes (10:00 to 17:00), as well as campus building staff who oversee shared study rooms."),
            ("3. Supporting Observations or Evidence", "In a preliminary campus observation and survey of [N, e.g., 40] students [1], [X, e.g., 32] reported losing 15 to 25 minutes searching for open group study spaces during peak hours, while an estimated 25% of reserved rooms went unclaimed due to no-shows. Additionally, [Y, e.g., 29] respondents stated that coordinating shared notes, whiteboard sketches, and lecture slides across separate apps slows down group problem-solving."),
            ("4. Proposed Solution and Core User Flow", "OmniNook is a web application that connects physical study room booking and peer matching directly to a shared digital study workspace. The core user flow has four steps: (1) A student signs in with their campus account and uploads their semester schedule PDF once so the system detects their enrolled courses and free time blocks. (2) On a live building map, the student books a free room (Green) or joins an \"Open Study Pod\" (Yellow) of peers studying the same course. (3) Upon arriving, members scan the room's dynamic QR code within 15 minutes to confirm occupancy—otherwise the room is automatically released; scanning the QR immediately unlocks a synchronized digital session for everyone at that table. (4) Inside this session, members co-draw diagrams on an embedded Excalidraw whiteboard, ask a course-grounded AI tutor questions cited directly to their uploaded lecture PDFs, and export a summary sheet. The first version covers one campus building (12 rooms) and two courses."),
            ("5. How It Differs from Existing Alternatives", "Existing campus booking forms neither release unclaimed rooms automatically nor help solo students join course peers, while digital whiteboard and AI chat tools operate completely disconnected from physical study groups. OmniNook uniquely uses the 15-minute physical QR check-in as the trigger that both eliminates ghost bookings and launches an instant multiplayer Excalidraw and RAG study session."),
            ("6. Planned Technologies", "A responsive Next.js and TypeScript web app backed by Supabase (PostgreSQL, pgvector, authentication, and Realtime WebSockets). The shared visual workspace embeds @excalidraw/excalidraw and BlockNote with Yjs sync, while a Python FastAPI service uses MarkItDown, Google LangExtract, and the Gemini API to parse schedule PDFs and provide citation-grounded answers from uploaded course slides."),
            ("7. Expected Benefit and Development Plan", "Expected benefit: reduce room and study-partner search time to under 3 minutes, cut ghost bookings by 60%, and improve group task completion speed during a two-week trial with 24 students, measured via check-in logs and session telemetry. Plan: Week 1 live room map, booking, and QR auto-release; Week 2 schedule parser and QR-triggered Excalidraw pod; Week 3 course PDF RAG and user testing. The main risk is unstable building Wi-Fi during check-in, mitigated by offline-tolerant local state sync and a staff override view.")
        ],
        "sources": "[1] Preliminary team observation of campus study rooms and student survey (November 2026)."
    }
}

for name, data in abstracts.items():
    sections_html = "\n".join(
        f"<p><strong>{sec_title}.</strong> {sec_body}</p>"
        for sec_title, sec_body in data["sections"]
    )
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{data['title']}</title>
<style>
  @page {{ size: A4; margin: 2.2cm; }}
  body {{ font-family: Arial, Helvetica, sans-serif; font-size: 10.5pt; line-height: 1.38; color: #111; margin: 0; padding: 0; }}
  table {{ width: 100%; border-collapse: collapse; margin-bottom: 14px; font-size: 10pt; }}
  td {{ border: 1px solid #444; padding: 6px 10px; vertical-align: top; }}
  td.label {{ width: 22%; font-weight: bold; background: #f3f4f6; }}
  h2 {{ font-size: 11.5pt; margin: 10px 0 6px 0; }}
  p {{ margin: 0 0 8px 0; text-align: justify; }}
  .sources {{ margin-top: 12px; font-size: 9.5pt; color: #333; border-top: 1px solid #ccc; padding-top: 6px; }}
</style>
</head>
<body>
  <table>
    <tr><td class="label">Team name</td><td>{data['team']}</td></tr>
    <tr><td class="label">Project title</td><td>{data['title']}</td></tr>
    <tr><td class="label">Selected case</td><td>{data['case']}</td></tr>
    <tr><td class="label">Members</td><td>{data['members']}</td></tr>
  </table>
  <h2>Abstract</h2>
  {sections_html}
  <div class="sources">
    <strong>Source Acknowledgments.</strong> {data['sources']}
  </div>
</body>
</html>"""
    html_path = os.path.join(out_dir, f"{name}.html")
    pdf_path = os.path.join(out_dir, f"{name}.pdf")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Saved HTML:", html_path)

    # Render to PDF via Edge headless if available
    edge_paths = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
    ]
    for ep in edge_paths:
        if os.path.exists(ep):
            subprocess.run([ep, "--headless", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={pdf_path}", html_path], check=False)
            if os.path.exists(pdf_path):
                print("Generated PDF:", pdf_path)
            break

