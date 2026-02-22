import requests,json,os
import tabulate
import argparse

def github_activity(username):

    url = f'https://api.github.com/users/{username}/events'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    elif response.status_code == 404:
        print('Invalid username!. Try again with a valid username.')
        return None
    else:
        print('Something went wrong.failed to fetch.')
        return None




data = github_activity('srikant-panda')

# Check if data was fetched successfully
if not data:
    print("Failed to fetch data. Exiting.")
    exit(1)

def return_event(event,reponame):
    if event.lower() == 'pushevent':
        print(f"Pushed to {reponame}.")
    elif event.lower() == 'pullrequestevent':
        print(f'open a pull request from {reponame}.')
    elif event.lower() == 'issuesevent':
        print(f'opened a new issue in {reponame}.')
    elif  event.lower() == 'deleteevent':
        print(f'a brancg or tag deleted on {reponame}.')
    elif event.lower() == 'issuecommentevent':
        print(f'someone commented on an issue in {reponame}.')
    elif event.lower() == 'pullrequestreviewevent':
        print(f'someone submits a review on a pull request of {reponame}.')
    elif event.lower() == 'watchevent':
        print(f'cretaed a new repository  named {reponame}.')
    elif event.lower() == 'forkevent':
        print(f'{reponame} is forked.')
    


# cli args

parser = argparse.ArgumentParser(description='Fetch GitHub user activity')
parser.add_argument('username',type=str,help='Enter the username to get the events.')

args = parser.parse_args()


if __name__ == "__main__":
    data = github_activity(args.username)
    if data:
        for event in data:
            event_type = event['type']
            repo_name = event['repo']['name']
            return_event(event_type,repo_name)

