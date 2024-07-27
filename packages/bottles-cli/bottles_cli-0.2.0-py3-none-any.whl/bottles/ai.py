def call_anthropic(client, system_prompt, messages):
    """Call the Anthropic API."""
    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=4000,
        temperature=0,
        system=system_prompt,
        messages=messages
    )
    return response.content[0].text  # Extract the text content from the response

