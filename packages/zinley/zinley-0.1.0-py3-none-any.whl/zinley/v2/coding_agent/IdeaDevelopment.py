import os
import aiohttp
import asyncio
import json
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util.utils import clean_json

class IdeaDevelopment:
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
        try:
            with open(file_path, "r") as file:
                return file.read()
        except Exception as e:
            print(f"Failed to read file {file_path}: {e}")
            return None

    async def get_idea_plan(self, session, all_file_contents, user_prompt):
        """
        Get development plan for all txt files from Azure OpenAI based on user prompt.

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
                        "You are a senior iOS developer. Analyze the provided project files and create a detailed core purely technical development and feature plan to achieve the user request that fits with the current project setup. Focus on the following:\n\n"
                        "1. **Requirements Analysis:**\n"
                        "- Identify existing files to work on and explain why they are needed, describe exactly what to be updated, does it need to work with any files for integration.\n"
                        "- Identify new files that need to be created and explain why they are needed, describe exactly what to be built, does it need to work with any files for integration\n"
                        "- All new file names must be detailed, and show specific usage, preventing future conflict or overlapping.\n"
                        "- For each working file, list all related file to work together to provide enough context and prevent redeclaration or conflict.\n"
                        "- Follow best coding practices by using as many files as possible for specific needs, aiming for clean code.\n\n"
                        "- Do not rename file, only modify inside content. If file can't be used with that name, create a new file.\n"
                        "2. **UX Workflow:**\n"
                        "- Define screen-to-screen transitions (e.g., screen A -> screen B -> screen C).\n"
                        "3. **System Design:**\n"
                        "- Provide a detailed and clear system design without writing code.\n\n"
                        "Capabilities that you don’t have right now, ignore these related tasks:\n"
                        "- Third party integration\n"
                        "- Create Core data\n"
                        "- Install Networking dependencies like Firebase, AWS\n"
                        "- Create new Test file tasks\n"
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"Follow the user prompt strictly and provide a no code response:\n{user_prompt}\n\n"
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
                print(f"Error: {error_message}")
                return {
                    "reason": error_message
                }

            plan = await response.json()

            if 'choices' in plan and len(plan['choices']) > 0:
                message_content = plan['choices'][0]['message']['content']
                return message_content

    async def get_idea_plans(self, files, user_prompt):
        """
        Get development plans for a list of txt files from Azure OpenAI based on user prompt.

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
            plan = await self.get_idea_plan(session, all_file_contents, user_prompt)
            return plan
