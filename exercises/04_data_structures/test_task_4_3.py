

def test_task_stdout(capsys):
    """
    Перевірка роботи завдання
    """
    import task_4_3

    out, err = capsys.readouterr()
    correct_stdout = "['1', '3', '10', '20', '30', '100']"
    assert (
        out
    ), (
        "Нічого не виведено стандартний потік виведення. Потрібно не лише "
        "отримати потрібний результат, але й вивести його на стандартний потік "
        "виведення за допомогою print"
    )
    assert (
        correct_stdout == out.strip()
    ), "На стандартний потік виведення виводиться неправильний рядок"


def test_task_variables():
    """
    Перевірка, що в завданні створена потрібна змінна
    і в ній міститься правильний результат
    """
    import task_4_3

    task_vars = [var for var in dir(task_4_3) if not var.startswith("_")]

    correct_result = ["1", "3", "10", "20", "30", "100"]
    assert (
        "result" in task_vars
    ), "Список має бути записаний у змінну result"
    assert (
        type(task_4_3.result) == list
    ), f"За завданням у змінній result має бути список, а в ній {type(task_4_3.result).__name__}"
    assert (
        correct_result == task_4_3.result
    ), f"У змінній result має бути список {correct_result}"
