from django.shortcuts import render,redirect
import requests
from bs4 import BeautifulSoup
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from urllib.parse import urljoin
def home(request):
    text=""
    links=[]
    if request.method=="POST":
        url=request.POST.get("url")
        res=requests.get(url)
        soup=BeautifulSoup(res.content,'html.parser')
        text=soup.body.get_text()
        api_key="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"
        URL = "https://api.openai.com/v1/chat/completions"
        prompt="Can you make notes for this article:"+text
        payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "temperature" : 1.0,
        "top_p":1.0,
        "n" : 1,
        "stream": False,
        "presence_penalty":0,
        "frequency_penalty":0,
        }

        headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
        }

        response = requests.post(URL, headers=headers, json=payload, stream=False)
        response=response.json()
        context={"response":response['choices'][0]['message']['content'],"links":links}

        style_sheet = getSampleStyleSheet()
        font = style_sheet['Normal'].fontName
        font_size = 11
        buffer = io.BytesIO()
        pdf_canvas = canvas.Canvas(buffer)
        pdf_canvas.setFont(font, font_size)
        notes=response['choices'][0]['message']['content'].split(' ')
        lines=[]
        current_line=""
        for word in notes:
            if not current_line:
                current_line = word
            elif "\n-" in word:
                current_line+=" "+word[:-len("\n-")]
                lines.append(current_line)
                current_line = ""
            elif "\n" in word:
                current_line+=" "+word[:-len("\n")]
                lines.append(current_line)
                current_line = ""
            elif len(current_line) + len(word) + 1 <= 100:
                current_line += " " + word
            else:
                lines.append(current_line)
                current_line = ""
    
        if current_line:
                lines.append(current_line)
        y=800
        pdf_canvas.drawString(50,y,"Your Notes:")
        pdf_canvas.setFillColorRGB(240/255,78/255,126/255)
        pdf_canvas.drawString(50,y-20,"_______________________________________________________________________")
        pdf_canvas.setFillColorRGB(0,0,0)
        y=y-50
        for n in lines:
            pdf_canvas.drawString(50,y,n)
            y=y-20
        pdf_canvas.showPage()
        pdf_canvas.save()
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename='notes.pdf')
    context={}
    return render(request,'base\home.html',context)
