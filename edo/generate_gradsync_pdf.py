import os
import subprocess

out_dir = r"p:\Hackaton Google\edo\submissions"
os.makedirs(out_dir, exist_ok=True)

academiaflow_abstract = {
    "team": "Pray First",
    "title": "AcademiaFlow: Unified Student Lifecycle Workspace for Course Planning, Lecture Mastery, Accountable Groupwork, Internships, and Thesis SLA Tracking",
    "case": "Case 1: Smarter Campus and Learning",
    "members": "Allfridhoo Prima Anjaynata Saragi (Leader), Mikhael Yuli Ananda Elvan Permana, Nathanael Christian Putra",
    "sections": [
        (
            "1. Problem",
            "Across their university lifecycle, undergraduates face four connected bottlenecks caused by rigid legacy portals and fragmented chat groups: (a) during course registration (KRS/FRS), students lack real syllabus previews, face server slowdowns, and get separated from their study circle; (b) in lectures and group projects (Tugas Besar), fast-paced slides hinder comprehension while lecturers cannot track individual progress or prevent free-riders; (c) in semesters 5–7, scholarship and MoU-internship posters get buried in chat groups, delaying credit (SKS) conversion and alumni networking; and (d) during thesis (Tugas Akhir) supervision, unstated advisor quotas, messaging anxiety, and extended advisor inactivity stall graduation."
        ),
        (
            "2. Intended Users",
            "First- through final-year undergraduate students, course lecturers supervising team assignments, and program coordinators (Kaprodi/Dosen Wali) overseeing credit conversions and thesis advisor workloads."
        ),
        (
            "3. Supporting Observations or Evidence",
            "From multi-campus workflow audits and preliminary interviews across ITB, Telkom University Surabaya, and UNESA [1], students identified stalled thesis revisions from overloaded advisors as their top graduation bottleneck, compounded by untransparent advisor quotas and WhatsApp messaging anxiety. Respondents also confirmed frequent free-riding in lecturer-assigned group projects (currently tracked via manual sheets), buried scholarship/internship posters in student association chats, and registration quota clashes."
        ),
        (
            "4. Proposed Solution and Core User Flow",
            "AcademiaFlow is a semester-adaptive web workspace using one-click KRS PDF import: (1) Smart KRS & Circle Sync: previews 14-week syllabi, practicum schedules, and lecturer styles while simulating conflict-free parallel classes with live quota indicators; (2) StudyPulse & Accountable Groupwork: students drop lecture audio and slide PDFs to generate slide-synced transcripts, Socratic explanations, FSRS active-recall quizzes, and shared notes, while team boards auto-intersect free hours, trigger relay handover alerts when a prerequisite task finishes, stream contribution logs to lecturers, and allow objective free-rider escalation; (3) Adaptive Opportunity & Alumni Hub (Semesters 5–7): surfaces filtered scholarships, MoU internships with 20-SKS conversion simulators, activity-point (TAK/SKKM) trackers, and opt-in alumni contacts (WA/IG/LinkedIn); and (4) Thesis SLA & In-App Supervision: provides semantic advisor matching, standardized consultation tickets with one-click logbook approval, and 21-day inactivity alerts recommending replacement advisors to coordinators."
        ),
        (
            "5. How It Differs from Existing Alternatives",
            "Legacy portals (SIX, iGracias, SIAKAD) only record registration and final grades, whereas generic chat, note, and kanban apps lack KRS schedule intersection, slide-synced audio active recall, lecturer contribution telemetry, MoU SKS mapping, and advisor SLA rebalancing. AcademiaFlow unifies these workflows without requiring write-access to university databases."
        ),
        (
            "6. Planned Technologies",
            "A Next.js 15 and TypeScript web app backed by Supabase (PostgreSQL, pgvector, Auth, and Realtime WebSockets). Collaborative notes and quizzes use BlockNote, Yjs, and ts-fsrs, while a Python FastAPI service uses faster-whisper, MarkItDown, PaddleOCR, and Google LangExtract (Gemini API) to parse audio, KRS/syllabus PDFs, and posters."
        ),
        (
            "7. Expected Benefit and Development Plan",
            "Expected benefit: cut exam review and group coordination time by 50%, curb free-riding, and speed up SKS consultation and logbook approval in a two-week trial with 30 students. Plan: Week 1 KRS Circle Sync and StudyPulse/Groupwork Engine; Week 2 Opportunity/Alumni Hub and Thesis SLA Rebalancer; Week 3 pilot testing. Unavailable campus APIs are mitigated via PDF parsing."
        )
    ],
    "sources": "[1] Multi-campus student workflow audit and field interviews across Institut Teknologi Bandung (ITB), Telkom University Surabaya, and Universitas Negeri Surabaya (UNESA) (November 2026)."
}

body_text = " ".join(f"{sec_title} {sec_body}" for sec_title, sec_body in academiaflow_abstract["sections"])
word_count = len(body_text.split())
body_only_count = len(" ".join(sec_body for _, sec_body in academiaflow_abstract["sections"]).split())
print(f"FINAL AcademiaFlow Abstract Word Count: {body_only_count} words (body only) / {word_count} words (with headers) (Target: 300-500 words)")

for filename in ["FINAL_AcademiaFlow_Abstract", "Option_E_GradSync_Unified_Abstract"]:
    sections_html = "\n".join(
        f"<p><strong>{sec_title}.</strong> {sec_body}</p>"
        for sec_title, sec_body in academiaflow_abstract["sections"]
    )
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{academiaflow_abstract['title']}</title>
<style>
  @page {{ size: A4; margin: 2.1cm; }}
  body {{ font-family: Arial, Helvetica, sans-serif; font-size: 10.2pt; line-height: 1.36; color: #111; margin: 0; padding: 0; }}
  table {{ width: 100%; border-collapse: collapse; margin-bottom: 12px; font-size: 9.8pt; }}
  td {{ border: 1px solid #444; padding: 5px 10px; vertical-align: top; }}
  td.label {{ width: 22%; font-weight: bold; background: #f3f4f6; }}
  h2 {{ font-size: 11.2pt; margin: 8px 0 6px 0; }}
  p {{ margin: 0 0 7px 0; text-align: justify; }}
  .sources {{ margin-top: 10px; font-size: 9.2pt; color: #333; border-top: 1px solid #ccc; padding-top: 5px; }}
</style>
</head>
<body>
  <table>
    <tr><td class="label">Team name</td><td>{academiaflow_abstract['team']}</td></tr>
    <tr><td class="label">Project title</td><td>{academiaflow_abstract['title']}</td></tr>
    <tr><td class="label">Selected case</td><td>{academiaflow_abstract['case']}</td></tr>
    <tr><td class="label">Members</td><td>{academiaflow_abstract['members']}</td></tr>
  </table>
  <h2>Abstract</h2>
  {sections_html}
  <div class="sources">
    <strong>Source Acknowledgments.</strong> {academiaflow_abstract['sources']}
  </div>
</body>
</html>"""
    html_path = os.path.join(out_dir, f"{filename}.html")
    pdf_path = os.path.join(out_dir, f"{filename}.pdf")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Saved HTML:", html_path)

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
