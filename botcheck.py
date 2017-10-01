def is_hope_channel(message):
	if message.channel.id == '357191670825091084':
		return True
	return False

def is_all_color_roles(role_name):
	if "*" in role_name:
		return True
	return False

def check_all_color_roles_list(roles):
	for arole in roles:
		name = arole.name
		if(is_all_color_roles(name)):
			return True
	return False

def check_is_error_color_mentions(roles,mention):
	is_error_mention = True
	for role in roles:
		if role.mention == mention:
			is_error_mention =  False

	return is_error_mention
def check_contain_http_img(url):
	if url.startswith('http'):
		if 'jpg' in url or 'png' in url or 'gif' in url:
			return True
	return False