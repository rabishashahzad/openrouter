from dotenv import load_dotenv
import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

# Load environment variables from .env filedo
load_dotenv()
openrouter_api_key = os.getenv("OPENAIROUTER_API_KEY") # Ensure this matches your .env

# Check if the API key is set
if not openrouter_api_key:
    raise ValueError("OPENAIROUTER_API_KEY is not set. Please ensure it is defined in your .env file.")
# External client for Gemini via OpenAI-compatible endpoint
external_client = AsyncOpenAI(
    api_key=openrouter_api_key,
    base_url="https://openrouter.ai/api/v1",
)

# Define the model configuration
model = OpenAIChatCompletionsModel(
    model="deepseek/deepseek-r1-0528-qwen3-8b:free",  # Specify the model to use
    openai_client=external_client
)

# Setup config
config = RunConfig(
    model=model,
    model_provider=model,
    tracing_disabled=True
)

# Define the agent
agent = Agent(
    name="writer agent",
    instructions="You are a writer agent. Generate stories, poems, etc."
)

# Run the agent synchronously with input and config
response = Runner.run_sync(
    agent,
    input="write a story about struggle till the success in advanced English.",
    run_config=config
)

# Print the response
print(response)