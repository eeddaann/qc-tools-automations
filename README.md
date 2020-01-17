# qc-tools-automations

This repo contains the automations for the following workflow:
1. Video added to the input folder.
2. Qcli analyze the video and create *.xml.gz file.
3. Python script triggered and summerizes the *.xml.gz file.
4. The script sends the data as a log to elasticsearch.

## installtion
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
4. Download the relevant ```qc-tools``` artifact from here:
https://old.mediaarea.net/download/snapshots/binary/qctools/

