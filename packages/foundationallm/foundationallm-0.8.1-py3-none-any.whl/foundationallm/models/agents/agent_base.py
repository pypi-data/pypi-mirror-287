"""
Base Agent fulfilling the orchestration request.
"""
from pydantic import Field
from typing import Optional
from foundationallm.models.agents import (
    AgentConversationHistorySettings,
    AgentGatekeeperSettings,
    AgentOrchestrationSettings
)
from foundationallm.models.resource_providers import ResourceBase

class AgentBase(ResourceBase):
    """ Agent Base model."""
    sessions_enabled: bool = Field(default=False, description="Indicates whether sessions are enabled for the agent.")
    conversation_history_settings: Optional[AgentConversationHistorySettings] = Field(default=AgentConversationHistorySettings(), description="Configuration for the agent's conversation history.")
    gatekeeper_settings: Optional[AgentGatekeeperSettings] = Field(default=AgentGatekeeperSettings(), description="Gatekeeper configuration for the agent.")
    orchestration_settings: Optional[AgentOrchestrationSettings] = Field(default=AgentOrchestrationSettings(), description="Agent settings for the orchestrator.")
    prompt_object_id: Optional[str] = Field(default=None, description="The object identifier of the Prompt object providing the prompt for the agent.")
    ai_model_object_id: Optional[str] = Field(default=None, description="The object identifier of the AIModelBase object providing the AI model for the agent.")
    long_running: bool = Field(default=False, description="Indicates whether the agent is a long-running agent.")
