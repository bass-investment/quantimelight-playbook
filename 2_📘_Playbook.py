import streamlit as st
import streamlit.components.v1 as components
from bs4 import BeautifulSoup
import os
import base64
import random

document_hierarchy = {
    "Maximising founder impact": {
        "One-to-one meetings": {},
        "Business review meetings": {
            "Best practices for Jira/Notion Roadmaps": {},
        },
        "Product review meetings": {},
        "Project More meetings": {},
        "Founder best practices": {},
    },
    "CEO Office & Chief of Staff": {
        "CEO Office structure": {},
        "CEO Office hiring": {}
    },
    "Hiring": {
        "Internal recruitment org": {
            "Recruiter Incentives": {},
            "Resources for recruiters": {
                "Retaining Candidates": {},
                "Advertising open positions": {},
                "Screening Candidates": {},
                "Offer calls": {},
                "Offer letters": {}
            },
            "Hire scale-up-ready profiles": {
                "Problem Solving interview playbook": {
                    "Problem Solving case study library": {}
                },
                "Bar-raiser - interview playbook": {
                    "Bar-raiser interview scorecard": {}
                },
                "People management and hiring interview playbook": {},
                "Probation": {}
            },
            "Hyper-structure hiring": {
                "Talent framework": {
                    "Standardised hiring processes": {
                        "Example hiring process document – Data Analyst": {},
                    },
                },
                "Reference checks": {},
                "Interviewer certification": {},
                "Role-specific playbooks": {
                    "Product Owner hiring playbook": {},
                    "ML Engineer_Data Scientist hiring playbook": {},
                    "Software Engineer - hiring playbook": {}
                },
                "Adapting this playbook as you scale": {}
            },
        }
    },
    "Performance management": {
        "Assessing performance": {},
        "Promotions": {},
        "Handling poor performance": {},
        "Performance Team": {},
        "Compensation": {
            "Compensation benchmarks": {},
            "Pay reviews": {},
            "Performance bonuses": {}
        }
    },
    "B2B go-to-market": {
        "Phase #1 - learn": {
            "Calculating ROI": {},
        },
        "Phase #2 – scale": {
            "Hiring Account Executives": {},
            "Sales enablement": {}
        },
        "Phase #3 – go multi-channel": {}
    },
    "Org design": {
        "Product Teams": {},
        "Departments": {},
        "Functions": {}
    },
    "Setting goals": {
        "KPI standards": {},
        "Yearly planning": {},
        "Quarterly goals": {}
    },
    "Company meeting routines": {
        "One-to-one meetings": {},
        "Business review meetings": {}
    },
    "Board management": {
        "Ideal board design": {}
    }
}


def get_image_as_base64(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()


def load_config() -> dict:
    st.set_page_config(layout='wide')

    qp = st.query_params.to_dict()
    if 'doc' in qp:
        st.session_state.doc = qp['doc']
        st.query_params.clear()

    elif 'doc' not in st.session_state:
        st.session_state.doc = "One-to-one meetings"

    st.markdown(
        """
       <style>
       [data-testid="stSidebar"][aria-expanded="true"]{
           min-width: 300px;
           max-width: 300px;
       }
       .reportview-container .main .block-container{{
        {max-width: 3600px;}
        }}
       """,
        unsafe_allow_html=True,
    )


def render_docs(doc: str):
    try:
        doc = doc.replace("/", "_")

        Htmlfile = open(f"src_kor/{doc}.html", 'r', encoding="utf-8")

    except FileNotFoundError:
        st.error(f"Document {doc} not found")
        return False

    soup = BeautifulSoup(Htmlfile.read(), "html.parser")

    title = soup.find("h1").text

    src = (soup
           .find("div", {"class": "container docs-main"})
           .find("div", {"class": "docs-main-content"})
           .find("div", {"class": "content_block"})
           .find("div", {"id": "partialViewContainer"})
           .find("div", {"id": "doc_content_block"})
           .find("div", {"class": "content_container"})
           .find("div", {"class": "content_container_text_sec"})
           .find("div", {"class": "content_container_text_sec_in"})
           .find("div", {"class": "content_block_text"})
           )

    for img in src.find_all('img'):
        if img['src'].startswith('./'):
            image_file = img['src'].split('/')[-1]
            rich_path = os.getcwd() + '/src_kor/' + doc + "_files/" + image_file
            # os.listdir('./app/src/One-to-one meetings_files')
            image_base65 = get_image_as_base64(rich_path)
            img['src'] = f"data:image/png;base64,{image_base65}"
            if 'style' not in img.attrs:
                img['style'] = 'max-width: 50%;'

    """
    for href in src.find_all('a'):
        # find all links in the document, and replace them with the correct link
        href.decompose()
    """

    result = src.prettify()

    head = soup.find("head")
    head = head.prettify()

    st.title('📘 ' + title)

    components.html(head + result, scrolling=True, height=4000, width=1000)


load_config()


with st.sidebar:
    for category in document_hierarchy.keys():
        with st.expander(category):
            docs = document_hierarchy[category]
            # tree의 모든 원소 찾아오기

            emoji_per_depth = {
                0: "📚",
                1: "📖",
                2: "📝",
                3: "📌",
                4: "📍",
            }


            def set_doc(doc):
                st.session_state.doc = doc


            def search_tree(tree, depth=0):
                for key in tree.keys():
                    if tree[key]:
                        st.button(f"{emoji_per_depth[depth]}️ {key}",
                                  on_click=set_doc,
                                  args=(key,),
                                  key=key+str(random.randint(0, 100)),
                                  use_container_width=True)
                        search_tree(tree[key], depth=depth + 1)
                    else:
                        st.button(f"{emoji_per_depth[depth]} {key}",
                                  on_click=set_doc,
                                  args=(key,),
                                  key=key+str(random.randint(0, 100)),
                                  use_container_width=True
                                  )

            try:
                search_tree(docs)
            except st.exception:
                st.rerun()


render_docs(st.session_state.doc)
