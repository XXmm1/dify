from enum import Enum
from typing import Optional

from pydantic import BaseModel

from models.workflow import WorkflowNodeExecutionStatus


class NodeType(Enum):
    """
    Node Types.
    """
    START = 'start'
    END = 'end'
    DIRECT_ANSWER = 'direct-answer'
    LLM = 'llm'
    KNOWLEDGE_RETRIEVAL = 'knowledge-retrieval'
    IF_ELSE = 'if-else'
    CODE = 'code'
    TEMPLATE_TRANSFORM = 'template-transform'
    QUESTION_CLASSIFIER = 'question-classifier'
    HTTP_REQUEST = 'http-request'
    TOOL = 'tool'
    VARIABLE_ASSIGNER = 'variable-assigner'

    @classmethod
    def value_of(cls, value: str) -> 'NodeType':
        """
        Get value of given node type.

        :param value: node type value
        :return: node type
        """
        for node_type in cls:
            if node_type.value == value:
                return node_type
        raise ValueError(f'invalid node type value {value}')


class SystemVariable(Enum):
    """
    System Variables.
    """
    QUERY = 'query'
    FILES = 'files'
    CONVERSATION = 'conversation'


class NodeRunResult(BaseModel):
    """
    Node Run Result.
    """
    status: WorkflowNodeExecutionStatus = WorkflowNodeExecutionStatus.RUNNING

    inputs: Optional[dict] = None  # node inputs
    process_data: Optional[dict] = None  # process data
    outputs: Optional[dict] = None  # node outputs
    metadata: Optional[dict] = None  # node metadata

    edge_source_handle: Optional[str] = None  # source handle id of node with multiple branches

    error: Optional[str] = None  # error message if status is failed