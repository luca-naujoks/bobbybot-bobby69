if voice_client.is_playing():
    voice_client.source = source
else:
    voice_client.play(source)






