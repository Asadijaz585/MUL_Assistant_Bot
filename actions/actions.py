# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher



# class Actionadmission(Action):
#
#     def name(self) -> Text:
#         return "action_admission"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         msg = {"type": "video", "payload": {"title": "How to Apply Online_ Instructions for Students",
#                                             "src": "https://youtu.be/P1g8wWn6IMI"}}
#         dispatcher.utter_message(text="Complete Process")
#
#         return []
