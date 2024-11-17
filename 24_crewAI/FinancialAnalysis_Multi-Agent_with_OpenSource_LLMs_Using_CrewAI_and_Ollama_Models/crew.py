from crewai import Agent, Task, Crew, Process
from langchain_ollama import ChatOllama
from tools.yf_tech_analysis_tool import yf_tech_analysis
from tools.yf_fundamental_analysis_tool import yf_fundamental_analysis
from tools.sentiment_analysis_tool import sentiment_analysis
from tools.competitor_analysis_tool import competitor_analysis
from tools.risk_assessment_tool import risk_assessment

def create_crew(stock_symbol):
    # Initialize Ollama LLM
    #llm = Ollama(model="tinyllama")  # Make sure you have the llama2 model installed in Ollama
    llm = ChatOllama(
        model="tinyllama", #"tinyllama",   llama3.1:8b
        temperature=0.0,
        #base_url="http://localhost:11434"  # Adiciona a URL base do Ollama
    )
    

    # Define Agents
    researcher = Agent(
        role='Stock Market Researcher',
        goal='Gather and analyze comprehensive data about the stock',
        backstory="You're an experienced stock market researcher with a keen eye for detail and a talent for uncovering hidden trends.",
        tools=[yf_tech_analysis, yf_fundamental_analysis, competitor_analysis],
        llm=llm
    )

    analyst = Agent(
        role='Financial Analyst',
        goal='Analyze the gathered data and provide investment insights',
        backstory="You're a seasoned financial analyst known for your accurate predictions and ability to synthesize complex information.",
        tools=[yf_tech_analysis, yf_fundamental_analysis, risk_assessment],
        llm=llm
    )

    sentiment_analyst = Agent(
        role='Sentiment Analyst',
        goal='Analyze market sentiment and its potential impact on the stock',
        backstory="You're an expert in behavioral finance and sentiment analysis, capable of gauging market emotions and their effects on stock performance.",
        tools=[sentiment_analysis],
        llm=llm
    )

    strategist = Agent(
        role='Investment Strategist',
        goal='Develop a comprehensive investment strategy based on all available data',
        backstory="You're a renowned investment strategist known for creating tailored investment plans that balance risk and reward.",
        tools=[],
        llm=llm
    )

    # Define Tasks
    research_task = Task(
        description=f"Research {stock_symbol} using advanced technical and fundamental analysis tools. Provide a comprehensive summary of key metrics, including chart patterns, financial ratios, and competitor analysis.",
        agent=researcher,
        expected_output="""JSON string containing:
    {
        "technical_analysis": "Detailed technical analysis",
        "chart_patterns": "Identified chart patterns",
        "fundamental_analysis": "Fundamental analysis results",
        "sentiment_analysis": "Market sentiment overview",
        "risk_assessment": "Risk evaluation",
        "competitor_analysis": "Competitor comparison",
        "investment_strategy": "Recommended strategy"
    }"""
    )

    sentiment_task = Task(
        description=f"Analyze the market sentiment for {stock_symbol} using news and social media data. Evaluate how current sentiment might affect the stock's performance.",
        agent=sentiment_analyst,
        expected_output="""JSON string containing:
    {
        "sentiment_score": "Numeric sentiment score",
        "sentiment_analysis": "Detailed sentiment analysis",
        "news_impact": "Analysis of news impact",
        "social_media_trends": "Key social media trends",
        "market_mood": "Overall market mood assessment"
    }"""
    )

    analysis_task = Task(
        description=f"Synthesize the research data and sentiment analysis for {stock_symbol}. Conduct a thorough risk assessment and provide a detailed analysis of the stock's potential.",
        agent=analyst,
        expected_output="""JSON string containing:
    {
        "analysis_summary": "Summary of all analyses",
        "risk_assessment": "Detailed risk analysis",
        "potential_evaluation": "Stock potential evaluation",
        "key_findings": "Main findings and insights",
        "recommendations": "Initial recommendations"
    }"""
    )

    strategy_task = Task(
        description=f"Based on all the gathered information about {stock_symbol}, develop a comprehensive investment strategy. Consider various scenarios and provide actionable recommendations for different investor profiles.",
        agent=strategist,
        expected_output="""JSON string containing:
    {
        "investment_strategy": "Detailed investment strategy",
        "scenarios": "Different market scenarios analysis",
        "recommendations": "Specific recommendations by investor profile",
        "risk_management": "Risk management guidelines",
        "timeline": "Suggested investment timeline"
    }"""
    )

    # Create Crew
    crew = Crew(
        agents=[researcher, sentiment_analyst, analyst, strategist],
        tasks=[research_task, sentiment_task, analysis_task, strategy_task],
        process=Process.sequential
    )

    return crew

def run_analysis(stock_symbol):
    crew = create_crew(stock_symbol)
    result = crew.kickoff()
    return result