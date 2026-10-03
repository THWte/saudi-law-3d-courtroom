from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from legal_ai_system import LegalAIBackend, process_legal_case

# Load environment variables
load_dotenv()

# Create Flask app
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max file size
CORS(app)

# Initialize AI system
ai_system = LegalAIBackend()

# ====== API Routes ======

@app.route('/')
def index():
    """Serve the main dashboard"""
    return render_template('dashboard.html')

@app.route('/api/set-mode', methods=['POST'])
def set_mode():
    """Set the AI mode for the session"""
    data = request.get_json()
    mode = data.get('mode')
    
    if mode not in ['FULL_AI', 'AI_ASSISTED', 'USER_ONLY']:
        return jsonify({'error': 'Invalid mode'}), 400
    
    # Store in session or database
    session_mode = mode
    
    return jsonify({
        'status': 'success',
        'mode': mode,
        'message': f'Switched to {mode} mode'
    })

@app.route('/api/analyze-case', methods=['POST'])
def analyze_case():
    """Analyze a legal case using AI"""
    data = request.get_json()
    case_data = data.get('case')
    mode = data.get('mode', 'AI_ASSISTED')
    
    try:
        # Convert to uppercase for consistency
        ai_mode = mode.upper().replace('-', '_')
        
        # Process the case
        result = process_legal_case(case_data, mode=ai_mode)
        
        return jsonify({
            'status': 'success',
            'analysis': result,
            'mode': ai_mode
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/upload-files', methods=['POST'])
def upload_files():
    """Handle file uploads and process them"""
    try:
        files = request.files.getlist('files')
        processed_files = []
        
        for file in files:
            if file.filename == '':
                continue
            
            # Process the file
            file_data = ai_system.process_documents([{
                'name': file.filename,
                'type': file.filename.split('.')[-1],
                'content': file.read()
            }])
            
            processed_files.append(file_data[0])
        
        return jsonify({
            'status': 'success',
            'files': processed_files,
            'count': len(processed_files)
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/strategy/<case_id>', methods=['GET'])
def get_strategy(case_id):
    """Get strategy for a specific case"""
    try:
        # Retrieve case from database
        # Generate strategy using AI
        strategy = ai_system.generate_strategy({}, mode='AI_ASSISTED')
        
        return jsonify({
            'status': 'success',
            'case_id': case_id,
            'strategy': strategy
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/courtroom-scene', methods=['GET'])
def get_courtroom_scene():
    """Get 3D courtroom scene data"""
    return jsonify({
        'status': 'success',
        'scene': {
            'courtroom': {
                'judgesBench': {'position': [0, 2, -3]},
                'lawyerTable': {'position': [-2, 0, 0]},
                'witnessPodium': {'position': [0, 0, 2]},
                'spectatorSeats': {'rows': 5, 'seatsPerRow': 8}
            }
        }
    })

@app.route('/api/training-scenarios', methods=['GET'])
def get_training_scenarios():
    """Get available training scenarios"""
    scenarios = [
        {
            'id': 1,
            'name': 'محاكاة قضية مدنية',
            'description': 'نزاع تجاري حول عقد شراء',
            'difficulty': 'متوسط',
            'duration': 45
        },
        {
            'id': 2,
            'name': 'محاكاة قضية جزائية',
            'description': 'قضية جزائية من المستوى الأول',
            'difficulty': 'صعب',
            'duration': 60
        },
        {
            'id': 3,
            'name': 'محاكاة قضية عمل',
            'description': 'نزاع بين الموظف والمؤسسة',
            'difficulty': 'سهل',
            'duration': 30
        }
    ]
    
    return jsonify({
        'status': 'success',
        'scenarios': scenarios
    })

@app.route('/api/statistics', methods=['GET'])
def get_statistics():
    """Get system statistics"""
    return jsonify({
        'status': 'success',
        'statistics': {
            'total_cases': 1842,
            'closed_cases': 1256,
            'active_cases': 586,
            'success_rate': 94.2,
            'average_response_time': 2.3  # seconds
        }
    })

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'version': '1.0.0',
        'ai_engine': 'active'
    })

# ====== Error Handlers ======

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not Found'}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Server Error'}), 500

# ====== Main ======

if __name__ == '__main__':
    debug = os.getenv('FLASK_DEBUG', 'False') == 'True'
    port = int(os.getenv('PORT', 5000))
    
    print(f"Starting Saudi Legal AI Platform...")
    print(f"Debug mode: {debug}")
    print(f"Listening on port {port}")
    
    app.run(
        debug=debug,
        host='0.0.0.0',
        port=port
    )
