def create_clone_prompt(model, ref_audio, ref_text):
    prompt = model.create_voice_clone_prompt(
        ref_audio=ref_audio,
        ref_text=ref_text
    )
    return prompt