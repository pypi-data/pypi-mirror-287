import asyncio
import io
import select
import time
import websockets
import json
import socket
import struct
import nacl.secret
import nacl.utils
import nacl.public
import nacl.encoding
from nacl.bindings import crypto_secretbox_open


def __init__():
    print("Voicecord package initialized")


class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    VOICECORD_TAG = f"{OKGREEN}[VoiceCord]{ENDC} "
    VOICECORD_ERROR_TAG = f"{FAIL}[VoiceCord]{ENDC} "


#custom exceptions
class VoiceCordError(Exception):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"VoiceCordError: {self.message}"


class VoiceClient:
    def __init__(self, ip, token, guild_id, channel_id):
        self.IP = ip
        self.TOKEN = token
        self.GUILD_ID = guild_id
        self.CHANNEL_ID = channel_id
        #BOT THINGS
        self.BOT_SESSION_ID = None
        self.BOT_USER_ID = None
        self.BOT_TOKEN = None
        self.BOT_ENDPOINT = None
        #VOICE SERVER THINGS
        self.VOICE_WS = None
        self.VOICE_IP = None
        self.VOICE_PORT = None

        self.final_audio_data = b''
        print(f"{colors.WARNING}[VoiceCord]{colors.ENDC} Voice client initialized")
        #return None

    async def connect(self):
        while True:
            try:
                uri = "wss://gateway.discord.gg/?v=10&encoding=json"
                async with websockets.connect(uri) as websocket:
                    await self.__identify(websocket)
                    await self.__state_update(websocket) #this will respond with 2 events: Voice State Update and Voice Server Update
                    await self.__listen_gateway(websocket)
            except websockets.exceptions.ConnectionClosedError as e:
                print(colors.VOICECORD_ERROR_TAG, f"Connection error: {e}. Reconnecting in 5 seconds...")
                await asyncio.sleep(5)
        print("Connecting to voice channel...")

    def disconnect(self):
        print("Disconnecting from voice channel...")

    def record(self):
        print("Recording audio...")

    def stop(self):
        print("Stopping audio recording...")

    def save(self):
        print("Saving audio recording...")

    def play(self):
        print("Playing audio recording...")

    def delete(self):
        print("Deleting audio recording...")

    def __del__(self):
        print("Voice client destroyed")

    async def __identify(self, websocket):
        payload = {
            "op": 2,
            "d": {
                "token": self.TOKEN,
                "intents": 513,  # Intents for GUILD_VOICE_STATES
                "properties": {
                    "$os": "linux",
                    "$browser": "my_library",
                    "$device": "my_library"
                }
            }
        }
        await websocket.send(json.dumps(payload))
    
    async def __state_update(self, websocket):
        await websocket.send(json.dumps(
            {
                "op": 4,
                "d": {
                    "guild_id": self.GUILD_ID,
                    "channel_id": self.CHANNEL_ID,
                    "self_mute": False,
                    "self_deaf": False
                }
            }
        ))
    

    async def __listen_gateway(self, websocket):
        #global YOUR_SESSION_ID
        #global YOUR_USER_ID
        #global YOUR_TOKEN
        #global YOUR_ENDPOINT
        print(colors.VOICECORD_TAG, "Handshaking with gateway...")
        async for message in websocket:
                event = json.loads(message)
                if event["op"] == 0:
                    if event["t"] == "READY":
                        self.BOT_SESSION_ID = event["d"]["session_id"]
                        self.BOT_USER_ID = event["d"]["user"]["id"]

                        await websocket.send(json.dumps({
                            "op": 4,
                            "d": {
                                "guild_id": self.GUILD_ID,
                                "channel_id": self.CHANNEL_ID,
                                "self_mute": False,
                                "self_deaf": False
                            }
                        }))
                    elif event["t"] == "VOICE_SERVER_UPDATE":
                        self.BOT_TOKEN = event["d"]["token"]
                        self.BOT_ENDPOINT = event["d"]["endpoint"]

                        await self.__voice_identify(websocket)
                elif event["op"] == 2:
                    print("GREAT SUCCESS!!!")

    
    async def __voice_identify(self, websocket):
        #connect to endpoint
        print(colors.VOICECORD_TAG, "Authenticating with voice server...")#
        #global VOICE_SERVER_WS
        #global YOUR_ENDPOINT
        #global YOUR_USER_ID
        #global YOUR_SESSION_ID
        #global YOUR_TOKEN

        async with websockets.connect(f"wss://{self.BOT_ENDPOINT}?v=4") as self.VOICE_WS:
            await self.VOICE_WS.send(json.dumps({
                "op": 0,
                "d": {
                    "server_id": self.GUILD_ID,
                    "user_id": self.BOT_USER_ID,
                    "session_id": self.BOT_SESSION_ID,
                    "token": self.BOT_TOKEN
                }
            }))
            await self.__listen_voice_server(self.VOICE_WS)

        """VOICE_SERVER_WS = await websockets.connect(f"wss://{YOUR_ENDPOINT}?v=4")

        await VOICE_SERVER_WS.send(json.dumps({
            "op": 0,
            "d": {
                "server_id": GUILD_ID,
                "user_id": YOUR_USER_ID,
                "session_id": YOUR_SESSION_ID,
                "token": YOUR_TOKEN
            }
        }))"""

    

    
    async def __listen_voice_server(self, websocket):
        print(websocket.closed)
        global VOICE_IP
        global VOICE_PORT
        udp_socket = None
        ssrc = None
        async for message in websocket:
                event = json.loads(message)
                #print(event) #I'm getting this one with op code 8
                # After receiving Opcode 8 Hello, you should send Opcode 3 Heartbeat—which contains an integer nonce—every elapsed interval:
                if event["op"] == 8: #heartbeat
                    print(colors.VOICECORD_TAG, "Initializing heartbeat after getting hello...")
                    interval = event["d"]["heartbeat_interval"]
                    timestamp = int(time.time() * 1000)
                    await websocket.send(json.dumps({
                        "op": 3,
                        "d": timestamp
                    }))
                    asyncio.create_task(self.__heartbeat(interval, websocket))
                elif event["op"] == 2:
                    print(colors.VOICECORD_TAG, "Got voice ready event, setting up UDP socket...")
                    self.VOICE_IP = event["d"]["ip"]
                    self.VOICE_PORT = event["d"]["port"]
                    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    udp_socket.bind(("", 0))
                    local_ip = udp_socket.getsockname()[0]
                    local_port = udp_socket.getsockname()[1]
                    print(colors.VOICECORD_TAG, f"UDP socket bound to {local_ip}:{local_port}")
                    ssrc = event["d"]["ssrc"]
                    ip, port = await self.__perform_ip_discovery(udp_socket, self.VOICE_IP, self.VOICE_PORT, event["d"]["ssrc"])
                    print("Discovered IP and port: ", ip, port)
                    await websocket.send(json.dumps({
                        "op": 1,
                        "d": {
                            "protocol": "udp",
                            "data": {
                                "address": self.IP,
                                "port": port,
                                "mode": "xsalsa20_poly1305"
                            }
                        }
                    }))
                elif event["op"] == 4:
                    #print("WOAHHHHH!!!!!") #SUCCESSFUL TO THIS POINT
                    #print(event)
                    await self.__handle_session_description(event["d"], udp_socket, ssrc)
                    #await test_udp()
                else:
                    pass
                    #print("Received voice server event:", event)
                    #await handle_voice_server_event(event)
                
    async def __heartbeat(self, interval, websocket):
        #print args
        while True:
            await asyncio.sleep(interval / 1000)
            try:
                await websocket.send(json.dumps({
                    "op": 3,
                    "d": int(time.time() * 1000)
                }))
                print("Heartbeat sent")
            except websockets.exceptions.ConnectionClosedError:
                print("Failed to send heartbeat: connection closed")
                
    
    async def __perform_ip_discovery(self, udp_socket, server_ip, server_port, ssrc):

        # Create a discovery packet
        packet = struct.pack('>HHI64sH', 0x1, 70, ssrc, b'\0' * 64, 0)

        # Send discovery packet to the server
        udp_socket.sendto(packet, (server_ip, server_port))

        # Set a timeout for receiving the response
        udp_socket.settimeout(5.0)

        try:
            # Receive the response from the server
            response, _ = udp_socket.recvfrom(74)
        except socket.timeout:
            print("IP discovery timeout")
            return None, None

        if len(response) < 74:
            print("Received malformed response")
            return None, None

        # Extract IP and port from the response
        ip = socket.inet_ntoa(response[8:12])
        port = struct.unpack('>H', response[72:74])[0]

        return ip, port
        

    async def __handle_session_description(self, data, udp_socket, ssrc):
        secret_key = data["secret_key"]
        udp_socket.settimeout(1000)
        await asyncio.create_task(self.__record_audio(udp_socket, ssrc, secret_key))


    async def __record_audio(self, udp_socket, ssrc, secret_key):
        box = nacl.secret.SecretBox(bytes(secret_key)) # TODO: Fix decryption xsalsa20_poly1305
        
        print(colors.VOICECORD_TAG, "Recording 10 bytes of audio...")

        while len(self.final_audio_data) < 10:
            #print("Waiting for audio data...")
            try:
                ready, _, _ = select.select([udp_socket], [], [], 5.0)
                if udp_socket in ready:
                    data, addr = udp_socket.recvfrom(65536)  # Adjust buffer size as necessary
                    #print(f"Received {len(data)} bytes from {addr}: {data.hex()}")

                    if len(data) > 12:

                        #convert the data to the format secret key is in

                        data = bytearray(data)

                        #data = bytes(data)
                        array = []

                        for i in range(len(data)):
                            array.append(data[i])

                        #print(f"Data: {array}")

                        #print(bytearray(bytes(b'\x00' * 12))[0])
                        

                        # convert data to string
                        #data = data.decode('utf-8')
                        #data = struct.unpack(f'{len(data)}B', data)

                        # Extract the RTP header
                        header = array[:12]

                        #print(f"RTP header: {header}")

                        # Add 12 zeros to the end of the header to construct the nonce
                        nonce = header + list(bytes(12))

                        # Construct the nonce
                        #nonce = 

                        #print(f"Nonce: {nonce}")

                        voice_data = array[12:]

                        #print(f"Voice data: {voice_data}")


                        #The rest of the data is the encrypted audio data (Should be 48 - 24 = 24 bytes)


                        #nonce  = data[:12]

                        #print(f"Nonce: {nonce}")

                        #if len(nonce) < 12:
                        #    nonce.ljust(24, b'\x00')
                        #remaining 12 bytes can be zeros or another fixed pattern
                        #nonce = nonce_part + bytes(12)
                        #copy the RTP header to get the nonce
                        #nonce = bytearray(24)
                        #nonce[:12] = data[:12]#data[:12]

                        #get the encrypted audio data
                        #encrypted = data[12:]
                        #print(f"Encrypted audio data: {bytes(encrypted)}")
                        try:
                            audio_data = box.decrypt(bytes(voice_data), bytes(nonce))
                            print("Received audio data", audio_data)
                            self.final_audio_data += audio_data

                            #exit()
                        except Exception as e:
                            #print(f"Decryption error: {e}")
                            print(colors.VOICECORD_ERROR_TAG, "Error decrypting audio data! Make sure someone is speaking in the voice channel")
                            raise VoiceCordError(f"Error decrypting audio data: {e}")
            except Exception as e:
                print(f"Error receiving audio data: {e}")
                break

        print(colors.VOICECORD_TAG, "Audio data recorded in OPUS format")
        return io.BytesIO(self.final_audio_data)


def join_voice():
    print("Joining voice channel...")