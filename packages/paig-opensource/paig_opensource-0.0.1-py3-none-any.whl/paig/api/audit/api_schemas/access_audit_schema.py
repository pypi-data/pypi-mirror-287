from pydantic import BaseModel
from typing import List, Optional
from core.factory.database_initiator import BaseAPIFilter
from pydantic import Field
from fastapi import Query


class BaseAccessAuditView(BaseModel):
    app_key: Optional[str] = Field(None, description="The Application key", alias="applicationKey")
    app_name: Optional[str] = Field(None, description="The Application name", alias="applicationName")
    client_app_key: Optional[str] = Field(None, description="The Client Application key", alias="clientApplicationKey")
    client_app_name: Optional[str] = Field(None, description="The Client Application name", alias="clientApplicationName")
    client_host_name: Optional[str] = Field(None, description="The Client Host name", alias="clientHostname")
    client_ip: Optional[str] = Field(None, description="The Client IP", alias="clientIp")
    context: Optional[dict] = Field({}, description="The context of the audit")
    event_id: Optional[str] = Field(None, description="The Event ID", alias="eventId")
    event_time: Optional[int] = Field(None, description="The Event time", alias="eventTime")
    masked_traits: Optional[dict] = Field({}, description="The masked traits", alias="maskedTraits")
    messages: Optional[List[dict]] = Field([], description="The messages")
    number_of_tokens: Optional[int] = Field(None, description="The number of tokens", alias="numberOfTokens")
    paig_policy_ids: Optional[List[int]] = Field([], description="The Paige policy IDs", alias="paigPolicyIds")
    request_id: Optional[str] = Field(None, description="The Request ID", alias="requestId")
    request_type: Optional[str] = Field(None, description="The Request type", alias="requestType")
    result: Optional[str] = Field(None, description="The Result")
    tenant_id: Optional[str] = Field(None, description="The Tenant ID", alias="tenantId")
    thread_id: Optional[str] = Field(None, description="The Thread ID", alias="threadId")
    thread_sequence_number: Optional[int] = Field(None, description="The Thread sequence number", alias="threadSequenceNumber")
    traits: Optional[List[str]] = Field([], description="The traits")
    user_id: Optional[str] = Field(None, description="The User ID", alias="userId")
    encryption_key_id: Optional[int] = Field(None, description="The Encryption key ID", alias="encryptionKeyId")
    log_time: Optional[int] = Field(None, description="The Log time", alias="logTime")
    transaction_sequence_number: Optional[int] = Field(None, description="The Transaction sequence number", alias="transactionSequenceNumber")

    class Config:
        from_attributes = True
        orm_mode = True
        populate_by_name = True


class QueryParamsBase(BaseAPIFilter):
    user_id: Optional[str] = Field(None, description="The User ID")
    app_name: Optional[str] = Field(None, description="The Application name")
    result: Optional[str] = Field(None, description="The Result")
    request_type: Optional[str] = Field(None, description="The Request type")
    traits: Optional[str] = Field(None, description="The trait")


class IncludeQueryParams(QueryParamsBase):
    thread_id: Optional[str] = Field(None, description="The Thread ID")


def include_query_params(
    includeQuery_userId: Optional[str] = Query(None, alias="includeQuery.userId"),
    includeQuery_applicationName: Optional[str] = Query(None, alias="includeQuery.applicationName"),
    includeQuery_requestType: Optional[str] = Query(None, alias="includeQuery.requestType"),
    includeQuery_traits: Optional[str] = Query(None, alias="includeQuery.trait"),
    includeQuery_result: Optional[str] = Query(None, alias="includeQuery.result"),
    includeQuery_threadId: Optional[str] = Query(None, alias="includeQuery.threadId")
) -> IncludeQueryParams:
    return IncludeQueryParams(
        user_id=includeQuery_userId,
        app_name=includeQuery_applicationName,
        result=includeQuery_result,
        request_type=includeQuery_requestType,
        traits=includeQuery_traits,
        thread_id=includeQuery_threadId
    )


def exclude_query_params(
    excludeQuery_userId: Optional[str] = Query(None, alias="excludeQuery.userId"),
    excludeQuery_applicationName: Optional[str] = Query(None, alias="excludeQuery.applicationName"),
    excludeQuery_requestType: Optional[str] = Query(None, alias="excludeQuery.requestType"),
    excludeQuery_traits: Optional[str] = Query(None, alias="excludeQuery.trait"),
    excludeQuery_result: Optional[str] = Query(None, alias="excludeQuery.result")
) -> QueryParamsBase:
    return QueryParamsBase(
        user_id=excludeQuery_userId,
        app_name=excludeQuery_applicationName,
        result=excludeQuery_result,
        request_type=excludeQuery_requestType,
        traits=excludeQuery_traits
)
