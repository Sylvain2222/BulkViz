from django.shortcuts import render, redirect
from flask import Flask, request
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'cards/index.html',context={})


#uploading file
app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('file')
        if uploaded_file:
            # Traitement du fichier ici (sauvegarde, validation, etc.)
            with open("storage/" + uploaded_file.name, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            return HttpResponse("Fichier uploadé avec succès.")
        return HttpResponse("Échec de l'upload.")
#ajouter gestion des erreurs