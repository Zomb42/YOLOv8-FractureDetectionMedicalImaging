import yaml

def conda_to_pip(conda_file, pip_file):
    with open(conda_file, 'r') as file:
        conda_env = yaml.safe_load(file)

    pip_requirements = conda_env.get('dependencies', [])
    pip_packages = []

    for dependency in pip_requirements:
        if isinstance(dependency, dict) and 'pip' in dependency:
            pip_packages.extend(dependency['pip'])
        elif isinstance(dependency, str):
            pip_packages.append(dependency)

    with open(pip_file, 'w') as file:
        for package in pip_packages:
            file.write(f"{package}\n")

conda_file = 'environment.yml'
pip_file = 'requirements.txt'
conda_to_pip(conda_file, pip_file)