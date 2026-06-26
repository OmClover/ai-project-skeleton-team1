# AI Project Skeleton (Team 1)

A standardized, production-ready project repository layout designed for machine learning and artificial intelligence applications. This template establishes the core directory structure, module boundaries, automated test suites, and collaborative workflows required for stable team capstones.

---

## 📂 Folder Structure Overview

```text
project-root/
├── data/               # Raw and structured input datasets (CSV, JSON, etc.)
├── notebooks/          # Jupyter notebooks for EDA and model prototyping
├── src/                # Core production codebase
│   ├── __init__.py     # Makes src an importable package
│   ├── data_loader.py  # Custom CSV extraction routines
│   ├── preprocess.py   # Data cleaning, normalization, and parsing functions
│   ├── model.py        # Dummy model architectures and training structures
│   └── utils.py        # Shared helper utilities (e.g., global logging configs)
├── tests/              # Automated unit tests framework
│   └── __init__.py     # Makes tests an importable package
├── .gitignore          # System and local environment runtime exclusions
├── CONTRIBUTING.md     # Team development, branching, and commit workflows
├── README.md           # High-level project guidelines and setup instructions
└── requirements.txt    # Frozen dependency manifest (e.g., pytest)

🚀 Quick Start Setup Instructions

Follow these steps sequentially to configure your local runtime workspace on your Ubuntu environment.
1. Clone the Repository

Get a local copy of the repository by cloning it via HTTPS:
Bash

git clone [https://github.com/OmClover/ai-project-skeleton-team1.git](https://github.com/OmClover/ai-project-skeleton-team1.git)
cd ai-project-skeleton-team1

2. Create a Virtual Environment

Isolate your workspace dependencies using Python's built-in venv tool:
Bash

python3 -m venv venv

3. Activate the Virtual Environment

Activate the isolated virtual environment context:
Bash

source venv/bin/activate

4. Install Project Dependencies

Upgrade pip and install all necessary testing and processing packages listed in the requirements file:
Bash

pip install --upgrade pip
pip install -r requirements.txt

🧪 How to Run Automated Tests

Our architecture leverages pytest as the core testing engine to guarantee functional module stability.

To discover and execute all unit tests located inside the tests/ directory, run the following command from the root of your project directory while your virtual environment is active:
Bash

pytest

To see verbose output with detailed test execution summaries, add the flag:
Bash

pytest -v