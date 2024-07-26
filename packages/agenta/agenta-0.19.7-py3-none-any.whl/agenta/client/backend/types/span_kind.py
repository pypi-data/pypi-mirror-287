# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class SpanKind(str, enum.Enum):
    """
    An enumeration.
    """

    TOOL = "TOOL"
    CHAIN = "CHAIN"
    LLM = "LLM"
    WORKFLOW = "WORKFLOW"
    RETRIEVER = "RETRIEVER"
    EMBEDDING = "EMBEDDING"
    AGENT = "AGENT"
    UNKNOWN = "UNKNOWN"

    def visit(
        self,
        tool: typing.Callable[[], T_Result],
        chain: typing.Callable[[], T_Result],
        llm: typing.Callable[[], T_Result],
        workflow: typing.Callable[[], T_Result],
        retriever: typing.Callable[[], T_Result],
        embedding: typing.Callable[[], T_Result],
        agent: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SpanKind.TOOL:
            return tool()
        if self is SpanKind.CHAIN:
            return chain()
        if self is SpanKind.LLM:
            return llm()
        if self is SpanKind.WORKFLOW:
            return workflow()
        if self is SpanKind.RETRIEVER:
            return retriever()
        if self is SpanKind.EMBEDDING:
            return embedding()
        if self is SpanKind.AGENT:
            return agent()
        if self is SpanKind.UNKNOWN:
            return unknown()
