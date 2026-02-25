from draw_rich_local.style import enrich_d2_styles


def test_enriches_plain_nodes_with_icon_and_fill() -> None:
    source = """api: API Gateway
db: Postgres DB
api -> db: reads/writes
"""
    enriched = enrich_d2_styles(source)

    assert 'api: API Gateway {' in enriched
    assert 'style.fill: "#D6E4FF"' in enriched
    assert 'db: Postgres DB {' in enriched
    assert 'style.fill: "#E8F5E9"' in enriched
    assert "api -> db: reads/writes" in enriched
