import pytest
from domains.shared.entities import Command, CommandList


@pytest.mark.parametrize(
    "string,expected_list",
    [
        (
            "MLR",
            CommandList(commands=[Command("M"), Command("L"), Command("R")]),
        ),
        ("M", CommandList(commands=[Command("M")])),
        ("L", CommandList(commands=[Command("L")])),
        ("R", CommandList(commands=[Command("R")])),
    ],
)
def test_success(string, expected_list):
    result = CommandList.validate(commands_str=string)

    assert result == expected_list


def test_empty_list():
    with pytest.raises(ValueError):
        CommandList.validate(commands_str="")


def test_list_to_str():
    result = str(CommandList.validate(commands_str="MLR"))

    assert result == "MLR"
