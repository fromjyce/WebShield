from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib
import requests
from bs4 import BeautifulSoup
from features import WebsiteFeatures

#

app = FastAPI()

model = joblib.load("C:/Users/jaya2/Visual Code/Phishing-Website-Detection/backend/models/random_forest_model.joblib")

class URLRequest(BaseModel):
    url: str

def extract_features(url: str):
    try:
        response = requests.get(url, timeout=4)
        soup = BeautifulSoup(response.content, "html.parser")
        features = WebsiteFeatures(soup)
        vector = features.create_vector()
        return vector
    except requests.RequestException:
        raise HTTPException(status_code=400, detail="Unable to fetch URL")

@app.post("/predict/")
async def predict(request: URLRequest):
    features = extract_features(request.url)
    feature_names = [
        'has_title',
        'has_input',
        'has_button',
        'has_image',
        'has_submit',
        'has_link',
        'has_password',
        'has_email_input',
        'has_hidden_element',
        'has_audio',
        'has_video',
        'number_of_inputs',
        'number_of_buttons',
        'number_of_images',
        'number_of_option',
        'number_of_list',
        'number_of_th',
        'number_of_tr',
        'number_of_href',
        'number_of_paragraph',
        'number_of_script',
        'length_of_title',
        'has_h1',
        'has_h2',
        'has_h3',
        'length_of_text',
        'number_of_clickable_button',
        'number_of_a',
        'number_of_img',
        'number_of_div',
        'number_of_figure',
        'has_footer',
        'has_form',
        'has_text_area',
        'has_iframe',
        'has_text_input',
        'number_of_meta',
        'has_nav',
        'has_object',
        'has_picture',
        'number_of_sources',
        'number_of_span',
        'number_of_table'
    ]
    features_df = pd.DataFrame([features], columns=feature_names)
    prediction = model.predict(features_df)
    return {"prediction": "phishing" if prediction[0] else "not phishing"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
