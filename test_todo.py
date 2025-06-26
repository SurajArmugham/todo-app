import todo

def test_add_task():
    todo.tasks = []  # Reset task list
    todo.add_task("Test task")
    assert len(todo.tasks) == 1
    assert todo.tasks[0]["description"] == "Test task"
    assert todo.tasks[0]["done"] is False

def test_complete_task():
    todo.tasks = [{"description": "Sample task", "done": False}]
    todo.complete_task(0)
    assert todo.tasks[0]["done"] is True

def test_list_tasks_output(capsys):
    todo.tasks = [{"description": "Sample task", "done": False}]
    todo.list_tasks()
    captured = capsys.readouterr()
    assert "Sample task" in captured.out