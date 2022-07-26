# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
import webbrowser

import sqlite3

class ValidateRestaurantForm(Action):
    def name(self) -> Text:
        return "user_details_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        required_slots = ["name", "number",  "tech", "mail"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]

        # All slots are filled.
        return [SlotSet("requested_slot", None)]

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        # Took from -> https://github.com/RasaHQ/rasa/issues/3050
        # This is a Simpler way of doing this. Must be better better way to do same

        sender_id_ = tracker.current_state()['sender_id']
        name_ = tracker.get_slot("name")
        mobile_number_ = tracker.get_slot("number")
        tech_ = tracker.get_slot('tech')
        mail_ = tracker.get_slot('mail')
        if_inserted = 'New User Inserted Successfully...'
        try:
            conn = sqlite3.connect('datas.db')

            conn.execute("INSERT INTO rasa (ID,NAME,PHONE,TECH,MAIL) \
                VALUES (?,?,?,?,?)", (sender_id_ , name_ , mobile_number_ , tech_, mail_));
            conn.commit()
        except Exception as e:
            if_inserted = 'Some Error Occured.. (User Already Registered...)'
            print(e)
        dispatcher.utter_message(template="utter_details_thanks",
                                 Name=name_,
                                 Mobile_number=mobile_number_,
                                 W_Tech=tech_,
                                 E_Mail=mail_,
                                 If_Inserted = if_inserted)

