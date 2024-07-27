import os
import asyncio
import re
from pbxproj import XcodeProject
from pbxproj.pbxextensions import FileOptions
import shutil
from datetime import datetime

class XcodeProjectManager:
    def __init__(self, directory_path):
        self.directory_path = directory_path

    async def create_and_add_folder_to_xcodeproj(self, project_root_path, project_path, group_name, parent_group_name=None):
        project_root_path = os.path.expanduser(project_root_path)
        project_path = os.path.expanduser(project_path)

        try:
            if not os.path.exists(project_root_path):
                print(f"The specified project path {project_root_path} does not exist.")
                return

            full_path = (
                os.path.join(project_root_path, parent_group_name, group_name)
                if parent_group_name
                else os.path.join(project_root_path, group_name)
            )
            os.makedirs(full_path, exist_ok=True)
            print(
                f"Folder '{group_name}' created successfully in {os.path.join(project_root_path, parent_group_name) if parent_group_name else project_root_path}."
            )

            xcodeproj_path = next(
                (
                    os.path.join(project_root_path, item)
                    for item in os.listdir(project_root_path)
                    if item.endswith(".xcodeproj")
                ),
                None,
            )
            if not xcodeproj_path:
                print(f"No .xcodeproj file found in {project_root_path}")
                return

            project = XcodeProject.load(os.path.join(xcodeproj_path, "project.pbxproj"))
            parent_group = project.get_or_create_group(parent_group_name) if parent_group_name else None
            project.get_or_create_group(group_name, parent=parent_group)
            project.save()

            print(f"Folder '{group_name}' added to the Xcode project successfully.")
            return full_path
        except Exception as e:
            print(f"Error creating and adding folder: {e}")
            return None

    def get_current_time_formatted(self):
        current_time = datetime.now()
        formatted_time = current_time.strftime("%m/%d/%y")
        return formatted_time

    async def create_and_add_file_to_xcodeproj(self, project_root_path, relative_path, file_name):
        try:
            if not os.path.exists(project_root_path):
                print(f"The specified project root path {project_root_path} does not exist.")
                return

            full_path = os.path.join(project_root_path, relative_path, file_name) if relative_path else os.path.join(project_root_path, file_name)

            # Check if the file already exists
            if os.path.exists(full_path):
                print(f"The file '{file_name}' already exists in {os.path.join(project_root_path, relative_path) if relative_path else project_root_path}. Skipping creation.")
                return

            # Create the file with content
            file_content = f"""// \n//  {file_name}.swift \n//  {relative_path} \n// \n//  Created by Zinley on {self.get_current_time_formatted()} \n// \n"""
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, 'w') as file:
                file.write(file_content)
            print(f"File '{file_name}' created successfully in {os.path.join(project_root_path, relative_path) if relative_path else project_root_path}.")

            # Find the .xcodeproj file
            xcodeproj_path = next((os.path.join(project_root_path, item) for item in os.listdir(project_root_path) if item.endswith('.xcodeproj')), None)
            if not xcodeproj_path:
                print(f"No .xcodeproj file found in {project_root_path}")
                return

            # Add the file to the Xcode project
            project = XcodeProject.load(os.path.join(xcodeproj_path, "project.pbxproj"))
            file_options = FileOptions(create_build_files=True)
            parent_group = project.get_or_create_group(relative_path) if relative_path else None
            project.add_file(full_path, file_options=file_options, force=False, parent=parent_group)
            project.save()
            print(f"File '{file_name}' added to the Xcode project successfully.")
            return full_path
        except Exception as e:
            print(f"Error creating and adding file: {e}")
            return None

    async def execute_instructions(self, instructions):
        for instruction in instructions:
            print("---------------------------------------------------------------------------------------")
            try:
                print(f"Executing Step {instruction['Step']}: {instruction['Title']}")
            except:
                print(f"Something wrong with instruction: {instruction}")

            function_name = instruction["Function_to_call"]
            parameters = instruction["Parameters"]
            if function_name == "create_and_add_folder_to_xcodeproj":
                await self.create_and_add_folder_to_xcodeproj(**parameters)
            elif function_name == "create_and_add_file_to_xcodeproj":
                await self.create_and_add_file_to_xcodeproj(**parameters)
            elif function_name == "replace_snippet_code_in_file":
                await self.replace_snippet_code_in_file(**parameters)
            elif function_name == "replace_all_code_in_file":
                file_path = parameters['file_path']
                await self.replace_all_code_in_file(file_path, parameters['new_code_snippet'])
            else:
                print(f"Unknown function: {function_name}")

    async def execute_files_creation(self, instructions):
        for instruction in instructions:
            print("---------------------------------------------------------------------------------------")
            try:
                print(f"Executing Step {instruction['Title']}")
            except:
                print(f"Something wrong with instruction: {instruction}")

            parameters = instruction["Parameters"]
            function_name = instruction["Function_to_call"]
            if function_name == "create_and_add_file_to_xcodeproj":
                await self.create_and_add_file_to_xcodeproj(**parameters)
            else:
                print(f"Unknown function: {function_name}")


# Usage example:
# manager = XcodeProjectManager("/path/to/project")
# asyncio.run(manager.execute_instructions(instructions))
