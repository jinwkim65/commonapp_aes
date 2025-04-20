from essay_scoring.tagging import tag_essay, evaluate_tagged_essay

def calculate_pst(essay, client):
    tagged_essay = tag_essay(essay, client)
    _, score = evaluate_tagged_essay(tagged_essay)
    return score
    

### SPECIFICITY SCORE

def calculate_specificity(essay, client):
    instructions = """
You are a helpful assistant that receives a student essay and determines its specificity score. 
The specificity score is a number between 1.0 and 10.0 that measures how vivid and detailed the language of an essay is. Essays that exhibit powerful and specific language must have higher specificity scores. Be thorough and harsh.

Score ranges:
- 1–3: Very vague language
- 4–6: Some specific imagery, but mostly general
- 7–8: Strong detail and imagery, could be a little more specific
- 9–10: Highly vivid, specific, and memorable throughout

The response must be the numerical score to one decimal place for the essay.
The response must not contain any additional text.
    """
        
    response = client.responses.create(
        model="gpt-4o",
        instructions=instructions,
        input=essay,
    )
    return response.output_text

### PACE SCORE

def calculate_pace(essay, client):
    instructions = """
You are a helpful assistant that receives a student essay and determines its pace score. The pace score is a number between 1.0 and 10.0 that measures how effectively the essay varies its sentence lengths to create dynamic storytelling. Essays that exhibit a natural, engaging rhythm with a mix of short, medium, and long sentences must have higher pace scores. Be thorough and harsh.

Score ranges:
- 1–3: Very monotonous sentence length (all long or all short)
- 4–6: Some variation, but still mostly repetitive in pacing
- 7–8: Good sentence length variety, with minor lapses in flow
- 9–10: Excellent pacing with consistent variation that enhances storytelling

The response must be the numerical score to one decimal place for the essay.
The response must not contain any additional text.
    """
        
    response = client.responses.create(
        model="gpt-4o",
        instructions=instructions,
        input=essay,
    )
    return response.output_text

### VSPICE SCORE
    
def calculate_vspice(essay, client):
    instructions = """
You are a helpful assistant that receives a student essay and determines its VSPICE score. The VSPICE score is a number between 1.0 and 10.0 that measures how effectively the essay demonstrates Vulnerability, Selflessness, Perseverance, Initiative, Curiosity, and Expression. Essays that balance personal growth (VSP: heart) with intellectual exploration (ICE: mind), clearly showcasing development in these traits, must have higher VSPICE scores. Be thorough and harsh.

Score ranges:
- 1–3: Little or no demonstration of VSPICE traits, or very imbalanced by focusing too much on either emotion or intellect
- 4–6: Some demonstration of VSPICE traits, but several traits underdeveloped or imbalance apparent
- 7–8: Good demonstration of VSPICE traits with minor imbalances or areas needing deeper development
- 9–10: Excellent, balanced demonstration of all six VSPICE traits with clear and compelling personal and intellectual growth throughout

The response must be the numerical score to one decimal place for the essay.
The response must not contain any additional text.
    """
        
    response = client.responses.create(
        model="gpt-4o",
        instructions=instructions,
        input=essay,
    )
    return response.output_text

### CREATIVITY SCORE

def calculate_creativity(essay, client):
    instructions = """
You are an expert college admissions counselor that has read over 10,000 essays. You receive a student essay and determine its Creativity score. The Creativity score is a number between 1.0 and 10.0 that measures how original the essay's content and angle are compared to typical college application essays. Creativity is based on the uniqueness of the story, the perspective, and the style of expression. Be thorough and harsh.

Score ranges:
- 1–3: Very common topic and angle; little originality in the content and angle
- 4–6: Somewhat common topic or approach, but some signs of unique thinking
- 7–8: Uncommon topic or a creative approach to a familiar idea
- 9–10: Highly original idea, story, or perspective rarely seen in other essays

The response must be the numerical score to one decimal place for the essay.
The response must not contain any additional text.
    """
        
    response = client.responses.create(
        model="gpt-4o",
        instructions=instructions,
        input=essay,
    )
    return response.output_text