from gtts import gTTS
import os

output_dir = "/Users/arghamukherjee/Downloads/Codebase/GithbProjects/TextToVoice_Python/Output/"
text_content = "Hello World !"
test_image_conversion_output = "a  kitchen with a refrigerator , sink and stove ."
language = 'en'
audio = gTTS(text=test_image_conversion_output,lang=language,slow=False)
audio.save(output_dir+"kitchen_with_refrigerator_sink_stove.mp3")
