from setuptools import setup, find_packages
setup(
    name = 'report_top_customers',
    version = '1.0',
    packages = find_packages(include = ['job*', ]),
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.3.1'],
    entry_points = {
'console_scripts' : [
'main = job.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)
