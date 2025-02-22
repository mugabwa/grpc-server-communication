import threading
from django.apps import AppConfig


class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'book_mx.store'

    def ready(self):
        from book_mx.store import grpc_server
        grpc_server_thread = threading.Thread(target=grpc_server.serve, daemon=True)
        grpc_server_thread.start()