from pathlib import Path


PROJECT_ROOT = Path(__file__).parent


folders = [
    # Book chapters
    "book/00-preface",
    "book/01-foundations",
    "book/02-sql",
    "book/03-databases",
    "book/04-pipelines",
    "book/05-big-data",
    "book/06-spark",
    "book/07-nosql",
    "book/08-cloud",
    "book/09-modern-data-platforms",
    "book/10-production",

    # Practical code
    "code/01-python-foundations",
    "code/02-sql",
    "code/03-databases",
    "code/04-etl-pipelines",
    "code/05-pyspark",
    "code/06-streaming",
    "code/07-cloud",
    "code/08-capstone-projects",

    # Jupyter notebooks
    "notebooks/sql",
    "notebooks/pyspark",
    "notebooks/databases",
    "notebooks/databricks",

    # Datasets
    "datasets/sample_data",

    # Diagrams
    "diagrams/architecture",
    "diagrams/database",
    "diagrams/distributed_systems",

    # Exercises
    "exercises/sql",
    "exercises/python",
    "exercises/spark",
    "exercises/system_design",

    # Projects
    "projects/project-01-batch-etl",
    "projects/project-02-cloud-lakehouse",
    "projects/project-03-streaming-pipeline",
    "projects/project-04-capstone",
]


files = [
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "requirements.txt",
    "pyproject.toml",
    "mkdocs.yml",
    "datasets/README.md",
]


def create_structure():
    for folder in folders:
        folder_path = PROJECT_ROOT / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {folder}")

    for file in files:
        file_path = PROJECT_ROOT / file

        if not file_path.exists():
            file_path.touch()
            print(f"Created file: {file}")
        else:
            print(f"Already exists: {file}")


if __name__ == "__main__":
    create_structure()
    print("\nComplete Data Engineering book structure created successfully.")