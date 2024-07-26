"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import nucliadb_protos.knowledgebox_pb2
import nucliadb_protos.writer_pb2
import typing
from nucliadb_protos.audit_pb2 import (
    API as API,
    AuditField as AuditField,
    AuditKBCounter as AuditKBCounter,
    AuditRequest as AuditRequest,
    CHROME_EXTENSION as CHROME_EXTENSION,
    ChatAudit as ChatAudit,
    ChatContext as ChatContext,
    ClientType as ClientType,
    DASHBOARD as DASHBOARD,
    DESKTOP as DESKTOP,
    WEB as WEB,
    WIDGET as WIDGET,
)
from nucliadb_protos.knowledgebox_pb2 import (
    CONFLICT as CONFLICT,
    CreateExternalIndexProviderMetadata as CreateExternalIndexProviderMetadata,
    CreatePineconeConfig as CreatePineconeConfig,
    DeleteKnowledgeBoxResponse as DeleteKnowledgeBoxResponse,
    DeletedEntitiesGroups as DeletedEntitiesGroups,
    ERROR as ERROR,
    EntitiesGroup as EntitiesGroup,
    EntitiesGroupSummary as EntitiesGroupSummary,
    EntitiesGroups as EntitiesGroups,
    Entity as Entity,
    EntityGroupDuplicateIndex as EntityGroupDuplicateIndex,
    ExternalIndexProviderType as ExternalIndexProviderType,
    KBConfiguration as KBConfiguration,
    KnowledgeBoxConfig as KnowledgeBoxConfig,
    KnowledgeBoxID as KnowledgeBoxID,
    KnowledgeBoxNew as KnowledgeBoxNew,
    KnowledgeBoxResponseStatus as KnowledgeBoxResponseStatus,
    KnowledgeBoxUpdate as KnowledgeBoxUpdate,
    KnowledgeBoxVectorSetsConfig as KnowledgeBoxVectorSetsConfig,
    Label as Label,
    LabelSet as LabelSet,
    Labels as Labels,
    NOTFOUND as NOTFOUND,
    NewKnowledgeBoxResponse as NewKnowledgeBoxResponse,
    OK as OK,
    PINECONE as PINECONE,
    SemanticModelMetadata as SemanticModelMetadata,
    StoredExternalIndexProviderMetadata as StoredExternalIndexProviderMetadata,
    StoredPineconeConfig as StoredPineconeConfig,
    Synonyms as Synonyms,
    TermSynonyms as TermSynonyms,
    UNSET as UNSET,
    UpdateKnowledgeBoxResponse as UpdateKnowledgeBoxResponse,
    VectorSet as VectorSet,
    VectorSetConfig as VectorSetConfig,
    VectorSets as VectorSets,
)
from nucliadb_protos.noderesources_pb2 import (
    EmptyQuery as EmptyQuery,
    EmptyResponse as EmptyResponse,
    IndexMetadata as IndexMetadata,
    IndexParagraph as IndexParagraph,
    IndexParagraphs as IndexParagraphs,
    NodeMetadata as NodeMetadata,
    ParagraphMetadata as ParagraphMetadata,
    Position as Position,
    Representation as Representation,
    Resource as Resource,
    ResourceID as ResourceID,
    SentenceMetadata as SentenceMetadata,
    Shard as Shard,
    ShardCreated as ShardCreated,
    ShardId as ShardId,
    ShardIds as ShardIds,
    ShardMetadata as ShardMetadata,
    TextInformation as TextInformation,
    VectorSentence as VectorSentence,
    VectorSetID as VectorSetID,
    VectorSetList as VectorSetList,
    VectorsetSentences as VectorsetSentences,
)
from nucliadb_protos.resources_pb2 import (
    AllFieldIDs as AllFieldIDs,
    Answers as Answers,
    Basic as Basic,
    Block as Block,
    CONVERSATION as CONVERSATION,
    Classification as Classification,
    CloudFile as CloudFile,
    ComputedMetadata as ComputedMetadata,
    Conversation as Conversation,
    Entity as Entity,
    Extra as Extra,
    ExtractedTextWrapper as ExtractedTextWrapper,
    ExtractedVectorsWrapper as ExtractedVectorsWrapper,
    FILE as FILE,
    FieldClassifications as FieldClassifications,
    FieldComputedMetadata as FieldComputedMetadata,
    FieldComputedMetadataWrapper as FieldComputedMetadataWrapper,
    FieldConversation as FieldConversation,
    FieldFile as FieldFile,
    FieldID as FieldID,
    FieldLargeMetadata as FieldLargeMetadata,
    FieldLink as FieldLink,
    FieldMetadata as FieldMetadata,
    FieldQuestionAnswerWrapper as FieldQuestionAnswerWrapper,
    FieldText as FieldText,
    FieldType as FieldType,
    FileExtractedData as FileExtractedData,
    FilePages as FilePages,
    GENERIC as GENERIC,
    LINK as LINK,
    LargeComputedMetadata as LargeComputedMetadata,
    LargeComputedMetadataWrapper as LargeComputedMetadataWrapper,
    LinkExtractedData as LinkExtractedData,
    Message as Message,
    MessageContent as MessageContent,
    Metadata as Metadata,
    NestedListPosition as NestedListPosition,
    NestedPosition as NestedPosition,
    Origin as Origin,
    PageInformation as PageInformation,
    PagePositions as PagePositions,
    PageSelections as PageSelections,
    PageStructure as PageStructure,
    PageStructurePage as PageStructurePage,
    PageStructureToken as PageStructureToken,
    Paragraph as Paragraph,
    ParagraphAnnotation as ParagraphAnnotation,
    ParagraphRelations as ParagraphRelations,
    Position as Position,
    Positions as Positions,
    Question as Question,
    QuestionAnswer as QuestionAnswer,
    QuestionAnswerAnnotation as QuestionAnswerAnnotation,
    QuestionAnswers as QuestionAnswers,
    Relations as Relations,
    Representation as Representation,
    RowsPreview as RowsPreview,
    Sentence as Sentence,
    TEXT as TEXT,
    TokenSplit as TokenSplit,
    UserFieldMetadata as UserFieldMetadata,
    UserMetadata as UserMetadata,
    UserVectorsWrapper as UserVectorsWrapper,
    VisualSelection as VisualSelection,
)

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class WriterStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    NewKnowledgeBox: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.knowledgebox_pb2.KnowledgeBoxNew,
        nucliadb_protos.knowledgebox_pb2.NewKnowledgeBoxResponse,
    ]

    NewKnowledgeBoxV2: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.NewKnowledgeBoxV2Request,
        nucliadb_protos.writer_pb2.NewKnowledgeBoxV2Response,
    ]

    DeleteKnowledgeBox: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.knowledgebox_pb2.KnowledgeBoxID,
        nucliadb_protos.knowledgebox_pb2.DeleteKnowledgeBoxResponse,
    ]

    UpdateKnowledgeBox: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.knowledgebox_pb2.KnowledgeBoxUpdate,
        nucliadb_protos.knowledgebox_pb2.UpdateKnowledgeBoxResponse,
    ]

    ProcessMessage: grpc.StreamUnaryMultiCallable[
        nucliadb_protos.writer_pb2.BrokerMessage,
        nucliadb_protos.writer_pb2.OpStatusWriter,
    ]

    NewEntitiesGroup: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.NewEntitiesGroupRequest,
        nucliadb_protos.writer_pb2.NewEntitiesGroupResponse,
    ]
    """Entities"""

    GetEntities: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.GetEntitiesRequest,
        nucliadb_protos.writer_pb2.GetEntitiesResponse,
    ]

    GetEntitiesGroup: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.GetEntitiesGroupRequest,
        nucliadb_protos.writer_pb2.GetEntitiesGroupResponse,
    ]

    ListEntitiesGroups: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.ListEntitiesGroupsRequest,
        nucliadb_protos.writer_pb2.ListEntitiesGroupsResponse,
    ]

    SetEntities: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.SetEntitiesRequest,
        nucliadb_protos.writer_pb2.OpStatusWriter,
    ]

    UpdateEntitiesGroup: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.UpdateEntitiesGroupRequest,
        nucliadb_protos.writer_pb2.UpdateEntitiesGroupResponse,
    ]

    DelEntities: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.DelEntitiesRequest,
        nucliadb_protos.writer_pb2.OpStatusWriter,
    ]

    Status: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.WriterStatusRequest,
        nucliadb_protos.writer_pb2.WriterStatusResponse,
    ]

    ListMembers: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.ListMembersRequest,
        nucliadb_protos.writer_pb2.ListMembersResponse,
    ]

    Index: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.IndexResource,
        nucliadb_protos.writer_pb2.IndexStatus,
    ]

    ReIndex: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.IndexResource,
        nucliadb_protos.writer_pb2.IndexStatus,
    ]

    NewVectorSet: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.NewVectorSetRequest,
        nucliadb_protos.writer_pb2.NewVectorSetResponse,
    ]

    DelVectorSet: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.DelVectorSetRequest,
        nucliadb_protos.writer_pb2.DelVectorSetResponse,
    ]

class WriterAsyncStub:
    NewKnowledgeBox: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.knowledgebox_pb2.KnowledgeBoxNew,
        nucliadb_protos.knowledgebox_pb2.NewKnowledgeBoxResponse,
    ]

    NewKnowledgeBoxV2: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.NewKnowledgeBoxV2Request,
        nucliadb_protos.writer_pb2.NewKnowledgeBoxV2Response,
    ]

    DeleteKnowledgeBox: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.knowledgebox_pb2.KnowledgeBoxID,
        nucliadb_protos.knowledgebox_pb2.DeleteKnowledgeBoxResponse,
    ]

    UpdateKnowledgeBox: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.knowledgebox_pb2.KnowledgeBoxUpdate,
        nucliadb_protos.knowledgebox_pb2.UpdateKnowledgeBoxResponse,
    ]

    ProcessMessage: grpc.aio.StreamUnaryMultiCallable[
        nucliadb_protos.writer_pb2.BrokerMessage,
        nucliadb_protos.writer_pb2.OpStatusWriter,
    ]

    NewEntitiesGroup: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.NewEntitiesGroupRequest,
        nucliadb_protos.writer_pb2.NewEntitiesGroupResponse,
    ]
    """Entities"""

    GetEntities: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.GetEntitiesRequest,
        nucliadb_protos.writer_pb2.GetEntitiesResponse,
    ]

    GetEntitiesGroup: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.GetEntitiesGroupRequest,
        nucliadb_protos.writer_pb2.GetEntitiesGroupResponse,
    ]

    ListEntitiesGroups: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.ListEntitiesGroupsRequest,
        nucliadb_protos.writer_pb2.ListEntitiesGroupsResponse,
    ]

    SetEntities: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.SetEntitiesRequest,
        nucliadb_protos.writer_pb2.OpStatusWriter,
    ]

    UpdateEntitiesGroup: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.UpdateEntitiesGroupRequest,
        nucliadb_protos.writer_pb2.UpdateEntitiesGroupResponse,
    ]

    DelEntities: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.DelEntitiesRequest,
        nucliadb_protos.writer_pb2.OpStatusWriter,
    ]

    Status: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.WriterStatusRequest,
        nucliadb_protos.writer_pb2.WriterStatusResponse,
    ]

    ListMembers: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.ListMembersRequest,
        nucliadb_protos.writer_pb2.ListMembersResponse,
    ]

    Index: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.IndexResource,
        nucliadb_protos.writer_pb2.IndexStatus,
    ]

    ReIndex: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.IndexResource,
        nucliadb_protos.writer_pb2.IndexStatus,
    ]

    NewVectorSet: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.NewVectorSetRequest,
        nucliadb_protos.writer_pb2.NewVectorSetResponse,
    ]

    DelVectorSet: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.DelVectorSetRequest,
        nucliadb_protos.writer_pb2.DelVectorSetResponse,
    ]

class WriterServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def NewKnowledgeBox(
        self,
        request: nucliadb_protos.knowledgebox_pb2.KnowledgeBoxNew,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.knowledgebox_pb2.NewKnowledgeBoxResponse, collections.abc.Awaitable[nucliadb_protos.knowledgebox_pb2.NewKnowledgeBoxResponse]]: ...

    @abc.abstractmethod
    def NewKnowledgeBoxV2(
        self,
        request: nucliadb_protos.writer_pb2.NewKnowledgeBoxV2Request,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.writer_pb2.NewKnowledgeBoxV2Response, collections.abc.Awaitable[nucliadb_protos.writer_pb2.NewKnowledgeBoxV2Response]]: ...

    @abc.abstractmethod
    def DeleteKnowledgeBox(
        self,
        request: nucliadb_protos.knowledgebox_pb2.KnowledgeBoxID,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.knowledgebox_pb2.DeleteKnowledgeBoxResponse, collections.abc.Awaitable[nucliadb_protos.knowledgebox_pb2.DeleteKnowledgeBoxResponse]]: ...

    @abc.abstractmethod
    def UpdateKnowledgeBox(
        self,
        request: nucliadb_protos.knowledgebox_pb2.KnowledgeBoxUpdate,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.knowledgebox_pb2.UpdateKnowledgeBoxResponse, collections.abc.Awaitable[nucliadb_protos.knowledgebox_pb2.UpdateKnowledgeBoxResponse]]: ...

    @abc.abstractmethod
    def ProcessMessage(
        self,
        request_iterator: _MaybeAsyncIterator[nucliadb_protos.writer_pb2.BrokerMessage],
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.writer_pb2.OpStatusWriter, collections.abc.Awaitable[nucliadb_protos.writer_pb2.OpStatusWriter]]: ...

    @abc.abstractmethod
    def NewEntitiesGroup(
        self,
        request: nucliadb_protos.writer_pb2.NewEntitiesGroupRequest,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.writer_pb2.NewEntitiesGroupResponse, collections.abc.Awaitable[nucliadb_protos.writer_pb2.NewEntitiesGroupResponse]]:
        """Entities"""

    @abc.abstractmethod
    def GetEntities(
        self,
        request: nucliadb_protos.writer_pb2.GetEntitiesRequest,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.writer_pb2.GetEntitiesResponse, collections.abc.Awaitable[nucliadb_protos.writer_pb2.GetEntitiesResponse]]: ...

    @abc.abstractmethod
    def GetEntitiesGroup(
        self,
        request: nucliadb_protos.writer_pb2.GetEntitiesGroupRequest,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.writer_pb2.GetEntitiesGroupResponse, collections.abc.Awaitable[nucliadb_protos.writer_pb2.GetEntitiesGroupResponse]]: ...

    @abc.abstractmethod
    def ListEntitiesGroups(
        self,
        request: nucliadb_protos.writer_pb2.ListEntitiesGroupsRequest,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.writer_pb2.ListEntitiesGroupsResponse, collections.abc.Awaitable[nucliadb_protos.writer_pb2.ListEntitiesGroupsResponse]]: ...

    @abc.abstractmethod
    def SetEntities(
        self,
        request: nucliadb_protos.writer_pb2.SetEntitiesRequest,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.writer_pb2.OpStatusWriter, collections.abc.Awaitable[nucliadb_protos.writer_pb2.OpStatusWriter]]: ...

    @abc.abstractmethod
    def UpdateEntitiesGroup(
        self,
        request: nucliadb_protos.writer_pb2.UpdateEntitiesGroupRequest,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.writer_pb2.UpdateEntitiesGroupResponse, collections.abc.Awaitable[nucliadb_protos.writer_pb2.UpdateEntitiesGroupResponse]]: ...

    @abc.abstractmethod
    def DelEntities(
        self,
        request: nucliadb_protos.writer_pb2.DelEntitiesRequest,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.writer_pb2.OpStatusWriter, collections.abc.Awaitable[nucliadb_protos.writer_pb2.OpStatusWriter]]: ...

    @abc.abstractmethod
    def Status(
        self,
        request: nucliadb_protos.writer_pb2.WriterStatusRequest,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.writer_pb2.WriterStatusResponse, collections.abc.Awaitable[nucliadb_protos.writer_pb2.WriterStatusResponse]]: ...

    @abc.abstractmethod
    def ListMembers(
        self,
        request: nucliadb_protos.writer_pb2.ListMembersRequest,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.writer_pb2.ListMembersResponse, collections.abc.Awaitable[nucliadb_protos.writer_pb2.ListMembersResponse]]: ...

    @abc.abstractmethod
    def Index(
        self,
        request: nucliadb_protos.writer_pb2.IndexResource,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.writer_pb2.IndexStatus, collections.abc.Awaitable[nucliadb_protos.writer_pb2.IndexStatus]]: ...

    @abc.abstractmethod
    def ReIndex(
        self,
        request: nucliadb_protos.writer_pb2.IndexResource,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.writer_pb2.IndexStatus, collections.abc.Awaitable[nucliadb_protos.writer_pb2.IndexStatus]]: ...

    @abc.abstractmethod
    def NewVectorSet(
        self,
        request: nucliadb_protos.writer_pb2.NewVectorSetRequest,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.writer_pb2.NewVectorSetResponse, collections.abc.Awaitable[nucliadb_protos.writer_pb2.NewVectorSetResponse]]: ...

    @abc.abstractmethod
    def DelVectorSet(
        self,
        request: nucliadb_protos.writer_pb2.DelVectorSetRequest,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.writer_pb2.DelVectorSetResponse, collections.abc.Awaitable[nucliadb_protos.writer_pb2.DelVectorSetResponse]]: ...

def add_WriterServicer_to_server(servicer: WriterServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
