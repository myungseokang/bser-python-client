from bser_client import BserAPIClient

api_client = BserAPIClient(api_key='your_token', version='v1')

user_number = api_client.get_user_number_by_nickname(nickname='보라색맛팬텀')

print(user_number)
