def classify_intent(query):
    query = query.lower()

    if "skill" in query or "learn" in query:
        return "skill_matching"
    elif "project" in query:
        return "project_lookup"
    else:
        return "career_planning"