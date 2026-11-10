import os
import base64
import shutil
import subprocess

out_dir = r"p:\Hackaton Google\edo\submissions"
assets_dir = os.path.join(out_dir, "twibbon_assets")
os.makedirs(assets_dir, exist_ok=True)

# 1. Generate Updated Abstract PDF (with corrected spelling: Allfridho Prima Anjaynata Saragi)
academiaflow_baton_abstract = {
    "team": "Pray First",
    "title": "AcademiaFlow: Tracking Who Holds the Baton in Group Projects and Thesis Supervision",
    "case": "Case 1: Smarter Campus and Learning",
    "members": "Allfridho Prima Anjaynata Saragi (Leader), Mikhael Yuli Ananda Elvan Permana, Nathanael Christian Putra",
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

edge_paths = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
]

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
    for ep in edge_paths:
        if os.path.exists(ep):
            subprocess.run([ep, "--headless", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={pdf_path}", html_path], check=False)
            if os.path.exists(pdf_path):
                print("Generated Abstract PDF:", pdf_path)
            break

# 2. Generate Consolidated Twibbon Evidence PDF
twibbon_members = [
    {
        "role": "Team Leader",
        "name": "Allfridho Prima Anjaynata Saragi",
        "handle": "@allfridhosaragi",
        "profile_url": "https://www.instagram.com/allfridhosaragi/",
        "post_url": "https://www.instagram.com/p/DfcgvAQzgrl/?xtok=dHozaGQ2d21iYTBi",
        "img_src": r"C:\Users\Pedo\.gemini\antigravity\brain\adf50785-9d54-4504-b89b-9598dadfc8c2\.user_uploaded\media_1794312580625_5a8b3291.jpg",
        "asset_name": "1_allfridho_twibbon.jpg"
    },
    {
        "role": "Member 2",
        "name": "Mikhael Yuli Ananda Elvan Permana",
        "handle": "@myeap29",
        "profile_url": "https://www.instagram.com/myeap29/",
        "post_url": "https://www.instagram.com/p/Dfcg91Bgjs5/?srtk=Z3YyOWN3MnU0bWlt",
        "img_src": r"C:\Users\Pedo\.gemini\antigravity\brain\adf50785-9d54-4504-b89b-9598dadfc8c2\.user_uploaded\media_1794312866773_54ea0fe6.jpg",
        "asset_name": "2_mikhael_twibbon.jpg"
    },
    {
        "role": "Member 3",
        "name": "Nathanael Christian Putra",
        "handle": "@nathananaell",
        "profile_url": "https://www.instagram.com/nathananaell/",
        "post_url": "https://www.instagram.com/p/DfcirtFT8oH/?exln=MTcwdm0yczYyc25qcQ==",
        "img_src": r"C:\Users\Pedo\.gemini\antigravity\brain\adf50785-9d54-4504-b89b-9598dadfc8c2\.user_uploaded\media_1794312820260_0a6f3b61.jpg",
        "asset_name": "3_nathanael_twibbon.jpg"
    }
]

for m in twibbon_members:
    dst = os.path.join(assets_dir, m["asset_name"])
    shutil.copy2(m["img_src"], dst)
    with open(dst, "rb") as img_f:
        m["data_uri"] = "data:image/jpeg;base64," + base64.b64encode(img_f.read()).decode("ascii")

cards_html = ""
for idx, m in enumerate(twibbon_members, start=1):
    cards_html += f"""
    <div class="card">
      <div class="card-header">#{idx} — {m['role']}</div>
      <div class="card-meta">
        <div><strong>Full Name:</strong><br>{m['name']}</div>
        <div><strong>Instagram Handle:</strong><br><a href="{m['profile_url']}">{m['handle']}</a></div>
        <div><strong>Twibbon Post URL:</strong><br><a href="{m['post_url']}">{m['post_url']}</a></div>
      </div>
      <div class="img-wrap">
        <img src="{m['data_uri']}" alt="{m['name']} Twibbon Screenshot" />
      </div>
    </div>
    """

twibbon_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>STACK 2026 Twibbon Evidence — Team Pray First</title>
<style>
  @page {{ size: A4; margin: 1.2cm 1.4cm; }}
  body {{ font-family: Arial, Helvetica, sans-serif; color: #111; margin: 0; padding: 0; font-size: 9pt; }}
  .header {{ border-bottom: 2px solid #1e293b; padding-bottom: 8px; margin-bottom: 10px; }}
  .header h1 {{ font-size: 13pt; margin: 0 0 4px 0; color: #0f172a; }}
  .header p {{ margin: 0; font-size: 9.2pt; color: #334155; }}
  table.summary {{ width: 100%; border-collapse: collapse; margin-bottom: 12px; font-size: 8.6pt; }}
  table.summary th, table.summary td {{ border: 1px solid #475569; padding: 4px 7px; text-align: left; vertical-align: middle; }}
  table.summary th {{ background: #f1f5f9; font-weight: bold; }}
  .grid {{ display: flex; flex-direction: row; justify-content: space-between; gap: 10px; width: 100%; }}
  .card {{ width: 32%; border: 1px solid #64748b; border-radius: 6px; overflow: hidden; background: #fff; display: flex; flex-direction: column; }}
  .card-header {{ background: #0f172a; color: #fff; font-weight: bold; padding: 5px 8px; font-size: 9pt; text-align: center; }}
  .card-meta {{ padding: 6px 8px; font-size: 8pt; line-height: 1.32; border-bottom: 1px solid #cbd5e1; background: #f8fafc; min-height: 112px; word-break: break-all; }}
  .card-meta div {{ margin-bottom: 5px; }}
  .card-meta a {{ color: #1d4ed8; text-decoration: underline; }}
  .img-wrap {{ padding: 6px; text-align: center; background: #000; flex: 1; display: flex; align-items: center; justify-content: center; }}
  .img-wrap img {{ width: 100%; max-height: 540px; object-fit: contain; display: block; border-radius: 3px; }}
</style>
</head>
<body>
  <div class="header">
    <h1>STACK 2026 by GDGoC ITB — Consolidated Twibbon Evidence</h1>
    <p><strong>Team Name:</strong> Pray First &nbsp;|&nbsp; <strong>Selected Case:</strong> Case 1: Smarter Campus and Learning &nbsp;|&nbsp; <strong>Project:</strong> AcademiaFlow</p>
  </div>

  <table class="summary">
    <thead>
      <tr>
        <th style="width: 5%;">No</th>
        <th style="width: 14%;">Role</th>
        <th style="width: 28%;">Member Full Name</th>
        <th style="width: 16%;">Instagram Handle</th>
        <th style="width: 37%;">Twibbon Post URL</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>1</td>
        <td>Team Leader</td>
        <td>Allfridho Prima Anjaynata Saragi</td>
        <td><a href="https://www.instagram.com/allfridhosaragi/">@allfridhosaragi</a></td>
        <td><a href="https://www.instagram.com/p/DfcgvAQzgrl/?xtok=dHozaGQ2d21iYTBi">https://www.instagram.com/p/DfcgvAQzgrl/?xtok=dHozaGQ2d21iYTBi</a></td>
      </tr>
      <tr>
        <td>2</td>
        <td>Member</td>
        <td>Mikhael Yuli Ananda Elvan Permana</td>
        <td><a href="https://www.instagram.com/myeap29/">@myeap29</a></td>
        <td><a href="https://www.instagram.com/p/Dfcg91Bgjs5/?srtk=Z3YyOWN3MnU0bWlt">https://www.instagram.com/p/Dfcg91Bgjs5/?srtk=Z3YyOWN3MnU0bWlt</a></td>
      </tr>
      <tr>
        <td>3</td>
        <td>Member</td>
        <td>Nathanael Christian Putra</td>
        <td><a href="https://www.instagram.com/nathananaell/">@nathananaell</a></td>
        <td><a href="https://www.instagram.com/p/DfcirtFT8oH/?exln=MTcwdm0yczYyc25qcQ==">https://www.instagram.com/p/DfcirtFT8oH/?exln=MTcwdm0yczYyc25qcQ==</a></td>
      </tr>
    </tbody>
  </table>

  <div class="grid">
    {cards_html}
  </div>
</body>
</html>"""

twibbon_html_path = os.path.join(out_dir, "FINAL_PrayFirst_Twibbon_Evidence.html")
twibbon_pdf_path = os.path.join(out_dir, "FINAL_PrayFirst_Twibbon_Evidence.pdf")
with open(twibbon_html_path, "w", encoding="utf-8") as f:
    f.write(twibbon_html)
print("Saved Twibbon HTML:", twibbon_html_path)

for ep in edge_paths:
    if os.path.exists(ep):
        subprocess.run([ep, "--headless", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={twibbon_pdf_path}", twibbon_html_path], check=False)
        if os.path.exists(twibbon_pdf_path):
            print("Generated Twibbon PDF:", twibbon_pdf_path)
        break
