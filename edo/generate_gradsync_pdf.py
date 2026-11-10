import os
import subprocess

out_dir = r"p:\Hackaton Google\edo\submissions"
os.makedirs(out_dir, exist_ok=True)

academiaflow_baton_abstract = {
    "team": "Pray First",
    "title": "AcademiaFlow: Tracking Who Holds the Baton in Group Projects and Thesis Supervision",
    "case": "Case 1: Smarter Campus and Learning",
    "members": "Allfridhoo Prima Anjaynata Saragi (Leader), Mikhael Yuli Ananda Elvan Permana, Nathanael Christian Putra",
    "sections": [
        (
            "1. Problem",
            "Shared academic work often stalls silently because nobody sees who is responsible for the next step. In lecturer-assigned group projects (Tugas Besar), free-riders stay invisible while peers wait on unfinished dependencies, and lecturers judge contribution through manual sheets filled in at the end. In thesis supervision (Tugas Akhir), drafts wait weeks for advisor feedback while students hesitate to follow up on WhatsApp for fear of being impolite. Both delays surface only after deadlines are missed."
        ),
        (
            "2. Intended Users",
            "Undergraduates in lecturer-assigned group projects, final-year students and their thesis advisors, and lecturers or thesis coordinators who need early, fair visibility into stalled work. The first version targets computing programs."
        ),
        (
            "3. Supporting Observations or Evidence",
            "Evidence comes from our team's experience at Telkom University Surabaya and UNESA and an interview with an ITB student [1]. The ITB student reported that free-riding is very common when groups are not self-selected, that contribution is recorded on manual sheets, and that every year some theses stall because busy advisors remain unresponsive; asked to rank four campus problems, they chose stalled supervision as most urgent. At UNESA, our teammate documented students commuting between two campuses for weekly logbook signatures."
        ),
        (
            "4. Proposed Solution and Core User Flow",
            "AcademiaFlow treats shared academic work as a baton with one current holder, a due date, and an evidence trail. Group projects: a lecturer creates an assignment and members split it into owned, dated sub-tasks; when a member finishes and attaches evidence, the next member is notified and must accept the handover, generating a live contribution timeline for the lecturer and an evidence-backed escalation option for inactive peers. Thesis: a student submits a draft or logbook entry, and the advisor approves or comments via a one-click email link without logging in. If the baton stays with an advisor beyond a program-set limit, the system sends polite reminders and alerts the coordinator with the timeline."
        ),
        (
            "5. How It Differs from Existing Alternatives",
            "Campus portals (SIX, iGracias, SIAKAD) and Google Classroom record submissions and grades, not who holds the work in between. Trello or Notion boards track tasks but lack accepted handovers, lecturer-facing contribution evidence, zero-login advisor approval links, and coordinator escalation. AcademiaFlow powers both student-to-student and student-to-advisor handoffs with one engine and needs no access to university databases."
        ),
        (
            "6. Planned Technologies",
            "A Next.js and TypeScript web app on Supabase (PostgreSQL, Auth, Realtime) for live handover alerts, scheduled functions for overdue checks, signed email links for advisor reviews, GitHub webhooks for commit evidence, and the Gemini API to summarize revisions and draft polite follow-up messages."
        ),
        (
            "7. Expected Benefit and Development Plan",
            "We expect fewer silent stalls, fairer individual grading, and faster advisor feedback, measured by handover delay between members, lecturer grading time, and days a draft waits for review. Plan: Week 1, baton engine and group-project flow; Week 2, thesis flow, advisor links, and escalation; Week 3, pilot with student groups and a lecturer. Low lecturer adoption risk is mitigated via zero-login links and PDF exports."
        )
    ],
    "sources": "[1] Pray First Team, Academic workflow observations at Telkom University Surabaya and Universitas Negeri Surabaya (UNESA), and field interview with an Institut Teknologi Bandung (ITB) undergraduate (November 2026)."
}

body_text = " ".join(f"{sec_title} {sec_body}" for sec_title, sec_body in academiaflow_baton_abstract["sections"])
word_count = len(body_text.split())
body_only_count = len(" ".join(sec_body for _, sec_body in academiaflow_baton_abstract["sections"]).split())
print(f"FINAL AcademiaFlow Baton Abstract Word Count: {body_only_count} words (body only) / {word_count} words (with headers) (Target: 300-500 words)")

for filename in ["FINAL_AcademiaFlow_Abstract", "FINAL_AcademiaFlow_Baton_Focused_Abstract"]:
    sections_html = "\n".join(
        f"<p><strong>{sec_title}.</strong> {sec_body}</p>"
        for sec_title, sec_body in academiaflow_baton_abstract["sections"]
    )
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{academiaflow_baton_abstract['title']}</title>
<style>
  @page {{ size: A4; margin: 1.8cm 2.0cm; }}
  body {{ font-family: Arial, Helvetica, sans-serif; font-size: 10pt; line-height: 1.36; color: #111; margin: 0; padding: 0; }}
  table {{ width: 100%; border-collapse: collapse; margin-bottom: 12px; font-size: 9.6pt; }}
  td {{ border: 1px solid #444; padding: 5px 9px; vertical-align: top; }}
  td.label {{ width: 20%; font-weight: bold; background: #f3f4f6; }}
  h2 {{ font-size: 11pt; margin: 8px 0 6px 0; }}
  p {{ margin: 0 0 7px 0; text-align: justify; }}
  .sources {{ margin-top: 10px; font-size: 8.8pt; line-height: 1.3; color: #333; border-top: 1px solid #ccc; padding-top: 5px; text-align: justify; }}
</style>
</head>
<body>
  <table>
    <tr><td class="label">Team name</td><td>{academiaflow_baton_abstract['team']}</td></tr>
    <tr><td class="label">Project title</td><td>{academiaflow_baton_abstract['title']}</td></tr>
    <tr><td class="label">Selected case</td><td>{academiaflow_baton_abstract['case']}</td></tr>
    <tr><td class="label">Members</td><td>{academiaflow_baton_abstract['members']}</td></tr>
  </table>
  <h2>Abstract</h2>
  {sections_html}
  <div class="sources">
    <strong>Source Acknowledgments.</strong> {academiaflow_baton_abstract['sources']}
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
