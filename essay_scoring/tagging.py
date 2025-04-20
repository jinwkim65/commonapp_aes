import re
from collections import defaultdict

def tag_essay(essay, client):
    instructions = """
    
You are a helpful assistant that receives a student essay and attaches labels for the problem, solution, and takeaway sections.
The problem sections introduce a challenge, limitation, or conflict the author faced, showing what needed to change or be overcome. They give readers a reason to care by showing what was difficult, missing, or unresolved.
    
The solution sections show the writer’s efforts, actions, or growth as they work to address a problem. They demonstrate agency, persistence, and specific steps taken to improve or adapt.
    
The takeaway sections reveal the deeper insight, lesson, or new belief the writer gained from the experience. They connect the personal story to broader growth and often hint at how the writer will carry the lesson forward.
    
Insert the tag [P] at the beginning of problem sections and the tag [/P] at the end of them. 
Insert the tag [S] at the beginning of solution sections and the tag [/S] at the end of them.
Insert the tag [T] at the beginning of takeaway sections and the tag [/T] at the end of them.
    
Two tags in the response must always have a space between them. For example, the response must output “come.[/P] [S]Why” and not “come.[/P][S]Why”.
The response must not return two of the same sections in a row. For example, there should never be a problem section followed by another problem section.
The response must contain the essay modified only by the tags that indicate the problem, solution, and takeaway sections. 
The response must not contain any additional text.

    """
    
    response = client.responses.create(
        model="gpt-4o",
        instructions=instructions,
        input=essay,
    )
    return response.output_text
    
def calculate_section_word_distribution(text):
    # Define the tags we're interested in
    tags = ['P', 'S', 'T']
    
    # Initialize a dictionary to store word counts
    word_counts = defaultdict(int)

    for tag in tags:
        # Create a regex pattern to find content between [TAG] and [/TAG]
        pattern = fr'\[{tag}\](.*?)\[/\s*{tag}\]'
        matches = re.findall(pattern, text, re.DOTALL)

        for match in matches:
            # Count words by splitting on whitespace
            words = match.strip().split()
            word_counts[tag] += len(words)

    # Calculate total words in tagged sections
    total_words = sum(word_counts.values())

    # Calculate the distribution
    distribution = {tag: (count, (count / total_words) * 100 if total_words > 0 else 0) for tag, count in word_counts.items()}

    return distribution

def score_distribution(distribution):
    # Ideal distribution
    ideal = {'P': 0.2, 'S': 0.6, 'T': 0.2}

    # Calculate total deviation
    total_deviation = 0
    for tag in ideal:
        actual_percent = distribution.get(tag, (0, 0))[1] / 100  # convert % back to 0-1 scale
        total_deviation += abs(actual_percent - ideal[tag])

    # Compute score out of 10.0
    score = max(0.0, 10.0 * (1 - total_deviation))

    return round(score, 2)

def evaluate_tagged_essay(text):
    distribution = calculate_section_word_distribution(text)
    score = score_distribution(distribution)
    return distribution, score