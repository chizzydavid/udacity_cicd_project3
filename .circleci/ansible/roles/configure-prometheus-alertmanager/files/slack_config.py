import os
from yaml import load, dump

def main():
    # Get environment variable that store webhook url
    content = {}
    content['slack_api_url'] = os.environ['SLACK_WEBHOOK'] #this will error out if key doesn't exist
    # WEBHOOK = os.getenv['SLACK_WEBHOOK'] # returns None if key doesn't exist
    with open('slack_configuration.yml', 'w') as file:
        documents = dump(content, file)

if __name__ == '__main__':
    main()
