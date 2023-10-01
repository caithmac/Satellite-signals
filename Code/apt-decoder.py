# Import the libraries
import pyaudio
import wave
import noaa_apt as apt

# Define some constants
CHUNK = 1024 # Number of audio samples per buffer
FORMAT = pyaudio.paInt16 # Audio format (16-bit integer)
CHANNELS = 1 # Number of audio channels (mono)
RATE = 11025 # Sampling rate (Hz)
RECORD_SECONDS = 600 # Maximum recording time (seconds)
WAVE_FILE = "signal.wav" # File name to save the audio
IMAGE_FILE = "image.png" # File name to save the image

# Create a PyAudio object
p = pyaudio.PyAudio()

# Open a stream for recording
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# Ask the user to start the APT signal transmission
print("Please start the APT signal transmission and press Enter.")
input()

# Start recording
print("Recording...")
frames = [] # List of audio frames

# Loop until the maximum recording time is reached or the user presses Ctrl+C
try:
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK) # Read a chunk of data from the stream
        frames.append(data) # Append the data to the frames list
except KeyboardInterrupt:
    print("Recording stopped by user.")

# Stop recording
print("Recording finished.")
stream.stop_stream() # Stop the stream
stream.close() # Close the stream
p.terminate() # Terminate the PyAudio object

# Save the audio to a WAV file
wf = wave.open(WAVE_FILE, 'wb') # Open a WAV file for writing
wf.setnchannels(CHANNELS) # Set the number of channels
wf.setsampwidth(p.get_sample_size(FORMAT)) # Set the sample width
wf.setframerate(RATE) # Set the frame rate
wf.writeframes(b''.join(frames)) # Write the frames as bytes
wf.close() # Close the file

# Decode the APT signal and save it as an image
image = apt.decode(WAVE_FILE, False) # Decode the WAV file without histogram equalization
image.save(IMAGE_FILE) # Save the image as a PNG file

# Show a message to the user
print(f"Image saved as {IMAGE_FILE}.")
