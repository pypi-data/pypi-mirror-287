from typing import Any, Dict
from kbrainsdk.apibase import APIBase
from kbrainsdk.validation.signalr import validate_signalr_broadcast

class SignalR(APIBase):

    def __init__(self, *args: Any, **kwds: Any) -> Any:
        return super().__init__(*args, **kwds)
    
    def broadcast(self, 
        target:str, 
        action: Dict[str, Any], 
    ):
        payload = {
            "target": target,
            "action": action
        }
        validate_signalr_broadcast(payload)
        path = f"/websocket/broadcast/v1"
        response = self.apiobject.call_endpoint(path, payload, "post")
        return response

"""
    def subscribe_to_websocket_group(self, token: str, group_name: str, client_id: str, tenant_id: str, client_secret: str):
        payload = {
            "token": token,
            "group_name": group_name,
            "client_id": client_id,
            "tenant_id": tenant_id,
            "client_secret": client_secret
        }
        validate_websocket_group_request(payload)
        path = f"/websocket/group/subscribe/v1"
        response = self.apiobject.call_endpoint(path, payload, "post")
        return response

    def authenticate_to_websocket_group(self, token: str, group_name: str, client_id: str, tenant_id: str, client_secret: str):
        payload = {
            "token": token,
            "group_name": group_name,
            "client_id": client_id,
            "tenant_id": tenant_id,
            "client_secret": client_secret
        }
        validate_websocket_group_request(payload)
        path = f"/websocket/group/authenticate/v1"
        response = self.apiobject.call_endpoint(path, payload, "post")
        return response

    def authenticate_to_websocket_subscription(self, token: str, group_name: str, subscription_id:str, client_id: str, tenant_id: str, client_secret: str):
        payload = {
            "token": token,
            "group_name": group_name,
            "subscription_id": subscription_id,
            "client_id": client_id,
            "tenant_id": tenant_id,
            "client_secret": client_secret
        }
        validate_websocket_subscription_request(payload)
        path = f"/websocket/subscription/authenticate/v1"
        response = self.apiobject.call_endpoint(path, payload, "post")
        return response

    def unsubscribe_to_websocket_group(self, token: str, group_name: str, subscription_id: str, client_id: str, tenant_id: str, client_secret: str):
        payload = {
            "token": token,
            "group_name": group_name,
            "subscription_id": subscription_id,
            "client_id": client_id,
            "tenant_id": tenant_id,
            "client_secret": client_secret
        }
        validate_websocket_subscription_request(payload)
        path = f"/websocket/group/unsubscribe/v1"
        response = self.apiobject.call_endpoint(path, payload, "post")
        return response

    def get_websocket_group_subscribers(self, token: str, group_name: str, client_id: str, tenant_id: str, client_secret: str):
        payload = {
            "token": token,
            "group_name": group_name,
            "client_id": client_id,
            "tenant_id": tenant_id,
            "client_secret": client_secret
        }
        validate_websocket_group_request(payload)
        path = f"/websocket/group/subscribers/v1"
        response = self.apiobject.call_endpoint(path, payload, "post")
        return response
"""