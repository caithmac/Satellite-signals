This is a brief documentation for the program that asks the user for an APT signal and converts that into an image for NOAA.

- The program uses the Python programming language and requires two external libraries: pyaudio and noaa-apt.
- The program records the audio input from the user's microphone using the pyaudio library and saves it as a WAV file named "signal.wav".
- The program then decodes the APT signal from the WAV file using the noaa-apt library and saves it as a PNG image named "image.png".
- The program also prints some messages to the user during the recording and decoding process.
- The program has some constants that can be changed by the user, such as the maximum recording time, the file names, and the audio parameters.
- The program assumes that the user has a valid APT signal transmission ready to be recorded and that the audio input device is working properly.
- The program does not perform any error handling or validation on the input or output files.