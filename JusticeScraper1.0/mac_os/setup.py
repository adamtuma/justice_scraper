from setuptools import setup

setup(app=["JusticeScraper_mac.py"],options={"py2app":{"argv_emulation":True, "packages":['docx', 'requests']}},setup_requires=["py2app"])