import requests
import vk_api

vk_session = vk_api.VkApi(token= '4c2253e7478404390dca3997e183f44e48ec2fd30a83b2a6283ac08b8d42633453294e4b9b8881ceef631')

from vk_api.longpool import VkLongPoll, VkEventType
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VKEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.text == 'Привет проглот' or event.text == 'Привет бот':
            if event.from_user:
                vk.messages.send(
                    user_id=event.user_id,
                    message= 'Здравствуйте, сэр'
                    )
            elif event.from_chat:
                vk.messages.send(
                    chat_id=event.chat_id,
                    message='Приветствую вас'