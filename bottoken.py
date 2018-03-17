import os


def get_bot_token(test_mode):
	token_test = os.environ.get('DISCORD_BOT_TEST_TOKEN','')
	token = os.environ.get('DISCORD_BOT_TOKEN','')
	if not test_mode:
		return token
	else:
		return token_test
