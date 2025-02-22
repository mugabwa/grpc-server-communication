import grpc
from book_accounts.accounts import book_store_events_pb2
from book_accounts.accounts import book_store_events_pb2_grpc

def send_event(event_type, event_data, event_id):
    channel = grpc.insecure_channel('localhost:50051')
    stub = book_store_events_pb2_grpc.EventServiceStub(channel)
    response = stub.ReportEvent(book_store_events_pb2.EventRequest(event_type=event_type, event_data=event_data, event_id=event_id))
    print(response)

