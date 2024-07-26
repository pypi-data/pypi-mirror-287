from typing import Annotated
import typer
import requests
import posixpath
import os
import re
import json

import inquirer
from inquirer.themes import GreenPassion

from services import Projects
from constants import endpoint
from utils import UserProfile

from rich.console import Console

console = Console()

class Project:
    app = typer.Typer()

    def select():
        profile = UserProfile.load()
        projects = Projects(profile).get_all()	
        _projects = [f"{proj['title']}({proj['name']})" for proj in projects]

        projects_list = [
            inquirer.List(
                "project",
                message="Select a project from the options below",
                choices=_projects,
            ),
        ]
        answer = inquirer.prompt(projects_list, theme=GreenPassion())
        name = re.findall('\(([^)]+)\)', answer['project'])[0]

        selected = [project for project in projects if project.get('name') == name][0]
        
        profile['project'] = selected
        
        UserProfile.save(profile)

    @app.command(short_help="List all projects")
    def list():
        profile = UserProfile.load()
        project = profile.get('project', None)
        projects = Projects(profile).get_all()
        _ = [
            console.print(f"{ '*' if project is not None and proj['id'] == project['id']else ''} {proj['title']}({proj['id']})")
            for proj in projects
        ]


    @app.command(short_help="Create a new project")
    def create(name: Annotated[str, typer.Argument(help="The name of the project")]):
        url = posixpath.join(endpoint, 'projects')
        profile = UserProfile.load()
        try:
            resp = requests.put(url, headers={'x-api-key': profile['token']}, json=dict(title=name))
            resp.raise_for_status()

            print("Project created successfully")
        except Exception as ex:
            print(ex)

    @app.command(short_help="Set the default project")
    def set(id: Annotated[str, typer.Option(help="project Id to use")]):
        profile = UserProfile.load()
        projects = Projects(profile).get_all()
        project = [project for project in projects if project.get('id') == id]

        if len(project) > 0:
            profile['project'] = project[0]
            console.print(f"{project[0]['title']} as set as default project")
            UserProfile.save(profile)
        else:
            console.print("No project found")
