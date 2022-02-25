
import pandas as pd
import base64
import pandas_gbq
from google.oauth2 import service_account

credentials_path = 'gcp-service-account-auth-key.json'
credentials = service_account.Credentials.from_service_account_file(credentials_path)

project_id = "PROEJCT_ID"
table_id = "DATASET.TABLE_NAME"

def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    df = pd.DataFrame([event['attributes']])
    df['type'] = event['@type']
    df['data_id'] = event['data']
    df['message'] = pubsub_message
    df = df.astype({
                        "cpu_count":"int64",
                        "cpu_dcp_hour":"float",
                        "cpu_dcp_second":"float",
                        "cpu_freq_current":"float",
                        "cpu_freq_max":"float",
                        "cpu_freq_min":"float",
                        "cpu_idle_hour":"float",
                        "cpu_idle_second":"float",
                        "cpu_interrupt_hour":"float",
                        "cpu_interrupt_second":"float",
                        "cpu_stats_ctx_switches": "int64",
                        "cpu_stats_interrupts": "int64",
                        "cpu_stats_soft_interrupts": "int64",
                        "cpu_stats_syscalls": "int64",
                        "cpu_system_hour": "float",
                        "cpu_system_second": "float",
                        "cpu_user_hour": "float",
                        "cpu_user_second": "float",
                        "data_collection_time_local":"datetime64", 
                        "data_collection_time_utc": "datetime64",
                        "disk_io_counters_read_bytes": "int64",
                        "disk_io_counters_read_count": "int64",
                        "disk_io_counters_read_time": "int64",
                        "disk_io_counters_write_bytes": "int64",
                        "disk_io_counters_write_count": "int64",
                        "disk_io_counters_write_time": "int64",
                        "last_boot_time": "datetime64",
                        "user_start_time": "datetime64"
                    })
    print(df.dtypes)
    print(df)

    pandas_gbq.to_gbq(df, table_id, project_id=project_id, credentials=credentials, if_exists='append')




