from kbrainsdk.validation.common import get_payload, validate_required_parameters

def validate_signalr_broadcast(req):
    body = get_payload(req)
    required_arguments = ["target", "action"]
    validate_required_parameters(body, required_arguments)

    target = body.get('target')
    action = body.get('action')
    
    return target, action
