import datetime
import json
import re

import pandas as pd

from solution import extract, load, transform, validate


def test_extract_reads_json_records(tmp_path):
    source_path = tmp_path / "records.json"
    records = [{"id": 1, "price": 100, "category": "electronics"}]
    source_path.write_text(json.dumps(records), encoding="utf-8")

    assert extract(source_path) == records


def test_extract_returns_empty_list_when_file_is_missing(tmp_path, capsys):
    result = extract(tmp_path / "missing.json")

    assert result == []
    assert "not found" in capsys.readouterr().out.lower()


def test_validate_keeps_only_positive_prices_and_nonempty_categories(capsys):
    records = [
        {"id": 1, "price": 100, "category": "electronics"},
        {"id": 2, "price": 0, "category": "books"},
        {"id": 3, "price": -5, "category": "clothing"},
        {"id": 4, "price": 50, "category": ""},
        {"id": 5, "price": 75, "category": "   "},
        {"id": 6, "price": 25},
    ]

    result = validate(records)

    assert result == [records[0]]
    output = capsys.readouterr().out
    assert re.search(r"1\s+valid", output, re.IGNORECASE)
    assert re.search(r"5\s+errors?", output, re.IGNORECASE)


def test_transform_applies_business_rules():
    records = [
        {"id": 1, "price": 100, "category": "home appliances"},
        {"id": 2, "price": 50, "category": "BOOKS"},
    ]

    result = transform(records)

    assert isinstance(result, pd.DataFrame)
    assert result["discounted_price"].tolist() == [90.0, 45.0]
    assert result["category"].tolist() == ["Home Appliances", "Books"]
    assert result["processed_at"].nunique() == 1
    datetime.datetime.fromisoformat(result["processed_at"].iloc[0])


def test_load_writes_csv_without_dataframe_index(tmp_path):
    output_path = tmp_path / "processed.csv"
    frame = pd.DataFrame([{"id": 1, "price": 100}])

    load(frame, output_path)

    loaded = pd.read_csv(output_path)
    assert loaded.to_dict(orient="records") == [{"id": 1, "price": 100}]
