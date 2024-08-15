import streamlit as st
import os

# 65개의 HTML 파일 리스트 (공백을 포함한 파일 이름)
html_files = {
    "Adapting this playbook as you scale": "html_files/Adapting this playbook as you scale.html",
    "Advertising open positions": "html_files/Advertising open positions.html",
    "Assessing performance": "html_files/Assessing performance.html",
    "B2B go-to-market": "html_files/B2B go-to-market.html",
    "Bar-raiser - interview playbook": "html_files/Bar-raiser - interview playbook.html",
    "Bar-raiser interview scorecard": "html_files/Bar-raiser interview scorecard.html",
    "Best practices for Jira_Notion roadmaps": "html_files/Best practices for Jira_Notion roadmaps.html",
    "Board Management": "html_files/Board Management.html",
    "Business review meetings": "html_files/Business review meetings.html",
    "Calculating ROI": "html_files/Calculating ROI.html",
    "CEO Office & Chief of Staff": "html_files/CEO Office & Chief of Staff.html",
    "CEO Office hiring": "html_files/CEO Office hiring.html",
    "CEO Office structure": "html_files/CEO Office structure.html",
    "Company meeting routines": "html_files/Company meeting routines.html",
    "Compensation benchmarks": "html_files/Compensation benchmarks.html",
    "Compensation": "html_files/Compensation.html",
    "Departments": "html_files/Departments.html",
    "Example case study for people management and hiring": "html_files/Example case study for people management and hiring.html",
    "Example hiring process document – Data Analyst": "html_files/Example hiring process document – Data Analyst.html",
    "Founder best practices": "html_files/Founder best practices.html",
    "Functions": "html_files/Functions.html",
    "Handling poor performance": "html_files/Handling poor performance.html",
    "Hire scale-up-ready profiles": "html_files/Hire scale-up-ready profiles.html",
    "Hiring Account Executives": "html_files/Hiring Account Executives.html",
    "Hyper-structure hiring": "html_files/Hyper-structure hiring.html",
    "Ideal board design": "html_files/Ideal board design.html",
    "Internal recruitment org": "html_files/Internal recruitment org.html",
    "Interviewer certification": "html_files/Interviewer certification.html",
    "KPI standards": "html_files/KPI standards.html",
    "Maximising founder impact": "html_files/Maximising founder impact.html",
    "ML Engineer_Data Scientist hiring playbook": "html_files/ML Engineer_Data Scientist hiring playbook.html",
    "Offer calls": "html_files/Offer calls.html",
    "Offer letters": "html_files/Offer letters.html",
    "One-to-one meetings": "html_files/One-to-one meetings.html",
    "One-to-one-meetings": "html_files/One-to-one-meetings.html",
    "Pay reviews": "html_files/Pay reviews.html",
    "People management and hiring interview playbook": "html_files/People management and hiring interview playbook.html",
    "Performance bonuses": "html_files/Performance bonuses.html",
    "Performance management": "html_files/Performance management.html",
    "Performance Team": "html_files/Performance Team.html",
    "Phase #1 - learn": "html_files/Phase #1 - learn.html",
    "Phase #2 – scale": "html_files/Phase #2 – scale.html",
    "Phase #3 – go multi-channel": "html_files/Phase #3 – go multi-channel.html",
    "Probation": "html_files/Probation.html",
    "Problem Solving case study library": "html_files/Problem Solving case study library.html",
    "Problem Solving interview playbook": "html_files/Problem Solving interview playbook.html",
    "Product Owner hiring playbook": "html_files/Product Owner hiring playbook.html",
    "Product review meetings": "html_files/Product review meetings.html",
    "Product teams": "html_files/Product teams.html",
    "Project More meetings": "html_files/Project More meetings.html",
    "Promotions": "html_files/Promotions.html",
    "QuantumLight Capital_mail": "html_files/QuantumLight Capital_mail.html",
    "Quarterly goals": "html_files/Quarterly goals.html",
    "Recruiter incentives": "html_files/Recruiter incentives.html",
    "Reference checks": "html_files/Reference checks.html",
    "Resources for recruiters": "html_files/Resources for recruiters.html",
    "Retaining candidates": "html_files/Retaining candidates.html",
    "Role-specific Playbooks": "html_files/Role-specific Playbooks.html",
    "Sales enablement": "html_files/Sales enablement.html",
    "Screening candidates": "html_files/Screening candidates.html",
    "Software Engineer - hiring playbook": "html_files/Software Engineer - hiring playbook.html",
    "Sourcing candidates": "html_files/Sourcing candidates.html",
    "Standardised hiring processes": "html_files/Standardised hiring processes.html",
    "Talent framework": "html_files/Talent framework.html",
    "Yearly planning": "html_files/Yearly planning.html",
}

# 사용자로부터 HTML 파일 선택
selected_page = st.selectbox("Choose an HTML page to display", list(html_files.keys()))

# 선택된 HTML 파일 경로
html_file_path = html_files[selected_page]

# HTML 파일 읽기
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# HTML 렌더링
st.components.v1.html(html_content, height=800, scrolling=True)
