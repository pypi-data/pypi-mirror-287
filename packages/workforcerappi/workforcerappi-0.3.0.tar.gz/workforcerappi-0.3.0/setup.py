from setuptools import setup, find_packages


with open("./README.md", "r") as f:
    description = f.read()

setup(
    name="workforcerappi",
    version="0.3.0",
    packages=find_packages(),
    install_requires=[
        'pandas==2.1.4',
        'numpy==1.26.4',
        'scikit-learn==1.3.2',
        'xgboost==2.0.3',
        'snowflake-connector-python==3.7.1',
        'snowflake-snowpark-python==1.13.0',
        'pyarrow==16.1.0',
        'seaborn==0.13.2',
        'matplotlib==3.9.0',
        'ipykernel==6.29.4',
        'openpyxl==3.1.5'
    ],
    # entry_points={
    #     "console_scripts": [
    #         "wf-rappi = wfrappi:hello",
    #     ],
    # },
    long_description=description,
    long_description_content_type="text/markdown",
)