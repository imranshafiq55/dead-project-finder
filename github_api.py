from config import GITHUB_TOKEN, GITHUB_API_BASE
import requests

def repo_details(owner,repo):
   
   try:
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}"
    response = requests.get(url, headers=headers, timeout=10)

   except requests.exceptions.Timeout:
     raise ConnectionError("GitHub API request timed out")

   except requests.exceptions.ConnectionError:
     raise ConnectionError("Network connection failed")

   except requests.exceptions.RequestException as e:
     raise ConnectionError(f"Unexpected GitHub API error: {e}")
   
   if response.status_code == 404:
        raise FileNotFoundError("Repo not found. Enter valid repo.")

   if response.status_code in (403, 429):
        raise PermissionError("API rate limit exceeded")
   
  
    
   return response.json()


   
   


