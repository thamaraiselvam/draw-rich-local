from draw_rich_local.prompting import SYSTEM_PROMPT, build_user_prompt


def test_system_prompt_mentions_d2() -> None:
    assert "valid D2 code" in SYSTEM_PROMPT


def test_user_prompt_wraps_request() -> None:
    request = "A simple API with Redis cache"
    built = build_user_prompt(request)
    assert "REQUEST:" in built
    assert request in built
