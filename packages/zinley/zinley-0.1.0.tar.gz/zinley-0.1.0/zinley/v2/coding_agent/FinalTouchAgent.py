import os
import asyncio
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from zinley.v2.scanner.ProjectScanner import ProjectScanner  # Ensure this module is correctly imported and available
from zinley.v2.ResultsManager import ResultsManager


class FinalTouchAgent:
    def __init__(self, directory_path, api_key, endpoint, deployment_id, max_tokens):
        self.directory_path = directory_path
        self.api_key = api_key
        self.endpoint = endpoint
        self.deployment_id = deployment_id
        self.max_tokens = max_tokens
        self.scanner = ProjectScanner(directory_path, api_key, endpoint, deployment_id, max_tokens)
        self.results_manager = ResultsManager()

    def find_full_paths(self, filenames):
        file_paths = []
        for root, _, files in os.walk(self.directory_path):
            for file in files:
                if file in filenames:
                    file_paths.append(os.path.join(root, file))
        return file_paths

    async def scanFiles(self, files):
        categorized_files = {
            "nib_files": [],
            "storyboard_files": [],
            "objc_files": [],
            "plist_files": [],
            "swift_files": []
        }

        full_paths = self.find_full_paths(files)
        for file in full_paths:
            if file.endswith('.xib'):
                categorized_files["nib_files"].append(file)
            elif file.endswith('.storyboard'):
                categorized_files["storyboard_files"].append(file)
            elif file.endswith('.m'):
                categorized_files["objc_files"].append(file)
            elif file.endswith('.plist'):
                categorized_files["plist_files"].append(file)
            elif file.endswith('.swift'):
                categorized_files["swift_files"].append(file)

        scan_tasks = []
        for category, file_list in categorized_files.items():
            if not file_list:  # Skip empty categories
                continue
            print(f"{category}: {file_list}")
            task = {
                "nib_files": self.scanner.get_nib_files_summaries,
                "storyboard_files": self.scanner.get_storyboard_files_summaries,
                "objc_files": self.scanner.get_objc_files_summaries,
                "plist_files": self.scanner.get_plist_files_summaries,
                "swift_files": self.scanner.get_swift_files_summaries
            }.get(category)

            if task:
                scan_tasks.append(self.analyze_task(category, task(file_list), self.results_manager))
            else:
                print(f"Unknown scan category: {category}")

        await asyncio.gather(*scan_tasks)

    async def analyze_task(self, category, task, results_manager):
        try:
            print(f"Starting analysis of {category}...")
            current_results = await task
            print(f"Completed analysis of {category}")
            self.results_manager.load_results_from_files(self.directory_path)
            result = self.results_manager.get_results()
            final = self.merge_json_arrays(current_results, result.get(category, []))
            result[category] = final
            results_manager.save_milestones_to_files(self.directory_path, result)

        except Exception as e:
            print(f"Error processing {category}: {e}")

    def merge_json_arrays(self, array1, array2):
        merged_array = []
        file_names = set()

        # Add entries from the first array
        for entry in array1:
            file_name = os.path.basename(entry["file_path"])
            if file_name not in file_names:
                merged_array.append(entry)
                file_names.add(file_name)

        # Add entries from the second array
        for entry in array2:
            file_name = os.path.basename(entry["file_path"])
            if file_name not in file_names:
                merged_array.append(entry)
                file_names.add(file_name)

        return merged_array
