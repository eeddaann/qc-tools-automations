import argparse
import os
import subprocess
from datetime import datetime
from metrics import extract_metrics

__version__ = "0.1"
start_time = datetime.now()
operational_log = {
    "script_version": __version__
    # ? "qcli_version": get_qcli_version()
    # video_size
    # qcli_duration
    # analysis_duration
    # script_duration
    # status
}
metrics_log = None

def is_qcli_installed():
    pass

def send_log(log,output_url):
    if output_url == "stdout":
        print(log)
    else:
        pass

parser = argparse.ArgumentParser(description='Analyzes video quality and sends results in JSON format.')
parser.add_argument('v_path',
                       metavar='video-path',
                       type=str,
                       help='the path to video')
parser.add_argument('output_url',
                       metavar='url',
                       nargs='?',
                       default='stdout',
                       help='the url for the server which will store the results, "stdout" for writing to stdout')

args = parser.parse_args()
video_path = args.v_path
output_url = args.output_url

try:
    qcli_output = video_path + '.qctools.xml.gz'
    operational_log["video_size_bytes"] = os.path.getsize(video_path) # log video size
    cmd = ['qcli', '-i', video_path]
    qcli_start_time = datetime.now()
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    if p.returncode != 0:
        if str(stderr) == "b''":
            # qcli sends it's errors to stdout
            operational_log["qcli_error"] = str(stdout)
        else:
            # if qcli not installed or os related error...
            operational_log["qcli_error"] = str(stderr)
        raise Exception
    p.wait() # wait for qcli 
    operational_log["qcli_duration"] = (datetime.now() - qcli_start_time).total_seconds()
    # TODO: calc qcli output size
    metrics_start_time = datetime.now()
    metrics_log = extract_metrics(qcli_output)
    operational_log["metrics_extraction_duration"] = (datetime.now() - metrics_start_time).total_seconds()
    send_log(metrics_log,output_url)
    operational_log["status"] = "success"
except Exception as e:
    operational_log["status"] = "failed"
    operational_log["error"] = str(e)
finally:
    if os.path.exists(qcli_output): # delete qcli output
        os.remove(qcli_output)
    operational_log["total_duration"] = (datetime.now() - start_time).total_seconds()
    send_log(operational_log,output_url)

'''
video-path
qcli-path
output
bool - save xml.gz
bool - dry
'''