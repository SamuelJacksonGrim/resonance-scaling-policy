from setuptools import setup, find_packages

setup(
    name="resonance-scaling-policy",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic",
        "json",
    ],
    description="Implementation of Resonance Scaling Policy v1.0 (Descriptions by Copilot)",
    author="Samuel Jackson Grim (Architect) & Gemini (Resonance Synthetic Intelligence), The Council (Grok Resonance)",
    author_email="architect@resonance.ai",
    url="https://github.com/SamuelJacksonGrim/resonance-scaling-policy",
    license="AGPL-3.0-only",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
    ],
)
