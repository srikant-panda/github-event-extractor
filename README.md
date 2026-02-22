📦 GitHub Activity CLI

A simple Python CLI tool that fetches and displays a user's recent public GitHub activity using the GitHub Events API.

🚀 Features

Fetch recent public events of any GitHub user

Supports common GitHub events:
```bash
PushEvent

PullRequestEvent

IssuesEvent

DeleteEvent

IssueCommentEvent

PullRequestReviewEvent

WatchEvent

ForkEvent
```

Clean CLI-based output

Built using requests and argparse

📥 Installation

Clone the repository:
```bash
git clone https://github.com/your-username/github-activity-cli.git
cd github-activity-cli
```
Install dependencies:
``` bash
pip install requirement.txt
```
▶️ Usage
python main.py <github-username>
Example:
python main.py srikant-panda
🧠 How It Works

The tool fetches data from:

https://api.github.com/users/<username>/events

It then parses event types and prints human-readable activity messages.

🛠 Built With

Python

requests

argparse

📌 Notes

Only public events are fetched.

GitHub API rate limits apply (60 requests per hour for unauthenticated requests).

If you want next level improvement ideas later:

Add table formatting with tabulate

Add event count summary

Add pagination support

Add authentication with token

Convert to pip-installable CLI

You're building something solid here. Keep going 🚀