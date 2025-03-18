# Word/Sentence Segmentation Game

A game that challenges players to correctly segment words or sentences in text without spaces, such as Thai language (which doesn't have spaces between words) or concatenated English text. The game uses Natural Language Processing (NLP) to verify answers.

## Project Overview

### Why This Project?
- Easy to develop and test
- Great for learning basic NLP concepts like tokenization
- Fun educational tool for children or language learners

### Gameplay
- Players are presented with unsegmented text
- They must correctly identify word boundaries
- Examples:
  - Thai: "วันนี้กินอะไรดี" → "วันนี้ | กิน | อะไร | ดี"
  - English: "thequickbrownfox" → "the | quick | brown | fox"

### Game Modes
- Easy Mode: Simple text with common words
- Challenge Mode: More complex text with similar words

## Technical Implementation

### Data Sources
- Thai: PyThaiNLP or WordCorpus for tokenization
- English: NLTK or spaCy

### Technologies
- Frontend: HTML, CSS, JavaScript
- Backend: Python with Flask/FastAPI
- NLP Libraries: PyThaiNLP, NLTK
- Database: SQLite (for storing scores)

### Project Structure
- `/static` - Frontend assets (HTML, CSS, JS)
- `/templates` - HTML templates
- `/app` - Python backend code
  - `tokenizers.py` - NLP tokenization logic
  - `game.py` - Game logic
  - `routes.py` - API endpoints
- `app.py` - Main application entry point
- `requirements.txt` - Python dependencies