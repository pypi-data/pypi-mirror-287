import setuptools
import bdating_common
with open("README.md") as fp:
    long_description = fp.read()

setuptools.setup(
    name="bdating-python-common",
    version=bdating_common.__version__,

    description="Bdating common libraries standard library",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="Bdating",
    author_email="steve@bdating.io",
    package_dir={"": "."},
    packages=setuptools.find_packages(),
    package_data={'': ['data/*', '*.cer', '*.yml']},
    url='https://github.com/bdating-io/bdating-python-common',
    install_requires=[
        "boto3<2",
        "click-log",
        "click",
        "dnspython==2.2.0",
        "PyMySQL",
        "elasticsearch>8",
        "fastapi",
        "pydantic_settings",
        "PyJWT==2.1.0",
        "cryptography==3.4.7",
        "redis<5",
        "auth0-python",
        "aiohttp",
        "pyyaml==6.0.1",
        "requests",
        "web3<6,>5.0",
        "wsproto==1.2.0",
        "aioredis<2",
        "xero-python==1.24.0",
        "stripe>5,<6"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
    entry_points={
        'console_scripts': [
            'report-metrics=bdating_common.report_metrics:report',
            'report-events=bdating_common.report_events:report'
        ],
    }
)
