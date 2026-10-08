from datetime import date

import streamlit as st

from github_service import get_commits
from ai_service import analyze_commits
from release_notes import generate_release_notes, generate_changelog


# Page configuration
st.set_page_config(
    page_title="Release Notes Drafter",
    page_icon="📝",
    layout="wide"
)


# Title
st.title("📝 Release Notes and Changelog Drafter")
st.write(
    "Generate release notes and changelog automatically from Git commits."
)


# Sidebar
st.sidebar.header("Project Settings")


owner = st.sidebar.text_input(
    "GitHub Username / Owner",
    placeholder="your-github-username"
)


repo = st.sidebar.text_input(
    "Repository Name",
    placeholder="your-repository"
)


branch = st.sidebar.text_input(
    "Branch",
    value="main"
)


version = st.sidebar.text_input(
    "Version",
    value="1.0"
)


release_date = st.sidebar.date_input(
    "Release Date",
    value=date.today()
)


# Generate button
if st.button("🚀 Generate Release Notes", type="primary"):

    # Check GitHub details
    if not owner or not repo:
        st.error(
            "Please enter GitHub username and repository name."
        )
        st.stop()

    try:

        # Step 1: Get GitHub commits
        with st.spinner("Getting Git commits..."):

            commits = get_commits(
                owner,
                repo,
                branch
            )

        if not commits:
            st.warning("No commits found.")
            st.stop()

        st.success(
            f"{len(commits)} commits found."
        )


        # Step 2: Analyze commits
        with st.spinner("Analyzing commits..."):

            analysis = analyze_commits(
                commits
            )


        # Step 3: Generate release notes
        release_notes = generate_release_notes(
            analysis,
            version,
            str(release_date)
        )


        # Step 4: Generate changelog
        changelog = generate_changelog(
            analysis,
            version,
            str(release_date)
        )


        # Display results
        st.subheader("✅ Generated Output")


        tab1, tab2, tab3 = st.tabs(
            [
                "📄 Release Notes",
                "📋 Changelog",
                "🔀 Git Commits"
            ]
        )


        # Release Notes
        with tab1:

            st.markdown(
                release_notes
            )

            st.download_button(
                label="⬇️ Download Release Notes",
                data=release_notes,
                file_name=f"release_notes_{version}.md",
                mime="text/markdown"
            )


        # Changelog
        with tab2:

            st.markdown(
                changelog
            )

            st.download_button(
                label="⬇️ Download Changelog",
                data=changelog,
                file_name=f"CHANGELOG_{version}.md",
                mime="text/markdown"
            )


        # Git Commits
        with tab3:

            st.write(
                f"Total commits: **{len(commits)}**"
            )

            for commit in commits:

                st.markdown(
                    f"**{commit['message']}**  \n"
                    f"Author: {commit['author']}  \n"
                    f"Date: {commit['date']}  \n"
                    f"SHA: `{commit['sha']}`"
                )

                st.divider()


    except Exception as error:

        st.error(
            f"Could not generate release notes: {error}"
        )