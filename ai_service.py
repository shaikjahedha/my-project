def analyze_commits(commits):
    result = {
        "new_features": [],
        "bug_fixes": [],
        "improvements": [],
        "documentation": [],
        "breaking_changes": []
    }

    for commit in commits:
        message = commit["message"]
        text = message.lower()

        if any(word in text for word in [
            "breaking", "break", "removed api", "incompatible"
        ]):
            result["breaking_changes"].append(message)

        elif any(word in text for word in [
            "fix", "bug", "error", "issue", "repair", "resolve"
        ]):
            result["bug_fixes"].append(message)

        elif any(word in text for word in [
            "docs", "documentation", "readme"
        ]):
            result["documentation"].append(message)

        elif any(word in text for word in [
            "improve", "improvement", "update",
            "optimize", "refactor", "enhance", "performance"
        ]):
            result["improvements"].append(message)

        elif any(word in text for word in [
            "add", "added", "feature", "implement",
            "create", "new", "upload"
        ]):
            result["new_features"].append(message)

        else:
            result["improvements"].append(message)

    return result