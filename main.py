# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
from pprint import pprint


def github_accept_invites():
    token = 'INSERT_TOKEN_HERE'
    if token == 'INSERT_TOKEN_HERE':
        print('You must created a personal access token with repo, notifications, and user scopes.')
        print('See the following link: https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token')
        exit()
    base_url = "https://api.github.com"
    github_headers = {'Authorization': f'token {token}'}

    # Get a list of all of the repo invites for the user
    invites = requests.get(f'{base_url}/user/repository_invitations', headers=github_headers).json()

    expired_invites = []
    accepted_invites = []

    while invites:
        for inv in invites:
            # Check if the invite has expired or not
            if inv['expired']:
                expired_invites.append(inv['repository']['full_name'])
            else:
                accepted_invites.append(inv['repository']['full_name'])

            # Accept all repo invites (accepting expired invites clears them)
            inv_id = inv['id']
            requests.patch(f'{base_url}/user/repository_invitations/{inv_id}', headers=github_headers)
        invites = requests.get(f'{base_url}/user/repository_invitations', headers=github_headers).json()

    print("The following invitations to collaborate were accepted:")
    pprint(accepted_invites)
    print("The following invitations to collaborate were expired:")
    pprint(expired_invites)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    github_accept_invites()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
