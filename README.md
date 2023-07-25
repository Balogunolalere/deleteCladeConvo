## Claude Conversation Manager

### This is a simple command line application for managing conversations in Claude.
### Prerequisites

    Python 3.6+
    Claude account
    Claude session key (SESSION_KEY)
    Claude account id (ACCOUNT_ID)

### Installation

    Clone the repo


### Install dependencies
    
    pip install -r requirements.txt

    Set the SESSION_KEY and ACCOUNT_ID environment variables

## Usage


    $ python manager.py --help

    Usage: manager.py [OPTIONS] COMMAND [ARGS]...

### Options:

    --install-completion  Install completion for the current shell.
    --show-completion     Show completion for the current shell, to copy it or
                          customize the installation.

    --help                Show this message and exit.

### Commands:

    delete-conversation  Delete a conversation by UUID.
    delete-conversations  Delete all conversations. 
    fetch-conversations   Fetch all conversations.

### Fetch conversations


    $ python manager.py fetch-conversations

    This will make a request to fetch all conversations and print them to the console.

### Delete a conversation


    $ python manager.py delete-conversation [uuid]

    Delete a conversation by its UUID.

### Delete all conversations


    $ python manager.py delete-conversations

    Loop through and delete all conversations.

### Environment Variables

    SESSION_KEY - Claude session key
    ACCOUNT_ID - Claude account ID

### Contributing

    Pull requests are welcome. Feel free to open an issue first to discuss what you would like to change.
