import requests,os,json
import tabulate
import argparse

def github_activity(username='srikant-panda'):

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


data = github_activity()


activity = {}

for i in data:
    date = i['created_at'].split('T')[0]
    reponame= i['repo']['name']
    event = i['type']
    if not date in activity:
        activity[date] = {}
    if not reponame in activity[date]:
        activity[date][reponame] = {}
    if not event in activity[date][reponame]:
        activity[date][reponame][event] = 1
    else:
        activity[date][reponame][event] += 1

with open('sample.json','w') as f:
    json.dump(activity,f,indent=4)


if __name__ == '__main__':

    counter = 0
    for date in activity:

        print(date)

        for repo in activity[date]:
            print('     |')
            print('      ->',repo)

            for event in activity[date][repo]:
                print()
                print('                         ->',f'{event}({activity[date][repo][event]})')
        counter +=1

        if counter == 2:
            choose = input('Enter (m) for more result or exit: ')
            
            if choose == 'm':
                counter = 0
                pass

            elif choose == 'exit':
                break
        
        
       