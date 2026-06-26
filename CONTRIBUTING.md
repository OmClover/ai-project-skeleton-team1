# Contributing to AI Project Skeleton

Thank you for contributing to our Capstone AI Project! To maintain a clean commit history, uniform branching patterns, and stable collaboration across our shared repository, all team members must follow these explicit engineering standards.

---

## 🛠️ 1. Cloning the Repository & Virtual Environment Setup

Always ensure you isolate your runtime environments before working on project modules to avoid dependency conflicts.

### Step-by-Step Initialization:
1. **Clone the Remote Repository:**
   ```bash
   git clone [https://github.com/OmClover/ai-project-skeleton-team1.git](https://github.com/OmClover/ai-project-skeleton-team1.git)
   cd ai-project-skeleton-team1

    Create a Localized Virtual Environment:
    Using Python's built-in venv module, create an isolated runtime environment named venv:
    Bash

    python3 -m venv venv

    Activate the Virtual Environment:

        Ubuntu/Linux/macOS:
        Bash

        source venv/bin/activate

        Windows (Git Bash):
        Bash

        source venv/Scripts/activate

    Install Dependencies:
    Ensure your testing frameworks and environment baseline packages are completely up to date:
    Bash

    pip install --upgrade pip
    pip install -r requirements.txt

🌿 2. Branch Naming Conventions

Direct pushes to the main branch are strictly prohibited by our branch protection parameters. All development tasks must be executed on distinct feature branches built from an updated main branch.
Feature Branch Structure:

Every feature branch must follow this explicit format:
Plaintext

feature/issue-<number>-<short-description>

Examples:

    feature/issue-1-data-loader

    feature/issue-2-preprocess

    feature/issue-3-model

💬 3. Commit Message Standards (Conventional Commits)

Our repository enforces the Conventional Commits standard to guarantee a clear, logical, and fully auditable git commit log (git log --oneline --all). Every commit message must use a structural, lowercase type prefix followed by an operational description written in the present tense, with a total length under 60 characters.
Permitted Type Prefixes:

    feat — Introduction of a new functional capability or module (e.g., feat: implement load_csv matrix extraction)

    fix — A bug fix or runtime error correction (e.g., fix: resolve whitespace stripping empty value error)

    docs — Documentation changes only (e.g., docs: update setup guidelines inside README)

    refactor — Code adjustment that neither fixes an operational bug nor appends a new module feature

    test — Appending, fixing, or modifying unit test suites (e.g., test: add unit test for preprocess engine)

    chore — Maintenance operations, updating configurations, dependencies, or structural additions to .gitignore

🔍 4. The Pull Request (PR) & Code Peer Review Process

To guarantee code quality control across the team, our branch protection rule requires at least 1 peer review approval before any contribution merges into main.
The Development Cycle:

    Synchronize Main: Ensure your local workspace is completely up to date before breaking out a task branch:
    Bash

    git checkout main
    git pull origin main

    Checkout Your Branch: Create your branch utilizing the uniform naming conventions outlined above.

    Commit Incrementally: Apply atomic additions using Conventional Commit labels. Link your tracking items by typing closes #<issue-number> inside the commit description or PR summary text box to enable auto-closure.

    Push & Open a Pull Request: Push your localized feature branch to GitHub and spin up a new Pull Request targeting main.

    Assign Peer Reviewers: Tag your team collaborators on the right-side configuration bar.

    Code Audit & Resolution: Reviewers must navigate to Files changed, inspect the modifications, and select Review changes -> Approve.

    Merge & Prune: Once approved and automated test checks pass green, the original author must click Merge pull request and delete the remote feature branch.