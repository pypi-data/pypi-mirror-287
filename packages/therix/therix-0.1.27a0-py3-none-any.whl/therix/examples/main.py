from typing import List
from pydantic import BaseModel, Field
from therix.core.data_sources import PDFDataSource
from therix.core.embedding_models import BedrockTitanEmbedding

from therix.core.output_parser import OutputParserWrapper
from therix.core.agent import Agent

from therix.core.system_prompt_config import SystemPromptConfig
from therix.core.agent import Agent
from therix.core.data_sources import PDFDataSource
from therix.core.embedding_models import BedrockTitanEmbedding
from therix.core.inference_models import GroqMixtral87bInferenceModel,GroqLlama370b
import asyncio

GROQ_API_KEY='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'

sys_prompt = """Answer the question like a pirate based only on the following context and reply with your capabilities if something is out of context.
        Context: 
        {{context}}

        Question: {{question}}
        
        Give the output as follows : {{format_instructions}}

        """
        # Always adress me with my name {name}


variables = {
        "name": "Abhishek Dubey",
}

agent = Agent(name="new smarttttttt agent")
(
        agent.add(PDFDataSource(config={"files": ["../../test-data/rat.pdf"]}))   
        .add(BedrockTitanEmbedding(config={"bedrock_aws_access_key_id" : "ASIA5FTZANLGMZXNPUE5",
                                "bedrock_aws_secret_access_key" : "GqRZENaEgAj9+8S2EdoXhZXiCPigWbs/2pn+ZaLY",
                                "bedrock_aws_session_token" : "IQoJb3JpZ2luX2VjEFYaCmFwLXNvdXRoLTEiRzBFAiAqaQKmlK6wpFEX7Lsab0M/2Gdyj1+Edtqu8AWs/qCfxAIhAOAWKrGmR/whOB2inbimiBaXrvwAzktcOlQCqQarad1VKpcDCD8QABoMOTA1NDE4MTQwMzY0Igzmkgr0RqireCGFkcMq9AIylb7tZuFAOPSIypLKjzlz5tNnrtkIOl5rj7TGWsPxJ8SOGqCWEq6h5hjyropgTsrkTzMbCZOptQPKlZNJ9BgY4BlxfjY3vR0RZlZxZG8Pjc6bYsUrGfA0+QRDwkQ0Ull8zKFaNAC/6iBGiToZLnNCU3RLIJ/PDj0B2Th1hT77j0Ztj7gHM2X2AF8GOl7DHkPrzpoWAvm3JlKcTKNHQJIOtSe7JX14389RKUHE0uXTPexDm2f5dPLWW82e28CmArjfQXDguXJiOvHnbCnVzz6Qwscf99zR8Gu008GzAoAmVm2nNh9sy6GUo3AgAR4tFFAJM/GeZRAnGS4xu0+0TsgoEtehCIgxN2kmKsyuy/zJTcbjPeMZtCvKlFZ0xuvdMtqw84U3hczRWDq3dBZN8AYnFkjZs4oguK+IHrXJDTAmEkacgSYdktW7Z9mAisquJWm4kxXefRiwidPY7am0nWatI2sSQyDVRsz2MGwQyEJPH9uQymQw9PahtQY6pgFvEDg2eKamoiMs92JUMI9fBiYYBfFgGyqdX52xlycPUq98Dh8R6S4IamikE0moeTLsgXQ5CHicQG5TNpmOcdVwnILP2/NHCFH9U+AYft3Z0ySAyG90WZCzNi9fSAGdN8JLi/1U2Zje/XbwuHA9ITd932vrhG8E2FsFtlwYSUNxIzEJ77v9pXl1zbP9hAxgFBczUtlfNuyfg8QVkn+fkTxW041UdrVf",
                                "bedrock_region_name" : "us-east-1"}))
        .add(GroqLlama370b(config={"groq_api_key": GROQ_API_KEY}))
        # .add(SystemPromptConfig(config={"system_prompt" : "new-prompt"}))
        .save()
    )

agent.preprocess_data()

print(agent.id)

class TestDetails(BaseModel):
        name: str = Field(description="Name of the Topic")
        description: str = Field(description="Short description of the Topic")
        citations: str = Field(description="add source of every topic, from where it is generated")
        page: str = Field(description="page number of the topic")


class OutputParserJSON(BaseModel):
    tests: List[TestDetails] = Field(description="Topic")
    
answer = agent.invoke("What kind of experiments are performed in the study?" , output_parser=OutputParserWrapper.parse_output(pydantic_object=OutputParserJSON))

print(answer)