from prefect import flow, task

@task
def greet(name):
    print(f"Hello, {name}!")

@flow
def my_flow():
    greet("Prefect user")

if __name__ == "__main__":
    my_flow()
