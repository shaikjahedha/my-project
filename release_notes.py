def generate_release_notes(analysis, version, release_date):
    """
    Generate release notes in Markdown format.
    """

    notes = f"# Release Notes - Version {version}\n\n"
    notes += f"**Release Date:** {release_date}\n\n"

    notes += "## 🚀 New Features\n\n"

    if analysis.get("new_features"):
        for item in analysis["new_features"]:
            notes += f"- {item}\n"
    else:
        notes += "- No new features in this release.\n"

    notes += "\n## 🐛 Bug Fixes\n\n"

    if analysis.get("bug_fixes"):
        for item in analysis["bug_fixes"]:
            notes += f"- {item}\n"
    else:
        notes += "- No bug fixes in this release.\n"

    notes += "\n## ✨ Improvements\n\n"

    if analysis.get("improvements"):
        for item in analysis["improvements"]:
            notes += f"- {item}\n"
    else:
        notes += "- No improvements in this release.\n"

    notes += "\n## 📚 Documentation\n\n"

    if analysis.get("documentation"):
        for item in analysis["documentation"]:
            notes += f"- {item}\n"
    else:
        notes += "- No documentation changes.\n"

    notes += "\n## ⚠️ Breaking Changes\n\n"

    if analysis.get("breaking_changes"):
        for item in analysis["breaking_changes"]:
            notes += f"- {item}\n"
    else:
        notes += "- No breaking changes.\n"

    return notes


def generate_changelog(analysis, version, release_date):
    """
    Generate CHANGELOG in Markdown format.
    """

    changelog = f"# Changelog\n\n"
    changelog += f"## [{version}] - {release_date}\n\n"

    categories = {
        "Added": "new_features",
        "Fixed": "bug_fixes",
        "Changed": "improvements",
        "Documentation": "documentation",
        "Breaking Changes": "breaking_changes"
    }

    for title, key in categories.items():

        items = analysis.get(key, [])

        if items:
            changelog += f"### {title}\n\n"

            for item in items:
                changelog += f"- {item}\n"

            changelog += "\n"

    return changelog