def build_prompt(topic, genre, mood, scene_length, context):
    return f"""
You are an expert entertainment industry writing assistant.

Your task is to generate a professional-quality script scene.

Use the following retrieved context for industry standards and tone:
{context}

User Requirements:
- Topic: {topic}
- Genre: {genre}
- Mood: {mood}
- Scene Length: {scene_length}

Instructions:
1. Write in screenplay scene format.
2. Use proper scene heading (INT./EXT.).
3. Keep tone consistent with the genre and mood.
4. Include character names in uppercase before dialogue.
5. Make the scene cinematic, engaging, and professional.
6. Maintain concise but vivid descriptions.
7. End the scene with a strong dramatic or emotional beat.

Output only the script scene.
"""