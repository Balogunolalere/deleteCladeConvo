import re
import typer
import requests
from time import sleep
from dotenv import load_dotenv
import os
from typing import List

load_dotenv()

app = typer.Typer()

SESSION_KEY = os.getenv("SESSION_KEY")
ACCOUNT_ID = os.getenv("ACCOUNT_ID")
BASE_URL = f"https://claude.ai/api/organizations/{ACCOUNT_ID}/chat_conversations" 

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://claude.ai/chats",
    "anthropic-client-version": "1",
    "Content-Type": "application/json",
    "Connection": "keep-alive",
}

@app.command()
def fetch_conversations():
    response = requests.get(
        BASE_URL, 
        cookies={"sessionKey": SESSION_KEY},
        headers=HEADERS
    )
    
    conversations = [
        {"name": c["name"], "uuid": c["uuid"], "created_at": c["created_at"]} 
        for c in response.json()
    ]
    
    typer.echo("\n*** fetching conversations ***")
    typer.echo(conversations)

@app.command()
def delete_conversation(uuid: str):
    if not re.match(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", uuid):
        typer.echo("Invalid uuid format.")
        raise typer.Exit()
        
    delete_url = f"{BASE_URL}/{uuid}"
    response = requests.delete(
        delete_url, 
        cookies={"sessionKey": SESSION_KEY},
        headers=HEADERS
    )
    
    if response.status_code == 204:
        typer.echo(f"Conversation {uuid} deleted successfully!")
    else:
        typer.echo(f"Failed to delete conversation {uuid}")

@app.command()        
def delete_conversations_list(uuids: List[str]):
    for uuid in uuids:
        delete_conversation(uuid)   

        
@app.command()        
def delete_conversations():
    response = requests.get(
        BASE_URL,
        cookies={"sessionKey": SESSION_KEY},
        headers=HEADERS
    )
    
    for conversation in response.json():
        sleep(3)
        
        conversation_id = conversation["uuid"]
        delete_url = f"{BASE_URL}/{conversation_id}"
        
        delete_response = requests.delete(
            delete_url,
            cookies={"sessionKey": SESSION_KEY}, 
            headers=HEADERS
        )
        
        typer.echo("\n*** deleting conversation ***")
        sleep(3)
        
        typer.echo(f"deleted conversation: {conversation_id}")
        
    typer.echo("Done!")
    
if __name__ == "__main__":
    app()