# VoiceCord | Discord voice recorder library
VoiceCord is a simple yet powerful voice recording package for Discord

## Usage

### Installation
```pip install voicecord```

### Usage

```python
import voicecord
import asyncio

client = voicecord.VoiceClient(ip="YOUR_PUBLIC_IP", token="YOUR_TOKEN", guild_id="YOUR_GUILD_ID", channel_id="VC_ID")


asyncio.run(client.connect())
```
