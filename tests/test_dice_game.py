import asyncio

import pytest

import main as main


@pytest.mark.parametrize(
    "simulated_inputs",
    [
        (["0", "1"]),
    ],
)
def test_ai_player_function(monkeypatch, simulated_inputs):
    inputs_iter = iter(simulated_inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs_iter))

    asyncio.run(main.play_game())

    assert True  # Ensure the function completes without crashing
