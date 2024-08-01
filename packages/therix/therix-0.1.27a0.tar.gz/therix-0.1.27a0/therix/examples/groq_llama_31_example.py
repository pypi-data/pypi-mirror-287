from therix.core.data_sources import PDFDataSource
from therix.core.embedding_models import (
    BedrockTitanEmbedding,

)
from therix.core.inference_models import Anthropic_Claude_Opus, GroqLlama31405B, GroqLlama3170B, GroqLlama318B, OpenAIGPT4OMiniInferenceModel
from therix.core.agent import Agent
import sys

from therix.core.trace import Trace

agent = Agent(name="My New Published Agent")
(
        agent
        # .add(GroqLlama3170B(
        #     config={"groq_api_key":""}
        # ))
        # .add(GroqLlama318B(
        #     config={"groq_api_key":""}
        # ))
        .add(GroqLlama31405B(
            config={"groq_api_key":""}
        ))
        .save()
    )

print(agent.id)
ans = agent.invoke("Who is sonu nigam?")

print(ans)