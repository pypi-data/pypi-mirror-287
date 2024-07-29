from typing import Any
from kbrainsdk.validation.messages import validate_create_subscription, validate_servicebus_message, validate_servicebus_queue, validate_servicebus_topic, validate_websocket_group_request, validate_websocket_subscription_request
from kbrainsdk.apibase import APIBase

class Events(APIBase):

    def __init__(self, *args: Any, **kwds: Any) -> Any:
        return super().__init__(*args, **kwds)
    
    def publish_message(self, message: str, topic_name: str, application_properties: dict | None = None) -> None:
        payload = {
            "message": message,
            "topic_name": topic_name,
            "application_properties": application_properties
        }
        
        validate_servicebus_message(payload)
        path = f"/service_bus/send/v1"
        response = self.apiobject.call_endpoint(path, payload, "post")
        return response
    
    def create_topic(self, topic_name: str) -> None:
        payload = {
            "topic_name": topic_name
        }
        
        validate_servicebus_topic(payload)
        path = f"/service_bus/topic/create/v1"
        response = self.apiobject.call_endpoint(path, payload, "post")
        return response

    def create_queue(self, queue_name: str) -> None:
        payload = {
            "queue_name": queue_name
        }
        validate_servicebus_queue(payload)
        path = f"/service_bus/queue/create/v1"
        response = self.apiobject.call_endpoint(path, payload, "post")
        return response

    def create_subscription(self, topic_name: str, subscription_name: str) -> None:
        payload = {
            "topic_name": topic_name,
            "subscription_name": subscription_name
        }
        validate_create_subscription(payload)
        path = f"/service_bus/subscription/create/v1"
        response = self.apiobject.call_endpoint(path, payload, "post")
        return response

