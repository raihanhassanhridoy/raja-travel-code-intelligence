import requests

class GitHubCollector:
    def __init__(self, token):
        self.token = token
        self.headers = {'Authorization': f'token {self.token}'}

    def discover_repositories(self, username):
        url = f'https://api.github.com/users/{username}/repos'
        response = requests.get(url, headers=self.headers)
        return response.json()

    def collect_metadata(self, repo_name):
        url = f'https://api.github.com/repos/{repo_name}'
        response = requests.get(url, headers=self.headers)
        return response.json()

if __name__ == '__main__':
    TOKEN = 'your_github_token'
    collector = GitHubCollector(TOKEN)
    username = 'raihanhassanhridoy'

    # Discover repositories
    repos = collector.discover_repositories(username)
    print(f'Found {len(repos)} repositories for user {username}.')

    # Collect metadata for each repository
    for repo in repos:
        metadata = collector.collect_metadata(repo['full_name'])
        print(metadata)