@echo off
set ZIP=C:\PROGRA~1\7-Zip\7z.exe a -tzip -y -r
set REPO=agent_orange

fsum -r -jm -md5 -d%REPO% * > checksum.md5
move checksum.md5 %REPO%/checksum.md5

quick_manifest.exe "Agent Orange" "agent_orange" >%REPO%/manifest.json


cd %REPO%
%ZIP% ../%REPO%_21.ankiaddon *

REM cd %REPO%
%ZIP% ../%REPO%_CCBC.adze *
