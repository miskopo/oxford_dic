from argparse import ArgumentParser
from json import loads
from logging import getLogger
from os import environ as env

from requests import get

logger = getLogger(__name__)

argument_parser = ArgumentParser()
argument_parser.add_argument("word",
                             action="store",
                             nargs=1)
args = argument_parser.parse_args()


def main():
    try:
        app_id = env['OXFORD_DICTIONARY_APP_KEY']
        api_key = env['OXFORD_DICTIONARY_API_KEY']
    except KeyError:
        logger.error("API variables not found, populate "
                     "OXFORD_DICTIONARY_APP_KEY and OXFORD_DICTIONARY_API_KEY with"
                     "proper values.")
        return -1

    try:
        prepared_url = f"https://od-api.oxforddictionaries.com:443/api/v2/" \
                   f"entries/en-gb/{args.word[0].lower()}"
    except KeyError:
        logger.error("Argument 'word' is required.")
        return -1

    with get(prepared_url,
             headers={"app_id": app_id, "app_key": api_key}) as request:
        if request.ok:
            result_text =request.text
        else:
            logger.error(f"{request.status_code}: {request.text}")

    result_json = loads(result_text)
    for entry in result_json['results'][0]['lexicalEntries'][0]['entries']:
        print(args.word[0])
        print(len(args.word[0]) * '_')
        print("\nEtymology:")
        print(f"\t{entry['etymologies'][0]}")
        print("\nDefinition:")
        print(f"\t{entry['senses'][0]['definitions'][0]}")
        print("\nExamples:")
        print(f"\t{entry['senses'][0]['examples'][0]['text']}")


if __name__ == '__main__':
    main()
