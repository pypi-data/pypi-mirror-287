import requests
import os
from locust import events

def send_github_dispatch():
    if os.environ.get("GITHUB_ACTIONS") != "true":
        github_token = os.environ['GITHUB_TOKEN']
        repo = os.environ['GITHUB_REPOSITORY']

        url = f"https://api.github.com/repos/{repo}/dispatches"
        data = {
            "event_type": "locust_test_completed",
            "client_payload": {"message": "Locust test finished, triggering Pulumi destroy"}
        }
        headers = {
            "Accept": "application/vnd.github.everest-preview+json",
            "Authorization": f"token {github_token}"
        }

        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 204:
            print("Successfully sent GitHub dispatch event")
        else:
            print(f"Failed to send dispatch event: {response.status_code} - {response.text}")
    else:
        print("Code is running inside a GitHub Actions workflow, skipping dispatch event")

@events.init_command_line_parser.add_listener
def _(parser):
    parser.add_argument(
        '--github-dispatch',
        action='store_true',
        default=False,
        help="Send GitHub dispatch event on test completion"
    )

@events.test_stop.add_listener
def _(environment, **kwargs):
    if environment.parsed_options.github_dispatch:
        send_github_dispatch()
