import unittest
import requests

class User:
    def __init__(self, name, html_url, public_repos, followers, following):
        self.name = name
        self.html_url = html_url
        self.public_repos = public_repos
        self.followers = followers
        self.following = following

def get_user(username: str) -> User:
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        return User(
            name = data.get("name"),
            html_url = data.get("html_url"),
            public_repos = data.get("public_repos"),
            followers = data.get("followers"),
            following = data.get("following")
        )
    else:
        raise ValueError("User not found!")

def get_user_repos(username: str) -> dict:
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        repos_dict = {repo['name']: repo['html_url'] for repo in data}
        return repos_dict

    else:
        raise ValueError("User repositories not found!")
    

def user_report(user: User, repos: dict) -> None:
    filename = f"{user.name}.txt" if user.name else f"{user.html_url.split('/')[-1]}.txt"
    
    with open(filename, 'w') as file:
        file.write(f"Nome: {user.name}\n")
        file.write(f"Perfil: {user.html_url}\n")
        file.write(f"Número de repositórios publicos: {user.public_repos}\n")
        file.write(f"Número de seguidores: {user.followers}\n")
        file.write(f"Número de usuários seguidos: {user.following}\n")
        file.write("Repositórios:\n")
        for repo_name, repo_url in repos_dict.items():
            file.write(f"   {repo_name}: {repo_url}\n")

class TestMethods(unittest.TestCase):
   
    def test_user_class_has_minimal_parameters(self):
        parameters = [
            'name', 'html_url', 'public_repos', 'followers', 'following'
            ]
        user = get_user('githubuser')
    
        for param in parameters:
            self.assertTrue(hasattr(user, param))

    #def test_(self):
        

if __name__ == "__main__":
    username = "githubuser"
    user = get_user(username)
    repos_dict = get_user_repos(username)
    user_report(user, repos_dict)

    unittest.main()
