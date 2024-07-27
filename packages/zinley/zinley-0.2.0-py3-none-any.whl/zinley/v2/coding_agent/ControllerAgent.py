import os
import sys
import json
import subprocess
import asyncio
import re

from zinley.v2.coding_agent.CodingAgent import CodingAgent
from zinley.v2.coding_agent.FormattingAgent import FormattingAgent
from zinley.v2.coding_agent.FileManagerAgent import FileManagerAgent
from zinley.v2.coding_agent.FileFinderAgent import FileFinderAgent
from zinley.v2.coding_agent.IdeaDevelopment import IdeaDevelopment
from zinley.v2.coding_agent.IdeaDevelopment import IdeaDevelopment
from zinley.v2.coding_agent.LongIdeaDevelopment import LongIdeaDevelopment
from zinley.v2.coding_agent.PromptAgent import PromptAgent
from zinley.v2.coding_agent.PrePromptAgent import PrePromptAgent
from zinley.v2.coding_agent.FinalTouchAgent import FinalTouchAgent
from zinley.v2.coding_agent.ReplacingAgent import ReplacingAgent
from zinley.v2.coding_agent.FileReplacingAgent import FileReplacingAgent
from zinley.v2.coding_agent.BugScannerAgent import BugScannerAgent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from xcodeOperation.XcodeProjectManager import XcodeProjectManager
from xcodeOperation.XcodeRunner import XcodeRunner

# Initialization and Setup
class ControllerAgent:
    def __init__(self, directory_path, api_key, endpoint, deployment_id, max_tokens):
        self.directory_path = directory_path
        self.api_key = api_key
        self.endpoint = endpoint
        self.deployment_id = deployment_id
        self.max_tokens = max_tokens
        self.idea = IdeaDevelopment(os.path.join(directory_path, "Zinley/Project_analysis"), api_key, endpoint, deployment_id, max_tokens)
        self.bug_scanner = BugScannerAgent(os.path.join(directory_path, "Zinley/Project_analysis"), api_key, endpoint, deployment_id, max_tokens)
        self.long = LongIdeaDevelopment(os.path.join(directory_path, "Zinley/Project_analysis"), api_key, endpoint, deployment_id, max_tokens)
        self.prompt = PromptAgent(os.path.join(directory_path, "Zinley/Project_analysis"), api_key, endpoint, deployment_id, max_tokens)
        self.preprompt = PrePromptAgent(os.path.join(directory_path, "Zinley/Project_analysis"), api_key, endpoint, deployment_id, max_tokens)
        self.coder = CodingAgent(os.path.join(directory_path), api_key, endpoint, deployment_id, max_tokens)
        self.xcode_operations = XcodeProjectManager(os.path.join(directory_path))
        self.xcode_runner = XcodeRunner(os.path.join(directory_path), api_key, endpoint, deployment_id, max_tokens)
        self.format = FormattingAgent(os.path.join(directory_path), api_key, endpoint, deployment_id, max_tokens)
        self.replace = FormattingAgent(os.path.join(directory_path), api_key, endpoint, deployment_id, max_tokens)
        self.fileManager = FileManagerAgent(os.path.join(directory_path), api_key, endpoint, deployment_id, max_tokens)
        self.fileFinder = FileFinderAgent(os.path.join(directory_path), api_key, endpoint, deployment_id, max_tokens)
        self.replaceFinder = FileReplacingAgent(os.path.join(directory_path), api_key, endpoint, deployment_id, max_tokens)
        self.final = FinalTouchAgent(os.path.join(directory_path), api_key, endpoint, deployment_id, max_tokens)

    # File and Directory Management
    def get_tree_txt_files(self):
        """Scan for tree.txt files in the specified directory."""
        tree_txt_files = []
        tree_path = self.directory_path + "/Zinley/Project_analysis"

        if not os.path.exists(tree_path):
            print(f"Directory does not exist: {tree_path}")
            return tree_txt_files

        for root, dirs, files in os.walk(tree_path):
            for file in files:
                if file == 'tree.txt':
                    file_path = os.path.join(root, file)
                    tree_txt_files.append(file_path)

        return tree_txt_files

    def get_txt_files(self):
        """Scan for all txt files in the specified directory."""
        txt_files = []
        txt_path = self.directory_path + "/Zinley/Project_analysis"

        if not os.path.exists(txt_path):
            print(f"Directory does not exist: {txt_path}")
            return txt_files

        for root, dirs, files in os.walk(txt_path):
            for file in files:
                if file.endswith('.txt'):
                    file_path = os.path.join(root, file)
                    txt_files.append(file_path)

        return txt_files

    async def update_tree(self):
        """Update the project directory tree and save to tree.txt."""
        tree_path = self.directory_path
        output_dir = os.path.join(tree_path, "Zinley", "Project_analysis")
        os.makedirs(output_dir, exist_ok=True)
        tree_file_path = os.path.join(output_dir, "tree.txt")
        # Open the file to write the tree output
        with open(tree_file_path, 'w') as f:
            # Run the tree command and capture the output
            result = subprocess.run(['tree', self.directory_path, '-I', 'Zinley'], stdout=subprocess.PIPE, text=True)
            # Write the output to the file
            f.write(result.stdout)

    def scan_needed_files(self, filenames):
        """Scan for specified files in the specified directory."""
        found_files = []

        if not os.path.exists(self.directory_path):
            print(f"Directory does not exist: {self.directory_path}")
            return found_files

        for root, dirs, files in os.walk(self.directory_path):
            for filename in filenames:
                if filename in files:
                    file_path = os.path.join(root, filename)
                    found_files.append(file_path)

        return found_files

    def read_file_content(self, file_path):
        try:
            with open(file_path, "r") as file:
                return file.read()
        except Exception as e:
            print(f"Failed to read file {file_path}: {e}")
            return None

    # Prompt and Idea Generation
    async def get_prompt(self, files, user_prompt):
        """Generate idea plans based on user prompt and available files."""
        return await self.prompt.get_prompt_plans(files, user_prompt)

    async def get_prePrompt(self, files, user_prompt):
        """Generate idea plans based on user prompt and available files."""
        return await self.preprompt.get_prePrompt_plans(files, user_prompt)

    async def get_idea_plans(self, files, user_prompt):
        """Generate idea plans based on user prompt and available files."""
        return await self.idea.get_idea_plans(files, user_prompt)

    async def get_bugs_plans(self, files, user_prompt):
        """Generate idea plans based on user prompt and available files."""
        return await self.bug_scanner.get_idea_plans(files, user_prompt)

    async def get_long_idea_plans(self, files, user_prompt, is_first):
        """Generate idea plans based on user prompt and available files."""
        return await self.long.get_idea_plans(files, user_prompt, is_first)

    async def get_file_planning(self, idea_plan, tree):
        """Generate idea plans based on user prompt and available files."""
        return await self.fileManager.get_file_plannings(idea_plan, tree)

    async def get_formatting_files(self, prompt, tree):
        """Generate idea plans based on user prompt and available files."""
        return await self.fileFinder.get_file_plannings(prompt, tree)

    async def get_replacing_files(self, prompt, files):
        """Generate idea plans based on user prompt and available files."""
        return await self.replaceFinder.get_file_plannings(prompt, files)

    async def scan_and_update(self, files):
        """Scan updated files and log the updates."""
        await self.final.scanFiles(files)
        return 'Done!'

    # Xcode Operations
    async def run_requests(self, list):
        return await self.xcode_runner.run_xcode_project(list, 'khoa_test')

    async def process_creation(self, data):
        # Check if 'Is_creating' is True
        if data.get('Is_creating'):
            # Extract the processes array
            processes = data.get('Adding_new_files', [])
            # Create a list of process details
            await self.xcode_operations.execute_files_creation(processes)
            await self.update_tree()

    # Coding Pipeline
    async def build_existing_context(self, existing_files):
        all_path = self.scan_needed_files(existing_files)
        all_context = ""

        for path in all_path:
            file_context = self.read_file_content(path)
            all_context += f"\n\nFile: {path}:\n{file_context}"

        return all_context

    async def get_coding_requests(self, instructions, context):
        self.coder.initialSetup(instructions, context)
        is_first = True
        title = ""
        totalfile = set()
        while True:
            result = await self.coder.get_coding_requests(is_first, title)

            Is_Completed = result['Is_Completed']
            is_first = False
            title = result['Title']
            Purpose_detail = result['Title']
            file_name = result['file_name']
            totalfile.update([file_name])
            code = result['code']
            if code == "":
                break
            print(f"Working on: {Purpose_detail}")
            main_path = self.coder.scan_for_single_file(file_name)
            await self.replace_all_code_in_file(main_path, code)
            if Is_Completed == "True" or Purpose_detail == "All tasks completed":
                break

        self.coder.clearConversationHistory()
        return totalfile

    async def replace_all_code_in_file(self, file_path, new_code_snippet):
        """Replace the entire content of a file with the new code snippet."""
        try:
            with open(file_path, 'w') as file:
                if self.contains_markdown_code(new_code_snippet):
                    cleaned_code = self.remove_markdown_code(new_code_snippet)
                    file.write(cleaned_code)
                else:
                    file.write(new_code_snippet)
            print(f"The codes have been successfully written in... {file_path}.")
        except Exception as e:
            print(f"Error writing code. Error: {e}")

    def contains_markdown_code(self, content):
        """Check if the content contains markdown code blocks."""
        markdown_code_pattern = r'```[\w]*[\s\S]*?```'  # code blocks with language specification
        return bool(re.search(markdown_code_pattern, content, re.MULTILINE))

    def remove_markdown_code(self, content):
        """This function removes the first and last lines if they are markdown code block delimiters."""
        lines = content.splitlines()

        if lines and lines[0].startswith('```') and lines[-1].startswith('```'):
            lines = lines[1:-1]

        return '\n'.join(lines).strip()

    # Pipelines
    async def code_format_pipeline(self, finalPrompt):
        print("code_format_pipeline")
        await self.update_tree()
        files = self.get_txt_files()
        tree = self.get_tree_txt_files()
        print("Now, I am working on file processing")
        file_result = await self.get_formatting_files(finalPrompt, tree)
        print(file_result)
        await self.process_creation(file_result)
        print("Completed processing files")
        print(f"Next, I will start the formatting/refactoring phase")
        working_files = file_result.get('working_files', [])
        print(f"Formatting: {working_files}")
        if working_files:
            await self.format.get_formats(working_files, finalPrompt)
            self.format.clearConversationHistory()
            print(f"Next, I will build to check if any compile error was made")
            all_fixing_files = await self.build_and_fix_compile_error(working_files)
            print(f"all_fixing_files: {all_fixing_files}")
            all_final_files = set()
            all_final_files.update(working_files)
            all_final_files.update(all_fixing_files)
            print(f"Formatting/refactoring phase phase done")
            if all_final_files:
                await self.scan_and_update(all_final_files)


    async def build_and_fix_compile_error(self, list):
        await self.update_tree()
        final_files = await self.run_requests(list)
        return final_files

    async def fix_compile_error_pipeline(self, file_list):
        print("fix_compile_error_pipeline")
        final_files = await self.build_and_fix_compile_error(file_list)
        if len(final_files) > 0:
            await self.scan_and_update(final_files)


    async def scan_potential_bug_pipeline(self, finalPrompt):
        print("scan_potential_bug_pipeline")
        await self.update_tree()
        files = self.get_txt_files()
        tree = self.get_tree_txt_files()

        print(f"Now I will create technical project analysis for clarification")

        idea_plan = await self.get_bugs_plans(files, finalPrompt)

        print(f"This is technical project analysis: {idea_plan}")
        """
        print("Now, I am working on file processing")
        file_result = await self.get_file_planning(idea_plan, tree)
        await self.process_creation(file_result)
        print("Completed processing files")
        print(f"Next, I will start the coding phase")
        existing_files = file_result.get('Existing_files', [])
        all_context = await self.build_existing_context(existing_files)
        totalfile = await self.get_coding_requests(idea_plan, all_context)

        print(f"Next, I will build to check if any compile error was made")
        all_fixing_files = await self.build_and_fix_compile_error(totalfile)
        print(f"all_fixing_files: {all_fixing_files}")
        all_final_files = set()
        all_final_files.update(totalfile)
        all_final_files.update(all_fixing_files)
        print(f"Coding phase done")
        if all_final_files:
            await self.scan_and_update(all_final_files)
            """


    async def replace_code_pipeline(self, finalPrompt):
        print("replace_code_pipeline")
        await self.update_tree()
        files = self.get_txt_files()
        tree = self.get_tree_txt_files()
        print("Now, I am working on file processing")
        file_result = await self.get_replacing_files(finalPrompt, files)
        print(file_result)
        await self.process_creation(file_result)
        print("Completed processing files")
        print(f"Next, I will start the replacing phase")
        working_files = file_result.get('working_files', [])
        print(f"Formatting: {working_files}")
        if working_files:
            await self.format.get_formats(working_files, finalPrompt)
            self.format.clearConversationHistory()
            print(f"Next, I will build to check if any compile error was made")
            all_fixing_files = await self.build_and_fix_compile_error(working_files)
            print(f"all_fixing_files: {all_fixing_files}")
            all_final_files = set()
            all_final_files.update(working_files)
            all_final_files.update(all_fixing_files)
            print(f"Replacing phase phase done")
            if all_final_files:
                await self.scan_and_update(all_final_files)

    async def regular_code_task_pipeline(self, finalPrompt):
        print("regular_code_task_pipeline")
        await self.update_tree()
        files = self.get_txt_files()
        tree = self.get_tree_txt_files()

        print(f"Now I will create technical project analysis for clarification")

        idea_plan = await self.get_idea_plans(files, finalPrompt)

        print(f"This is technical project analysis: {idea_plan}")

        print("Now, I am working on file processing")
        file_result = await self.get_file_planning(idea_plan, tree)
        await self.process_creation(file_result)
        print("Completed processing files")
        print(f"Next, I will start the coding phase")
        existing_files = file_result.get('Existing_files', [])
        all_context = await self.build_existing_context(existing_files)
        totalfile = await self.get_coding_requests(idea_plan, all_context)

        print(f"Next, I will build to check if any compile error was made")
        all_fixing_files = await self.build_and_fix_compile_error(totalfile)
        print(f"all_fixing_files: {all_fixing_files}")
        all_final_files = set()
        all_final_files.update(totalfile)
        all_final_files.update(all_fixing_files)
        print(f"Coding phase done")
        if all_final_files:
            await self.scan_and_update(all_final_files)


    async def major_code_task_pipeline(self, finalPrompt):
        print("major_code_task_pipeline")
        files = self.get_txt_files()
        tree = self.get_tree_txt_files()
        prompt = await self.get_prompt(files, finalPrompt)

        milestones = prompt.get('milestones', [])
        self.long.initial_setup(finalPrompt)
        is_first = True
        for milestone in milestones:
            await self.update_tree()
            goal = milestone['Goal']
            implementation_prompt = milestone['implementation_prompt']
            print(f"Working on: {goal}")

            print(f"Now I will create technical project analysis for clarification")

            idea_plan = await self.get_long_idea_plans(files, implementation_prompt, is_first)
            is_first = False

            print(f"This is technical project analysis: {idea_plan}")

            print("Now, I am working on file processing")
            file_result = await self.get_file_planning(idea_plan, tree)
            await self.process_creation(file_result)
            print("Completed processing files")
            print(f"Next, I will start the coding phase")
            existing_files = file_result.get('Existing_files', [])
            all_context = await self.build_existing_context(existing_files)
            totalfile = await self.get_coding_requests(idea_plan, all_context)

            print(f"Next, I will build to check if any compile error was made")
            all_fixing_files = await self.build_and_fix_compile_error(totalfile)
            all_final_files = set()
            all_final_files.update(totalfile)
            all_final_files.update(all_fixing_files)
            print(f"Coding phase done")

            if all_final_files:
                await self.scan_and_update(all_final_files)

        self.long.clear_conversation_history()


    async def get_started(self, user_prompt):
        files = self.get_txt_files()
        tree = self.get_tree_txt_files()

        print("Hi I am Zinley, I will process your prompt now")

        prePrompt = await self.get_prePrompt(files, user_prompt)
        finalPrompt = prePrompt['processed_prompt']
        pipeline = prePrompt['pipeline']
        await self.update_tree()
        if pipeline == "1":
            await self.code_format_pipeline(finalPrompt)
        elif pipeline == "2":
            await self.fix_compile_error_pipeline(list())  # add a missing parameter
        elif pipeline == "3":
            await self.replace_code_pipeline(finalPrompt)
        elif pipeline == "4":
            await self.regular_code_task_pipeline(finalPrompt)
        elif pipeline == "5":
            await self.major_code_task_pipeline(finalPrompt)

        print(f"Done work for: {user_prompt}")


# Main Execution
async def main():
    project_path = "../../projects/DemoApp"
    api_key = os.getenv("OPENAI_API_KEY", "96ae909e40534d49a70c5e4bdfe54f62")
    endpoint = "https://zinley.openai.azure.com"
    deployment_id = "gpt-4o"
    max_tokens = 4096
    user_prompt = input("What do you want to build? ")
    controller = ControllerAgent(project_path, api_key, endpoint, deployment_id, max_tokens)
    files = controller.get_txt_files()
    tree = controller.get_tree_txt_files()

    print("Hi I am Zinley, I will process your prompt now")

    prePrompt = await controller.get_prePrompt(files, user_prompt)
    print(prePrompt)
    finalPrompt = prePrompt['processed_prompt']
    pipeline = prePrompt['pipeline']
    await controller.update_tree()
    if pipeline == "1":
        await controller.code_format_pipeline(finalPrompt)
    elif pipeline == "2":
        await controller.fix_compile_error_pipeline(list())  # add a missing parameter
    elif pipeline == "3":
        await controller.replace_code_pipeline(finalPrompt)
    elif pipeline == "4":
        await controller.regular_code_task_pipeline(finalPrompt)
    elif pipeline == "5":
        await controller.major_code_task_pipeline(finalPrompt)

    print(f"Done work for: {user_prompt}")

if __name__ == "__main__":
    asyncio.run(main())
