# skidspammer
# Spams IP Loggers or "Image Logger" IP logging links as an anti-deterrent

It does this by restarting the TOR daemon every few seconds assigning you a new IP Address each time for each exit node allowing you to bypass features set by IP Logging systems like "unique IP Address" only options including rate limiting solutions set by these IP Loggers. Use this tool is someone is trying to threaten you or your potentially true IP Address was leaked or logged by these skids. This currently only works on Ubuntu and Debian based systems like Kali Linux but I'll add arch functionality later in the future including a web hook request technique.

## Make sure to have these installed

```
pip install -r requirements.txt
sudo apt-get install proxychains -y
```
### Next run this command

```
sudo proxychains -q main.py
```

