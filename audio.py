import openai
import pyaudio
import wave
import json

openai.api_key = "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"

def record_audio(output_file, duration=5, sample_rate=44100, chunk_size=1024, channels=2):
    audio = pyaudio.PyAudio()

    stream = audio.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=sample_rate,
                        input=True,
                        frames_per_buffer=chunk_size)

    print("Recording audio...")

    frames = []
    for _ in range(0, int(sample_rate / chunk_size * duration)):
        data = stream.read(chunk_size)
        frames.append(data)

    print("Finished recording.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio to a WAV file
    wave_file = wave.open(output_file, 'wb')
    wave_file.setnchannels(channels)
    wave_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    wave_file.setframerate(sample_rate)
    wave_file.writeframes(b''.join(frames))
    wave_file.close()


def audio_to_text(filename):
    audio_file = open(filename, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    text_string = json.dumps(transcript)

    return text_string


def main_func():
    # Example usage
    output_file = 'recorded_audio.wav'
    record_audio(output_file, duration=8)  # Record for 8 seconds
    print("Audio successfully recorded!")

    print("--------------------------------------\n")

    text_string = audio_to_text(output_file)

    sport, team1, team2 = get_contents(text_string)

    return sport, team1, team2


def get_contents(text_string):
    openai.api_key = "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"
    messages = [ {"role": "system", "content": 
              "Basketball"} ]
    
    prompt = f"In the below sentence, what is the sport and what are the names of the two sports teams? Answer in the format Sport: \n Team 1: \n Team2: \n The sentence is {text_string}."
    messages.append(
            {"role": "user", "content": prompt},
        )
    chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    contents = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": contents})

    sport_index = 0 + 7
    sport_end_index = contents.index("Team 1:")
    sport = contents[sport_index:sport_end_index]

    team1_index = contents.index("Team 1:") + 8
    team1_end_index = contents.index("Team 2:")
    team1 = contents[team1_index:team1_end_index]

    team2_index = contents.index("Team 2:") + 8
    team2_end_index = len(contents)
    team2 = contents[team2_index:team2_end_index]

    return sport.strip(), team1.strip(), team2.strip()
