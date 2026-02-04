from github_api import repo_details

def main():
    repo_input = input("Enter Repo Details in this format 'owner/repo' :")
    owner, repo = repo_input.split('/')
    print(repo_details(owner,repo))

main()    
  
