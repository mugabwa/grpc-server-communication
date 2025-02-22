import grpc
from concurrent import futures
from django.db import transaction

from book_mx.store import book_store_events_pb2
from book_mx.store import book_store_events_pb2_grpc
from book_mx.store.models import Book


class EventService(book_store_events_pb2_grpc.EventServiceServicer):
    def ReportEvent(self, request, context):
        print(f"Received event: {request.event_type} -> {request.event_data} ({request.event_id})")
        try:
            if request.event_data not in ['AVAILABLE', 'BORROWED']:
                return book_store_events_pb2.EventResponse(status='ERROR: Inavlid status')
            with transaction.atomic():
                book = Book.objects.get(guid=request.event_id)
                book.status = request.event_data
                book.save()
        except Exception as e:
            return book_store_events_pb2.EventResponse(status=f'ERROR: {e}')
        return book_store_events_pb2.EventResponse(status='OK')

    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    book_store_events_pb2_grpc.add_EventServiceServicer_to_server(EventService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("App 2 gRPC Server started on port 50052")
    server.wait_for_termination()

