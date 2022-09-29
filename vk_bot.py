import random

import vk_api as vk
from environs import Env
from vk_api.longpoll import VkLongPoll, VkEventType

from dialog_flow import detect_intent_texts


def echo(event, vk_api, project_id):
    answer = detect_intent_texts(project_id, event.user_id, [event.text], "ru")
    vk_api.messages.send(
        user_id=event.user_id,
        message=answer.fulfillment_text,
        random_id=random.randint(1, 1000)
    )


if __name__ == '__main__':
    env = Env()
    env.read_env()
    vk_api_token = env('VK_API_TOKEN')
    project_id = env("PROJECT_ID")
    vk_session = vk.VkApi(token=vk_api_token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            echo(event, vk_api, project_id)
