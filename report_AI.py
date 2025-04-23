import openai
import re

# Configurez votre clé API OpenAI via une variable d'environnement pour plus de sécurité
openai.api_key = ""

def tool_nmap(input_text: str) -> tuple[bool, str]:
    nmap_patterns = [
        r"Nmap scan report for",
        r"PORT\s+STATE\s+SERVICE",
        r"\d+/tcp\s+(?:open|filtered|closed)",
        r"Starting Nmap"
    ]
    is_nmap_output = any(re.search(pattern, input_text, re.IGNORECASE) for pattern in nmap_patterns)
    if not is_nmap_output:
        return False, "L'entrée ne semble pas être une sortie de la commande nmap."
    try:
        with open("prompt_nmap.txt", "r", encoding="utf-8") as file:
            nmap_prompt = file.read()
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
            {"role": "system", "content": "Tu es un assistant spécialisé dans le pentesting"},
            {"role": "user", "content": f"{nmap_prompt}\n\n{input_text}"}
            ],
            max_tokens=1500,
            temperature=0.5
        )
        return True, response.choices[0].message.content.strip()
    except Exception as e:
        return True, f"Erreur lors de l'analyse nmap : {str(e)}"

def tool_gobuster(input_text: str) -> tuple[bool, str]:
    gobuster_patterns = [
        r"Status: \d{3}",
        r"Found:",
        r"Threads: \d+",
        r"\s+/\S+\s+\(Status:"
    ]
    is_gobuster_output = any(re.search(pattern, input_text, re.IGNORECASE) for pattern in gobuster_patterns)
    if not is_gobuster_output:
        return False, "L'entrée ne semble pas être une sortie de la commande Gobuster."
    try:
        with open("prompt_gobuster.txt", "r", encoding="utf-8") as file:
            gobuster_prompt = file.read()
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
            {"role": "system", "content": "Tu es un assistant spécialisé dans le pentesting"},
            {"role": "user", "content": f"{gobuster_prompt}\n\n{input_text}"}
            ],
            max_tokens=1500,
            temperature=0.5
        )
        return True, response.choices[0].message.content.strip()
    except Exception as e:
        return True, f"Erreur lors de l'analyse Gobuster : {str(e)}"

def call_AI(command_output):
    if not command_output or command_output.isspace():
        print("Veuillez fournir une sortie de commande à analyser.")
        return

    is_nmap, result_nmap = tool_nmap(command_output)
    if is_nmap:
        print("\nAnalyse du scan Nmap :")
        print("-" * 50)
        print(result_nmap)
        return

    is_gobuster, result_gobuster = tool_gobuster(command_output)
    if is_gobuster:
        print("\nAnalyse du scan Gobuster :")
        print("-" * 50)
        print(result_gobuster)
        return

    print("\nSortie non reconnue comme Nmap ou Gobuster.")
