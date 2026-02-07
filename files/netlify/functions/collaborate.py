"""
Netlify Function: Handle collaboration submissions
Saves to dist/data/collaborations.json
"""

import json
import os
from datetime import datetime
from pathlib import Path

def handler(event, context):
    """Handle collaboration POST requests"""
    
    if event['httpMethod'] != 'POST':
        return {
            'statusCode': 405,
            'body': json.dumps({'error': 'Method not allowed'})
        }
    
    try:
        # Parse form data or JSON
        body = event.get('body', '{}')
        
        # Handle both JSON and form-encoded data
        if isinstance(body, str):
            if body.startswith('{'):
                data = json.loads(body)
            else:
                # Simple form parser
                data = {}
                for pair in body.split('&'):
                    if '=' in pair:
                        k, v = pair.split('=', 1)
                        data[k] = v
        else:
            data = body
        
        name = data.get('name', '').strip()
        category = data.get('category', '').strip()
        title = data.get('title', '').strip()
        region = data.get('region', '').strip()
        content = data.get('content', '').strip()
        
        if not all([name, category, title, content]):
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'All fields required'})
            }
        
        # Create collaboration entry
        entry = {
            'name': name,
            'category': category,
            'title': title,
            'region': region,
            'content': content,
            'filename': None,
            'timestamp': datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')
        }
        
        # Save to file
        data_dir = os.path.join(os.path.dirname(__file__), '../../dist/data')
        os.makedirs(data_dir, exist_ok=True)
        
        collab_file = os.path.join(data_dir, 'collaborations.json')
        
        # Load existing collaborations
        collabs = []
        if os.path.exists(collab_file):
            with open(collab_file, 'r', encoding='utf-8') as f:
                collabs = json.load(f)
        
        # Add new collaboration
        collabs.insert(0, entry)
        
        # Save updated collaborations
        with open(collab_file, 'w', encoding='utf-8') as f:
            json.dump(collabs, f, ensure_ascii=False, indent=2)
        
        return {
            'statusCode': 200,
            'body': json.dumps({'success': True, 'message': 'Collaboration submitted!'})
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
