import logging
import uuid
from datetime import datetime
import pytz
from tommytomato_utils.database_client.database_client import DatabaseClient


class DatabaseLoggingHandler(logging.Handler):
    def __init__(self, db_client: DatabaseClient, hub_id: str, run_id: str, user_id: str, tool_name: str):
        super().__init__()
        self.db_client = db_client
        self.hub_id = hub_id
        self.run_id = run_id
        self.user_id = user_id
        self.tool_name = tool_name

    def emit(self, record):
        try:
            log_status = record.__dict__.get('log_status', 'status_undefined')
        except AttributeError:
            log_status = 'status_undefined'


        log_entry = {
            'id': str(uuid.uuid4()),
            'tool_name': self.tool_name,
            'status': log_status,
            'message': record.getMessage(),
            'run_id': self.run_id,
            'user_id': self.user_id,
            'hub_id': self.hub_id,
            'production_date': datetime.now(pytz.timezone('Europe/Amsterdam')).date(),
            'inserted_at': datetime.now(pytz.timezone('Europe/Amsterdam')),
        }
        try:
            self.db_client.insert_data('ecs_task_logs', [log_entry])
        except Exception as e:
            logging.error(f"Failed to log to database: {e}")
