import subprocess
from datetime import datetime

GITHUB_BOT_EMAIL = (
    "github-actions[bot] <41898282+github-actions[bot]@users.noreply.github.com>"
)

branch_name = str(hash(datetime.now().timestamp()))
os.system(f"git checkout -b {branch_name}")
subprocess.run(f"git add ./default-policies/*", check=True)
subprocess.run(
    f'GIT_COMMITTER_NAME="PROFILE_UPDATE_BOT" git commit --author="{GITHUB_BOT_EMAIL}" -m "Update Seccomp Default Profiles"',
    check=True,
)
subprocess.run(f"git push origin {branch_name}")

PR_TITLE = "chore: bump default policy update"
PR_BODY = "Bumps [seccomp default policy](https://raw.githubusercontent.com/moby/moby/master/profiles/seccomp/default.json) update"

subprocess.run(
    " ".join(
        [
            f'GITHUB_TOKEN={os.environ["GH_TOKEN"]}',
            f"gh pr create",
            f'--title "{PR_TITLE}"',
            f'--body "{PR_BODY}"',
            f'--repo "lablup/backend.ai-jail"',
            f'--base "main"',
            f'--label "infrastructure"',
            # TODO: Remove below flag.
            f"--draft",
        ]
    ),
    check=True,
)
