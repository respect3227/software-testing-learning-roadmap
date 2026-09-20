import os

import pytest
import requests


BASE_URL = os.getenv("TEST_API_BASE_URL", "https://example.test/api")


@pytest.mark.api
@pytest.mark.parametrize(
    "keyword",
    ["汉绣", "黄梅戏", "不存在的项目"],
    ids=["existing-embroidery", "existing-opera", "not-found"],
)
def test_search_projects(keyword):
    """占位示例：替换 BASE_URL 后再执行真实接口测试。"""
    response = requests.get(
        f"{BASE_URL}/projects",
        params={"keyword": keyword, "page": 1, "page_size": 10},
        timeout=10,
    )

    assert response.status_code == 200
    body = response.json()
    assert "data" in body
    assert isinstance(body["data"], list)

