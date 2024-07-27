import re
import click
from tqdm import tqdm
from bottles.ai import call_anthropic

def extract_file_content(response):
    match = re.search(r'<batch_response>(.*?)</batch_response>', response, re.DOTALL)
    if match:
        content = match.group(1)
        # remove the \n at the start of the content but keep the \n at the end
        if content[0] == '\n':
            content = content[1:]
        return content
    else:
        click.secho(f"Warning: Could not extract file content from response.", fg='yellow', err=True)
        return None

def update_file(client, system_prompt, messages, git_root, file_path, batch_size=100):
    # make a deep copy of messages
    messages = messages.copy()
    file_lines = open(git_root / file_path, 'r').readlines()

    # Split the file into batches of 100 lines
    num_lines = len(file_lines)

    updated_file = ""

    
    user_message = f"""
Examine the batch of code below from the file '{file_path}' and provide the updated content for the batch based on the @b instructions.
Before making any changes, consider:
1. Before making any changes, consider:
   - How the instructions apply to this specific batch
   - The batch in the context of the entire file and all previously edited batches
   - The overall structure and purpose of the code
   - Potential impacts on other parts of the file and other files in the project
   - Best practices and coding standards for the language
   - Potential issues and improvements not mentioned in the instructions

2. Make improvements to the code, ensuring you:
   - Address all relevant aspects of the instructions
   - Maintain or enhance code readability and efficiency
   - Use the correct indentation and formatting of each line
   - Add, remove, or modify lines as necessary, matching surrounding indentation
   - Consider the file type when formatting the edited lines
   - Ensure consistency with all previously edited batches and the project context

3. If no improvements are needed or if the instructions don't apply to this batch, respond with the lines unchanged.

CRITICAL: 
- USE THE RIGHT indentation and formatting.
- Focus only on code improvements based on the instructions and your analysis of the file and project context.
- Ensure consistency with all previously edited batches and other files in the project.

IMPORTANT: RETURN ONLY THE EDITED BATCH INSIDE <batch_response> TAGS, WITH THE RIGHT INDENTATION. NO EXPLANATIONS OR COMMENTS.
DO NOT FOR ANY REASON RETURN THE LINE NUMBERS. WE ONLY NEED THE CODE LIKE YOU WERE WRITING IT IN A FILE. MAKE SURE TO INCLUDE CORRECT NUMBER OF TRAILING NEW LINES
""".strip()
    messages.append({"role": "user", "content": user_message})
    messages.append({"role": "assistant", "content": "Understood, awaiting batch of code to be provided."})

    for i in tqdm(range(0, num_lines, 100), desc=f"Updating {file_path}...", total=num_lines // 100):
        batch_lines = file_lines[i:i+100]
        batch_content = ''.join(batch_lines)

        user_message = f"""<batch file={file_path} batch_num={i}>
{batch_content}
</batch>
"""
        messages.append({"role": "user", "content": user_message})
        messages.append({"role": "assistant", "content": "<batch_response>"})

        response = "<batch_response>"+call_anthropic(client, system_prompt, messages)
        messages[-1]["content"] = response
        response = extract_file_content(response) or batch_content

        updated_file += response

    return updated_file



        
