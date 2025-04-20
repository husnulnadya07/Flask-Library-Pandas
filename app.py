from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    # Baca file CSV dengan Pandas
    df = pd.read_csv("data.csv")
    
    # Mengubah data menjadi list of dictionaries (records) untuk lebih mudah digunakan di template
    data = df.to_dict(orient="records")
    
    # Kirim data ke template index.html
    return render_template("index.html", data=data)

@app.route("/about")
def about():
    # Menggunakan pandas untuk baca data dan mengirimkan data ke template About
    df = pd.read_csv("data.csv")
    about_data = df.head()  # Hanya mengambil beberapa data pertama
    return render_template("about.html", about_data=about_data)

if __name__ == "__main__":
    app.run(debug=True)
