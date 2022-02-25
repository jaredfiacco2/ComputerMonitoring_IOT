import platform,socket,re,uuid,json,psutil,logging,subprocess
from datetime import datetime, timezone

def getSystemInfo():
    try:
        info={}
        info['data_collection_time_utc']=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        info['data_collection_time_local']=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        info['data_collection_time_local_tz']=str(datetime.now().astimezone().tzinfo)
        info['os']=str(platform.system())
        info['os_release']=str(platform.release())
        info['os_version']=str(platform.version())
        info['architecture']=str(platform.machine())
        info['hostname']=str(socket.gethostname())
        info['ip_address']=str(socket.gethostbyname(socket.gethostname()))
        info['mac_address']=str(':'.join(re.findall('..', '%012x' % uuid.getnode())))
        info['machine_id']=str(subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip())
        info['processor']=str(platform.processor())
        info['ram_total_gb']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        info['ram_available_gb']=str(round(psutil.virtual_memory().available / (1024.0 **3)))+" GB"
        info['ram_used_gb']=str(round(psutil.virtual_memory().used / (1024.0 **3)))+" GB"
        info['ram_total_mb']=str(round(psutil.virtual_memory().total / (1024.0 **2)))+" MB"
        info['ram_available_mb']=str(round(psutil.virtual_memory().available / (1024.0 **2)))+" MB"
        info['ram_used_mb']=str(round(psutil.virtual_memory().used / (1024.0 **2)))+" MB"
        info['ram_used_percent']=str(psutil.virtual_memory().percent) +"%"
        info['swap_total_gb']=str(round(psutil.swap_memory().total / (1024.0 **3)))+" GB"
        info['swap_used_gb']=str(round(psutil.swap_memory().used / (1024.0 **3)))+" GB"
        info['swap_free_gb']=str(round(psutil.swap_memory().free / (1024.0 **3)))+" GB"
        info['swap_total_mb']=str(round(psutil.swap_memory().total / (1024.0 **2)))+" MB"
        info['swap_used_mb']=str(round(psutil.swap_memory().used / (1024.0 **2)))+" MB"
        info['swap_free_mb']=str(round(psutil.swap_memory().free / (1024.0 **2)))+" MB"
        info['swap_used_percent']=str(psutil.swap_memory().percent) +"%"
        info['python_version']=str(platform.python_version())
        info['last_boot_time']=datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')
        info['user_name']=str(psutil.users()[0].name)
        info['user_start_time']=datetime.fromtimestamp(psutil.users()[0].started).strftime('%Y-%m-%d %H:%M:%S')
        info['cpu_user_second']=str(psutil.cpu_times().user)
        info['cpu_system_second']=str(psutil.cpu_times().system)
        info['cpu_idle_second']=str(psutil.cpu_times().idle)
        info['cpu_interrupt_second']=str(psutil.cpu_times().interrupt)
        info['cpu_dcp_second']=str(psutil.cpu_times().dpc)
        info['cpu_user_hour']=str(psutil.cpu_times().user/60/60)
        info['cpu_system_hour']=str(psutil.cpu_times().system/60/60)
        info['cpu_idle_hour']=str(psutil.cpu_times().idle/60/60)
        info['cpu_interrupt_hour']=str(psutil.cpu_times().interrupt/60/60)
        info['cpu_dcp_hour']=str(psutil.cpu_times().dpc/60/60)
        info['cpu_count']=str(psutil.cpu_count())
        info['cpu_stats_ctx_switches']=str(psutil.cpu_stats().ctx_switches)
        info['cpu_stats_interrupts']=str(psutil.cpu_stats().interrupts)
        info['cpu_stats_soft_interrupts']=str(psutil.cpu_stats().soft_interrupts)
        info['cpu_stats_syscalls']=str(psutil.cpu_stats().syscalls)
        info['cpu_freq_current']=str(psutil.cpu_freq().current)
        info['cpu_freq_min']=str(psutil.cpu_freq().min)
        info['cpu_freq_max']=str(psutil.cpu_freq().max)
        info['disk_total_gb']=str(round(psutil.disk_usage('C://').total / (1024.0 **3)))+" GB"
        info['disk_used_gb']=str(round(psutil.disk_usage('C://').used / (1024.0 **3)))+" GB"
        info['disk_free_gb']=str(round(psutil.disk_usage('C://').free / (1024.0 **3)))+" GB"
        info['disk_total_mb']=str(round(psutil.disk_usage('C://').total / (1024.0 **2)))+" MB"
        info['disk_used_mb']=str(round(psutil.disk_usage('C://').used / (1024.0 **2)))+" MB"
        info['disk_free_mb']=str(round(psutil.disk_usage('C://').free / (1024.0 **2)))+" MB"
        info['disk_io_counters_read_count']=str(psutil.disk_io_counters(perdisk=False).read_count)
        info['disk_io_counters_write_count']=str(psutil.disk_io_counters(perdisk=False).write_count)
        info['disk_io_counters_read_bytes']=str(psutil.disk_io_counters(perdisk=False).read_bytes)
        info['disk_io_counters_write_bytes']=str(psutil.disk_io_counters(perdisk=False).write_bytes)
        info['disk_io_counters_read_time']=str(psutil.disk_io_counters(perdisk=False).read_time)
        info['disk_io_counters_write_time']=str(psutil.disk_io_counters(perdisk=False).write_time)
        print(json.dumps(info))
        return info
    except Exception as e:
        logging.exception(e)

# print(str(getSystemInfo()))

####################################################################
### For Future Versions of this github package #####################
####################################################################
# # gets the disk partitions in order to get a list of NFTS drives
# drps = psutil.disk_partitions()
# drives = [dp.device for dp in drps ]#if dp.fstype == 'NTFS']
# # records the drive usage for each drive found
# for drive in drives:
#     df['{}_DriveUsage'.format(drive.replace(":\\",""))] = psutil.disk_usage(drive)[3]
# psutil.sensors_temperatures()


