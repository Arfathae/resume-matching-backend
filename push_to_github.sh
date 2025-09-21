#!/bin/bash

# Push to GitHub Script
echo "🚀 Pushing Resume Matching Backend to GitHub"
echo "============================================="

# Set the correct remote URL
git remote set-url origin https://github.com/Arfathae/resume-matching-backend-.git

echo "📤 Pushing to GitHub..."
echo "When prompted, use:"
echo "  Username: Arfathae"
echo "  Password: [your personal access token]"
echo ""

git push -u origin main

if [ $? -eq 0 ]; then
    echo "✅ Successfully pushed to GitHub!"
    echo "🌐 Repository: https://github.com/Arfathae/resume-matching-backend-"
else
    echo "❌ Push failed. Please check your credentials."
fi
