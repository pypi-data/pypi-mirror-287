from pathlib import Path
from nodestream.project import Project, ProjectPlugin


class GreatPlugin(ProjectPlugin):
    # def activate(self, project: Project) -> None:
    #     print("@@@@@@@@@@activating")
    #     project.add_plugin_scope_from_pipeline_resources(
    #         name="great", package="great_plugin"
    #     )
    
    def before_project_load(self, file_path: Path) -> None:
        print("beforrrrre")
    
    # def after_project_load(self, project: Project) -> None:
    #     print("after")