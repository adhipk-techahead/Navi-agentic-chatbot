from google.adk.agents import Agent
from multi_tool_agent.tools.video_cms import get_video_metadata, get_transcript_excerpt, get_claims_list, get_citations_list

video_info_agent = Agent(
    name="video_info_bot",
    model="gemini-2.0-flash",
    description="Answers questions about medical education videos using provided context.",
    instruction=(
        "You are the Video Info Agent specializing in a medical education video.\n"
        "You will be told the video context (metadata, transcript, claims, citations) and the user's latest message.\n"
        "Answer only using the provided context and transcript.\n"
        "Cite using [source-id], e.g. '[Transcript at 00:45]'.\n"
        "If unsure, say 'I don’t have enough info in this video to answer.'\n"
        "Offer to return to onboarding with: 'Shall we continue your setup?'\n"
        "Respond with a JSON object: answer (with citations), source_citations (list), end (true|false)."
    ),
    tools=[get_video_metadata, get_transcript_excerpt, get_claims_list, get_citations_list],
) 