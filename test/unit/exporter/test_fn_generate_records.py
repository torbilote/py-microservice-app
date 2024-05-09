import pytest
import exporter.utils as utils


@pytest.mark.parametrize("number", [1, 15, 100])
def test_fn_generate_records_no_empty(number: int) -> None:
    records = utils.generate_records(number)

    assert len(records) == number
    assert records[0]["address"] == {
        "city": "Thomashaven",
    }
    assert records[0]["name"] == {
        "first": "Emma",
        "last": "Reed",
    }
