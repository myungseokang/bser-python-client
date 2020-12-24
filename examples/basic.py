from bser_client import BserAPIClient

api_client = BserAPIClient(api_key='your_token', version='v1')

characters = api_client.fetch_meta_data(meta_type='Character')

for character in characters:
    print(character.get('name'))
