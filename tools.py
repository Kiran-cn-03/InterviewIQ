filler_words = [
        "um",
        "uh",
        "erm",
        "basically",
        "actually",
        "literally",
        "like",
        "you know",
        "I mean",
        "sort of",
        "kind of"
    ]


def detect_filler_words(answer: str) -> dict:
    """
    Detect unnecessary filler words in a candidate's answer.
    """
    text=answer.lower()
    found={w:text.count(w) for w in filler_words if text.count(w)>0}
    total = sum(found.values())
    return{
        "total":total,
        "found":found,
        "verdict": "Clean" if total <= 2  else "need immprovement"
    }

star_keywords = {
    "situation": ["when","during","while","project","situation","company","team","environment"],
    "task": ["responsible","task","requirement","assigned","goal","needed to","had to"],
    "action": ["implemented","developed","created","designed","analyzed","debugged","resolved","I did","I worked"],
    "result": ["result","improved","reduced","increased","achieved","successfully","saved","performance"]
    }

def check_star_structure(answer: str) -> dict:
    """
    Check whether an answer covers all four STAR components.
    Uses simple rule-based keyword detection.
    """
    text=answer.lower()
    present={stage: any(sig in text for sig in signals) for stage,signals in star_keywords.items()}
    missing=[stage for stage, ok in present.items() if not ok]
    return{
        "present":present,
        "missing":missing,
        "allPresent":not missing
    }

def score_relevance(answer: str,expected_keywords: list) -> dict:
    """
    Calculate relevance based on expected keywords present in the candidate's answer.
    """

    text = answer.lower()
    covered = {kw for kw in expected_keywords if kw.lower() in text}
    missing = {kw for kw in expected_keywords if kw.lower() not in text}   
    score = round(100 * len(covered) / len(expected_keywords)) if expected_keywords else 0
    return {
        "covered": covered,
        "missing": missing,
        "score": score
    }