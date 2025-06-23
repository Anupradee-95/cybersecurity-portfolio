# Splunk Log Analysis – Brute Force Detection

## Objective
Detect multiple failed login attempts indicating brute force activity.

## Sample Query Used
```spl
index=windows sourcetype="WinEventLog:Security" EventCode=4625
| stats count by Account_Name, host, src_ip
| where count > 10
