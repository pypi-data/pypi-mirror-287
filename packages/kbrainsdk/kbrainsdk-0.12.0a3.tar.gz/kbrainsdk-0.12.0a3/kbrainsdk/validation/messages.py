from kbrainsdk.validation.common import get_payload, validate_required_parameters

def validate_servicebus_message(req):
    body = get_payload(req)
    required_arguments = ["message", "topic_name", "application_properties"]
    validate_required_parameters(body, required_arguments)

    message = body.get('message')
    topic_name = body.get('topic_name')
    application_properties = body.get('application_properties')    

    return message, topic_name, application_properties

def validate_servicebus_topic(req):
    body = get_payload(req)
    required_arguments = ["topic_name"]
    validate_required_parameters(body, required_arguments)

    topic_name = body.get('topic_name')

    return topic_name

def validate_servicebus_queue(req):
    body = get_payload(req)
    required_arguments = ["queue_name"]
    validate_required_parameters(body, required_arguments)

    queue_name = body.get('queue_name')

    return queue_name

def validate_create_subscription(req):

    body = get_payload(req)
    required_arguments = ["topic_name", "subscription_name"]
    validate_required_parameters(body, required_arguments)
    topic_name = body.get('topic_name')
    subscription_name = body.get('subscription_name')
    max_delivery_count = body.get('max_delivery_count', 10)
    default_message_time_to_live = body.get('default_message_time_to_live', "P14D")
    lock_duration = body.get('lock_duration', "PT1M")
    requires_session = body.get('requires_session', False)
    dead_lettering_on_message_expiration = body.get('dead_lettering_on_message_expiration', True)
    dead_lettering_on_filter_evaluation_exceptions = body.get('dead_lettering_on_filter_evaluation_exceptions', True)
    forward_to = body.get('forward_to', None)
    forward_dead_lettered_messages_to = body.get('forward_dead_lettered_messages_to', None)
    enable_batched_operations = body.get('enable_batched_operations', True)
    status = body.get('status', "active")

    return topic_name, subscription_name, max_delivery_count, default_message_time_to_live, \
        lock_duration, requires_session, dead_lettering_on_message_expiration, dead_lettering_on_filter_evaluation_exceptions, \
            forward_to, forward_dead_lettered_messages_to, enable_batched_operations, status

def validate_websocket_group_request(req):
    body = get_payload(req)
    required_arguments = ["token", "group_name", "client_id", "tenant_id", "client_secret"]
    validate_required_parameters(body, required_arguments)

    token = body.get('token')
    client_id = body.get('client_id')
    tenant_id = body.get('tenant_id')
    group_name = body.get('group_name')
    client_secret = body.get('client_secret')

    return token, group_name, client_id, tenant_id, client_secret

def validate_websocket_subscription_request(req):
    body = get_payload(req)
    required_arguments = ["token", "group_name", "subscription_id", "client_id", "tenant_id", "client_secret"]
    validate_required_parameters(body, required_arguments)

    token = body.get('token')
    client_id = body.get('client_id')
    tenant_id = body.get('tenant_id')
    group_name = body.get('group_name')
    subscription_id = body.get('subscription_id')
    client_secret = body.get('client_secret')

    return token, group_name, subscription_id, client_id, tenant_id, client_secret