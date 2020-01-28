# qc-tools-automations

This repo contains the automations for the following workflow:
1. Video added to the input folder.
2. Qcli analyze the video and create *.xml.gz file.
3. Python script triggered and summerizes the *.xml.gz file.
4. The script sends the data as a log to elasticsearch.

## Installtion
1. Verify that ```inotify-tools``` installed by running:
```bash
inotifywait --help | head -1
```
the output should be something like:
```bash
inotifywait 3.14
```
2. Let’s grant execute permissions on ```qc-watcher.sh```:
```bash
chmod u+x qc-watcher.sh
```
3. Run the script via:
```bash
./qc-watcher.sh
```
4. Download ```qcli``` from:
https://mediaarea.net/download/binary/qcli/1.0/

## Logs
### metrics log:
```
{
   'min_y':7.0,
   'max_y':248.0,
   'min_u':7.0,
   'max_u':248.0,
   'min_v':12.0,
   'max_v':245.0
}
```
### operational log:
```
{
   'script_version':'0.1',
   'video_size_bytes':2565759,
   'qcli_duration':29.675265,
   'metrics_extraction_duration':1.489104,
   'status':'success',
   'total_duration':31.165828
}
```
