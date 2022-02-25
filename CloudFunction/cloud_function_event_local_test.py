#################################################
#Use this to test locally before pushing to prod#
#################################################
from platform import architecture
from google.cloud import bigquery
import os
import pandas as pd
import base64
import pandas_gbq
from pandas.io.json import build_table_schema
from google.oauth2 import service_account

credentials_path = 'gcp-service-account-auth-key.json'
credentials = service_account.Credentials.from_service_account_file(credentials_path)

project_id = "PROEJCT_ID"
table_id = "DATASET.TABLE_NAME"


event = {'@type': 'type.googleapis.com/google.pubsub.v1.PubsubMessage', 'attributes': {'architecture': 'AMD64', 'cpu_count': '8', 'cpu_dcp_hour': '2.5331336805555558', 'cpu_dcp_second': '9119.28125', 'cpu_freq_current': '2995.0', 'cpu_freq_max': '2995.0', 'cpu_freq_min': '0.0', 'cpu_idle_hour': '1141.1929210069443', 'cpu_idle_second': '4108294.515625', 'cpu_interrupt_hour': '1.0834288194444446', 'cpu_interrupt_second': '3900.34375', 'cpu_stats_ctx_switches': '3549147889', 'cpu_stats_interrupts': '2367351607', 'cpu_stats_soft_interrupts': '0', 'cpu_stats_syscalls': '2969373015', 'cpu_system_hour': '20.364548611110983', 'cpu_system_second': '73312.37499999953', 'cpu_user_hour': '32.908945312499995', 'cpu_user_second': '118472.20312499999', 'data_collection_time_local': '2022-02-22 23:48:27', 'data_collection_time_local_tz': 'Eastern Standard Time', 'data_collection_time_utc': '2022-02-23 04:48:27', 'disk_free_gb': '680 GB', 'disk_free_mb': '696496 MB', 'disk_io_counters_read_bytes': '406380978176', 'disk_io_counters_read_count': '4789052', 'disk_io_counters_read_time': '2841', 'disk_io_counters_write_bytes': '390395870720', 'disk_io_counters_write_count': '4635168', 'disk_io_counters_write_time': '3170', 'disk_total_gb': '953 GB', 'disk_total_mb': '975665 MB', 'disk_used_gb': '273 GB', 'disk_used_mb': '279169 MB', 'hostname': 'COMPUTER01', 'ip_address': '000.000.000.000', 'last_boot_time': '2022-02-12 19:53:08', 'mac_address': '04:56:e5:75:6b:ff', 'machine_id': 'ABC123-DEF4-56HI-JK78-LMNOP90123', 'os': 'Windows', 'os_release': '10', 'os_version': '10.0.22000', 'processor': 'Intel64 Family 6 Model 140 Stepping 1, GenuineIntel', 'python_version': '3.7.9', 'ram_available_gb': '17 GB', 'ram_available_mb': '17171 MB', 'ram_total_gb': '32 GB', 'ram_total_mb': '32602 MB', 'ram_used_gb': '15 GB', 'ram_used_mb': '15431 MB', 'ram_used_percent': '47.3%', 'swap_free_gb': '-2 GB', 'swap_free_mb': '-1888 MB', 'swap_total_gb': '5 GB', 'swap_total_mb': '4864 MB', 'swap_used_gb': '7 GB', 'swap_used_mb': '6752 MB', 'swap_used_percent': '138.8%', 'user_name': 'username123', 'user_start_time': '2022-02-12 19:53:36'}, 'data': 'Q29tcHV0ZXItU3RhdHMtRGF0YQ=='}
context = {'event_id': 3230523596406045, 'timestamp': '2022-02-23T04:48:27.757Z', 'event_type': 'google.pubsub.topic.publish', 'resource': {'service': 'pubsub.googleapis.com', 'name': 'projects/project-name/topics/topic-name', 'type': 'type.googleapis.com/google.pubsub.v1.PubsubMessage'}}

def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    # print('pubsub_message: ' + str(pubsub_message))
    # print('context: ')
    # print(context)
    # print('event: ')
    # print(event)
    df = pd.DataFrame([event['attributes']])
    df['type'] = event['@type']
    df['data_id'] = event['data']
    df['message'] = pubsub_message
    # df2 = df[['architecture', 'cpu_count', 
    # 'data_collection_time_local']]
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
    # df = df.reset_index()
    # print(df)
    # print(df.info(verbose=True))
    #schema_info = {'fields': [{'name': 'index', 'type': 'integer'}, {'name': 'index', 'type': 'integer'}, {'name': 'architecture', 'type': 'string'}, {'name': 'cpu-count', 'type': 'string'}, {'name': 'cpu-dcp-hour', 'type': 'string'}, {'name': 'cpu-dcp-second', 'type': 'string'}, {'name': 'cpu-freq-current', 'type': 'string'}, {'name': 'cpu-freq-max', 'type': 'string'}, {'name': 'cpu-freq-min', 'type': 'string'}, {'name': 'cpu-idle-hour', 'type': 'string'}, {'name': 'cpu-idle-second', 'type': 'string'}, {'name': 'cpu-interrupt-hour', 'type': 'string'}, {'name': 'cpu-interrupt-second', 'type': 'string'}, {'name': 'cpu-stats-ctx-switches', 'type': 'string'}, {'name': 'cpu-stats-interrupts', 'type': 'string'}, {'name': 'cpu-stats-soft-interrupts', 'type': 'string'}, {'name': 'cpu-stats-syscalls', 'type': 'string'}, {'name': 'cpu-system-hour', 'type': 'string'}, {'name': 'cpu-system-second', 'type': 'string'}, {'name': 'cpu-user-hour', 'type': 'string'}, {'name': 'cpu-user-second', 'type': 'string'}, {'name': 'data-collection-time-local', 'type': 'string'}, {'name': 'data-collection-time-local-tz', 'type': 'string'}, {'name': 'data-collection-time-utc', 'type': 'string'}, {'name': 'disk-free-gb', 'type': 'string'}, {'name': 'disk-free-mb', 'type': 'string'}, {'name': 'disk-io-counters-read-bytes', 'type': 'string'}, {'name': 'disk-io-counters-read-count', 'type': 'string'}, {'name': 'disk-io-counters-read-time', 'type': 'string'}, {'name': 'disk-io-counters-write-bytes', 'type': 'string'}, {'name': 'disk-io-counters-write-count', 'type': 'string'}, {'name': 'disk-io-counters-write-time', 'type': 'string'}, {'name': 'disk-total-gb', 'type': 'string'}, {'name': 'disk-total-mb', 'type': 'string'}, {'name': 'disk-used-gb', 'type': 'string'}, {'name': 'disk-used-mb', 'type': 'string'}, {'name': 'hostname', 'type': 'string'}, {'name': 'ip-address', 'type': 'string'}, {'name': 'last-boot-time', 'type': 'string'}, {'name': 'mac-address', 'type': 'string'}, {'name': 'machine-id', 'type': 'string'}, {'name': 'os', 'type': 'string'}, {'name': 'os-release', 'type': 'string'}, {'name': 'os-version', 'type': 'string'}, {'name': 'processor', 'type': 'string'}, {'name': 'python-version', 'type': 'string'}, {'name': 'ram-available-gb', 'type': 'string'}, {'name': 'ram-available-mb', 'type': 'string'}, {'name': 'ram-total-gb', 'type': 'string'}, {'name': 'ram-total-mb', 'type': 'string'}, {'name': 'ram-used-gb', 'type': 'string'}, {'name': 'ram-used-mb', 'type': 'string'}, {'name': 'ram-used-percent', 'type': 'string'}, {'name': 'swap-free-gb', 'type': 'string'}, {'name': 'swap-free-mb', 'type': 'string'}, {'name': 'swap-total-gb', 'type': 'string'}, {'name': 'swap-total-mb', 'type': 'string'}, {'name': 'swap-used-gb', 'type': 'string'}, {'name': 'swap-used-mb', 'type': 'string'}, {'name': 'swap-used-percent', 'type': 'string'}, {'name': 'user-name', 'type': 'string'}, {'name': 'user-start-time', 'type': 'string'}, {'name': 'type', 'type': 'string'}, {'name': 'data_id', 'type': 'string'}, {'name': 'message', 'type': 'string'}], 'primaryKey': ['index'], 'pandas_version': '0.20.0'}
    # schema_info = build_table_schema(df)
    # print(schema_info)

    # pandas_gbq.to_gbq(df, table_id, project_id=project_id, credentials=credentials, if_exists='append')#, table_schema=schema_info)
    pandas_gbq.to_gbq(df, table_id, project_id=project_id, credentials=credentials, if_exists='append')#, table_schema=schema_info)

hello_pubsub(event, context)



