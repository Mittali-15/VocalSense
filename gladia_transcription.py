import requests
import os

gladia_key = 'dc7217fc-3024-4f69-949d-1cc5696298be'


def audio_transcription(filepath: str):
    """
    Transcribe audio file using Gladia API.

    Parameters:
        filepath (str): Path to the audio file.

    Returns:
        dict: Response from the Gladia API.
    """

    # Define API key as a header
    headers = {
        'x-gladia-key': f'{gladia_key}'  # Make sure to define 'gladia_key' somewhere in your code.
    }

    # Split the filename and extension
    filename, file_ext = os.path.splitext(filepath)

    with open(filepath, 'rb') as audio:
        # Prepare data for API request
        files = {
            'audio': (filename, audio, f'audio/{file_ext[1:]}'),  # Specify audio file type
            'toggle_diarization': (None, True),  # Toggle diarization option
            'diarization_max_speakers': (None, 2),  # Set maximum number of speakers for diarization
            'output_format': (None, 'txt')  # Specify output format as text
        }

        print('Sending request to Gladia API')
        
        # Make a POST request to Gladia API
        response = requests.post('https://api.gladia.io/audio/text/audio-transcription/', headers=headers, files=files)
        
        if response.status_code == 200:
            response = response.json()
        
            # Extract the transcription from the response
            prediction = response['prediction']

            # Write the transcription to a text file
            with open('transcription.txt', 'w') as f:
                f.write(prediction)
            
            return response
            
        else:
            # If the request fails, print an error message and return the JSON response
            print('Request failed')
            return response.json()

audio_transcription('./1.mp3')