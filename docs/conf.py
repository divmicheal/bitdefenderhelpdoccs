import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'bitdefender-helpdocs'
author = 'Documentation Team'
release = '1.0'

extensions = [
    'sphinx_sitemap',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# IMPORTANT: Default ReadTheDocs URL
html_baseurl = "https://bittdefender.readthedocs.io/en/latest/"

# ✅ GOOGLE + BING VERIFICATION META TAG
html_meta = {
    "google-site-verification": "Cva8KgvW-eQpRtsdf8vIcSb023IJtLJfC8PxJAlQ0mc",
    "msvalidate.01": "739245F5D54BCBF40AC056DC0CBF5710"
}
