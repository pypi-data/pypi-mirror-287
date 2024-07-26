import os
import aiohttp
import asyncio
import json
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util.utils import clean_json
from json_repair import repair_json

class PrePromptAgent:
    def __init__(self, directory_path, api_key, endpoint, deployment_id, max_tokens):
        self.directory_path = directory_path
        self.api_key = api_key
        self.endpoint = endpoint
        self.deployment_id = deployment_id
        self.max_tokens = max_tokens
        self.headers = {
            "api-key": self.api_key,
            "Content-Type": "application/json"
        }

    def scan_txt_files(self):
        """
        Scan for all txt files in the specified directory.

        Returns:
            list: Paths to all txt files.
        """
        txt_files = []

        if not os.path.exists(self.directory_path):
            print(f"Directory does not exist: {self.directory_path}")
            return txt_files

        for root, dirs, files in os.walk(self.directory_path):
            for file in files:
                if file.endswith('.txt'):
                    file_path = os.path.join(root, file)
                    txt_files.append(file_path)

        return txt_files

    def read_file_content(self, file_path):
        """
        Read the content of a specified file.

        Args:
            file_path (str): The path to the file.

        Returns:
            str: The content of the file, or None if an error occurs.
        """
        try:
            with open(file_path, "r") as file:
                return file.read()
        except Exception as e:
            print(f"Failed to read file {file_path}: {e}")
            return None

    async def get_prePrompt_plan(self, session, all_file_contents, user_prompt):
        """
        Get a development plan for all txt files from Azure OpenAI based on the user prompt.

        Args:
            session (aiohttp.ClientSession): The aiohttp session to use for the request.
            all_file_contents (str): The concatenated contents of all files.
            user_prompt (str): The user's prompt.

        Returns:
            dict: Development plan or error reason.
        """
        payload = {
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are a senior iOS developer and prompt engineering specialist. Analyze the provided project files and the user's prompt and response in JSON format. Follow these guidelines:\n\n"
                        "processed_prompt: If the user's original prompt is not in English, translate it to 100% English. Correct grammar, ensure it is clear, concise, and based on current project insights. Keep it crisp and short, avoiding confusion.\n"
                        "pipeline: You need to pick one best pipeline that fits the user's prompt. Only respond with a number for the specific pipeline you pick, such as 1, 2, 3, 4, 5, or 6, following the guideline below:\n"
                        "1. Format code: Must use For refactoring, formatting code, writing file comments, or anything related to code formatting.\n"
                        "2. Fix compile error: Must use If the user mentions any compile errors while running or building the app, fix them.\n"
                        "3. Replace code: Must use If the user asks to replace specific code in multiple files, such as adding 'self' to all closures etc...\n"
                        "4. Regular code builder: Mostly used for regular builder request, write a regular/simple app, writing test cases, simple milestones, etc., and modifies less than 10 files.\n"
                        "5. Significant code builder: Only for special significant large milestones, such as replacing significant code or writing extensive code for more than 10 new files, and modifying more than 10 files.\n\n"
                        "The JSON response must follow this format:\n\n"
                        "{\n"
                        '    "processed_prompt": "",\n'
                        '    "pipeline": "1 or 2 or 3 or 4 or 5"\n'
                        "}\n\n"
                        "Return only a valid JSON response without additional text or Markdown symbols or invalid escapes."
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"User original prompt:\n{user_prompt}\n\n"
                        f"Here are the current project files:\n{all_file_contents}\n"
                    )
                }
            ],
            "temperature": 0.2,
            "top_p": 0.1,
            "max_tokens": self.max_tokens
        }

        url = f"{self.endpoint}/openai/deployments/{self.deployment_id}/chat/completions?api-version=2024-04-01-preview"

        async with session.post(url, headers=self.headers, json=payload) as response:
            if response.status != 200:
                response_json = await response.json()
                error_message = response_json.get('error', {}).get('message', 'Unknown error')
                return {
                    "reason": error_message
                }

            plan = await response.json()

            if 'choices' in plan and len(plan['choices']) > 0:
                message_content = plan['choices'][0]['message']['content']
                try:
                    plan_json = json.loads(message_content)
                    return plan_json
                except json.JSONDecodeError:
                    good_json_string = repair_json(message_content)
                    plan_json = json.loads(good_json_string)
                    return plan_json

    async def get_prePrompt_plans(self, files, user_prompt):
        """
        Get development plans for a list of txt files from Azure OpenAI based on the user prompt.

        Args:
            files (list): List of file paths.
            user_prompt (str): The user's prompt.

        Returns:
            dict: Development plan or error reason.
        """
        all_file_contents = ""

        for file_path in files:
            file_content = self.read_file_content(file_path)
            if file_content:
                all_file_contents += f"\n\nFile: {file_path}:\n{file_content}"

        async with aiohttp.ClientSession() as session:
            plan = await self.get_prePrompt_plan(session, all_file_contents, user_prompt)
            print(f"Completed preparing for: {user_prompt}")
            return plan

# Example usage
async def main():
    directory_path = "path/to/your/project"
    api_key = "your_api_key"
    endpoint = "your_endpoint"
    deployment_id = "your_deployment_id"
    max_tokens = 1500
    files = ["file1.txt", "file2.txt"]
    user_prompt = "Your user prompt here"

    agent = PrePromptAgent(directory_path, api_key, endpoint, deployment_id, max_tokens)
    pre_prompt_plan = await agent.get_prePrompt_plans(files, user_prompt)
    print(pre_prompt_plan)

if __name__ == "__main__":
    asyncio.run(main())
