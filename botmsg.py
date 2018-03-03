import re

def filter_hope_topic(hope_topic):

	if('<@' not in hope_topic or '>' not in hope_topic):
		
		return '``'+hope_topic+'``'
	
	ids = re.findall(r'@(.+?)>', hope_topic)

	mention_ids = []
	for id in ids:
		mention_ids.append('<@'+id+'>')

	for mention_id in mention_ids:
		if(mention_id in hope_topic):
			hope_topic = hope_topic.replace(mention_id,',')

	hope_topic_array = hope_topic.split(',')
	print(hope_topic_array)


	result_str = ''
	index=0
	for hope_topic_item in hope_topic_array:
		if((hope_topic_item == '' or hope_topic_item.isspace()) and index < len(mention_ids)):
			result_str+= mention_ids[index]
			index+=1
			continue

		if(index < len(mention_ids) and not hope_topic_item.isspace()):
			result_str+= '``'+hope_topic_item+'``'+mention_ids[index]
			index+=1
		else:
			if hope_topic_item != '' and not hope_topic_item.isspace() :
				result_str+='``'+hope_topic_item+'``'

	return result_str