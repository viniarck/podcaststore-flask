from setuptools import setup

desc = "Podcaststore API"

setup(
    name="podcaststore",
    version="1.0",
    description=desc,
    author="Vinicius Arcanjo",
    author_email="viniarck@gmail.com",
    packages=["podcaststore"],
    install_requires=[
        "Flask==1.1.1",
        "Flask-SQLAlchemy==2.4.0",
        "flask-marshmallow==0.10.1",
        "psycopg2-binary==2.8.1",
        "gunicorn==19.9.0",
        "python-rapidjson==0.7.1",
        "django-extensions==2.1.7",
        "ipython==7.5.0",
        "packaging==19.0",
        "flask-shell-ipython==0.4.1",
    ],
    extras_require={
        "dev": [
            "pytest==4.5.0",
            "pytest-django==3.4.8",
            "pytest-cov==2.7.1",
            "flake8==3.7.7",
            "mypy==0.701",
            "black==19.3b0",
            "requests==2.22.0",
        ]
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
    ],
    zip_safe=False,
)
