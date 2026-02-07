#!/usr/bin/env python
"""
Build script to generate static HTML files from Flask templates
This allows the site to be deployed on Netlify (static hosting)
"""

import os
import json
from pathlib import Path
from flask import Flask, render_template
from data_enhanced import (regions, folk_stories_files, traditional_songs_audio, 
                          traditional_recipes, melody_section_name, wisdom_section_name, 
                          cultural_treasures, named_melodies, wisdom_riddles, GAME_POINTS)

# Create Flask app context
app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create dist directory
dist_dir = os.path.join(BASE_DIR, 'dist')
os.makedirs(dist_dir, exist_ok=True)

def ensure_audio_availability(songs):
    """Mark audio as available if it exists"""
    songs_with_status = []
    for s in songs:
        path = os.path.join(BASE_DIR, s['filename'].replace('/', os.sep))
        songs_with_status.append({
            'title': s.get('title'),
            'filename': s.get('filename'),
            'available': os.path.exists(path)
        })
    return songs_with_status

def build_static_pages():
    """Generate all static HTML pages"""
    
    with app.app_context():
        # 1. Build Home Page
        print("Building index.html...")
        home_html = render_template("index.html", 
                                   regions=regions, 
                                   cultural_treasures=cultural_treasures)
        with open(os.path.join(dist_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(home_html)
        
        # 2. Build Region Pages
        for region_id, region in regions.items():
            print(f"Building {region_id} region page...")
            songs_with_status = ensure_audio_availability(traditional_songs_audio)
            
            region_html = render_template("region.html", 
                                         region=region,
                                         folk_stories_files=folk_stories_files,
                                         traditional_songs_audio=songs_with_status,
                                         traditional_recipes=traditional_recipes,
                                         melody_section_name=melody_section_name,
                                         wisdom_section_name=wisdom_section_name,
                                         cultural_treasures=cultural_treasures,
                                         named_melodies=named_melodies,
                                         wisdom_riddles=wisdom_riddles)
            
            region_dir = os.path.join(dist_dir, 'region', region_id)
            os.makedirs(region_dir, exist_ok=True)
            
            with open(os.path.join(region_dir, 'index.html'), 'w', encoding='utf-8') as f:
                f.write(region_html)
        
        # 3. Build Privacy Policy Page
        print("Building privacy.html...")
        privacy_html = render_template("privacy.html")
        privacy_dir = os.path.join(dist_dir, 'privacy')
        os.makedirs(privacy_dir, exist_ok=True)
        with open(os.path.join(privacy_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(privacy_html)
        
        # 4. Build Feedback Page
        print("Building feedback.html...")
        feedback_html = render_template("feedback.html", success=False)
        feedback_dir = os.path.join(dist_dir, 'feedback')
        os.makedirs(feedback_dir, exist_ok=True)
        with open(os.path.join(feedback_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(feedback_html)
        
        # 5. Build Collaborate Page
        print("Building collaborate.html...")
        collaborate_html = render_template("collaborate.html", success=False)
        collab_dir = os.path.join(dist_dir, 'collaborate')
        os.makedirs(collab_dir, exist_ok=True)
        with open(os.path.join(collab_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(collaborate_html)
        
        # 6. Build Submissions Page
        print("Building submissions.html...")
        submissions_html = render_template("submissions.html", submissions=[])
        submissions_dir = os.path.join(dist_dir, 'submissions')
        os.makedirs(submissions_dir, exist_ok=True)
        with open(os.path.join(submissions_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(submissions_html)
        
        # 7. Build 404 Page
        print("Building 404.html...")
        notfound_html = render_template("404.html")
        with open(os.path.join(dist_dir, '404.html'), 'w', encoding='utf-8') as f:
            f.write(notfound_html)
        
        print("\n✅ All static pages built successfully!")
        print(f"📁 Output directory: {dist_dir}")
        print(f"🌐 Ready to deploy to Netlify")

if __name__ == "__main__":
    build_static_pages()
