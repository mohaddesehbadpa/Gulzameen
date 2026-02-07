"""
Netlify Function: Handle feedback submissions
Saves to dist/data/feedback.json
"""

import json
import os
from datetime import datetime

def handler(event, context):
    """Handle feedback POST requests"""
    
    if event['httpMethod'] != 'POST':
        return {
            'statusCode': 405,
            'body': json.dumps({'error': 'Method not allowed'})
        }
    
    try:
        body = json.loads(event['body'])
        name = body.get('name', 'Anonymous').strip()
        feedback_text = body.get('feedback', '').strip()
        
        if not feedback_text:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Feedback cannot be empty'})
            }
        
        # Create feedback entry
        entry = {
            'name': name,
            'feedback': feedback_text,
            'timestamp': datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')
        }
        
        # Save to file (in dist/data for Netlify)
        data_dir = os.path.join(os.path.dirname(__file__), '../../dist/data')
        os.makedirs(data_dir, exist_ok=True)
        
        feedback_file = os.path.join(data_dir, 'feedback.json')
        
        # Load existing feedback
        feedbacks = []
        if os.path.exists(feedback_file):
            with open(feedback_file, 'r', encoding='utf-8') as f:
                feedbacks = json.load(f)
        
        # Add new feedback
        feedbacks.insert(0, entry)
        
        # Save updated feedback
        with open(feedback_file, 'w', encoding='utf-8') as f:
            json.dump(feedbacks, f, ensure_ascii=False, indent=2)
        
        return {
            'statusCode': 200,
            'body': json.dumps({'success': True, 'message': 'Feedback saved!'})
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
