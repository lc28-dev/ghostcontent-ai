import openai
import os
import json
from dotenv import load_dotenv

load_dotenv()

# Configuration client (utilisera la clé API des secrets Streamlit)
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_social_bundle(business_name, industry, tone, goal):
    """Génère le pack de contenu complet"""
    
    prompt = f"""
    Tu es un expert en marketing digital.
    Business: {business_name} (Secteur: {industry})
    Objectif: {goal}
    Ton: {tone}
    
    Génère un objet JSON avec exactement cette structure:
    {{
      "posts": [
        {{"hook": "titre accrocheur", "caption": "texte du post"}}
      ],
      "scripts": ["script reel 1", "script reel 2"],
      "hashtags": "#tag1 #tag2",
      "calendar": [
        {{"Jour": "Lundi", "Action": "Post Instagram"}},
        {{"Jour": "Mercredi", "Action": "Réponse commentaires"}}
      ]
    }}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Tu es un assistant marketing qui répond uniquement en JSON."},
                {"role": "user", "content": prompt}
            ],
            response_format={{ "type": "json_object" }}
        )
        return response.choices[0].message.content
    except Exception as e:
        # Fallback de secours si l'API ne répond pas (pour test)
        return json.dumps({
            "posts": [{"hook": "Oups !", "caption": "Erreur de connexion API."}],
            "scripts": [],
            "hashtags": "",
            "calendar": []
        })
