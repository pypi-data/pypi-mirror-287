from typing import OrderedDict

import pytest

from pygitguardian.models import (
    Detail,
    DetailSchema,
    Document,
    DocumentSchema,
    HealthCheckResponseSchema,
    HoneytokenResponse,
    HoneytokenResponseSchema,
    HoneytokenWithContextResponse,
    HoneytokenWithContextResponseSchema,
    Match,
    MatchSchema,
    MultiScanResult,
    MultiScanResultSchema,
    PolicyBreak,
    PolicyBreakSchema,
    Quota,
    QuotaResponse,
    QuotaResponseSchema,
    QuotaSchema,
    ScanResult,
    ScanResultSchema,
)


class TestModel:
    def test_document_model(self):
        """
        GIVEN a simple document
        THEN base model methods should produce the appropriate types.
        """
        document = Document("hello", "hello")
        assert isinstance(document.to_json(), str)
        assert isinstance(document.to_dict(), dict)
        assert isinstance(str(document), str)

    def test_document_handle_0_bytes(self):
        document = Document.SCHEMA.load(
            {"filename": "name", "document": "hello\0world"}
        )
        assert document["document"] == "hello\x1aworld"

    def test_document_handle_surrogates(self):
        document = Document.SCHEMA.load(
            {"filename": "name", "document": "hello\udbdeworld"}
        )
        assert document["document"] == "hello?world", document

    @pytest.mark.parametrize(
        "schema_klass, expected_klass, instance_data",
        [
            (DocumentSchema, OrderedDict, {"filename": "hello", "document": "hello"}),
            (
                HealthCheckResponseSchema,
                OrderedDict,
                {"detail": "hello", "status_code": 200},
            ),
            (MatchSchema, Match, {"match": "hello", "type": "hello"}),
            (
                MultiScanResultSchema,
                MultiScanResult,
                {
                    "scan_results": [
                        {
                            "policy_break_count": 1,
                            "policies": ["pol"],
                            "policy_breaks": [
                                {
                                    "type": "break",
                                    "policy": "mypol",
                                    "matches": [
                                        {
                                            "match": "hello",
                                            "type": "hello",
                                        }
                                    ],
                                }
                            ],
                        }
                    ],
                    "type": "hello",
                },
            ),
            (
                PolicyBreakSchema,
                PolicyBreak,
                {
                    "type": "hello",
                    "policy": "hello",
                    "validity": "hey",
                    "matches": [{"match": "hello", "type": "hello"}],
                },
            ),
            (
                PolicyBreakSchema,
                PolicyBreak,
                {
                    "type": "hello",
                    "policy": "hello",
                    "validity": "hey",
                    "known_secret": True,
                    "incident_url": "https://api.gitguardian.com/workspace/2/incidents/3",
                    "matches": [{"match": "hello", "type": "hello"}],
                },
            ),
            (
                QuotaSchema,
                Quota,
                {
                    "count": 1,
                    "limit": 1,
                    "remaining": 1,
                    "since": "2021-04-18",
                },
            ),
            (
                QuotaResponseSchema,
                QuotaResponse,
                {
                    "content": {
                        "count": 1,
                        "limit": 1,
                        "remaining": 1,
                        "since": "2021-04-18",
                    }
                },
            ),
            (
                ScanResultSchema,
                ScanResult,
                {"policy_break_count": 1, "policy_breaks": [], "policies": []},
            ),
            (
                DetailSchema,
                Detail,
                {"detail": "Fail"},
            ),
            (
                HoneytokenResponseSchema,
                HoneytokenResponse,
                {
                    "id": "d45a123f-b15d-4fea-abf6-ff2a8479de5b",
                    "name": "honeytoken A",
                    "description": "honeytoken used in the repository AA",
                    "created_at": "2019-08-22T14:15:22Z",
                    "gitguardian_url": "https://dashboard.gitguardian.com/workspace/1/honeytokens/d45a123f-b15d-4fea-abf6-ff2a8479de5b",  # noqa: E501
                    "status": "active",
                    "triggered_at": "2019-08-22T14:15:22Z",
                    "revoked_at": None,
                    "open_events_count": 2,
                    "type": "AWS",
                    "creator_id": 122,
                    "revoker_id": None,
                    "creator_api_token_id": None,
                    "revoker_api_token_id": None,
                    "token": {"access_token_id": "AAAA", "secret_key": "BBB"},
                    "tags": ["publicly_exposed"],
                },
            ),
            (
                HoneytokenWithContextResponseSchema,
                HoneytokenWithContextResponse,
                {
                    "content": "def return_aws_credentials():\n \
                                    aws_access_key_id = XXXXXXXX\n \
                                    aws_secret_access_key = XXXXXXXX\n \
                                    aws_region = us-west-2\n \
                                    return (aws_access_key_id, aws_secret_access_key, aws_region)\n",
                    "filename": "aws.py",
                    "language": "python",
                    "suggested_commit_message": "Add AWS credentials",
                    "honeytoken_id": "d45a123f-b15d-4fea-abf6-ff2a8479de5b",
                    "gitguardian_url": "https://dashboard.gitguardian.com/workspace/1/honeytokens/d45a123f-b15d-4fea-abf6-ff2a8479de5b",  # noqa: E501
                },
            ),
        ],
    )
    def test_schema_loads(self, schema_klass, expected_klass, instance_data):
        """
        GIVEN the right kwargs  and an extra field in dict format
        WHEN loading using the schema
        THEN the extra field should be excluded
        AND the result should be an instance of the expected class
        """
        schema = schema_klass()

        data = {**instance_data, "field": "extra"}

        obj = schema.load(data)
        assert isinstance(obj, expected_klass)

    def test_detail_renames_error_field(self):
        """
        GIVEN a Detail JSON dict with an `error` field instead of a `detail` field
        WHEN loading using the schema
        THEN the created Detail instance contains a `detail` field with the right value
        """
        detail = Detail.SCHEMA.load({"error": "An error message"})
        assert detail.detail == "An error message"

    @pytest.mark.parametrize("known_secret", [True, False])
    def test_policy_break_known_secret_field(self, known_secret):
        """
        GIVEN the data with policy breaks
        WHEN loading using the schema
        THEN known_secret is parsed correctly with the default value set to False
        """
        data = {
            "type": "hello",
            "policy": "hello",
            "validity": "hey",
            "matches": [{"match": "hello", "type": "hello"}],
        }
        if known_secret:
            data["known_secret"] = True

        obj = PolicyBreakSchema().load(data)

        assert obj.known_secret is known_secret
