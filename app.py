import joblib
import os 

from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import FloatField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY']='wP4xQ8hUljJ5oI1c'
bootstrap = Bootstrap(app)

class InputForm(FlaskForm):
    alcohol = FloatField('Alcohol:', validators=[DataRequired()])
    malic_acid  = FloatField('Malic Acid:', validators=[DataRequired()])
    ash = FloatField('Ash:', validators=[DataRequired()])
    alcalinity_of_ash  = FloatField('Alcalinity of Ash:', validators=[DataRequired()])
    magnesium  = FloatField('Magnesium:', validators=[DataRequired()])
    total_phenols  = FloatField('Total Phenols:', validators=[DataRequired()])
    flavanoids  = FloatField('Flavanoids:', validators=[DataRequired()])
    nonflavanoid_phenols  = FloatField('Nonflavanoid Phenols:', validators=[DataRequired()])
    proanthocyanins  = FloatField('Proanthocyanins:', validators=[DataRequired()])
    color_intensity  = FloatField('Color Intensity:', validators=[DataRequired()])
    hue  = FloatField('Hue:', validators=[DataRequired()])
    diluted_wines  = FloatField('Diluted Wines:', validators=[DataRequired()])
    proline  = FloatField('Proline:', validators=[DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def index():
    form   = InputForm(request.form)
    name = 'No-name'
    if form.validate_on_submit():
       x = [[form.alcohol.data, form.malic_acid.data, form.ash.data, 
             form.alcalinity_of_ash.data, form.magnesium.data, 
             form.total_phenols.data, form.flavanoids.data, 
             form.nonflavanoid_phenols.data, form.proanthocyanins.data, 
             form.color_intensity.data, form.hue.data, 
             form.diluted_wines.data, form.proline.data]]
       name = make_prediction(x)
    
    return render_template('index.html', form=form, name=name)

def make_prediction(x):
    filename = os.path.join('model', 'finalized_model.sav')
    model = joblib.load(filename)
    return model.predict(x)[0]

if __name__ == '__main__':
    app.run()
