import os
from pipsetup.progress.progress import ProgressIndicator

class ProjectGenerator:
    def __init__(self, project_name: str, author: str, email: str):
        self.project_name = project_name
        self.author = author
        self.email = email
        self.templates_dir = os.path.join(os.path.dirname(__file__), 'templates')
    
    def create(self):
        with ProgressIndicator(message=f'Generating project {self.project_name}') as progress:
            os.makedirs(f'workspace_{self.project_name}', exist_ok=True)
            self._create_file('setup_py_template.py', 'setup.py')
            self._create_file('setup_cfg_template.cfg', 'setup.cfg')
            self._create_file('manifest_template.in', 'MANIFEST.in')
            self._create_file('readme_template.md', 'README.md')
            self._create_github_workflow()
            self._create_folder_project()
            progress.stop(final_message=f"Project {self.project_name} created successfully.")
    
    def _create_file(self, template_file, output_file):
        with ProgressIndicator(message=f'Generating file {output_file}') as progress:
            with open(os.path.join(self.templates_dir, template_file)) as src_file:
                content = src_file.read()
                content = content.format(
                    project_name=self.project_name,
                    author=self.author,
                    email=self.email
                )
            with open(os.path.join(f'workspace_{self.project_name}', output_file), 'w') as dest_file:
                dest_file.write(content)
            progress.stop(final_message=f"created successfully {output_file}")
    
    def _create_github_workflow(self):
        workflow_dir = os.path.join(f'workspace_{self.project_name}', '.github', 'workflows')
        os.makedirs(workflow_dir, exist_ok=True)
        self._create_file('publish_yml_template.yml', os.path.join('.github', 'workflows', 'publish.yml'))
    def _create_folder_project(self):
        workflow_dir = os.path.join(f'workspace_{self.project_name}', self.project_name)
        os.makedirs(workflow_dir, exist_ok=True)
        self._create_file('file_project_template.py', os.path.join(self.project_name,f'{self.project_name}.py'))

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Generate a Python project structure.')
    parser.add_argument('project_name', type=str, help='The name of the project')
    parser.add_argument('author', type=str, help='The author of the project')
    parser.add_argument('email', type=str, help='The author\'s email address')

    args = parser.parse_args()
    
    generator = ProjectGenerator(args.project_name, args.author, args.email)
    generator.create()